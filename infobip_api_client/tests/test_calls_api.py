import tempfile

import pytest
from pytest_httpserver import HTTPServer

from infobip_api_client import (
    ApiClient,
    Configuration,
    CallsApi,
    CallRequest,
    CallEndpointType,
    CallsPhoneEndpoint,
    Call,
    CallsMediaProperties,
    CallsAudioMediaProperties,
    CallsVideoMediaProperties,
    CallsMachineDetectionProperties,
    CallPage,
    PageInfo,
    CallLogPage,
    CallLog,
    CallsErrorCodeInfo,
    CallsConnectRequest,
    CallsConference,
    CallsParticipant,
    CallsConnectWithNewCallRequest,
    CallsActionCallRequest,
    CallsPreAnswerRequest,
    CallsConferenceAndCall,
    CallsActionResponse,
    CallsActionStatus,
    CallsAnswerRequest,
    CallRecordingRequest,
    CallsHangupRequest,
    CallsPlayRequest,
    CallsPlayContent,
    CallsStopPlayRequest,
    CallsSayRequest,
    CallsDtmfSendRequest,
    CallsDtmfCaptureRequest,
    CallsSpeechCaptureRequest,
    CallsRecordingStartRequest,
    CallsRecordingRequest,
    CallsStartMediaStreamRequest,
    CallsMediaStream,
    CallsMediaStreamAudioProperties,
    CallsApplicationTransferRequest,
    CallsVoicePreferences,
    CallsConferenceRecordingRequest,
    CallsConferenceBroadcastWebrtcTextRequest,
    CallsConferencePage,
    CallsConferenceRequest,
    CallsUpdateRequest,
    CallsAddNewCallRequest,
    CallsAddExistingCallRequest,
    CallsFilePage,
    CallsFile,
    CallsMediaStreamConfigPage,
    CallRecordingPage,
    CallRecording,
    CallsRecordingFile,
    CallsConferenceRecordingPage,
    CallsOnDemandComposition,
    CallBulkRequest,
    CallsBulkItem,
    CallsBulkCallRequest,
    CallsBulkPhoneEndpoint,
    CallsBulkCall,
    CallBulkResponse,
    CallBulkStatus,
    CallsRescheduleRequest,
    CallsConferenceRecording,
    Platform,
    CallState,
    CallDirection,
    CallsDetectionResult,
    CallsBulkEndpointType,
    CallsLanguage,
    CallsGender,
    CallVoice,
    CallsFileFormat,
    CallsRecordingFileLocation,
    CallsRecordingStatus,
    CallsPlayContentType,
    CallsConferencePlayRequest,
    CallsParticipantState,
    CallTranscriptionLanguage,
    CallsResponseMediaStreamConfigType,
    CallsMediaStreamingConfigResponse,
    CallsWebsocketEndpointConfigResponse,
    CallsMediaStreamingConfigRequest,
    BasicSecurityConfig,
    SecurityConfigType,
)

CALLS = "/calls/1/calls"
CALL = "/calls/1/calls/{callId}"
CALLS_HISTORY = "/calls/1/calls/history"
CALL_HISTORY = "/calls/1/calls/{callId}/history"
CONNECT_CALLS = "/calls/1/connect"
CONNECT_CALL = "/calls/1/calls/{callId}/connect"

PRE_ANSWER_CALL = "/calls/1/calls/{callId}/pre-answer"
ANSWER_CALL = "/calls/1/calls/{callId}/answer"
HANGUP_CALL = "/calls/1/calls/{callId}/hangup"
CALL_PLAY_FILE = "/calls/1/calls/{callId}/play"
CALL_STOP_PLAYING_FILE = "/calls/1/calls/{callId}/stop-play"
CALL_SAY_TEXT = "/calls/1/calls/{callId}/say"
CALL_SEND_DTMF = "/calls/1/calls/{callId}/send-dtmf"
CALL_CAPTURE_DTMF = "/calls/1/calls/{callId}/capture/dtmf"
CALL_CAPTURE_SPEECH = "/calls/1/calls/{callId}/capture/speech"
CALL_START_RECORDING = "/calls/1/calls/{callId}/start-recording"
CALL_STOP_RECORDING = "/calls/1/calls/{callId}/stop-recording"
START_MEDIA_STREAM = "/calls/1/calls/{callId}/start-media-stream"
STOP_MEDIA_STREAM = "/calls/1/calls/{callId}/stop-media-stream"

APPLICATION_TRANSFER = "/calls/1/calls/{callId}/application-transfer"
APPLICATION_TRANSFER_ACCEPT = (
    "/calls/1/calls/{callId}/application-transfer/{transferId}/accept"
)
APPLICATION_TRANSFER_REJECT = (
    "/calls/1/calls/{callId}/application-transfer/{transferId}/reject"
)

CONFERENCES = "/calls/1/conferences"
CONFERENCE = "/calls/1/conferences/{conferenceId}"
CONFERENCES_HISTORY = "/calls/1/conferences/history"
CONFERENCE_HISTORY = "/calls/1/conferences/{conferenceId}/history"
CONFERENCE_CALLS = "/calls/1/conferences/{conferenceId}/call"
CONFERENCE_CALL = "/calls/1/conferences/{conferenceId}/call/{callId}"

HANGUP_CONFERENCE = "/calls/1/conferences/{conferenceId}/hangup"
CONFERENCE_PLAY_FILE = "/calls/1/conferences/{conferenceId}/play"
CONFERENCE_SAY_TEXT = "/calls/1/conferences/{conferenceId}/say"
CONFERENCE_STOP_PLAYING_FILE = "/calls/1/conferences/{conferenceId}/stop-play"
CONFERENCE_START_RECORDING = "/calls/1/conferences/{conferenceId}/start-recording"
CONFERENCE_STOP_RECORDING = "/calls/1/conferences/{conferenceId}/stop-recording"
CONFERENCE_BROADCAST_WEBRTC_TEXT = (
    "/calls/1/conferences/{conferenceId}/broadcast-webrtc-text"
)

DIALOGS = "/calls/1/dialogs"
DIALOGS_EXISTING_CALLS = (
    "/calls/1/dialogs/parent-call/{parentCallId}/child-call/{childCallId}"
)
DIALOGS_BROADCAST_TEXT = "/calls/1/dialogs/{dialogId}/broadcast-webrtc-text"

SIP_TRUNKS = "/calls/1/sip-trunks"
SIP_TRUNK = "/calls/1/sip-trunks/{sipTrunkId}"

SIP_TRUNK_STATUS = "/calls/1/sip-trunks/{sipTrunkId}/status"

SIP_TRUNK_SERVICE_ADDRESSES = "/calls/1/sip-trunks/service-addresses"
SIP_TRUNK_SERVICE_ADDRESS = (
    "/calls/1/sip-trunks/service-addresses/{sipTrunkServiceAddressId}"
)
SIP_TRUNK_COUNTRIES = "/calls/1/sip-trunks/service-addresses/countries"
SIP_TRUNK_REGIONS = "/calls/1/sip-trunks/service-addresses/countries/regions"

CALLS_FILES = "/calls/1/files"
CALLS_FILE = "/calls/1/files/{fileId}"

CALLS_RECORDINGS = "/calls/1/recordings/calls"
CALL_RECORDINGS = "/calls/1/recordings/calls/{callId}"
CONFERENCES_RECORDINGS = "/calls/1/recordings/conferences"
CONFERENCE_RECORDINGS = "/calls/1/recordings/conferences/{conferenceId}"
CALLS_RECORDINGS_FILES = "/calls/1/recordings/files/{fileId}"
COMPOSE_CONFERENCE_RECORDING = "/calls/1/recordings/conferences/{conferenceId}/compose"

MEDIA_STREAM_CONFIGS = "/calls/1/media-stream-configs"
MEDIA_STREAM_CONFIG = "/calls/1/media-stream-configs/{mediaStreamConfigId}"

BULKS = "/calls/1/bulks"
BULK = "/calls/1/bulks/{bulkId}"

RESCHEDULE_BULK = "/calls/1/bulks/{bulkId}/reschedule"
PAUSE_BULK = "/calls/1/bulks/{bulkId}/pause"
RESUME_BULK = "/calls/1/bulks/{bulkId}/resume"
CANCEL_BULK = "/calls/1/bulks/{bulkId}/cancel"


def test_should_get_calls(httpserver: HTTPServer, get_api_client):
    given_call_id = "string"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_application_id = "61c060db2675060027d8c7a6"
    given_from = "44790123456"
    given_to = "44790987654"
    given_direction = "INBOUND"
    given_call_state = "CALLING"
    given_muted = True
    given_user_muted = True
    given_deaf = True
    given_camera = True
    given_screen_share = True
    given_start_time = "2022-05-01T14:25:45.125Z"
    given_answer_time = "2022-05-01T14:25:55.123Z"
    given_end_time = "2022-05-01T14:27:40.235Z"
    given_parent_call_id = "3ad8805e-d401-424e-9b03-e02a2016a5e2"
    given_detection_result = "HUMAN"
    given_ring_duration = 3
    given_conference_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_key1 = "value1"
    given_key2 = "value2"
    given_page = 0
    given_page_size = 1
    given_page_total_pages = 0
    given_page_total_results = 0

    given_response = {
        "results": [
            {
                "id": given_call_id,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "from": given_from,
                "to": given_to,
                "direction": given_direction,
                "state": given_call_state,
                "media": {
                    "audio": {
                        "muted": given_muted,
                        "userMuted": given_user_muted,
                        "deaf": given_deaf,
                    },
                    "video": {
                        "camera": given_camera,
                        "screenShare": given_screen_share,
                    },
                },
                "startTime": given_start_time,
                "answerTime": given_answer_time,
                "endTime": given_end_time,
                "parentCallId": given_parent_call_id,
                "machineDetection": {"detectionResult": given_detection_result},
                "ringDuration": given_ring_duration,
                "platform": {"applicationId": given_application_id},
                "conferenceId": given_conference_id,
                "customData": {"key1": given_key1, "key2": given_key2},
            }
        ],
        "paging": {
            "page": given_page,
            "size": given_page_size,
            "totalPages": given_page_total_pages,
            "totalResults": given_page_total_results,
        },
    }

    api_instance = CallsApi(get_api_client)

    setup_request(httpserver, CALLS, given_response)

    api_response = api_instance.get_calls()

    expected_response: CallPage = CallPage(
        results=[
            Call(
                id=given_call_id,
                endpoint=CallsPhoneEndpoint(
                    phone_number=given_phone_number, type=CallEndpointType.PHONE
                ),
                var_from=given_from,
                to=given_to,
                direction=given_direction,
                state=given_call_state,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_muted, user_muted=given_user_muted, deaf=given_deaf
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_camera, screen_share=given_screen_share
                    ),
                ),
                start_time=given_start_time,
                answer_time=given_answer_time,
                end_time=given_end_time,
                parent_call_id=given_parent_call_id,
                machine_detection=CallsMachineDetectionProperties(
                    detection_result=given_detection_result
                ),
                ring_duration=given_ring_duration,
                platform=Platform(application_id=given_application_id),
                conference_id=given_conference_id,
                custom_data={"key1": given_key1, "key2": given_key2},
            )
        ],
        paging=PageInfo(
            page=given_page,
            size=given_page_size,
            total_pages=given_page_total_pages,
            total_results=given_page_total_results,
        ),
    )

    assert api_response == expected_response


