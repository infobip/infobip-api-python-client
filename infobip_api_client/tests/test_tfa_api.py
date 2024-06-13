import pytest
from infobip_api_client import ApiClient, Configuration
from infobip_api_client.api.tfa_api import TfaApi
from infobip_api_client.models.tfa_application_configuration import (
    TfaApplicationConfiguration,
)
from infobip_api_client.models.tfa_application_request import TfaApplicationRequest
from infobip_api_client.models.tfa_create_message_request import TfaCreateMessageRequest
from infobip_api_client.models.tfa_india_dlt_options import TfaIndiaDltOptions
from infobip_api_client.models.tfa_language import TfaLanguage
from infobip_api_client.models.tfa_pin_type import TfaPinType
from infobip_api_client.models.tfa_regional_options import TfaRegionalOptions
from infobip_api_client.models.tfa_resend_pin_request import TfaResendPinRequest
from infobip_api_client.models.tfa_start_authentication_request import (
    TfaStartAuthenticationRequest,
)
from infobip_api_client.models.tfa_update_message_request import TfaUpdateMessageRequest
from infobip_api_client.models.tfa_verify_pin_request import TfaVerifyPinRequest
from pytest_httpserver import HTTPServer


def test_should_get_tfa_apps(httpserver: HTTPServer, get_api_client):
    tfa_applications_endpoint = "/2fa/2/applications"

    givenApplicationId1 = "0933F3BC087D2A617AC6DCB2EF5B8A61"
    givenGetApplicationName1 = "Test application BASIC 1"
    givenGetApplicationPinAttempts1 = 10
    givenAllowMultiplePinVerifications1 = True
    givenGetApplicationPinTimeToLive1 = "2h"
    givenGetApplicationVerifyPinLimit1 = "1/3s"
    givenGetAppSendPinPerApplicationLimit1 = "10000/1d"
    givenGetAppSendPinPerPhoneNumberLimit1 = "3/1d"
    givenEnabled1 = True

    givenApplicationId2 = "5F04FACFAA4978F62FCAEBA97B37E90F"
    givenGetApplicationName2 = "Test application BASIC 2"
    givenGetApplicationPinAttempts2 = 12
    givenAllowMultiplePinVerifications2 = True
    givenGetApplicationPinTimeToLive2 = "10m"
    givenGetApplicationVerifyPinLimit2 = "2/1s"
    givenGetAppSendPinPerApplicationLimit2 = "10000/1d"
    givenGetAppSendPinPerPhoneNumberLimit2 = "5/1h"
    givenEnabled2 = True

    givenApplicationId3 = "B450F966A8EF017180F148AF22C42642"
    givenGetApplicationName3 = "Test application BASIC 3"
    givenGetApplicationPinAttempts3 = 15
    givenAllowMultiplePinVerifications3 = True
    givenGetApplicationPinTimeToLive3 = "1h"
    givenGetApplicationVerifyPinLimit3 = "30/10s"
    givenGetAppSendPinPerApplicationLimit3 = "10000/3d"
    givenGetAppSendPinPerPhoneNumberLimit3 = "10/20m"
    givenEnabled3 = True

    expected_response = [
        {
            "applicationId": givenApplicationId1,
            "name": givenGetApplicationName1,
            "configuration": {
                "pinAttempts": givenGetApplicationPinAttempts1,
                "allowMultiplePinVerifications": givenAllowMultiplePinVerifications1,
                "pinTimeToLive": givenGetApplicationPinTimeToLive1,
                "verifyPinLimit": givenGetApplicationVerifyPinLimit1,
                "sendPinPerApplicationLimit": givenGetAppSendPinPerApplicationLimit1,
                "sendPinPerPhoneNumberLimit": givenGetAppSendPinPerPhoneNumberLimit1,
            },
            "enabled": givenEnabled1,
        },
        {
            "applicationId": givenApplicationId2,
            "name": givenGetApplicationName2,
            "configuration": {
                "pinAttempts": givenGetApplicationPinAttempts2,
                "allowMultiplePinVerifications": givenAllowMultiplePinVerifications2,
                "pinTimeToLive": givenGetApplicationPinTimeToLive2,
                "verifyPinLimit": givenGetApplicationVerifyPinLimit2,
                "sendPinPerApplicationLimit": givenGetAppSendPinPerApplicationLimit2,
                "sendPinPerPhoneNumberLimit": givenGetAppSendPinPerPhoneNumberLimit2,
            },
            "enabled": givenEnabled2,
        },
        {
            "applicationId": givenApplicationId3,
            "name": givenGetApplicationName3,
            "configuration": {
                "pinAttempts": givenGetApplicationPinAttempts3,
                "allowMultiplePinVerifications": givenAllowMultiplePinVerifications3,
                "pinTimeToLive": givenGetApplicationPinTimeToLive3,
                "verifyPinLimit": givenGetApplicationVerifyPinLimit3,
                "sendPinPerApplicationLimit": givenGetAppSendPinPerApplicationLimit3,
                "sendPinPerPhoneNumberLimit": givenGetAppSendPinPerPhoneNumberLimit3,
            },
            "enabled": givenEnabled3,
        },
    ]

    api_instance = TfaApi(get_api_client)

    setup_request(httpserver, tfa_applications_endpoint, expected_response)

    api_response = api_instance.get_tfa_applications()

    assert api_response[0].application_id == givenApplicationId1
    assert api_response[0].name == givenGetApplicationName1
    assert api_response[0].configuration.pin_attempts == givenGetApplicationPinAttempts1
    assert (
        api_response[0].configuration.allow_multiple_pin_verifications
        == givenAllowMultiplePinVerifications1
    )
    assert (
        api_response[0].configuration.pin_time_to_live
        == givenGetApplicationPinTimeToLive1
    )
    assert (
        api_response[0].configuration.verify_pin_limit
        == givenGetApplicationVerifyPinLimit1
    )
    assert (
        api_response[0].configuration.send_pin_per_application_limit
        == givenGetAppSendPinPerApplicationLimit1
    )
    assert (
        api_response[0].configuration.send_pin_per_phone_number_limit
        == givenGetAppSendPinPerPhoneNumberLimit1
    )
    assert api_response[0].enabled == givenEnabled1

    assert api_response[1].application_id == givenApplicationId2
    assert api_response[1].name == givenGetApplicationName2
    assert api_response[1].configuration.pin_attempts == givenGetApplicationPinAttempts2
    assert (
        api_response[1].configuration.allow_multiple_pin_verifications
        == givenAllowMultiplePinVerifications2
    )
    assert (
        api_response[1].configuration.pin_time_to_live
        == givenGetApplicationPinTimeToLive2
    )
    assert (
        api_response[1].configuration.verify_pin_limit
        == givenGetApplicationVerifyPinLimit2
    )
    assert (
        api_response[1].configuration.send_pin_per_application_limit
        == givenGetAppSendPinPerApplicationLimit2
    )
    assert (
        api_response[1].configuration.send_pin_per_phone_number_limit
        == givenGetAppSendPinPerPhoneNumberLimit2
    )
    assert api_response[1].enabled == givenEnabled2

    assert api_response[2].application_id == givenApplicationId3
    assert api_response[2].name == givenGetApplicationName3
    assert api_response[2].configuration.pin_attempts == givenGetApplicationPinAttempts3
    assert (
        api_response[2].configuration.allow_multiple_pin_verifications
        == givenAllowMultiplePinVerifications3
    )
    assert (
        api_response[2].configuration.pin_time_to_live
        == givenGetApplicationPinTimeToLive3
    )
    assert (
        api_response[2].configuration.verify_pin_limit
        == givenGetApplicationVerifyPinLimit3
    )
    assert (
        api_response[2].configuration.send_pin_per_application_limit
        == givenGetAppSendPinPerApplicationLimit3
    )
    assert (
        api_response[2].configuration.send_pin_per_phone_number_limit
        == givenGetAppSendPinPerPhoneNumberLimit3
    )
    assert api_response[2].enabled == givenEnabled3


