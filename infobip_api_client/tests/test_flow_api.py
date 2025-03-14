
import pytest
from infobip_api_client import (
    ApiClient,
    Configuration,
    FlowApi,
    FlowAddFlowParticipantsRequest,
    FlowParticipant,
    FlowPersonUniqueField,
    FlowPerson,
    FlowEmailContact,
    FlowPersonContacts,
    FlowAddFlowParticipantsResponse,
    FlowPersonUniqueFieldType,
    FlowAddFlowParticipantStatus,
    FlowErrorStatusReason,
)
from pytest_httpserver import HTTPServer


def test_should_add_participants_to_flow(httpserver: HTTPServer, get_api_client):
    campaign_id = 200000000000001
    notify_url = "https://example.com"
    callback_data = "Callback Data"

    identifier1 = "370329180020364"
    type1 = "FACEBOOK"

    identifier2 = "test@infobip.com"
    type2 = "EMAIL"
    order_number2 = 1167873391

    identifier3 = "test2@infobip.com"
    type3 = "EMAIL"
    order_number3 = 1595299041
    external_id3 = "optional_external_person_id"
    contract_expiry3 = "2023-04-01"
    company3 = "Infobip"
    email3 = "test@infobip.com"

    given_request = {
        "participants": [
            {"identifyBy": {"identifier": identifier1, "type": type1}},
            {"identifyBy": {"identifier": identifier2, "type": type2}},
            {
                "identifyBy": {"identifier": identifier3, "type": type3},
                "variables": {"orderNumber": order_number3},
                "person": {
                    "externalId": external_id3,
                    "contactInformation": {"email": [{"address": email3}]},
                },
            },
        ],
        "notifyUrl": notify_url,
        "callbackData": callback_data,
    }

    given_operation_id = "03f2d474-0508-46bf-9f3d-d8e2c28adaea"
    given_response = {"operationId": given_operation_id}

    setup_request(
        httpserver,
        f"/moments/1/flows/{campaign_id}/participants",
        given_response,
        "POST",
        200,
        given_request,
    )

    api_instance = FlowApi(get_api_client)
    request = FlowAddFlowParticipantsRequest(
        participants=[
            FlowParticipant(
                identify_by=FlowPersonUniqueField(
                    identifier=identifier1, type=FlowPersonUniqueFieldType.FACEBOOK
                )
            ),
            FlowParticipant(
                identify_by=FlowPersonUniqueField(
                    identifier=identifier2, type=FlowPersonUniqueFieldType.EMAIL
                ),
            ),
            FlowParticipant(
                identify_by=FlowPersonUniqueField(
                    identifier=identifier3, type=FlowPersonUniqueFieldType.EMAIL
                ),
                variables={"orderNumber": order_number3},
                person=FlowPerson(
                    external_id=external_id3,
                    contact_information=FlowPersonContacts(
                        email=[FlowEmailContact(address=email3)]
                    ),
                ),
            ),
        ],
        notify_url=notify_url,
        callback_data=callback_data,
    )

    api_response = api_instance.add_flow_participants(campaign_id, request)
    expected_response = FlowAddFlowParticipantsResponse(operation_id=given_operation_id)
    assert api_response == expected_response


def test_should_get_participants_report(httpserver: HTTPServer, get_api_client):
    campaign_id = 200000000000001
    given_operation_id = "03f2d474-0508-46bf-9f3d-d8e2c28adaea"
    given_callback_data = "Callback Data"
    given_identifier1 = "test@infobip.com"
    given_identifier2 = "test2@infobip.com"
    given_type = FlowPersonUniqueFieldType.EMAIL
    given_status1 = FlowAddFlowParticipantStatus.ACCEPTED
    given_status2 = FlowAddFlowParticipantStatus.REJECTED
    given_error_reason = FlowErrorStatusReason.REJECTED_INVALID_CONTACT

    given_response = {
        "operationId": given_operation_id,
        "campaignId": campaign_id,
        "callbackData": given_callback_data,
        "participants": [
            {
                "identifyBy": {"identifier": given_identifier1, "type": given_type},
                "status": given_status1,
            },
            {
                "identifyBy": {"identifier": given_identifier2, "type": given_type},
                "status": given_status2,
                "errorReason": given_error_reason,
            },
        ],
    }

    setup_request(
        httpserver,
        f"/moments/1/flows/{campaign_id}/participants/report",
        given_response,
    )

    api_instance = FlowApi(get_api_client)
    api_response = api_instance.get_flow_participants_added_report(
        campaign_id, given_operation_id
    )

    assert api_response.operation_id == given_operation_id
    assert api_response.campaign_id == campaign_id
    assert api_response.callback_data == given_callback_data

    participants = api_response.participants
    assert len(participants) == 2

    participant1 = participants[0]
    assert participant1.identify_by.identifier == given_identifier1
    assert participant1.identify_by.type == given_type
    assert participant1.status == given_status1

    participant2 = participants[1]
    assert participant2.identify_by.identifier == given_identifier2
    assert participant2.identify_by.type == given_type
    assert participant2.status == given_status2
    assert participant2.error_reason == given_error_reason


def test_should_remove_participant_from_flow(httpserver: HTTPServer, get_api_client):
    campaign_id = 200000000000001
    expected_response = None

    setup_request(
        httpserver,
        f"/communication/1/flows/{campaign_id}/participants",
        expected_response,
        "DELETE",
    )

    api_instance = FlowApi(get_api_client)
    api_response = api_instance.remove_people_from_flow(campaign_id)

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