def test_should_create_call(httpserver: HTTPServer, get_api_client):
    givenPhoneNumber = "41792036727"
    givenType = "PHONE"
    givenFrom = "41793026834"
    givenApplicationId = "61c060db2675060027d8c7a6"
    givenCallsConfigurationId = "dc5942707c704551a00cd2ea"
    givenMaxDuration = 28800

    givenRequest = {
        "endpoint": {
            "type": givenType,
            "phoneNumber": givenPhoneNumber,
        },
        "from": givenFrom,
        "callsConfigurationId": givenCallsConfigurationId,
        "maxDuration": givenMaxDuration,
        "platform": {"applicationId": givenApplicationId},
    }

    givenCallId = "d8d84155-3831-43fb-91c9-bb897149a79d"
    givenTo = "44790123456"
    givenDirection = "OUTBOUND"
    givenCallState = "CALLING"
    givenMuted = False
    givenDeaf = False
    givenCamera = False
    givenScreenShare = False
    givenStartTime = "2022-01-01T00:00:00.100+0000"
    givenAnswerTime = "2022-01-01T00:00:02.100+0000"
    givenRingDuration = 2
    givenConferenceId = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    givenKey1 = "value1"
    givenKey2 = "value2"

    given_response = {
        "id": givenCallId,
        "endpoint": {
            "type": givenType,
            "phoneNumber": givenTo,
        },
        "from": givenFrom,
        "to": givenTo,
        "direction": givenDirection,
        "state": givenCallState,
        "media": {
            "audio": {
                "muted": givenMuted,
                "deaf": givenDeaf,
            },
            "video": {
                "camera": givenCamera,
                "screenShare": givenScreenShare,
            },
        },
        "ringDuration": givenRingDuration,
        "callsConfigurationId": givenCallsConfigurationId,
        "platform": {"applicationId": givenApplicationId},
        "conferenceId": givenConferenceId,
        "customData": {"key1": givenKey1, "key2": givenKey2},
    }

    api_instance = CallsApi(get_api_client)

    setup_request(httpserver, CALLS, given_response, "POST", 201, givenRequest)

    request: CallRequest = CallRequest(
        endpoint=CallsPhoneEndpoint(
            type=CallEndpointType.PHONE, phone_number=givenPhoneNumber
        ),
        var_from=givenFrom,
        calls_configuration_id=givenCallsConfigurationId,
        platform=Platform(application_id=givenApplicationId),
    )

    api_response = api_instance.create_call(call_request=request)

    expected_response = Call(
        id=givenCallId,
        endpoint=CallsPhoneEndpoint(type=CallEndpointType.PHONE, phone_number=givenTo),
        var_from=givenFrom,
        to=givenTo,
        direction=CallDirection.OUTBOUND,
        state=CallState.CALLING,
        media=CallsMediaProperties(
            audio=CallsAudioMediaProperties(muted=givenMuted, deaf=givenDeaf),
            video=CallsVideoMediaProperties(
                camera=givenCamera, screen_share=givenScreenShare
            ),
        ),
        ring_duration=givenRingDuration,
        calls_configuration_id=givenCallsConfigurationId,
        platform=Platform(application_id=givenApplicationId),
        conference_id=givenConferenceId,
        custom_data={"key1": givenKey1, "key2": givenKey2},
    )

    assert api_response == expected_response


def test_should_get_a_call(httpserver: HTTPServer, get_api_client):
    givenPhoneNumber = "41792030000"
    givenType = "PHONE"
    givenFrom = "44790123456"
    givenMaxDuration = 28800
    givenApplicationId = "61c060db2675060027d8c7a6"
    givenParentCallId = "3ad8805e-d401-424e-9b03-e02a2016a5e2"
    givenCallId = "d8d84155-3831-43fb-91c9-bb897149a79d"
    givenTo = "44790987654"
    givenDirection = "INBOUND"
    givenCallState = "CALLING"
    givenMuted = True
    givenUserMuted = True
    givenDeaf = True
    givenCamera = True
    givenScreenShare = True
    givenStartTime = "2022-05-01T14:25:45.125Z"
    givenAnswerTime = "2022-05-01T14:25:55.123Z"
    givenEndTime = "2022-05-01T14:27:40.235Z"
    givenDetectionResult = "HUMAN"
    givenRingDuration = 3
    givenConferenceId = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    givenKey1 = "value1"
    givenKey2 = "value2"

    given_response = {
        "id": givenCallId,
        "endpoint": {
            "phoneNumber": givenPhoneNumber,
            "type": givenType,
        },
        "from": givenFrom,
        "to": givenTo,
        "direction": givenDirection,
        "state": givenCallState,
        "media": {
            "audio": {
                "muted": givenMuted,
                "userMuted": givenUserMuted,
                "deaf": givenDeaf,
            },
            "video": {"camera": givenCamera, "screenShare": givenScreenShare},
        },
        "startTime": givenStartTime,
        "answerTime": givenAnswerTime,
        "endTime": givenEndTime,
        "parentCallId": givenParentCallId,
        "machineDetection": {"detectionResult": givenDetectionResult},
        "ringDuration": givenRingDuration,
        "platform": {
            "applicationId": givenApplicationId,
        },
        "conferenceId": givenConferenceId,
        "customData": {"key1": givenKey1, "key2": givenKey2},
    }

    endpoint = CALL.replace("{callId}", givenCallId)

    setup_request(httpserver, endpoint, given_response)

    api_instance = CallsApi(get_api_client)
    api_response = api_instance.get_call(call_id=givenCallId)

    expected_response = Call(
        id=givenCallId,
        endpoint=CallsPhoneEndpoint(
            phone_number=givenPhoneNumber, type=CallEndpointType.PHONE
        ),
        var_from=givenFrom,
        to=givenTo,
        direction=givenDirection,
        state=givenCallState,
        media=CallsMediaProperties(
            audio=CallsAudioMediaProperties(
                muted=givenMuted, user_muted=givenUserMuted, deaf=givenDeaf
            ),
            video=CallsVideoMediaProperties(
                camera=givenCamera, screen_share=givenScreenShare
            ),
        ),
        start_time=givenStartTime,
        end_time=givenEndTime,
        answer_time=givenAnswerTime,
        parent_call_id=givenParentCallId,
        machine_detection=CallsMachineDetectionProperties(
            detection_result=givenDetectionResult
        ),
        ring_duration=givenRingDuration,
        platform=Platform(application_id=givenApplicationId),
        conference_id=givenConferenceId,
        custom_data={"key1": givenKey1, "key2": givenKey2},
    )

    assert api_response == expected_response


def test_should_get_a_call_history(httpserver: HTTPServer, get_api_client):
    given_call_id = "string"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_application_id = "61c060db2675060027d8c7a6"
    given_from = "44790123456"
    given_to = "44790987654"
    given_direction = "INBOUND"
    given_call_state = "CALLING"
    given_muted = True
    given_user_muted = True
    given_deaf = True
    given_camera = True
    given_screen_share = True
    given_start_time = "2022-05-01T14:25:45.125Z"
    given_answer_time = "2022-05-01T14:25:55.123Z"
    given_end_time = "2022-05-01T14:27:40.235Z"
    given_parent_call_id = "3ad8805e-d401-424e-9b03-e02a2016a5e2"
    given_detection_result = "HUMAN"
    given_duration = 5
    given_conference_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_has_camera_video = False
    given_has_screen_share_video = False
    given_error_code_id = 2
    given_error_code_name = "NORMAL_HANGUP"
    given_error_code_description = (
        "The call has ended with hangup initiated by caller, callee or API"
    )
    given_key1 = "value1"
    given_key2 = "value2"
    given_page = 0
    given_page_size = 1
    given_page_total_pages = 0
    given_page_total_results = 0

    given_response = {
        "results": [
            {
                "callId": given_call_id,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "from": given_from,
                "to": given_to,
                "direction": given_direction,
                "state": given_call_state,
                "media": {
                    "audio": {
                        "muted": given_muted,
                        "userMuted": given_user_muted,
                        "deaf": given_deaf,
                    },
                    "video": {
                        "camera": given_camera,
                        "screenShare": given_screen_share,
                    },
                },
                "startTime": given_start_time,
                "answerTime": given_answer_time,
                "endTime": given_end_time,
                "parentCallId": given_parent_call_id,
                "machineDetection": {"detectionResult": given_detection_result},
                "platform": {
                    "applicationId": given_application_id,
                },
                "conferenceIds": [given_conference_id],
                "duration": given_duration,
                "hasCameraVideo": given_has_camera_video,
                "hasScreenshareVideo": given_has_screen_share_video,
                "errorCode": {
                    "id": given_error_code_id,
                    "name": given_error_code_name,
                    "description": given_error_code_description,
                },
                "customData": {"key1": given_key1, "key2": given_key2},
            }
        ],
        "paging": {
            "page": given_page,
            "size": given_page_size,
            "totalPages": given_page_total_pages,
            "totalResults": given_page_total_results,
        },
    }

    api_instance = CallsApi(get_api_client)

    setup_request(httpserver, CALLS_HISTORY, given_response)

    api_response = api_instance.get_calls_history()

    expected_response: CallLogPage = CallLogPage(
        results=[
            CallLog(
                call_id=given_call_id,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                var_from=given_from,
                to=given_to,
                direction=given_direction,
                state=given_call_state,
                start_time=given_start_time,
                answer_time=given_answer_time,
                end_time=given_end_time,
                parent_call_id=given_parent_call_id,
                machine_detection=CallsMachineDetectionProperties(
                    detection_result=given_detection_result
                ),
                platform=Platform(application_id=given_application_id),
                conference_ids=[given_conference_id],
                duration=given_duration,
                has_camera_video=given_has_camera_video,
                has_screenshare_video=given_has_screen_share_video,
                error_code=CallsErrorCodeInfo(
                    id=given_error_code_id,
                    name=given_error_code_name,
                    description=given_error_code_description,
                ),
                custom_data={"key1": given_key1, "key2": given_key2},
                dialog_id=None,
                sender=None,
            )
        ],
        paging=PageInfo(
            page=given_page,
            size=given_page_size,
            total_pages=given_page_total_pages,
            total_results=given_page_total_results,
        ),
    )

    assert api_response == expected_response


def test_should_get_call_history(httpserver: HTTPServer, get_api_client):
    given_call_id = "string"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_application_id = "61c060db2675060027d8c7a6"
    given_from = "44790123456"
    given_to = "44790987654"
    given_direction = "INBOUND"
    given_call_state = "CALLING"
    given_muted = True
    given_user_muted = True
    given_deaf = True
    given_camera = True
    given_screen_share = True
    given_start_time = "2022-05-01T14:25:45.125Z"
    given_answer_time = "2022-05-01T14:25:55.123Z"
    given_end_time = "2022-05-01T14:27:40.235Z"
    given_parent_call_id = "3ad8805e-d401-424e-9b03-e02a2016a5e2"
    given_detection_result = "HUMAN"
    given_duration = 5
    given_conference_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_has_camera_video = False
    given_has_screen_share_video = False
    given_error_code_id = 2
    given_error_code_name = "NORMAL_HANGUP"
    given_error_code_description = (
        "The call has ended with hangup initiated by caller, callee or API"
    )
    given_key1 = "value1"
    given_key2 = "value2"

    given_response = {
        "callId": given_call_id,
        "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
        "from": given_from,
        "to": given_to,
        "direction": given_direction,
        "state": given_call_state,
        "media": {
            "audio": {
                "muted": given_muted,
                "userMuted": given_user_muted,
                "deaf": given_deaf,
            },
            "video": {"camera": given_camera, "screenShare": given_screen_share},
        },
        "startTime": given_start_time,
        "answerTime": given_answer_time,
        "endTime": given_end_time,
        "parentCallId": given_parent_call_id,
        "machineDetection": {"detectionResult": given_detection_result},
        "platform": {
            "applicationId": given_application_id,
        },
        "conferenceIds": [given_conference_id],
        "duration": given_duration,
        "hasCameraVideo": given_has_camera_video,
        "hasScreenshareVideo": given_has_screen_share_video,
        "errorCode": {
            "id": given_error_code_id,
            "name": given_error_code_name,
            "description": given_error_code_description,
        },
        "customData": {"key1": given_key1, "key2": given_key2},
    }

    endpoint = CALL_HISTORY.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response)

    api_instance = CallsApi(get_api_client)
    api_response = api_instance.get_call_history(call_id=given_call_id)

    expected_response: CallLog = CallLog(
        call_id=given_call_id,
        endpoint=CallsPhoneEndpoint(type=given_type, phone_number=given_phone_number),
        var_from=given_from,
        to=given_to,
        direction=given_direction,
        state=given_call_state,
        start_time=given_start_time,
        answer_time=given_answer_time,
        end_time=given_end_time,
        parent_call_id=given_parent_call_id,
        machine_detection=CallsMachineDetectionProperties(
            detection_result=given_detection_result
        ),
        platform=Platform(application_id=given_application_id),
        conference_ids=[given_conference_id],
        duration=given_duration,
        has_camera_video=given_has_camera_video,
        has_screenshare_video=given_has_screen_share_video,
        error_code=CallsErrorCodeInfo(
            id=given_error_code_id,
            name=given_error_code_name,
            description=given_error_code_description,
        ),
        custom_data={"key1": given_key1, "key2": given_key2},
        dialog_id=None,
        sender=None,
    )

    assert api_response == expected_response


