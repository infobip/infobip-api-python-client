from infobip_api_client import (
    ApiClient,
    Configuration,
    CallsVoiceResponse,
    CallsVoiceResponseDetails,
    CallsSingleMessageStatus,
)
from infobip_api_client.api.click_to_call_api import ClickToCallApi
from infobip_api_client.models.calls_click_to_call_message import (
    CallsClickToCallMessage,
)
from infobip_api_client.models.calls_click_to_call_message_body import (
    CallsClickToCallMessageBody,
)
from infobip_api_client.models.calls_delivery_day import CallsDeliveryDay
from infobip_api_client.models.calls_delivery_time import CallsDeliveryTime
from infobip_api_client.models.calls_delivery_time_window import CallsDeliveryTimeWindow
from infobip_api_client.models.calls_retry import CallsRetry
from infobip_api_client.models.calls_voice import CallsVoice

import pytest
from pytest_httpserver import HTTPServer

click_to_call_send_message = "/voice/ctc/1/send"


def test_should_send_click_to_call_message(httpserver: HTTPServer, get_api_client):
    given_bulk_id = "4fda521a-c680-470d-b134-83d468f7ac80"
    given_from = "41793026700"
    given_from_b = "41793026701"
    given_destination_a = "41793026727"
    given_destination_b = "41793026731"
    given_req_message_id = "MESSAGE-ID-123-xyz"
    given_text = "Test Voice message."
    given_language = "en"
    given_name = "Joanna"
    given_gender = "female"
    given_anonymization = False
    given_notify_url = "https=//www.example.com/voice/clicktocall"
    given_notify_content_type = "application/json"
    given_max_duration = 60
    given_warning_time = 5
    given_min_period = 1
    given_max_period = 5
    given_max_count = 5
    given_machine_detection = "hangup"
    given_from_hour = 6
    given_from_minute = 0
    given_to_hour = 15
    given_to_minute = 30

    given_request = {
        "bulkId": given_bulk_id,
        "messages": [
            {
                "from": given_from,
                "fromB": given_from_b,
                "destinationA": given_destination_a,
                "destinationB": given_destination_b,
                "messageId": given_req_message_id,
                "text": given_text,
                "language": given_language,
                "voice": {"name": given_name, "gender": given_gender},
                "anonymization": given_anonymization,
                "notifyUrl": given_notify_url,
                "notifyContentType": given_notify_content_type,
                "maxDuration": given_max_duration,
                "warningTime": given_warning_time,
                "retry": {
                    "minPeriod": given_min_period,
                    "maxPeriod": given_max_period,
                    "maxCount": given_max_count,
                },
                "machineDetection": given_machine_detection,
                "deliveryTimeWindow": {
                    "from": {"hour": given_from_hour, "minute": given_from_minute},
                    "to": {"hour": given_to_hour, "minute": given_to_minute},
                    "days": [
                        "MONDAY",
                        "TUESDAY",
                        "WEDNESDAY",
                        "THURSDAY",
                        "FRIDAY",
                        "SATURDAY",
                        "SUNDAY",
                    ],
                },
            }
        ],
    }

    given_to = "41793026727"
    given_status_group_id = 1
    given_status_group_name = "PENDING"
    given_status_id = 26
    given_status_name = "PENDING_ACCEPTED"
    given_status_description = "Message accepted, pending for delivery."
    given_message_id = "2250be2d4219-3af1-78856-aabe-1362af1edfd2"

    given_response = {
        "bulkId": given_bulk_id,
        "messages": [
            {
                "to": given_to,
                "status": {
                    "groupId": given_status_group_id,
                    "groupName": given_status_group_name,
                    "id": given_status_id,
                    "name": given_status_name,
                    "description": given_status_description,
                },
                "messageId": given_message_id,
            }
        ],
    }

    api_instance = ClickToCallApi(get_api_client)

    setup_request(
        httpserver,
        click_to_call_send_message,
        given_response,
        "POST",
        200,
        given_request,
    )

    request: CallsClickToCallMessageBody = CallsClickToCallMessageBody(
        bulk_id=given_bulk_id,
        messages=[
            CallsClickToCallMessage(
                var_from=given_from,
                from_b=given_from_b,
                destination_a=given_destination_a,
                destination_b=given_destination_b,
                message_id=given_req_message_id,
                text=given_text,
                language=given_language,
                voice=CallsVoice(name=given_name, gender=given_gender),
                anonymization=given_anonymization,
                notify_url=given_notify_url,
                notify_content_type=given_notify_content_type,
                max_duration=given_max_duration,
                warning_time=given_warning_time,
                retry=CallsRetry(
                    min_period=given_min_period,
                    max_period=given_max_period,
                    max_count=given_max_count,
                ),
                machine_detection=given_machine_detection,
                delivery_time_window=CallsDeliveryTimeWindow(
                    var_from=CallsDeliveryTime(
                        hour=given_from_hour, minute=given_from_minute
                    ),
                    to=CallsDeliveryTime(hour=given_to_hour, minute=given_to_minute),
                    days=[
                        CallsDeliveryDay.MONDAY,
                        CallsDeliveryDay.TUESDAY,
                        CallsDeliveryDay.WEDNESDAY,
                        CallsDeliveryDay.THURSDAY,
                        CallsDeliveryDay.FRIDAY,
                        CallsDeliveryDay.SATURDAY,
                        CallsDeliveryDay.SUNDAY,
                    ],
                ),
            )
        ],
    )

    api_response = api_instance.send_click_to_call_message(
        calls_click_to_call_message_body=request
    )

    expected_click_to_call_response = CallsVoiceResponse(
        bulk_id=given_bulk_id,
        messages=[
            CallsVoiceResponseDetails(
                to=given_to,
                status=CallsSingleMessageStatus(
                    group_id=given_status_group_id,
                    group_name=given_status_group_name,
                    id=given_status_id,
                    name=given_status_name,
                    description=given_status_description,
                ),
                message_id=given_message_id,
            )
        ],
    )

    assert api_response == expected_click_to_call_response


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