def test_should_create_tfa_app(httpserver: HTTPServer, get_api_client):
    given_application_id = "1234567"
    given_create_application_name = "2fa application name"
    given_create_application_pin_attempts = 5
    given_allow_multiple_pin_verifications = True
    given_create_application_pin_time_to_live = "10m"
    given_create_application_verify_pin_limit = "2/4s"
    given_create_application_send_pin_per_application_limit = "5000/12h"
    given_create_application_send_pin_per_phone_number_limit = "2/1d"
    given_enabled = True

    given_request = {
        "name": given_create_application_name,
        "enabled": given_enabled,
        "configuration": {
            "pinAttempts": given_create_application_pin_attempts,
            "allowMultiplePinVerifications": given_allow_multiple_pin_verifications,
            "pinTimeToLive": given_create_application_pin_time_to_live,
            "verifyPinLimit": given_create_application_verify_pin_limit,
            "sendPinPerApplicationLimit": given_create_application_send_pin_per_application_limit,
            "sendPinPerPhoneNumberLimit": given_create_application_send_pin_per_phone_number_limit,
        },
    }

    expected_response = {
        "applicationId": given_application_id,
        "name": given_create_application_name,
        "configuration": {
            "pinAttempts": given_create_application_pin_attempts,
            "allowMultiplePinVerifications": given_allow_multiple_pin_verifications,
            "pinTimeToLive": given_create_application_pin_time_to_live,
            "verifyPinLimit": given_create_application_verify_pin_limit,
            "sendPinPerApplicationLimit": given_create_application_send_pin_per_application_limit,
            "sendPinPerPhoneNumberLimit": given_create_application_send_pin_per_phone_number_limit,
        },
        "enabled": given_enabled,
    }

    tfa_applications_endpoint = "/2fa/2/applications"

    api_instance = TfaApi(get_api_client)

    setup_request(
        httpserver,
        tfa_applications_endpoint,
        expected_response,
        "POST",
        200,
        given_request,
    )

    request = TfaApplicationRequest(
        name=given_create_application_name,
        enabled=given_enabled,
        configuration=TfaApplicationConfiguration(
            allow_multiple_pin_verifications=given_allow_multiple_pin_verifications,
            pin_attempts=given_create_application_pin_attempts,
            pin_time_to_live=given_create_application_pin_time_to_live,
            send_pin_per_application_limit=given_create_application_send_pin_per_application_limit,
            send_pin_per_phone_number_limit=given_create_application_send_pin_per_phone_number_limit,
            verify_pin_limit=given_create_application_verify_pin_limit,
        ),
    )

    api_response = api_instance.create_tfa_application(tfa_application_request=request)
    assert api_response.application_id == given_application_id
    assert api_response.name == given_create_application_name
    assert api_response.enabled == given_enabled
    assert (
        api_response.configuration.allow_multiple_pin_verifications
        == given_allow_multiple_pin_verifications
    )
    assert (
        api_response.configuration.pin_attempts == given_create_application_pin_attempts
    )
    assert (
        api_response.configuration.pin_time_to_live
        == given_create_application_pin_time_to_live
    )
    assert (
        api_response.configuration.send_pin_per_application_limit
        == given_create_application_send_pin_per_application_limit
    )
    assert (
        api_response.configuration.send_pin_per_phone_number_limit
        == given_create_application_send_pin_per_phone_number_limit
    )
    assert (
        api_response.configuration.verify_pin_limit
        == given_create_application_verify_pin_limit
    )