def test_should_connect_calls(httpserver: HTTPServer, get_api_client):
    given_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_name = "Example conference"
    given_call_id1 = "d6d6058c-5077-49f9-a030-2fc40e8ca195"
    given_call_id2 = "6539fcb4-4b2a-4ac9-a43a-d60807af29b0"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_state = "JOINING"
    given_join_time = "2022-05-01T14:25:45.0Z"
    given_audio_muted = True
    given_audio_user_deaf = True
    given_video_camera = True
    given_video_screen_share = True
    given_application_id = "61c060db2675060027d8c7a6"

    participants = [
        {
            "callId": given_call_id1,
            "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
            "state": given_state,
            "joinTime": given_join_time,
            "media": {
                "audio": {"muted": given_audio_muted, "deaf": given_audio_user_deaf},
                "video": {
                    "camera": given_video_camera,
                    "screenShare": given_video_screen_share,
                },
            },
        },
        {
            "callId": given_call_id2,
            "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
            "state": given_state,
            "joinTime": given_join_time,
            "media": {
                "audio": {"muted": given_audio_muted, "deaf": given_audio_user_deaf},
                "video": {
                    "camera": given_video_camera,
                    "screenShare": given_video_screen_share,
                },
            },
        },
    ]

    given_response = {
        "id": given_id,
        "name": given_name,
        "participants": participants,
        "platform": {"applicationId": given_application_id},
    }

    expected_request = {"callIds": [given_call_id1, given_call_id2]}

    request: CallsConnectRequest = CallsConnectRequest(
        call_ids=[given_call_id1, given_call_id2]
    )

    setup_request(
        httpserver, CONNECT_CALLS, given_response, "POST", 200, expected_request
    )

    api_instance = CallsApi(get_api_client)
    api_response = api_instance.connect_calls(calls_connect_request=request)

    expected_response = CallsConference(
        id=given_id,
        name=given_name,
        participants=[
            CallsParticipant(
                call_id=given_call_id1,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                state=given_state,
                join_time=given_join_time,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_audio_muted, deaf=given_audio_user_deaf
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_video_camera, screen_share=given_video_screen_share
                    ),
                ),
            ),
            CallsParticipant(
                call_id=given_call_id2,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                state=given_state,
                join_time=given_join_time,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_audio_muted, deaf=given_audio_user_deaf
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_video_camera, screen_share=given_video_screen_share
                    ),
                ),
            ),
        ],
        platform=Platform(application_id=given_application_id),
    )

    assert api_response == expected_response


def test_should_connect_with_new_call(httpserver: HTTPServer, get_api_client):
    given_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_name = "Example conference"
    given_call_id = "string"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_state = "JOINING"
    given_join_time = "2022-05-01T14:25:45.0Z"
    given_audio_muted = True
    given_audio_user_muted = True
    given_audio_user_deaf = True
    given_video_camera = True
    given_video_screen_share = True
    given_application_id = "61c060db2675060027d8c7a6"
    given_from = "44790123456"
    given_to = "44790987654"
    given_direction = "INBOUND"
    given_call_state = "CALLING"
    given_muted = True
    given_user_muted = True
    given_deaf = True
    given_camera = True
    given_screen_share = True
    given_start_time = "2022-05-01T14:25:45.0+0000"
    given_answer_time = "2022-05-01T14:25:55.0+0000"
    given_end_time = "2022-05-01T14:27:40.0+0000"
    given_parent_call_id = "3ad8805e-d401-424e-9b03-e02a2016a5e2"
    given_detection_result = "HUMAN"
    given_conference_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_key1 = "value1"
    given_key2 = "value2"

    given_response = {
        "conference": {
            "id": given_id,
            "name": given_name,
            "participants": [
                {
                    "callId": given_call_id,
                    "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                    "state": given_state,
                    "joinTime": given_join_time,
                    "media": {
                        "audio": {
                            "muted": given_audio_muted,
                            "userMuted": given_audio_user_muted,
                            "deaf": given_audio_user_deaf,
                        },
                        "video": {
                            "camera": given_video_camera,
                            "screenShare": given_video_screen_share,
                        },
                    },
                }
            ],
            "applicationId": given_application_id,
        },
        "call": {
            "id": given_call_id,
            "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
            "from": given_from,
            "to": given_to,
            "direction": given_direction,
            "state": given_call_state,
            "media": {
                "audio": {
                    "muted": given_muted,
                    "userMuted": given_user_muted,
                    "deaf": given_deaf,
                },
                "video": {"camera": given_camera, "screenShare": given_screen_share},
            },
            "startTime": given_start_time,
            "answerTime": given_answer_time,
            "endTime": given_end_time,
            "parentCallId": given_parent_call_id,
            "machineDetection": {"detectionResult": given_detection_result},
            "platform": {"applicationId": given_application_id},
            "conferenceId": given_conference_id,
            "customData": {"key1": given_key1, "key2": given_key2},
        },
    }

    given_connect_on_early_media = False

    endpoint = CONNECT_CALL.replace("{callId}", given_call_id)

    setup_request(
        httpserver,
        endpoint,
        expected_response=given_response,
        http_verb="POST",
        status_code=200,
        request_body=None,
    )

    request: CallsConnectWithNewCallRequest = CallsConnectWithNewCallRequest(
        call_request=CallsActionCallRequest(
            endpoint=CallsPhoneEndpoint(
                phone_number=given_phone_number, type=CallEndpointType.PHONE
            ),
            var_from=given_from,
        ),
        connect_on_early_media=given_connect_on_early_media,
    )

    api_instance = CallsApi(get_api_client)
    api_response = api_instance.connect_with_new_call(
        calls_connect_with_new_call_request=request, call_id=given_call_id
    )

    expected_response: CallsConferenceAndCall = CallsConferenceAndCall(
        conference=CallsConference(
            id=given_id,
            name=given_name,
            participants=[
                CallsParticipant(
                    call_id=given_call_id,
                    endpoint=CallsPhoneEndpoint(
                        type=given_type, phone_number=given_phone_number
                    ),
                    state=given_state,
                    join_time=given_join_time,
                    media=CallsMediaProperties(
                        audio=CallsAudioMediaProperties(
                            muted=given_muted,
                            user_muted=given_user_muted,
                            deaf=given_deaf,
                        ),
                        video=CallsVideoMediaProperties(
                            camera=given_camera, screen_share=given_screen_share
                        ),
                    ),
                )
            ],
            application_id=given_application_id,
        ),
        call=Call(
            id=given_call_id,
            endpoint=CallsPhoneEndpoint(
                type=given_type, phone_number=given_phone_number
            ),
            var_from=given_from,
            to=given_to,
            direction=given_direction,
            state=given_call_state,
            media=CallsMediaProperties(
                audio=CallsAudioMediaProperties(
                    muted=given_muted, user_muted=given_user_muted, deaf=given_deaf
                ),
                video=CallsVideoMediaProperties(
                    camera=given_camera, screen_share=given_screen_share
                ),
            ),
            start_time=given_start_time,
            answer_time=given_answer_time,
            end_time=given_end_time,
            parent_call_id=given_parent_call_id,
            machine_detection=CallsMachineDetectionProperties(
                detection_result=given_detection_result
            ),
            platform=Platform(application_id=given_application_id),
            conference_id=given_conference_id,
            custom_data={"key1": given_key1, "key2": given_key2},
        ),
    )

    assert api_response == expected_response


def test_should_pre_answer_call(httpserver: HTTPServer, get_api_client):
    given_ringing = False
    given_property1 = "data"

    given_request = {
        "ringing": given_ringing,
        "custom_data": {"property1": given_property1},
    }

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = PRE_ANSWER_CALL.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    request: CallsPreAnswerRequest = CallsPreAnswerRequest(
        ringing=given_ringing, custom_data={"property1": given_property1}
    )

    api_response = api_instance.pre_answer_call(
        calls_pre_answer_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=CallsActionStatus.PENDING)

    assert api_response == expected_response


def test_should_answer(httpserver: HTTPServer, get_api_client):
    given_property1 = "string"
    given_property2 = "string"
    given_recording_type = "AUDIO"
    given_file_prefix = "string"

    given_request = {
        "customData": {"property1": given_property1, "property2": given_property2},
        "recording": {
            "recordingType": given_recording_type,
            "customData": {"property1": given_property1, "property2": given_property2},
            "filePrefix": given_file_prefix,
        },
    }

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = ANSWER_CALL.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    request: CallsAnswerRequest = CallsAnswerRequest(
        custom_data={"property1": given_property1, "property2": given_property2},
        recording=CallRecordingRequest(
            recording_type=given_recording_type,
            custom_data={"property1": given_property1, "property2": given_property2},
            file_prefix=given_file_prefix,
        ),
    )

    api_response = api_instance.answer_call(
        calls_answer_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=CallsActionStatus.PENDING)

    assert api_response == expected_response


def test_should_hangup(httpserver: HTTPServer, get_api_client):
    givenErrorCode = "NORMAL_HANGUP"

    givenCallId = "d8d84155-3831-43fb-91c9-bb897149a79d"
    givenPhoneNumber = "44790123456"
    givenType = "PHONE"
    givenFrom = "44790123456"
    givenTo = "44790123456"
    givenDirection = "OUTBOUND"
    givenState = "CALLING"
    givenAudioMuted = False
    givenAudioDeaf = False
    givenVideoCamera = False
    givenVideoScreenShare = False
    givenStartTime = "2022-01-01T00:00:00.100Z"
    givenAnswerTime = "2022-01-01T00:00:00.100Z"
    givenRingDuration = 2
    givenApplicationId = "61c060db2675060027d8c7a6"
    givenConferenceId = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    givenKey2 = "value2"
    givenKey1 = "value1"

    given_response = {
        "id": givenCallId,
        "endpoint": {"phoneNumber": givenPhoneNumber, "type": givenType},
        "from": givenFrom,
        "to": givenTo,
        "direction": givenDirection,
        "state": givenState,
        "media": {
            "audio": {"muted": givenAudioMuted, "deaf": givenAudioDeaf},
            "video": {"camera": givenVideoCamera, "screenShare": givenVideoScreenShare},
        },
        "startTime": givenStartTime,
        "answerTime": givenAnswerTime,
        "ringDuration": givenRingDuration,
        "platform": {
            "applicationId": givenApplicationId,
        },
        "conferenceId": givenConferenceId,
        "customData": {"key2": givenKey2, "key1": givenKey1},
    }

    expected_request = {"errorCode": givenErrorCode}

    endpoint = HANGUP_CALL.replace("{callId}", givenCallId)

    setup_request(httpserver, endpoint, given_response, "POST", 200, expected_request)

    api_instance = CallsApi(get_api_client)

    request: CallsHangupRequest = CallsHangupRequest(error_code=givenErrorCode)

    api_response = api_instance.hangup_call(
        calls_hangup_request=request, call_id=givenCallId
    )

    expected_response = Call(
        id=givenCallId,
        endpoint=CallsPhoneEndpoint(type=givenType, phone_number=givenPhoneNumber),
        var_from=givenFrom,
        to=givenTo,
        direction=givenDirection,
        state=givenState,
        media=CallsMediaProperties(
            audio=CallsAudioMediaProperties(muted=givenAudioMuted, deaf=givenAudioDeaf),
            video=CallsVideoMediaProperties(
                camera=givenVideoCamera, screen_share=givenVideoScreenShare
            ),
        ),
        start_time=givenStartTime,
        answer_time=givenAnswerTime,
        ring_duration=givenRingDuration,
        platform=Platform(application_id=givenApplicationId),
        conference_id=givenConferenceId,
        custom_data={"key2": givenKey2, "key1": givenKey1},
    )

    assert api_response == expected_response


def test_should_play_file(httpserver: HTTPServer, get_api_client):
    givenCallId = "123"

    givenStatus = "PENDING"
    givenLoopCount = 0
    givenContentType = "FILE"
    givenFileId = "100"

    given_response = {"status": givenStatus}

    endpoint = CALL_PLAY_FILE.replace("{callId}", givenCallId)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    request: CallsPlayRequest = CallsPlayRequest(
        content=CallsPlayContent(file_id=givenFileId, type=givenContentType),
        loop_count=givenLoopCount,
    )

    api_response = api_instance.call_play_file(
        calls_play_request=request, call_id=givenCallId
    )

    expected_response = CallsActionResponse(status=givenStatus)

    assert api_response == expected_response


