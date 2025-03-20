import datetime

import pytest
from dateutil.tz import tzoffset

from infobip_api_client import ApiClient, Configuration, VoiceApi, CallsUpdateScenarioRequest, \
    CallsUpdateScenarioResponse, CallsSearchResponse
from pytest_httpserver import HTTPServer



def test_should_get_voice_ivr_scenario(httpserver: HTTPServer, get_api_client):
    given_id = "E83E787CF2613450157ADA3476171E3F"
    given_name = "scenario"
    given_description = ""
    given_create_time = "2023-12-06T13:37:15Z"
    given_create_time_datetime = datetime.datetime(2023, 12, 6, 13, 37, 15, tzinfo=datetime.timezone.utc)
    given_update_time = None
    script = "[{\"dial\": \"dial\", \"actionId\": 1}]"
    given_last_usage_date = datetime.date(2024, 1, 1)

    given_response = [{
        "id": given_id,
        "name": given_name,
        "description": given_description,
        "createTime": given_create_time,
        "updateTime": given_update_time,
        "script": [
            {
                "dial": "dial",
                "actionId": 1
            }
        ],
        "lastUsageDate": "2024-01-01"
    }]

    setup_request(httpserver, "/voice/ivr/1/scenarios", given_response, "GET", 200)

    api_instance = VoiceApi(get_api_client)

    api_response = api_instance.search_voice_ivr_scenarios()

    expected_response = [
        CallsSearchResponse(
            id=given_id,
            name=given_name,
            description=given_description,
            create_time=given_create_time_datetime,
            update_time=None,
            script=script,
            last_usage_date=given_last_usage_date,
        )
    ]

    assert api_response == expected_response


def test_should_create_call_api_voice_ivr_scenario(httpserver: HTTPServer, get_api_client):
    script = "[{\"request\": \"https://example.com/api/12345\",\"options\": {\"method\": \"POST\",\"headers\": {\"content-type\": \"application/json\"},\"body\": {\"payload\": \"${to} finished the IVR.\"}}}]"
    given_request = {
        "name": "Call API",
        "description": "Perform a POST request to provided URL with headers and payload.",
        "script": [{
            "request": "https://example.com/api/12345",
            "options": {
                "method": "POST",
                "headers": {"content-type": "application/json"},
                "body": {"payload": "${to} finished the IVR."}
            }
        }]
    }

    given_response = {
        "id": "E83E787CF2613450157ADA3476171E3F",
        "name": "Call API",
        "description": "Perform a POST request to provided URL with headers and payload.",
        "createTime": "2024-11-09T17:00:00.000+01:00",
    }

    given_create_time_datetime = datetime.datetime(2024, 11, 9, 17, 0, 0, tzinfo=tzoffset(None, 3600))

    setup_request(httpserver, "/voice/ivr/1/scenarios", given_response, "POST", 200, given_request)

    api_instance = VoiceApi(get_api_client)

    request = CallsUpdateScenarioRequest(
        name="Call API",
        description="Perform a POST request to provided URL with headers and payload.",
        script=script
    )

    api_response = api_instance.create_a_voice_ivr_scenario(request)

    expected_response = CallsUpdateScenarioResponse(
        id="E83E787CF2613450157ADA3476171E3F",
        name="Call API",
        description="Perform a POST request to provided URL with headers and payload.",
        create_time=given_create_time_datetime
    )

    assert api_response == expected_response

def test_should_get_voice_ivr_scenario_by_id(httpserver: HTTPServer, get_api_client):
    given_id = "E83E787CF2613450157ADA3476171E3F"
    given_name = "scenario"
    given_description = ""
    given_create_time = "2023-12-06T13:37:15Z"
    given_create_time_datetime = datetime.datetime(2023, 12, 6, 13, 37, 15, tzinfo=tzoffset(None, 0))
    given_update_time = None
    script = "[{\"dial\": \"dial\", \"actionId\": 1}]"

    given_response = {
        "id": given_id,
        "name": given_name,
        "description": given_description,
        "createTime": given_create_time,
        "updateTime": given_update_time,
        "script": [{"dial": "dial", "actionId": 1}]
    }

    setup_request(httpserver, f"/voice/ivr/1/scenarios/{given_id}", given_response, "GET", 200)

    api_instance = VoiceApi(get_api_client)

    api_response = api_instance.get_a_voice_ivr_scenario(given_id)

    assert api_response is not None
    assert api_response.id == given_id
    assert api_response.name == given_name
    assert api_response.description == given_description
    assert api_response.create_time == given_create_time_datetime
    assert api_response.update_time is None
    assert api_response.script == script


def test_should_create_voice_ivr_scenario(httpserver: HTTPServer, get_api_client):
    given_id = "E83E787CF2613450157ADA3476171E3F"
    given_name = "scenario"
    given_description = ""
    given_create_time = "2023-12-06T13:37:15Z"
    given_create_time_datetime = datetime.datetime(2023, 12, 6, 13, 37, 15, tzinfo=tzoffset(None, 0))
    given_update_time = None
    script = "[{\"dial\": \"dial\", \"actionId\": 1}]"

    given_request = {
        "name": given_name,
        "description": given_description,
        "script": [{"dial": "dial", "actionId": 1}]
    }

    given_response = {
        "id": given_id,
        "name": given_name,
        "description": given_description,
        "createTime": given_create_time,
        "updateTime": given_update_time,
        "script": [{"dial": "dial", "actionId": 1}]
    }

    setup_request(httpserver, "/voice/ivr/1/scenarios", given_response, "POST", 200, given_request)

    api_instance = VoiceApi(get_api_client)

    request = CallsUpdateScenarioRequest(
        name=given_name,
        description=given_description,
        script="[{\"dial\": \"dial\", \"actionId\": 1}]"
    )

    expected_response = CallsUpdateScenarioResponse(
        id=given_id,
        name=given_name,
        description=given_description,
        create_time=given_create_time_datetime,
        update_time=None,
        script=script
    )

    api_response = api_instance.create_a_voice_ivr_scenario(request)

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