def test_should_get_tfa_app(httpserver: HTTPServer, get_api_client):
    given_application_id = "0933F3BC087D2A617AC6DCB2EF5B8A61"
    given_get_application_name = "Test application BASIC 1"
    given_get_application_pin_attempts = 10
    given_allow_multiple_pin_verifications = True
    given_get_application_pin_time_to_live = "2h"
    given_get_application_verify_pin_limit = "1/3s"
    given_get_app_send_pin_per_application_limit = "10000/1d"
    given_get_app_send_pin_per_phone_number_limit = "3/1d"
    given_enabled = True

    expected_response = {
        "applicationId": given_application_id,
        "name": given_get_application_name,
        "configuration": {
            "pinAttempts": given_get_application_pin_attempts,
            "allowMultiplePinVerifications": given_allow_multiple_pin_verifications,
            "pinTimeToLive": given_get_application_pin_time_to_live,
            "verifyPinLimit": given_get_application_verify_pin_limit,
            "sendPinPerApplicationLimit": given_get_app_send_pin_per_application_limit,
            "sendPinPerPhoneNumberLimit": given_get_app_send_pin_per_phone_number_limit,
        },
        "enabled": given_enabled,
    }

    tfa_get_app_endpoint = "/2fa/2/applications/" + given_application_id
    setup_request(httpserver, tfa_get_app_endpoint, expected_response)

    api_instance = TfaApi(get_api_client)
    api_response = api_instance.get_tfa_application(app_id=given_application_id)

    assert api_response.application_id == given_application_id