def test_should_stop_playing_file(httpserver: HTTPServer, get_api_client):
    given_property1 = "string"
    given_property2 = "string"

    given_request = {
        "customData": {"property1": given_property1, "property2": given_property2}
    }

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = CALL_STOP_PLAYING_FILE.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsStopPlayRequest = CallsStopPlayRequest(
        custom_data={"property1": given_property1, "property2": given_property2}
    )

    api_response = api_instance.call_stop_playing_file(
        calls_stop_play_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_say_text(httpserver: HTTPServer, get_api_client):
    given_text = "This is an example of text to speech"
    given_language = "en"

    given_request = {"text": given_text, "language": given_language}

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = CALL_SAY_TEXT.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsSayRequest = CallsSayRequest(text=given_text, language=given_language)

    api_response = api_instance.call_say_text(
        calls_say_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_send_dtmf(httpserver: HTTPServer, get_api_client):
    given_dtmf = "3"

    given_request = {"dtmf": given_dtmf}

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = CALL_SEND_DTMF.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsDtmfSendRequest = CallsDtmfSendRequest(dtmf=given_dtmf)

    api_response = api_instance.call_send_dtmf(
        calls_dtmf_send_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_capture_dtmf(httpserver: HTTPServer, get_api_client):
    given_max_length = 4
    given_timeout = 5000
    given_terminator = "#"
    given_digit_timeout = 3000

    given_request = {
        "maxLength": 4,
        "timeout": 5000,
        "terminator": "#",
        "digitTimeout": 3000,
    }

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = CALL_CAPTURE_DTMF.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsDtmfCaptureRequest = CallsDtmfCaptureRequest(
        max_length=given_max_length,
        timeout=given_timeout,
        terminator=given_terminator,
        digit_timeout=given_digit_timeout,
    )

    api_response = api_instance.call_capture_dtmf(
        calls_dtmf_capture_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_capture_speech(httpserver: HTTPServer, get_api_client):
    given_langauge = CallTranscriptionLanguage.EN_MINUS_US
    given_timeout = 30
    given_max_silence = 4
    given_key_phrases = ["phrase", "word"]

    given_request = {
        "language": given_langauge,
        "timeout": given_timeout,
        "maxSilence": given_max_silence,
        "keyPhrases": given_key_phrases,
    }

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = CALL_CAPTURE_SPEECH.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsSpeechCaptureRequest = CallsSpeechCaptureRequest(
        language=given_langauge,
        timeout=given_timeout,
        max_silence=given_max_silence,
        key_phrases=given_key_phrases,
    )

    api_response = api_instance.call_capture_speech(
        calls_speech_capture_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_start_recording(httpserver: HTTPServer, get_api_client):
    given_recording_type = "AUDIO"

    given_request = {"recording": {"recordingType": given_recording_type}}

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = CALL_START_RECORDING.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    request: CallsRecordingStartRequest = CallsRecordingStartRequest(
        recording=CallsRecordingRequest(recording_type=given_recording_type)
    )

    api_response = api_instance.call_start_recording(
        calls_recording_start_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_stop_recording(httpserver: HTTPServer, get_api_client):
    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = CALL_STOP_RECORDING.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.call_stop_recording(call_id=given_call_id)

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_start_streaming_media(httpserver: HTTPServer, get_api_client):
    given_media_stream_config_id = "63467c6e2885a5389ba11d80"
    given_replace_media = False

    given_request = {
        "mediaStream": {
            "audioProperties": {
                "mediaStreamConfigId": given_media_stream_config_id,
                "replaceMedia": given_replace_media,
            }
        }
    }

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = START_MEDIA_STREAM.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsStartMediaStreamRequest = CallsStartMediaStreamRequest(
        media_stream=CallsMediaStream(
            audio_properties=CallsMediaStreamAudioProperties(
                media_stream_config_id=given_media_stream_config_id,
                replace_media=given_replace_media,
            )
        )
    )

    api_response = api_instance.start_media_stream(
        calls_start_media_stream_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_stop_streaming_media(httpserver: HTTPServer, get_api_client):
    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = STOP_MEDIA_STREAM.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.stop_media_stream(call_id=given_call_id)

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_request_application_transfer(httpserver: HTTPServer, get_api_client):
    given_destination_application_id = "61c060db2675060027d8c7a6"
    given_timeout = 20

    given_request = {
        "destinationCallsConfigurationId": given_destination_application_id,
        "timeout": given_timeout,
    }

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"

    endpoint = APPLICATION_TRANSFER.replace("{callId}", given_call_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsApplicationTransferRequest = CallsApplicationTransferRequest(
        destination_calls_configuration_id=given_destination_application_id,
        timeout=given_timeout,
    )

    api_response = api_instance.application_transfer(
        calls_application_transfer_request=request, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_accept_application_transfer(httpserver: HTTPServer, get_api_client):
    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"
    given_transfer_id = "123"

    endpoint = APPLICATION_TRANSFER_ACCEPT.replace("{callId}", given_call_id).replace(
        "{transferId}", given_transfer_id
    )

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.application_transfer_accept(
        call_id=given_call_id, transfer_id=given_transfer_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_reject_application_transfer(httpserver: HTTPServer, get_api_client):
    given_status = "PENDING"

    given_response = {"status": given_status}

    given_call_id = "123"
    given_transfer_id = "123"

    endpoint = APPLICATION_TRANSFER_REJECT.replace("{callId}", given_call_id).replace(
        "{transferId}", given_transfer_id
    )

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.application_transfer_reject(
        call_id=given_call_id, transfer_id=given_transfer_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_get_conferences(httpserver: HTTPServer, get_api_client):
    given_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_name = "Example conference"
    given_call_id = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_call_id_2 = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_state = "JOINING"
    given_join_time = "2022-05-01T14:25:45.134Z"
    given_audio_muted = True
    given_audio_user_muted = True
    given_audio_user_deaf = True
    given_video_camera = True
    given_video_screen_share = True
    given_application_id = "61c060db2675060027d8c7a6"
    given_page = 0
    given_size = 1
    given_total_pages = 1
    given_total_results = 1

    given_response = {
        "results": [
            {
                "id": given_id,
                "name": given_name,
                "participants": [
                    {
                        "callId": given_call_id,
                        "endpoint": {
                            "phoneNumber": given_phone_number,
                            "type": given_type,
                        },
                        "state": given_state,
                        "joinTime": given_join_time,
                        "media": {
                            "audio": {
                                "muted": given_audio_muted,
                                "userMuted": given_audio_user_muted,
                                "deaf": given_audio_user_deaf,
                            },
                            "video": {
                                "camera": given_video_camera,
                                "screenShare": given_video_screen_share,
                            },
                        },
                    },
                    {
                        "callId": given_call_id_2,
                        "endpoint": {
                            "phoneNumber": given_phone_number,
                            "type": given_type,
                        },
                        "state": given_state,
                        "joinTime": given_join_time,
                        "media": {
                            "audio": {
                                "muted": given_audio_muted,
                                "userMuted": given_audio_user_muted,
                                "deaf": given_audio_user_deaf,
                            },
                            "video": {
                                "camera": given_video_camera,
                                "screenShare": given_video_screen_share,
                            },
                        },
                    },
                ],
                "platform": {
                    "applicationId": given_application_id,
                },
            }
        ],
        "paging": {
            "page": given_page,
            "size": given_size,
            "totalPages": given_total_pages,
            "totalResults": given_total_results,
        },
    }

    setup_request(httpserver, CONFERENCES, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_conferences()

    expected_response = CallsConferencePage(
        results=[
            CallsConference(
                id=given_id,
                name=given_name,
                participants=[
                    CallsParticipant(
                        call_id=given_call_id,
                        endpoint=CallsPhoneEndpoint(
                            type=given_type, phone_number=given_phone_number
                        ),
                        state=given_state,
                        join_time=given_join_time,
                        media=CallsMediaProperties(
                            audio=CallsAudioMediaProperties(
                                muted=given_audio_muted,
                                user_muted=given_audio_user_muted,
                                deaf=given_audio_user_deaf,
                            ),
                            video=CallsVideoMediaProperties(
                                camera=given_video_camera,
                                screen_share=given_video_screen_share,
                            ),
                        ),
                    ),
                    CallsParticipant(
                        call_id=given_call_id_2,
                        endpoint=CallsPhoneEndpoint(
                            type=given_type, phone_number=given_phone_number
                        ),
                        state=given_state,
                        join_time=given_join_time,
                        media=CallsMediaProperties(
                            audio=CallsAudioMediaProperties(
                                muted=given_audio_muted,
                                user_muted=given_audio_user_muted,
                                deaf=given_audio_user_deaf,
                            ),
                            video=CallsVideoMediaProperties(
                                camera=given_video_camera,
                                screen_share=given_video_screen_share,
                            ),
                        ),
                    ),
                ],
                platform=Platform(
                    application_id=given_application_id,
                ),
            )
        ],
        paging=PageInfo(
            page=given_page,
            size=given_size,
            total_pages=given_total_pages,
            total_results=given_total_results,
        ),
    )

    assert api_response == expected_response


def test_should_create_conference(httpserver: HTTPServer, get_api_client):
    given_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_name = "Example conference"
    given_call_id = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_call_id_2 = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_state = "JOINING"
    given_join_time = "2022-05-01T14:25:45.134Z"
    given_audio_muted = True
    given_audio_user_muted = True
    given_audio_user_deaf = True
    given_video_camera = True
    given_video_screen_share = True
    given_application_id = "61c060db2675060027d8c7a6"
    given_calls_configuration_id = "dc5942707c704551a00cd2ea"

    given_response = {
        "id": given_id,
        "name": given_name,
        "participants": [
            {
                "callId": given_call_id,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "state": given_state,
                "joinTime": given_join_time,
                "media": {
                    "audio": {
                        "muted": given_audio_muted,
                        "userMuted": given_audio_user_muted,
                        "deaf": given_audio_user_deaf,
                    },
                    "video": {
                        "camera": given_video_camera,
                        "screenShare": given_video_screen_share,
                    },
                },
            },
            {
                "callId": given_call_id_2,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "state": given_state,
                "joinTime": given_join_time,
                "media": {
                    "audio": {
                        "muted": given_audio_muted,
                        "userMuted": given_audio_user_muted,
                        "deaf": given_audio_user_deaf,
                    },
                    "video": {
                        "camera": given_video_camera,
                        "screenShare": given_video_screen_share,
                    },
                },
            },
        ],
        "platform": {
            "applicationId": given_application_id,
        },
    }

    setup_request(httpserver, CONFERENCES, given_response, "POST", 201, None)

    api_instance = CallsApi(get_api_client)

    request: CallsConferenceRequest = CallsConferenceRequest(
        name=given_name,
        calls_configuration_id=given_calls_configuration_id,
        platform=Platform(application_id=given_application_id),
    )

    api_response = api_instance.create_conference(calls_conference_request=request)

    expected_response = CallsConference(
        id=given_id,
        name=given_name,
        participants=[
            CallsParticipant(
                call_id=given_call_id,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                state=given_state,
                join_time=given_join_time,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_audio_muted,
                        user_muted=given_audio_user_muted,
                        deaf=given_audio_user_deaf,
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_video_camera, screen_share=given_video_screen_share
                    ),
                ),
            ),
            CallsParticipant(
                call_id=given_call_id_2,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                state=given_state,
                join_time=given_join_time,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_audio_muted,
                        user_muted=given_audio_user_muted,
                        deaf=given_audio_user_deaf,
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_video_camera, screen_share=given_video_screen_share
                    ),
                ),
            ),
        ],
        platform=Platform(
            application_id=given_application_id,
        ),
    )

    assert api_response == expected_response


def test_should_get_conference(httpserver: HTTPServer, get_api_client):
    given_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_name = "Example conference"
    given_call_id = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_call_id_2 = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_state = "JOINING"
    given_join_time = "2022-05-01T14:25:45.134Z"
    given_audio_muted = True
    given_audio_user_muted = True
    given_audio_user_deaf = True
    given_video_camera = True
    given_video_screen_share = True
    given_application_id = "61c060db2675060027d8c7a6"

    given_response = {
        "id": given_id,
        "name": given_name,
        "participants": [
            {
                "callId": given_call_id,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "state": given_state,
                "joinTime": given_join_time,
                "media": {
                    "audio": {
                        "muted": given_audio_muted,
                        "userMuted": given_audio_user_muted,
                        "deaf": given_audio_user_deaf,
                    },
                    "video": {
                        "camera": given_video_camera,
                        "screenShare": given_video_screen_share,
                    },
                },
            },
            {
                "callId": given_call_id_2,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "state": given_state,
                "joinTime": given_join_time,
                "media": {
                    "audio": {
                        "muted": given_audio_muted,
                        "userMuted": given_audio_user_muted,
                        "deaf": given_audio_user_deaf,
                    },
                    "video": {
                        "camera": given_video_camera,
                        "screenShare": given_video_screen_share,
                    },
                },
            },
        ],
        "platform": {
            "applicationId": given_application_id,
        },
    }

    given_conference_id = "123"
    endpoint = CONFERENCE.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_conference(conference_id=given_conference_id)

    expected_response = CallsConference(
        id=given_id,
        name=given_name,
        participants=[
            CallsParticipant(
                call_id=given_call_id,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                state=given_state,
                join_time=given_join_time,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_audio_muted,
                        user_muted=given_audio_user_muted,
                        deaf=given_audio_user_deaf,
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_video_camera, screen_share=given_video_screen_share
                    ),
                ),
            ),
            CallsParticipant(
                call_id=given_call_id_2,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                state=given_state,
                join_time=given_join_time,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_audio_muted,
                        user_muted=given_audio_user_muted,
                        deaf=given_audio_user_deaf,
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_video_camera, screen_share=given_video_screen_share
                    ),
                ),
            ),
        ],
        platform=Platform(
            application_id=given_application_id,
        ),
    )

    assert api_response == expected_response


def test_update_all_calls(httpserver: HTTPServer, get_api_client):
    given_muted = True

    given_request = {"muted": given_muted}

    given_status = CallsActionStatus.PENDING

    given_response = {"status": given_status}

    given_conference_id = "123"

    endpoint = CONFERENCE.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "PATCH", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsUpdateRequest = CallsUpdateRequest(muted=given_muted)

    api_response = api_instance.update_conference(
        calls_update_request=request, conference_id=given_conference_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_add_new_call(httpserver: HTTPServer, get_api_client):
    given_type = "PHONE"
    given_phone_number = "41792036727"
    given_from = "41793026834"
    given_connect_on_early_media = False

    given_request = {
        "callRequest": {
            "endpoint": {"type": given_type, "phoneNumber": given_phone_number},
            "from": given_from,
        },
        "connectOnEarlyMedia": given_connect_on_early_media,
    }
    given_call_id_2 = "d8d84155-3831-43fb-91c9-bb897149a79d"

    given_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_name = "Example conference"
    given_call_id = "string"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_state = "JOINING"
    given_join_time = "2022-05-01T14:25:45.0Z"
    given_audio_muted = True
    given_audio_user_muted = True
    given_audio_user_deaf = True
    given_video_camera = True
    given_video_screen_share = True
    given_application_id = "61c060db2675060027d8c7a6"
    given_from = "44790123456"
    given_to = "44790987654"
    given_direction = "INBOUND"
    given_call_state = "CALLING"
    given_muted = True
    given_user_muted = True
    given_deaf = True
    given_camera = True
    given_screen_share = True
    given_start_time = "2022-05-01T14:25:45.0+0000"
    given_answer_time = "2022-05-01T14:25:55.0+0000"
    given_end_time = "2022-05-01T14:27:40.0+0000"
    given_parent_call_id = "3ad8805e-d401-424e-9b03-e02a2016a5e2"
    given_detection_result = CallsDetectionResult.HUMAN
    given_conference_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_key1 = "value1"
    given_key2 = "value2"

    given_response = {
        "conference": {
            "id": given_id,
            "name": given_name,
            "participants": [
                {
                    "callId": given_call_id,
                    "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                    "state": given_state,
                    "joinTime": given_join_time,
                    "media": {
                        "audio": {
                            "muted": given_audio_muted,
                            "userMuted": given_audio_user_muted,
                            "deaf": given_audio_user_deaf,
                        },
                        "video": {
                            "camera": given_video_camera,
                            "screenShare": given_video_screen_share,
                        },
                    },
                },
                {
                    "callId": given_call_id_2,
                    "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                    "state": given_state,
                    "joinTime": given_join_time,
                    "media": {
                        "audio": {
                            "muted": given_audio_muted,
                            "userMuted": given_audio_user_muted,
                            "deaf": given_audio_user_deaf,
                        },
                        "video": {
                            "camera": given_video_camera,
                            "screenShare": given_video_screen_share,
                        },
                    },
                },
            ],
            "applicationId": given_application_id,
        },
        "call": {
            "id": given_call_id,
            "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
            "from": given_from,
            "to": given_to,
            "direction": given_direction,
            "state": given_call_state,
            "media": {
                "audio": {
                    "muted": given_muted,
                    "userMuted": given_user_muted,
                    "deaf": given_deaf,
                },
                "video": {"camera": given_camera, "screenShare": given_screen_share},
            },
            "startTime": given_start_time,
            "answerTime": given_answer_time,
            "endTime": given_end_time,
            "parentCallId": given_parent_call_id,
            "machineDetection": {"detectionResult": given_detection_result},
            "platform": {
                "applicationId": given_application_id,
            },
            "conferenceId": given_conference_id,
            "customData": {"key1": given_key1, "key2": given_key2},
        },
    }

    endpoint = CONFERENCE_CALLS.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    request: CallsAddNewCallRequest = CallsAddNewCallRequest(
        call_request=CallsActionCallRequest(
            endpoint=CallsPhoneEndpoint(
                type=given_type, phone_number=given_phone_number
            ),
            var_from=given_from,
        ),
        connect_on_early_media=given_connect_on_early_media,
    )

    api_response = api_instance.add_new_conference_call(
        calls_add_new_call_request=request, conference_id=given_conference_id
    )

    expected_response = CallsConferenceAndCall(
        conference=CallsConference(
            id=given_id,
            name=given_name,
            participants=[
                CallsParticipant(
                    call_id=given_call_id,
                    endpoint=CallsPhoneEndpoint(
                        type=given_type, phone_number=given_phone_number
                    ),
                    state=given_state,
                    join_time=given_join_time,
                    media=CallsMediaProperties(
                        audio=CallsAudioMediaProperties(
                            muted=given_audio_muted,
                            user_muted=given_audio_user_muted,
                            deaf=given_audio_user_deaf,
                        ),
                        video=CallsVideoMediaProperties(
                            camera=given_video_camera,
                            screen_share=given_video_screen_share,
                        ),
                    ),
                ),
                CallsParticipant(
                    call_id=given_call_id_2,
                    endpoint=CallsPhoneEndpoint(
                        type=given_type, phone_number=given_phone_number
                    ),
                    state=given_state,
                    join_time=given_join_time,
                    media=CallsMediaProperties(
                        audio=CallsAudioMediaProperties(
                            muted=given_audio_muted,
                            user_muted=given_audio_user_muted,
                            deaf=given_audio_user_deaf,
                        ),
                        video=CallsVideoMediaProperties(
                            camera=given_video_camera,
                            screen_share=given_video_screen_share,
                        ),
                    ),
                ),
            ],
            application_id=given_application_id,
        ),
        call=Call(
            id=given_call_id,
            endpoint=CallsPhoneEndpoint(
                type=given_type, phone_number=given_phone_number
            ),
            var_from=given_from,
            to=given_to,
            direction=given_direction,
            state=given_call_state,
            media=CallsMediaProperties(
                audio=CallsAudioMediaProperties(
                    muted=given_muted, user_muted=given_user_muted, deaf=given_deaf
                ),
                video=CallsVideoMediaProperties(
                    camera=given_camera, screen_share=given_screen_share
                ),
            ),
            start_time=given_start_time,
            answer_time=given_answer_time,
            end_time=given_end_time,
            parent_call_id=given_parent_call_id,
            machine_detection=CallsMachineDetectionProperties(
                detection_result=given_detection_result
            ),
            platform=Platform(
                application_id=given_application_id,
            ),
            conference_id=given_conference_id,
            custom_data={"key1": given_key1, "key2": given_key2},
        ),
    )

    assert api_response == expected_response


def test_should_add_existing_call(httpserver: HTTPServer, get_api_client):
    given_connect_on_early_media = False

    given_request = {"connectOnEarlyMedia": given_connect_on_early_media}

    given_call_id_2 = "d8d84155-3831-43fb-91c9-bb897149a79d"

    given_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_name = "Example conference"
    given_call_id = "string"
    given_phone_number = "41792030000"
    given_type = CallEndpointType.PHONE
    given_state = "JOINING"
    given_join_time = "2022-05-01T14:25:45.0Z"
    given_audio_muted = True
    given_audio_user_muted = True
    given_audio_user_deaf = True
    given_video_camera = True
    given_video_screen_share = True
    given_application_id = "61c060db2675060027d8c7a6"
    given_from = "44790123456"
    given_to = "44790987654"
    given_direction = "INBOUND"
    given_call_state = "CALLING"
    given_muted = True
    given_user_muted = True
    given_deaf = True
    given_camera = True
    given_screen_share = True
    given_start_time = "2022-05-01T14:25:45.0+0000"
    given_answer_time = "2022-05-01T14:25:55.0+0000"
    given_end_time = "2022-05-01T14:27:40.0+0000"
    given_parent_call_id = "3ad8805e-d401-424e-9b03-e02a2016a5e2"
    given_detection_result = "HUMAN"
    given_conference_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_key1 = "value1"
    given_key2 = "value2"

    given_response = {
        "id": given_id,
        "name": given_name,
        "participants": [
            {
                "callId": given_call_id,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "state": given_state,
                "joinTime": given_join_time,
                "media": {
                    "audio": {
                        "muted": given_audio_muted,
                        "userMuted": given_audio_user_muted,
                        "deaf": given_audio_user_deaf,
                    },
                    "video": {
                        "camera": given_video_camera,
                        "screenShare": given_video_screen_share,
                    },
                },
            },
            {
                "callId": given_call_id_2,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "state": given_state,
                "joinTime": given_join_time,
                "media": {
                    "audio": {
                        "muted": given_audio_muted,
                        "userMuted": given_audio_user_muted,
                        "deaf": given_audio_user_deaf,
                    },
                    "video": {
                        "camera": given_video_camera,
                        "screenShare": given_video_screen_share,
                    },
                },
            },
        ],
        "platform": {"applicationId": given_application_id},
    }

    endpoint = CONFERENCE_CALL.replace("{conferenceId}", given_conference_id).replace(
        "{callId}", given_call_id_2
    )

    setup_request(httpserver, endpoint, given_response, "PUT", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsAddExistingCallRequest = CallsAddExistingCallRequest(
        connect_on_early_media=given_connect_on_early_media
    )

    api_response = api_instance.add_existing_conference_call(
        calls_add_existing_call_request=request,
        conference_id=given_conference_id,
        call_id=given_call_id_2,
    )

    expected_response = CallsConference(
        id=given_id,
        name=given_name,
        participants=[
            CallsParticipant(
                call_id=given_call_id,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                state=given_state,
                join_time=given_join_time,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_audio_muted,
                        user_muted=given_audio_user_muted,
                        deaf=given_audio_user_deaf,
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_video_camera, screen_share=given_video_screen_share
                    ),
                ),
            ),
            CallsParticipant(
                call_id=given_call_id_2,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                state=given_state,
                join_time=given_join_time,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_audio_muted,
                        user_muted=given_audio_user_muted,
                        deaf=given_audio_user_deaf,
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_video_camera, screen_share=given_video_screen_share
                    ),
                ),
            ),
        ],
        platform=Platform(application_id=given_application_id),
    )

    assert api_response == expected_response


def test_should_conference_remove_call(httpserver: HTTPServer, get_api_client):
    given_status = CallsActionStatus.PENDING

    given_response = {"status": given_status}

    given_conference_id = "123"
    given_call_id = "321"

    endpoint = CONFERENCE_CALL.replace("{conferenceId}", given_conference_id).replace(
        "{callId}", given_call_id
    )

    setup_request(httpserver, endpoint, given_response, "DELETE", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.remove_conference_call(
        conference_id=given_conference_id, call_id=given_call_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_conference_update_call(httpserver: HTTPServer, get_api_client):
    given_muted = True

    given_request = {"muted": given_muted}

    given_status = CallsActionStatus.PENDING

    given_response = {"status": given_status}

    given_conference_id = "123"
    given_call_id = "321"

    endpoint = CONFERENCE_CALL.replace("{conferenceId}", given_conference_id).replace(
        "{callId}", given_call_id
    )

    setup_request(httpserver, endpoint, given_response, "PATCH", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsUpdateRequest = CallsUpdateRequest(muted=given_muted)

    api_response = api_instance.update_conference_call(
        conference_id=given_conference_id,
        call_id=given_call_id,
        calls_update_request=request,
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_hangup_conference(httpserver: HTTPServer, get_api_client):
    given_id = "034e622a-cc7e-456d-8a10-0ba43b11aa5e"
    given_name = "Example conference"
    given_call_id = "string"
    given_phone_number = "41792030000"
    given_type = CallEndpointType.PHONE
    given_state = CallsParticipantState.JOINING
    given_join_time = "2022-05-01T14:25:45.134Z"
    given_audio_muted = True
    given_audio_user_muted = True
    given_audio_user_deaf = True
    given_video_camera = True
    given_video_screen_share = True
    given_application_id = "61c060db2675060027d8c7a6"

    given_response = {
        "id": given_id,
        "name": given_name,
        "participants": [
            {
                "callId": given_call_id,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "state": given_state,
                "joinTime": given_join_time,
                "media": {
                    "audio": {
                        "muted": given_audio_muted,
                        "userMuted": given_audio_user_muted,
                        "deaf": given_audio_user_deaf,
                    },
                    "video": {
                        "camera": given_video_camera,
                        "screenShare": given_video_screen_share,
                    },
                },
            }
        ],
        "platform": {
            "applicationId": given_application_id,
        },
    }

    given_conference_id = "123"

    endpoint = HANGUP_CONFERENCE.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.hangup_conference(conference_id=given_conference_id)

    expected_response = CallsConference(
        id=given_id,
        name=given_name,
        participants=[
            CallsParticipant(
                call_id=given_call_id,
                endpoint=CallsPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                state=given_state,
                join_time=given_join_time,
                media=CallsMediaProperties(
                    audio=CallsAudioMediaProperties(
                        muted=given_audio_muted,
                        user_muted=given_audio_user_muted,
                        deaf=given_audio_user_deaf,
                    ),
                    video=CallsVideoMediaProperties(
                        camera=given_video_camera, screen_share=given_video_screen_share
                    ),
                ),
            )
        ],
        platform=Platform(
            application_id=given_application_id,
        ),
    )
    assert api_response == expected_response


def test_should_conference_play_file(httpserver: HTTPServer, get_api_client):
    given_loop_count = 0
    given_type = CallsPlayContentType.FILE

    given_request = {"loopCount": given_loop_count, "content": {"type": given_type}}

    given_status = CallsActionStatus.PENDING

    given_response = {"status": given_status}

    given_conference_id = "123"

    endpoint = CONFERENCE_PLAY_FILE.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsConferencePlayRequest = CallsConferencePlayRequest(
        loop_count=given_loop_count, content=CallsPlayContent(type=given_type)
    )

    api_response = api_instance.conference_play_file(
        calls_conference_play_request=request, conference_id=given_conference_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_conference_stop_file(httpserver: HTTPServer, get_api_client):
    given_status = CallsActionStatus.PENDING

    given_response = {"status": given_status}

    given_conference_id = "123"

    endpoint = CONFERENCE_STOP_PLAYING_FILE.replace(
        "{conferenceId}", given_conference_id
    )

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.conference_stop_playing_file(
        conference_id=given_conference_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_get_calls_recordings(httpserver: HTTPServer, get_api_client):
    given_id = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_phone_number = "41792030000"
    given_type = CallEndpointType.PHONE
    given_direction = CallDirection.INBOUND
    given_file_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = CallsFileFormat.WAV
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3
    given_start_time = "2022-05-01T14:25:45.134Z"
    given_end_time = "2022-05-01T14:35:45.154Z"
    given_location = CallsRecordingFileLocation.SFTP
    given_status = CallsRecordingStatus.SUCCESSFUL
    given_reason = "string"
    given_page = 0
    given_page_size = 1
    given_page_total_pages = 0
    given_page_total_results = 0

    given_response = {
        "results": [
            {
                "callId": given_id,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "direction": given_direction,
                "files": [
                    {
                        "id": given_file_id,
                        "name": given_name,
                        "fileFormat": given_file_format,
                        "size": given_size,
                        "creationMethod": given_creation_method,
                        "creationTime": given_creation_time,
                        "expirationTime": given_expiration_time,
                        "duration": given_duration,
                        "startTime": given_start_time,
                        "endTime": given_end_time,
                        "location": given_location,
                    }
                ],
                "status": given_status,
                "reason": given_reason,
            }
        ],
        "paging": {
            "page": given_page,
            "size": given_page_size,
            "totalPages": given_page_total_pages,
            "totalResults": given_page_total_results,
        },
    }

    setup_request(httpserver, CALLS_RECORDINGS, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_calls_recordings()

    expected_response = CallRecordingPage(
        results=[
            CallRecording(
                call_id=given_id,
                endpoint=CallsPhoneEndpoint(
                    type=CallEndpointType.PHONE, phone_number=given_phone_number
                ),
                direction=given_direction,
                files=[
                    CallsRecordingFile(
                        id=given_file_id,
                        name=given_name,
                        file_format=given_file_format,
                        size=given_size,
                        creation_time=given_creation_time,
                        duration=given_duration,
                        start_time=given_start_time,
                        end_time=given_end_time,
                        location=given_location,
                    )
                ],
                status=given_status,
                reason=given_reason,
            )
        ],
        paging=PageInfo(
            page=given_page,
            size=given_page_size,
            total_pages=given_page_total_pages,
            total_results=given_page_total_results,
        ),
    )

    assert api_response == expected_response


def test_should_get_call_recordings(httpserver: HTTPServer, get_api_client):
    given_id = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_phone_number = "41792030000"
    given_type = CallEndpointType.PHONE
    given_direction = CallDirection.INBOUND
    given_file_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = CallsFileFormat.WAV
    given_size = 292190
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3
    given_start_time = "2022-05-01T14:25:45.134Z"
    given_end_time = "2022-05-01T14:35:45.154Z"
    given_location = CallsRecordingFileLocation.SFTP
    given_status = CallsRecordingStatus.SUCCESSFUL

    given_response = {
        "callId": given_id,
        "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
        "direction": given_direction,
        "files": [
            {
                "id": given_file_id,
                "name": given_name,
                "fileFormat": given_file_format,
                "size": given_size,
                "creationTime": given_creation_time,
                "expirationTime": given_expiration_time,
                "duration": given_duration,
                "startTime": given_start_time,
                "endTime": given_end_time,
                "location": given_location,
            }
        ],
        "status": given_status,
    }

    endpoint = CALL_RECORDINGS.replace("{callId}", given_id)

    setup_request(httpserver, endpoint, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_call_recordings(call_id=given_id)

    expected_response = CallRecording(
        call_id=given_id,
        endpoint=CallsPhoneEndpoint(type=given_type, phone_number=given_phone_number),
        direction=given_direction,
        files=[
            CallsRecordingFile(
                id=given_file_id,
                name=given_name,
                file_format=given_file_format,
                size=given_size,
                creation_time=given_creation_time,
                duration=given_duration,
                start_time=given_start_time,
                end_time=given_end_time,
                location=given_location,
            ),
        ],
        status=given_status,
    )

    assert api_response == expected_response


def test_should_delete_call_recordings(httpserver: HTTPServer, get_api_client):
    given_id = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_direction = "INBOUND"
    given_file_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = "WAV"
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3
    given_start_time = "2022-05-01T14:25:45.134Z"
    given_end_time = "2022-05-01T14:35:45.154Z"
    given_location = "SFTP"
    given_status = "SUCCESSFUL"

    given_response = {
        "callId": given_id,
        "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
        "direction": given_direction,
        "files": [
            {
                "id": given_file_id,
                "name": given_name,
                "fileFormat": given_file_format,
                "size": given_size,
                "creationMethod": given_creation_method,
                "creationTime": given_creation_time,
                "expirationTime": given_expiration_time,
                "duration": given_duration,
                "startTime": given_start_time,
                "endTime": given_end_time,
                "location": given_location,
            }
        ],
        "status": given_status,
    }

    endpoint = CALL_RECORDINGS.replace("{callId}", given_id)

    setup_request(httpserver, endpoint, given_response, "DELETE", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.delete_call_recordings(call_id=given_id)

    expected_response = CallRecording(
        call_id=given_id,
        endpoint=CallsPhoneEndpoint(type=given_type, phone_number=given_phone_number),
        direction=given_direction,
        files=[
            CallsRecordingFile(
                id=given_file_id,
                name=given_name,
                file_format=given_file_format,
                size=given_size,
                creation_time=given_creation_time,
                duration=given_duration,
                start_time=given_start_time,
                end_time=given_end_time,
                location=given_location,
            )
        ],
        status=given_status,
    )

    assert api_response == expected_response


def test_should_get_conferences_recordings(httpserver: HTTPServer, get_api_client):
    given_conference_id = "string"
    given_conference_name = "string"
    given_application_id = "string"
    given_file_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = CallsFileFormat.WAV
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3
    given_start_time = "2022-05-01T14:25:45.134Z"
    given_end_time = "2022-05-01T14:35:45.154Z"
    given_location = CallsRecordingFileLocation.SFTP
    given_id = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_direction = CallDirection.INBOUND
    given_status = CallsRecordingStatus.SUCCESSFUL
    given_reason = "string"
    given_page = 0
    given_page_size = 1
    given_page_total_pages = 0
    given_page_total_results = 0

    given_response = {
        "results": [
            {
                "conferenceId": given_conference_id,
                "conferenceName": given_conference_name,
                "platform": {"applicationId": given_application_id},
                "composedFiles": [
                    {
                        "id": given_file_id,
                        "name": given_name,
                        "fileFormat": given_file_format,
                        "size": given_size,
                        "creationMethod": given_creation_method,
                        "creationTime": given_creation_time,
                        "expirationTime": given_expiration_time,
                        "duration": given_duration,
                        "startTime": given_start_time,
                        "endTime": given_end_time,
                        "location": given_location,
                    }
                ],
                "callRecordings": [
                    {
                        "callId": given_id,
                        "endpoint": {
                            "phoneNumber": given_phone_number,
                            "type": given_type,
                        },
                        "direction": given_direction,
                        "files": [
                            {
                                "id": given_file_id,
                                "name": given_name,
                                "fileFormat": given_file_format,
                                "size": given_size,
                                "creationMethod": given_creation_method,
                                "creationTime": given_creation_time,
                                "expirationTime": given_expiration_time,
                                "duration": given_duration,
                                "startTime": given_start_time,
                                "endTime": given_end_time,
                                "location": given_location,
                            }
                        ],
                        "status": given_status,
                    }
                ],
            }
        ],
        "paging": {
            "page": given_page,
            "size": given_page_size,
            "totalPages": given_page_total_pages,
            "totalResults": given_page_total_results,
        },
    }

    setup_request(httpserver, CONFERENCES_RECORDINGS, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_conferences_recordings()

    expected_response = CallsConferenceRecordingPage(
        results=[
            CallsConferenceRecording(
                conference_id=given_conference_id,
                conference_name=given_conference_name,
                platform=Platform(
                    application_id=given_application_id,
                ),
                composed_files=[
                    CallsRecordingFile(
                        id=given_file_id,
                        name=given_name,
                        file_format=given_file_format,
                        size=given_size,
                        creation_time=given_creation_time,
                        duration=given_duration,
                        start_time=given_start_time,
                        end_time=given_end_time,
                        location=given_location,
                    )
                ],
                call_recordings=[
                    CallRecording(
                        call_id=given_id,
                        endpoint=CallsPhoneEndpoint(
                            type=CallEndpointType.PHONE, phone_number=given_phone_number
                        ),
                        direction=given_direction,
                        files=[
                            CallsRecordingFile(
                                id=given_file_id,
                                name=given_name,
                                file_format=given_file_format,
                                size=given_size,
                                creation_time=given_creation_time,
                                duration=given_duration,
                                start_time=given_start_time,
                                end_time=given_end_time,
                                location=given_location,
                            )
                        ],
                        status=given_status,
                    )
                ],
            )
        ],
        paging=PageInfo(
            page=given_page,
            size=given_page_size,
            total_pages=given_page_total_pages,
            total_results=given_page_total_results,
        ),
    )

    assert api_response == expected_response


def test_should_get_conference_recordings(httpserver: HTTPServer, get_api_client):
    given_conference_id = "string"
    given_conference_name = "string"
    given_application_id = "string"
    given_file_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = CallsFileFormat.WAV
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3
    given_start_time = "2022-05-01T14:25:45.134Z"
    given_end_time = "2022-05-01T14:35:45.154Z"
    given_location = CallsRecordingFileLocation.SFTP
    given_id = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_direction = "INBOUND"
    given_status = "SUCCESSFUL"

    given_response = {
        "conferenceId": given_conference_id,
        "conferenceName": given_conference_name,
        "platform": {"applicationId": given_application_id},
        "composedFiles": [
            {
                "id": given_file_id,
                "name": given_name,
                "fileFormat": given_file_format,
                "size": given_size,
                "creationMethod": given_creation_method,
                "creationTime": given_creation_time,
                "expirationTime": given_expiration_time,
                "duration": given_duration,
                "startTime": given_start_time,
                "endTime": given_end_time,
                "location": given_location,
            }
        ],
        "callRecordings": [
            {
                "callId": given_id,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "direction": given_direction,
                "files": [
                    {
                        "id": given_file_id,
                        "name": given_name,
                        "fileFormat": given_file_format,
                        "size": given_size,
                        "creationMethod": given_creation_method,
                        "creationTime": given_creation_time,
                        "expirationTime": given_expiration_time,
                        "duration": given_duration,
                        "startTime": given_start_time,
                        "endTime": given_end_time,
                        "location": given_location,
                    }
                ],
                "status": given_status,
            }
        ],
    }

    endpoint = CONFERENCE_RECORDINGS.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_conference_recordings(
        conference_id=given_conference_id
    )

    expected_response = CallsConferenceRecording(
        conference_id=given_conference_id,
        conference_name=given_conference_name,
        platform=Platform(
            application_id=given_application_id,
        ),
        composed_files=[
            CallsRecordingFile(
                id=given_file_id,
                name=given_name,
                file_format=given_file_format,
                size=given_size,
                creation_time=given_creation_time,
                duration=given_duration,
                start_time=given_start_time,
                end_time=given_end_time,
                location=given_location,
            )
        ],
        call_recordings=[
            CallRecording(
                call_id=given_id,
                endpoint=CallsPhoneEndpoint(
                    type=CallEndpointType.PHONE, phone_number=given_phone_number
                ),
                direction=given_direction,
                files=[
                    CallsRecordingFile(
                        id=given_file_id,
                        name=given_name,
                        file_format=given_file_format,
                        size=given_size,
                        creation_time=given_creation_time,
                        duration=given_duration,
                        start_time=given_start_time,
                        end_time=given_end_time,
                        location=given_location,
                    )
                ],
                status=given_status,
            )
        ],
    )

    assert api_response == expected_response


def test_should_delete_conference_recordings(httpserver: HTTPServer, get_api_client):
    given_conference_id = "string"
    given_conference_name = "string"
    given_application_id = "string"
    given_file_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = CallsFileFormat.WAV
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3
    given_start_time = "2022-05-01T14:25:45.134Z"
    given_end_time = "2022-05-01T14:35:45.154Z"
    given_location = CallsRecordingFileLocation.SFTP
    given_id = "d8d84155-3831-43fb-91c9-bb897149a79d"
    given_phone_number = "41792030000"
    given_type = "PHONE"
    given_direction = "INBOUND"
    given_status = "SUCCESSFUL"

    given_response = {
        "conferenceId": given_conference_id,
        "conferenceName": given_conference_name,
        "platform": {"applicationId": given_application_id},
        "composedFiles": [
            {
                "id": given_file_id,
                "name": given_name,
                "fileFormat": given_file_format,
                "size": given_size,
                "creationMethod": given_creation_method,
                "creationTime": given_creation_time,
                "expirationTime": given_expiration_time,
                "duration": given_duration,
                "startTime": given_start_time,
                "endTime": given_end_time,
                "location": given_location,
            }
        ],
        "callRecordings": [
            {
                "callId": given_id,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "direction": given_direction,
                "files": [
                    {
                        "id": given_file_id,
                        "name": given_name,
                        "fileFormat": given_file_format,
                        "size": given_size,
                        "creationMethod": given_creation_method,
                        "creationTime": given_creation_time,
                        "expirationTime": given_expiration_time,
                        "duration": given_duration,
                        "startTime": given_start_time,
                        "endTime": given_end_time,
                        "location": given_location,
                    }
                ],
                "status": given_status,
            }
        ],
    }

    endpoint = CONFERENCE_RECORDINGS.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "DELETE", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.delete_conference_recordings(
        conference_id=given_conference_id
    )

    expected_response = CallsConferenceRecording(
        conference_id=given_conference_id,
        conference_name=given_conference_name,
        platform=Platform(application_id=given_application_id),
        composed_files=[
            CallsRecordingFile(
                id=given_file_id,
                name=given_name,
                file_format=given_file_format,
                size=given_size,
                creation_time=given_creation_time,
                duration=given_duration,
                start_time=given_start_time,
                end_time=given_end_time,
                location=given_location,
            )
        ],
        call_recordings=[
            CallRecording(
                call_id=given_id,
                endpoint=CallsPhoneEndpoint(
                    type=CallEndpointType.PHONE, phone_number=given_phone_number
                ),
                direction=given_direction,
                files=[
                    CallsRecordingFile(
                        id=given_file_id,
                        name=given_name,
                        file_format=given_file_format,
                        size=given_size,
                        creation_method=given_creation_method,
                        creation_time=given_creation_time,
                        expiration_time=given_expiration_time,
                        duration=given_duration,
                        start_time=given_start_time,
                        end_time=given_end_time,
                        location=given_location,
                    )
                ],
                status=given_status,
            )
        ],
    )

    assert api_response == expected_response


def test_should_compose_conference_recording_on_calls(
    httpserver: HTTPServer, get_api_client
):
    given_delete_call_recordings = True

    given_request = {"deleteCallRecordings": given_delete_call_recordings}
    given_status = "PENDING"

    given_response = {"status": given_status}

    given_conference_id = "123"

    endpoint = COMPOSE_CONFERENCE_RECORDING.replace(
        "{conferenceId}", given_conference_id
    )

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsOnDemandComposition = CallsOnDemandComposition(
        delete_call_recordings=given_delete_call_recordings
    )

    api_response = api_instance.compose_conference_recording(
        calls_on_demand_composition=request, conference_id=given_conference_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_delete_recording_file(httpserver: HTTPServer, get_api_client):
    given_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = "WAV"
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3
    given_start_time = "2021-12-31T23:59:50.100+0000"
    given_end_time = "2022-01-01T00:00:00.100+0000"

    given_response = {
        "id": given_id,
        "name": given_name,
        "fileFormat": given_file_format,
        "size": given_size,
        "creationMethod": given_creation_method,
        "creationTime": given_creation_time,
        "expirationTime": given_expiration_time,
        "duration": given_duration,
        "startTime": given_start_time,
        "endTime": given_end_time,
    }

    endpoint = CALLS_RECORDINGS_FILES.replace("{fileId}", given_id)

    setup_request(httpserver, endpoint, given_response, "DELETE", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.delete_recording_file(file_id=given_id)

    expected_response: CallsRecordingFile = CallsRecordingFile(
        id=given_id,
        name=given_name,
        file_format=given_file_format,
        size=given_size,
        creation_method=given_creation_method,
        creation_time=given_creation_time,
        expiration_time=given_expiration_time,
        duration=given_duration,
        start_time=given_start_time,
        end_time=given_end_time,
    )
    assert api_response == expected_response


def test_should_conference_say_text(httpserver: HTTPServer, get_api_client):
    given_text = "string"
    given_language = CallsLanguage.AR
    given_speech_rate = 0.5
    given_loop_count = 0
    given_voice_gender = CallsGender.FEMALE
    given_voice_name = CallVoice.HANS

    given_request = {
        "text": given_text,
        "language": given_language,
        "speechRate": given_speech_rate,
        "loopCount": given_loop_count,
        "preferences": {
            "voiceGender": given_voice_gender,
            "voiceName": given_voice_name,
        },
    }

    given_status = CallsActionStatus.PENDING

    given_response = {"status": given_status}

    given_conference_id = "123"

    endpoint = CONFERENCE_SAY_TEXT.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsSayRequest = CallsSayRequest(
        text=given_text,
        language=given_language,
        speech_rate=given_speech_rate,
        loop_count=given_loop_count,
        preferences=CallsVoicePreferences(
            voice_gender=given_voice_gender, voice_name=given_voice_name
        ),
    )

    api_response = api_instance.conference_say_text(
        calls_say_request=request, conference_id=given_conference_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_conference_start_recording(httpserver: HTTPServer, get_api_client):
    given_recording_type = "AUDIO_AND_VIDEO"

    given_request = {"recordingType": given_recording_type}

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_conference_id = "123"

    endpoint = CONFERENCE_START_RECORDING.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsConferenceRecordingRequest = CallsConferenceRecordingRequest(
        recording_type=given_recording_type
    )

    api_response = api_instance.conference_start_recording(
        calls_conference_recording_request=request, conference_id=given_conference_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_conference_stop_recording(httpserver: HTTPServer, get_api_client):
    given_status = "PENDING"

    given_response = {"status": given_status}

    given_conference_id = "123"

    endpoint = CONFERENCE_STOP_RECORDING.replace("{conferenceId}", given_conference_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.conference_stop_recording(
        conference_id=given_conference_id
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_conference_broadcast_text(httpserver: HTTPServer, get_api_client):
    given_text = "This meeting will end in 5 minutes."

    given_request = {"text": given_text}

    given_status = "PENDING"

    given_response = {"status": given_status}

    given_conference_id = "123"

    endpoint = CONFERENCE_BROADCAST_WEBRTC_TEXT.replace(
        "{conferenceId}", given_conference_id
    )

    setup_request(httpserver, endpoint, given_response, "POST", 200, given_request)

    api_instance = CallsApi(get_api_client)

    request: CallsConferenceBroadcastWebrtcTextRequest = (
        CallsConferenceBroadcastWebrtcTextRequest(text=given_text)
    )

    api_response = api_instance.conference_broadcast_webrtc_text(
        calls_conference_broadcast_webrtc_text_request=request,
        conference_id=given_conference_id,
    )

    expected_response = CallsActionResponse(status=given_status)

    assert api_response == expected_response


def test_should_get_files(httpserver: HTTPServer, get_api_client):
    given_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = "WAV"
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3
    given_page = 0
    given_page_size = 1
    given_page_total_pages = 0
    given_page_total_results = 0

    given_response = {
        "results": [
            {
                "id": given_id,
                "name": given_name,
                "fileFormat": given_file_format,
                "size": given_size,
                "creationMethod": given_creation_method,
                "creationTime": given_creation_time,
                "expirationTime": given_expiration_time,
                "duration": given_duration,
            }
        ],
        "paging": {
            "page": given_page,
            "size": given_page_size,
            "totalPages": given_page_total_pages,
            "totalResults": given_page_total_results,
        },
    }

    setup_request(httpserver, CALLS_FILES, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_calls_files()

    expected_response = CallsFilePage(
        results=[
            CallsFile(
                id=given_id,
                name=given_name,
                file_format=given_file_format,
                size=given_size,
                creation_method=given_creation_method,
                creation_time=given_creation_time,
                expiration_time=given_expiration_time,
                duration=given_duration,
            )
        ],
        paging=PageInfo(
            page=given_page,
            size=given_page_size,
            total_pages=given_page_total_pages,
            total_results=given_page_total_results,
        ),
    )

    assert api_response == expected_response


def test_should_upload_audio_file(httpserver: HTTPServer, get_api_client):
    given_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = "WAV"
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3

    given_attachment_text = "Test file text"

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_file.write(given_attachment_text.encode())

    temp_file_path = temp_file.name

    given_response = {
        "id": given_id,
        "name": given_name,
        "fileFormat": given_file_format,
        "size": given_size,
        "creationMethod": given_creation_method,
        "creationTime": given_creation_time,
        "expirationTime": given_expiration_time,
        "duration": given_duration,
    }

    setup_request(httpserver, CALLS_FILES, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.upload_calls_audio_file(file=temp_file_path)

    expected_response = CallsFile(
        id=given_id,
        name=given_name,
        file_format=given_file_format,
        size=given_size,
        creation_method=given_creation_method,
        creation_time=given_creation_time,
        expiration_time=given_expiration_time,
        duration=given_duration,
    )

    assert api_response == expected_response


def test_should_get_file(httpserver: HTTPServer, get_api_client):
    given_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = "WAV"
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3

    given_response = {
        "id": given_id,
        "name": given_name,
        "fileFormat": given_file_format,
        "size": given_size,
        "creationMethod": given_creation_method,
        "creationTime": given_creation_time,
        "expirationTime": given_expiration_time,
        "duration": given_duration,
    }

    given_file_id = "id1"

    endpoint = CALLS_FILE.replace("{fileId}", given_file_id)

    setup_request(httpserver, endpoint, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_calls_file(file_id=given_file_id)

    expected_response = CallsFile(
        id=given_id,
        name=given_name,
        file_format=given_file_format,
        size=given_size,
        creation_method=given_creation_method,
        creation_time=given_creation_time,
        expiration_time=given_expiration_time,
        duration=given_duration,
    )

    assert api_response == expected_response


def test_should_delete_file(httpserver: HTTPServer, get_api_client):
    given_id = "218eceba-c044-430d-9f26-8f1a7f0g2d03"
    given_name = "Example file"
    given_file_format = "WAV"
    given_size = 292190
    given_creation_method = "RECORDED"
    given_creation_time = "2022-05-01T14:25:45.143Z"
    given_expiration_time = "2022-06-01T14:25:45.143Z"
    given_duration = 3

    given_response = {
        "id": given_id,
        "name": given_name,
        "fileFormat": given_file_format,
        "size": given_size,
        "creationMethod": given_creation_method,
        "creationTime": given_creation_time,
        "expirationTime": given_expiration_time,
        "duration": given_duration,
    }

    given_file_id = "id1"

    endpoint = CALLS_FILE.replace("{fileId}", given_file_id)

    setup_request(httpserver, endpoint, given_response, "DELETE", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.delete_calls_file(file_id=given_file_id)

    expected_response = CallsFile(
        id=given_id,
        name=given_name,
        file_format=given_file_format,
        size=given_size,
        creation_method=given_creation_method,
        creation_time=given_creation_time,
        expiration_time=given_expiration_time,
        duration=given_duration,
    )

    assert api_response == expected_response


def test_should_get_media_stream_configs(httpserver: HTTPServer, get_api_client):
    given_id_1 = "63467c6e2885a5389ba11d80"
    given_type_1 = CallsResponseMediaStreamConfigType.MEDIA_STREAMING
    given_name_1 = "Media-stream config"
    given_url_1 = "ws://example-web-socket.com:3001"

    given_id_2 = "63467c6e2885a5389ba11d81"
    given_type_2 = CallsResponseMediaStreamConfigType.WEBSOCKET_ENDPOINT
    given_name_2 = "Media-stream config"
    given_url_2 = "ws://example-web-socket.com:3001"
    given_sample_rate_2 = "8000"

    given_page = 0
    given_size = 2
    given_total_pages = 1
    given_total_results = 2

    given_response = {
        "results": [
            {
                "id": given_id_1,
                "type": given_type_1,
                "name": given_name_1,
                "url": given_url_1,
            },
            {
                "id": given_id_2,
                "type": given_type_2,
                "name": given_name_2,
                "url": given_url_2,
                "sampleRate": given_sample_rate_2,
            },
        ],
        "paging": {
            "page": given_page,
            "size": given_size,
            "totalPages": given_total_pages,
            "totalResults": given_total_results,
        },
    }

    setup_request(httpserver, MEDIA_STREAM_CONFIGS, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_media_stream_configs()

    expected_response = CallsMediaStreamConfigPage(
        results=[
            CallsMediaStreamingConfigResponse(
                id=given_id_1, type=given_type_1, name=given_name_1, url=given_url_1
            ),
            CallsWebsocketEndpointConfigResponse(
                id=given_id_2,
                type=given_type_2,
                name=given_name_2,
                url=given_url_2,
                sample_rate=given_sample_rate_2,
            ),
        ],
        paging=PageInfo(
            page=given_page,
            size=given_size,
            total_pages=given_total_pages,
            total_results=given_total_results,
        ),
    )

    assert api_response == expected_response


def test_should_create_media_stream_config(httpserver: HTTPServer, get_api_client):
    given_url = "string"
    given_name = "Media-stream config"
    given_username = "user"
    given_password = "passw"
    given_id = "string"
    given_type = CallsResponseMediaStreamConfigType.MEDIA_STREAMING
    given_security_type = SecurityConfigType.BASIC

    given_response = {
        "id": given_id,
        "name": given_name,
        "url": given_url,
        "type": given_type,
    }

    setup_request(httpserver, MEDIA_STREAM_CONFIGS, given_response, "POST", 201, None)

    api_instance = CallsApi(get_api_client)

    request: CallsMediaStreamingConfigRequest = CallsMediaStreamingConfigRequest(
        name=given_name,
        url=given_url,
        type=given_type,
        security_config=BasicSecurityConfig(
            username=given_username, password=given_password, type=given_security_type
        ),
    )

    api_response = api_instance.create_media_stream_config(
        calls_media_stream_config_request=request
    )

    expected_response = CallsMediaStreamingConfigResponse(
        id=given_id, url=given_url, name=given_name, type=given_type
    )
    assert api_response == expected_response


def test_should_get_media_stream_config(httpserver: HTTPServer, get_api_client):
    given_url = "string"
    given_name = "Media-stream config"
    given_id = "string"
    given_type = CallsResponseMediaStreamConfigType.MEDIA_STREAMING

    given_response = {
        "id": given_id,
        "name": given_name,
        "type": given_type,
        "url": given_url,
    }

    endpoint = MEDIA_STREAM_CONFIG.replace("{mediaStreamConfigId}", given_id)

    setup_request(httpserver, endpoint, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_media_stream_config(media_stream_config_id=given_id)

    expected_response = CallsMediaStreamingConfigResponse(
        id=given_id, url=given_url, type=given_type, name=given_name
    )
    assert api_response == expected_response


def test_should_update_media_stream_config(httpserver: HTTPServer, get_api_client):
    given_url = "string"
    given_name = "Media-stream config"
    given_security_type = SecurityConfigType.BASIC
    given_username = "user"
    given_password = "passw"
    given_id = "string"
    given_type = CallsResponseMediaStreamConfigType.MEDIA_STREAMING

    given_response = {
        "id": given_id,
        "name": given_name,
        "type": given_type,
        "url": given_url,
    }

    endpoint = MEDIA_STREAM_CONFIG.replace("{mediaStreamConfigId}", given_id)

    setup_request(httpserver, endpoint, given_response, "PUT", 200, None)

    api_instance = CallsApi(get_api_client)

    request: CallsMediaStreamingConfigRequest = CallsMediaStreamingConfigRequest(
        name=given_name,
        url=given_url,
        security_config=BasicSecurityConfig(
            username=given_username, password=given_password, type=given_security_type
        ),
    )

    api_response = api_instance.update_media_stream_config(
        calls_media_stream_config_request=request, media_stream_config_id=given_id
    )

    expected_response = CallsMediaStreamingConfigResponse(
        id=given_id, url=given_url, type=given_type, name=given_name
    )
    assert api_response == expected_response


def test_should_delete_media_stream_config(httpserver: HTTPServer, get_api_client):
    given_url = "string"
    given_name = "Media-stream config"
    given_id = "string"
    given_type = CallsResponseMediaStreamConfigType.MEDIA_STREAMING

    given_response = {
        "id": given_id,
        "type": given_type,
        "name": given_name,
        "url": given_url,
    }

    endpoint = MEDIA_STREAM_CONFIG.replace("{mediaStreamConfigId}", given_id)

    setup_request(httpserver, endpoint, given_response, "DELETE", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.delete_media_stream_config(
        media_stream_config_id=given_id
    )

    expected_response = CallsMediaStreamingConfigResponse(
        id=given_id, url=given_url, name=given_name, type=given_type
    )
    assert api_response == expected_response


def test_should_create_bulk_of_calls(httpserver: HTTPServer, get_api_client):
    given_calls_configuration_id = "dc5942707c704551a00cd2ea"
    given_application_id = "61c060db2675060027d8c7a6"
    given_from = "41793026834"
    given_phone_number = "41792036727"
    given_type = CallsBulkEndpointType.PHONE
    given_bulk_id = "bulk"
    given_call_id = "call"
    given_external_id = "external"
    given_status = "PENDING"

    given_response = {
        "bulkId": given_bulk_id,
        "calls": [
            {
                "platform": {
                    "applicationId": given_application_id,
                },
                "callId": given_call_id,
                "externalId": given_external_id,
                "from": given_from,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "status": given_status,
            },
            {
                "platform": {
                    "applicationId": given_application_id,
                },
                "callId": given_call_id,
                "externalId": given_external_id,
                "from": given_from,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "status": given_status,
            },
            {
                "platform": {
                    "applicationId": given_application_id,
                },
                "callId": given_call_id,
                "externalId": given_external_id,
                "from": given_from,
                "endpoint": {"phoneNumber": given_phone_number, "type": given_type},
                "status": given_status,
            },
        ],
    }

    setup_request(httpserver, BULKS, given_response, "POST", 201, None)

    api_instance = CallsApi(get_api_client)

    request: CallBulkRequest = CallBulkRequest(
        calls_configuration_id=given_calls_configuration_id,
        platform=Platform(
            application_id=given_application_id,
        ),
        items=[
            CallsBulkItem(
                var_from=given_from,
                call_requests=[
                    CallsBulkCallRequest(
                        endpoint=CallsBulkPhoneEndpoint(
                            phone_number=given_phone_number, type=given_type
                        )
                    ),
                    CallsBulkCallRequest(
                        endpoint=CallsBulkPhoneEndpoint(
                            phone_number=given_phone_number, type=given_type
                        )
                    ),
                    CallsBulkCallRequest(
                        endpoint=CallsBulkPhoneEndpoint(
                            phone_number=given_phone_number, type=given_type
                        )
                    ),
                ],
            )
        ],
    )

    api_response = api_instance.create_bulk(call_bulk_request=request)

    expected_response = CallBulkResponse(
        bulk_id="bulk",
        calls=[
            CallsBulkCall(
                platform=Platform(application_id=given_application_id),
                call_id=given_call_id,
                external_id=given_external_id,
                var_from=given_from,
                endpoint=CallsBulkPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                status=CallsActionStatus.PENDING,
            ),
            CallsBulkCall(
                platform=Platform(application_id=given_application_id),
                call_id=given_call_id,
                external_id=given_external_id,
                var_from=given_from,
                endpoint=CallsBulkPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                status=CallsActionStatus.PENDING,
            ),
            CallsBulkCall(
                platform=Platform(application_id=given_application_id),
                call_id=given_call_id,
                external_id=given_external_id,
                var_from=given_from,
                endpoint=CallsBulkPhoneEndpoint(
                    type=given_type, phone_number=given_phone_number
                ),
                status=CallsActionStatus.PENDING,
            ),
        ],
    )

    assert api_response == expected_response


def test_should_get_bulk_status(httpserver: HTTPServer, get_api_client):
    given_bulk_id = "bulk"
    given_status = "PENDING"
    given_start_time = "2024-05-02T08:16:22Z"

    given_response = {
        "bulkId": given_bulk_id,
        "startTime": given_start_time,
        "status": given_status,
    }

    endpoint = BULK.replace("{bulkId}", given_bulk_id)

    setup_request(httpserver, endpoint, given_response, "GET", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.get_bulk_status(bulk_id=given_bulk_id)

    expected_response = CallBulkStatus(
        bulk_id=given_bulk_id, start_time=given_start_time, status=given_status
    )

    assert api_response == expected_response


def test_should_reschedule(httpserver: HTTPServer, get_api_client):
    given_start_time = "2024-05-02T08:16:22Z"

    given_bulk_id = "bulk"
    given_status = "PENDING"

    given_response = {
        "bulkId": given_bulk_id,
        "startTime": given_start_time,
        "status": given_status,
    }

    endpoint = RESCHEDULE_BULK.replace("{bulkId}", given_bulk_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    request = CallsRescheduleRequest(start_time=given_start_time)

    api_response = api_instance.reschedule_bulk(
        bulk_id=given_bulk_id, calls_reschedule_request=request
    )

    expected_response = CallBulkStatus(
        bulk_id=given_bulk_id, start_time=given_start_time, status=given_status
    )

    assert api_response == expected_response


def test_should_pause(httpserver: HTTPServer, get_api_client):
    given_start_time = "2024-05-02T08:16:22Z"
    given_bulk_id = "bulk"
    given_status = "PENDING"

    given_response = {
        "bulkId": given_bulk_id,
        "startTime": given_start_time,
        "status": given_status,
    }

    endpoint = PAUSE_BULK.replace("{bulkId}", given_bulk_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.pause_bulk(bulk_id=given_bulk_id)

    expected_response = CallBulkStatus(
        bulk_id=given_bulk_id, start_time=given_start_time, status=given_status
    )

    assert api_response == expected_response


def test_resume_pause(httpserver: HTTPServer, get_api_client):
    given_start_time = "2024-05-02T08:16:22Z"
    given_bulk_id = "bulk"
    given_status = "PENDING"

    given_response = {
        "bulkId": given_bulk_id,
        "startTime": given_start_time,
        "status": given_status,
    }

    endpoint = RESUME_BULK.replace("{bulkId}", given_bulk_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.resume_bulk(bulk_id=given_bulk_id)

    expected_response = CallBulkStatus(
        bulk_id=given_bulk_id, start_time=given_start_time, status=given_status
    )

    assert api_response == expected_response


def test_cancel_pause(httpserver: HTTPServer, get_api_client):
    given_start_time = "2024-05-02T08:16:22Z"
    given_bulk_id = "bulk"
    given_status = "PENDING"

    given_response = {
        "bulkId": given_bulk_id,
        "startTime": given_start_time,
        "status": given_status,
    }

    endpoint = CANCEL_BULK.replace("{bulkId}", given_bulk_id)

    setup_request(httpserver, endpoint, given_response, "POST", 200, None)

    api_instance = CallsApi(get_api_client)

    api_response = api_instance.cancel_bulk(bulk_id=given_bulk_id)

    expected_response = CallBulkStatus(
        bulk_id=given_bulk_id, start_time=given_start_time, status=given_status
    )

    assert api_response == expected_response


def setup_request(
    httpserver,
    endpoint: str,
    expected_response=None,
    http_verb: str = "GET",
    status_code: int = 200,
    request_body=None,
):
    if request_body is not None:
        httpserver.expect_request(
            uri=endpoint, method=http_verb, json=request_body
        ).respond_with_json(expected_response, status=status_code)
    else:
        httpserver.expect_request(uri=endpoint, method=http_verb).respond_with_json(
            expected_response, status=status_code
        )


@pytest.fixture
def get_api_client():
    configuration = Configuration(host="http://localhost:8088")
    configuration.api_key["APIKeyHeader"] = "GivenApiKey"
    configuration.api_key_prefix["APIKeyHeader"] = "App"
    return ApiClient(configuration)


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", 8088
