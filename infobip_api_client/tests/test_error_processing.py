import json

import pytest
from pytest_httpserver import HTTPServer

from infobip_api_client import (
    ApiClient,
    Configuration,
    SmsMessage,
    SmsTextContent,
    SmsDestination,
    SmsApi,
    SmsRequest,
    SmsMessageContent,
)
from infobip_api_client.exceptions import (
    ApiException,
    ForbiddenException,
    NotFoundException,
    UnauthorizedException,
    ServiceException,
    BadRequestException,
)
from infobip_api_client.tests.test_sms_api import sms_messages

sms_messages = "sms/3/messages"
sms_advanced_textual_endpoint = "/sms/2/text/advanced"
sms_advanced_binary_endpoint = "/sms/2/binary/advanced"
sms_preview_endpoint = "/sms/1/preview"
sms_bulks_endpoint = "/sms/1/bulks"
sms_bulks_status_endpoint = "/sms/1/bulks/status"
sms_outbound_reports_endpoint = "/sms/1/reports"
sms_outbound_logs_endpoint = "/sms/1/logs"
sms_inbound_messages_endpoint = "/sms/1/inbox/reports"

port = 8088


def error_response(message_id: str, text: str) -> dict:
    return {
        "requestError": {"serviceException": {"messageId": message_id, "text": text}}
    }


def error_response_with_validation_errors(
    message_id: str, text: str, validation_errors: dict
) -> dict:
    return {
        "requestError": {
            "serviceException": {
                "messageId": message_id,
                "text": text,
                "validationErrors": validation_errors,
            }
        }
    }


@pytest.mark.parametrize(
    ["status_code", "error_response_json", "exception_type"],
    [
        (
            401,
            error_response("UNAUTHORIZED", "Invalid login details"),
            UnauthorizedException,
        ),
        (
            403,
            error_response("UNAUTHORIZED", "Unauthorized access"),
            ForbiddenException,
        ),
        (
            404,
            error_response("NOT_FOUND", "Requested resource not found"),
            NotFoundException,
        ),
        (429, error_response("TOO_MANY_REQUESTS", "Too many requests"), ApiException),
        (
            500,
            error_response(
                "GENERAL_ERROR", "Something went wrong. Please contact support."
            ),
            ServiceException,
        ),
        (
            400,
            error_response_with_validation_errors(
                "BAD_REQUEST",
                "Bad Request",
                {"messages[0].destinations": ["must not be empty"]},
            ),
            BadRequestException,
        ),
    ],
)
def test_error_processing(
    httpserver: HTTPServer,
    sms_api_client: SmsApi,
    status_code: int,
    error_response_json: dict,
    exception_type: type,
):
    httpserver.expect_request(
        uri="/sms/3/messages",
        method="POST",
    ).respond_with_json(status=status_code, response_json=error_response_json)

    request = SmsRequest(
        messages=[
            SmsMessage(
                destinations=[SmsDestination(to="41793026727")],
                sender="InfoSMS",
                content=SmsMessageContent(
                    actual_instance=SmsTextContent(text="Test message")
                ),
            )
        ]
    )

    with pytest.raises(ApiException) as exception:
        sms_api_client.send_sms_messages(sms_request=request)

    assert exception.type == exception_type
    assert exception.value.body == json.dumps(error_response_json, indent=4)
    assert exception.value.status == status_code


@pytest.fixture
def sms_api_client():
    return SmsApi(
        ApiClient(
            Configuration(
                host="http://localhost:{}".format(port),
                api_key="givenApiKeyValue",
                api_key_prefix="App",
            )
        )
    )


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", port