def test_should_update_tfa_app(httpserver: HTTPServer, get_api_client):
    given_application_id = "0933F3BC087D2A617AC6DCB2EF5B8A61"
    given_application_name = "Test application BASIC 1"
    given_application_pin_attempts = 10
    given_allow_multiple_pin_verifications = True
    given_application_pin_time_to_live = "2h"
    given_application_verify_pin_limit = "1/3s"
    given_app_send_pin_per_application_limit = "10000/1d"
    given_app_send_pin_per_phone_number_limit = "3/1d"
    given_enabled = True

    expected_response = {
        "applicationId": given_application_id,
        "name": given_application_name,
        "configuration": {
            "pinAttempts": given_application_pin_attempts,
            "allowMultiplePinVerifications": given_allow_multiple_pin_verifications,
            "pinTimeToLive": given_application_pin_time_to_live,
            "verifyPinLimit": given_application_verify_pin_limit,
            "sendPinPerApplicationLimit": given_app_send_pin_per_application_limit,
            "sendPinPerPhoneNumberLimit": given_app_send_pin_per_phone_number_limit,
        },
        "enabled": given_enabled,
    }

    request = TfaApplicationRequest(
        name=given_application_name,
        enabled=given_enabled,
        configuration=TfaApplicationConfiguration(
            allow_multiple_pin_verifications=given_allow_multiple_pin_verifications,
            pin_attempts=given_application_pin_attempts,
            pin_time_to_live=given_application_pin_time_to_live,
            send_pin_per_application_limit=given_app_send_pin_per_application_limit,
            send_pin_per_phone_number_limit=given_app_send_pin_per_phone_number_limit,
            verify_pin_limit=given_application_verify_pin_limit,
        ),
    )

    endpoint = "/2fa/2/applications/" + given_application_id
    setup_request(httpserver, endpoint, expected_response, "PUT")

    api_instance = TfaApi(get_api_client)
    api_response = api_instance.update_tfa_application(
        app_id=given_application_id, tfa_application_request=request
    )

    assert api_response.application_id == given_application_id


def test_should_get_tfa_templates(httpserver: HTTPServer, get_api_client):
    given_application_id = "HJ675435E3A6EA43432G5F37A635KJ8B"
    given_message_id1 = "9C815F8AF3328"
    given_message_id2 = "8F0792F86035A"
    given_speech_rate1 = 1.0
    given_speech_rate2 = 1.5

    given_response = [
        {
            "messageId": given_message_id1,
            "applicationId": given_application_id,
            "pinPlaceholder": "{{pin}}",
            "messageText": "Your PIN is {{pin}}.",
            "pinLength": 4,
            "pinType": "NUMERIC",
            "language": "en",
            "repeatDTMF": "1#",
            "speechRate": given_speech_rate1,
        },
        {
            "messageId": given_message_id2,
            "applicationId": given_application_id,
            "pinPlaceholder": "{{pin}}",
            "messageText": "Your PIN is {{pin}}.",
            "pinLength": 6,
            "pinType": "HEX",
            "repeatDTMF": "1#",
            "speechRate": given_speech_rate2,
        },
    ]

    endpoint = "/2fa/2/applications/{appId}/messages".replace(
        "{appId}", given_application_id
    )

    setup_request(httpserver, endpoint, given_response)

    api_instance = TfaApi(get_api_client)
    api_response = api_instance.get_tfa_message_templates(app_id=given_application_id)

    assert api_response[0].application_id == given_application_id
    assert api_response[0].message_id == given_message_id1
    assert api_response[0].speech_rate == given_speech_rate1

    assert api_response[1].application_id == given_application_id
    assert api_response[1].message_id == given_message_id2
    assert api_response[1].speech_rate == given_speech_rate2


def test_should_create_tfa_templates(httpserver: HTTPServer, get_api_client):
    given_message_text = "Your PIN is {{pin}}"
    given_pin_length = 4
    given_pin_type = TfaPinType("NUMERIC")
    given_language = TfaLanguage("en")
    given_sender_id = "Infobip 2FA"
    given_repeat_dtmf = "1#"
    given_speech_rate = 1.0
    given_message_id = "7654321"
    given_application_id = "1234567"

    given_response = {
        "applicationId": given_application_id,
        "messageId": given_message_id,
        "messageText": "Your pin is {{pin}}",
        "pinLength": 4,
        "pinType": "ALPHANUMERIC",
        "language": "en",
        "senderId": "Infobip 2FA",
        "repeatDTMF": "1#",
        "speechRate": given_speech_rate,
    }
    endpoint = "/2fa/2/applications/{appId}/messages".replace(
        "{appId}", given_application_id
    )
    setup_request(httpserver, endpoint, given_response, "POST")

    request = TfaCreateMessageRequest(
        message_text=given_message_text,
        pin_length=given_pin_length,
        pin_type=given_pin_type,
        language=given_language,
        sender_id=given_sender_id,
        repeat_dtmf=given_repeat_dtmf,
        speech_rate=given_speech_rate,
    )

    api_instance = TfaApi(get_api_client)
    api_response = api_instance.create_tfa_message_template(
        app_id=given_application_id, tfa_create_message_request=request
    )

    assert api_response.application_id == given_application_id
    assert api_response.message_id == given_message_id
    assert api_response.speech_rate == given_speech_rate


def test_should_get_tfa_template(httpserver: HTTPServer, get_api_client):
    given_message_id = "7654321"
    given_application_id = "1234567"
    given_speech_rate = 1.0

    given_response = {
        "applicationId": given_application_id,
        "messageId": given_message_id,
        "messageText": "Your pin is {{pin}}",
        "pinLength": 4,
        "pinType": "ALPHANUMERIC",
        "language": "en",
        "senderId": "Infobip 2FA",
        "repeatDTMF": "1#",
        "speechRate": given_speech_rate,
    }

    endpoint = "/2fa/2/applications/{appId}/messages/{msgId}".replace(
        "{appId}", given_application_id
    ).replace("{msgId}", given_message_id)
    setup_request(httpserver, endpoint, given_response)

    api_instance = TfaApi(get_api_client)
    api_response = api_instance.get_tfa_message_template(
        app_id=given_application_id, msg_id=given_message_id
    )

    assert api_response.application_id == given_application_id
    assert api_response.message_id == given_message_id
    assert api_response.speech_rate == given_speech_rate


def test_should_update_tfa_template(httpserver: HTTPServer, get_api_client):
    given_message_id = "7654321"
    given_application_id = "1234567"
    given_content_template_id = "your-template-id"
    given_response = {
        "applicationId": given_application_id,
        "messageId": given_message_id,
        "pinType": "ALPHANUMERIC",
        "messageText": "Your pin is {{pin}}",
        "pinLength": 6,
        "language": "en",
        "senderId": "Infobip 2FA",
        "repeatDTMF": "1#",
        "speechRate": 1.0,
        "regional": {
            "indiaDlt": {
                "contentTemplateId": given_content_template_id,
                "principalEntityId": "your-entity-id",
            }
        },
    }

    request = TfaUpdateMessageRequest(
        message_text="Your pin is {{pin}}",
        pin_length=6,
        pin_type=TfaPinType("ALPHANUMERIC"),
        language=TfaLanguage("en"),
        sender_id="Infobip 2FA",
        repeat_dtmf="1#",
        speech_rate=1.0,
        regional=TfaRegionalOptions(
            india_dlt=TfaIndiaDltOptions(
                content_template_id=given_content_template_id,
                principal_entity_id="your-entity-id",
            )
        ),
    )

    endpoint = "/2fa/2/applications/{appId}/messages/{msgId}".replace(
        "{appId}", given_application_id
    ).replace("{msgId}", given_message_id)
    setup_request(httpserver, endpoint, given_response, "PUT")

    api_instance = TfaApi(get_api_client)
    api_response = api_instance.update_tfa_message_template(
        app_id=given_application_id,
        msg_id=given_message_id,
        tfa_update_message_request=request,
    )

    assert api_response.application_id == given_application_id
    assert api_response.message_id == given_message_id
    assert (
        api_response.regional.india_dlt.content_template_id == given_content_template_id
    )


def test_should_send_pin_over_sms(httpserver: HTTPServer, get_api_client):
    given_application_id = "1234567"
    given_message_id = "7654321"
    given_from = "Sender 1"
    given_first_name = "John"
    given_pin_id = "9C817C6F8AF3D48F9FE553282AFA2B67"
    given_to = "41793026727"
    given_nc_status = "NC_DESTINATION_REACHABLE"
    given_sms_status = "MESSAGE_SENT"

    given_response = {
        "pinId": given_pin_id,
        "to": given_to,
        "ncStatus": given_nc_status,
        "smsStatus": given_sms_status,
    }

    endpoint = "/2fa/2/pin"
    setup_request(httpserver, endpoint, given_response, "POST")

    request = TfaStartAuthenticationRequest(
        application_id=given_application_id,
        message_id=given_message_id,
        to=given_to,
        _from=given_from,
        placeholders={"firstName": given_first_name},
    )
    api_instance = TfaApi(get_api_client)
    api_response = api_instance.send_tfa_pin_code_over_sms(
        tfa_start_authentication_request=request
    )
    assert api_response.pin_id == given_pin_id
    assert api_response.sms_status == given_sms_status


def test_should_resend_pin_over_sms(httpserver: HTTPServer, get_api_client):
    given_first_name = "John"
    given_pin_id = "9C817C6F8AF3D48F9FE553282AFA2B67"
    given_to = "41793026727"
    given_nc_status = "NC_DESTINATION_REACHABLE"
    given_sms_status = "MESSAGE_SENT"

    given_response = {
        "pinId": given_pin_id,
        "to": given_to,
        "ncStatus": given_nc_status,
        "smsStatus": given_sms_status,
    }

    endpoint = "/2fa/2/pin/{pinId}/resend".replace("{pinId}", given_pin_id)
    setup_request(httpserver, endpoint, given_response, "POST")

    request = TfaResendPinRequest(placeholders={"firstName": given_first_name})
    api_instance = TfaApi(get_api_client)
    api_response = api_instance.resend_tfa_pin_code_over_sms(
        pin_id=given_pin_id, tfa_resend_pin_request=request
    )
    assert api_response.pin_id == given_pin_id
    assert api_response.sms_status == given_sms_status


def test_should_send_pin_over_voice(httpserver: HTTPServer, get_api_client):
    given_application_id = "1234567"
    given_message_id = "7654321"
    given_from = "Sender 1"
    given_first_name = "John"
    given_pin_id = "9C817C6F8AF3D48F9FE553282AFA2B67"
    given_to = "41793026727"
    given_nc_status = "NC_DESTINATION_REACHABLE"
    given_sms_status = "MESSAGE_SENT"
    given_call_status = "PENDING_ACCEPTED"

    given_response = {
        "pinId": given_pin_id,
        "to": given_to,
        "ncStatus": given_nc_status,
        "smsStatus": given_sms_status,
        "callStatus": given_call_status,
    }

    endpoint = "/2fa/2/pin/voice"
    setup_request(httpserver, endpoint, given_response, "POST")

    request = TfaStartAuthenticationRequest(
        application_id=given_application_id,
        message_id=given_message_id,
        to=given_to,
        _from=given_from,
        placeholders={"firstName": given_first_name},
    )
    api_instance = TfaApi(get_api_client)
    api_response = api_instance.send_tfa_pin_code_over_voice(
        tfa_start_authentication_request=request
    )
    assert api_response.pin_id == given_pin_id
    assert api_response.call_status == given_call_status


def test_should_resend_pin_over_voice(httpserver: HTTPServer, get_api_client):
    given_first_name = "John"
    given_pin_id = "9C817C6F8AF3D48F9FE553282AFA2B67"
    given_to = "41793026727"
    given_nc_status = "NC_DESTINATION_REACHABLE"
    given_sms_status = "MESSAGE_SENT"
    given_call_status = "PENDING_ACCEPTED"

    given_response = {
        "pinId": given_pin_id,
        "to": given_to,
        "ncStatus": given_nc_status,
        "smsStatus": given_sms_status,
        "callStatus": given_call_status,
    }

    endpoint = "/2fa/2/pin/{pinId}/resend/voice".replace("{pinId}", given_pin_id)
    setup_request(httpserver, endpoint, given_response, "POST")

    request = TfaResendPinRequest(placeholders={"firstName": given_first_name})
    api_instance = TfaApi(get_api_client)
    api_response = api_instance.resend_tfa_pin_code_over_voice(
        pin_id=given_pin_id, tfa_resend_pin_request=request
    )
    assert api_response.pin_id == given_pin_id
    assert api_response.call_status == given_call_status


def test_should_verify_phone_number(httpserver: HTTPServer, get_api_client):
    given_pin_id = "9C817C6F8AF3D48F9FE553282AFA2B67"
    given_msisdn = "41793026727"
    given_pin = "1598"

    given_response = {
        "pinId": given_pin_id,
        "msisdn": given_msisdn,
        "verified": True,
        "attemptsRemaining": 0,
    }

    endpoint = "/2fa/2/pin/{pinId}/verify".replace("{pinId}", given_pin_id)
    setup_request(httpserver, endpoint, given_response, "POST")

    request = TfaVerifyPinRequest(pin=given_pin)

    api_instance = TfaApi(get_api_client)
    api_response = api_instance.verify_tfa_phone_number(
        pin_id=given_pin_id, tfa_verify_pin_request=request
    )
    assert api_response.pin_id == given_pin_id
    assert api_response.msisdn == given_msisdn


def test_get_tfa_verification_status(httpserver: HTTPServer, get_api_client):
    given_app_id = "16A8B5FE2BCD6CA716A2D780CB3F3390"
    given_msisdn = "41793026727"

    given_response = {
        "verifications": [
            {
                "msisdn": given_msisdn,
                "verified": True,
                "verifiedAt": 1418364366,
                "sentAt": 1418364246,
            },
            {
                "msisdn": given_msisdn,
                "verified": False,
                "verifiedAt": 1418364226,
                "sentAt": 1418333246,
            },
        ]
    }

    endpoint = "/2fa/2/applications/{appId}/verifications".replace(
        "{appId}", given_app_id
    )

    setup_request(httpserver, endpoint, given_response)

    api_instance = TfaApi(get_api_client)
    api_response = api_instance.get_tfa_verification_status(
        msisdn=given_msisdn, app_id=given_app_id
    )

    assert len(api_response.verifications) == 2
    assert api_response.verifications[0].msisdn == given_msisdn


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
