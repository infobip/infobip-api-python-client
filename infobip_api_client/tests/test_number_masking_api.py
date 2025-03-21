import datetime

import pytest
from unittest.mock import patch
from pytest_httpserver import HTTPServer


from infobip_api_client import (
    ApiClient,
    Configuration,
    NumberMaskingApi,
    NumberMaskingSetupResponse,
    NumberMaskingSetupBody,
    NumberMaskingUploadBody,
    NumberMaskingUploadResponse,
    NumberMaskingCredentialsResponse,
    NumberMaskingCredentialsBody,
)


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


number_masking_configurations = "/voice/masking/2/config"
number_masking_configuration = "/voice/masking/2/config/{key}"
number_masking_upload_audio = "/voice/masking/1/upload"
number_masking_credentials = "/voice/masking/2/credentials"


def test_should_get_voice_masking_config(httpserver: HTTPServer, get_api_client):
    given_key = "string"
    given_name = "string"
    given_callback_url = "string"
    given_status_url = "string"
    given_backup_callback_url = "string"
    given_backup_status_url = "string"
    given_description = "string"
    given_insert_date_time = "2023-08-01T16:10:00+05:30"
    given_update_date_time = "2023-08-01T16:10:00+05:30"
    given_insert_date_time_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )
    given_update_date_time_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )

    given_response = [
        {
            "key": given_key,
            "name": given_name,
            "callbackUrl": given_callback_url,
            "statusUrl": given_status_url,
            "backupCallbackUrl": given_backup_callback_url,
            "backupStatusUrl": given_backup_status_url,
            "description": given_description,
            "insertDateTime": given_insert_date_time,
            "updateDateTime": given_update_date_time,
        }
    ]

    setup_request(httpserver, number_masking_configurations, given_response)

    api = NumberMaskingApi(get_api_client)

    response = api.get_number_masking_configurations()

    expected_response = [
        NumberMaskingSetupResponse(
            key=given_key,
            name=given_name,
            callback_url=given_callback_url,
            status_url=given_status_url,
            backup_callback_url=given_backup_callback_url,
            backup_status_url=given_backup_status_url,
            description=given_description,
            insert_date_time=given_insert_date_time_offset,
            update_date_time=given_update_date_time_offset,
        )
    ]

    assert response == expected_response


def test_get_number_masking_configuration_when_utc_date_is_returned_regardless_of_default_timezone(httpserver: HTTPServer, get_api_client):
    test_default_timezone = datetime.timezone(datetime.timedelta(hours=1))  # Europe/Zagreb is UTC+1

    given_key = "string"
    given_name = "string"
    given_callback_url = "string"
    given_status_url = "string"
    given_backup_callback_url = "string"
    given_backup_status_url = "string"
    given_description = "string"
    given_insert_date_time = "2023-08-01T16:10:00.00"
    given_update_date_time = "2023-08-01T16:10:00.00"
    given_insert_date_time_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone.utc,
    )
    given_update_date_time_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone.utc,
    )

    given_response = [
        {
            "key": given_key,
            "name": given_name,
            "callbackUrl": given_callback_url,
            "statusUrl": given_status_url,
            "backupCallbackUrl": given_backup_callback_url,
            "backupStatusUrl": given_backup_status_url,
            "description": given_description,
            "insertDateTime": given_insert_date_time,
            "updateDateTime": given_update_date_time,
        }
    ]

    setup_request(httpserver, number_masking_configurations, given_response)

    api = NumberMaskingApi(get_api_client)

    expected_response = [
        NumberMaskingSetupResponse(
            key=given_key,
            name=given_name,
            callback_url=given_callback_url,
            status_url=given_status_url,
            backup_callback_url=given_backup_callback_url,
            backup_status_url=given_backup_status_url,
            description=given_description,
            insert_date_time=given_insert_date_time_offset,
            update_date_time=given_update_date_time_offset,
        )
    ]

    with patch("datetime.timezone", test_default_timezone):
        response = api.get_number_masking_configurations()
        assert response == expected_response

def test_should_create_voice_masking_config(httpserver: HTTPServer, get_api_client):
    given_name = "UniqueConfigurationName"
    given_callback_url = "https://example.com/1/callback"
    given_status_url = "https://example.com/1/status"
    given_insert_date_time = "2019-08-16T09:11:36.573"
    given_update_date_time = "2019-08-16T09:11:36.573"
    given_insert_date_time_offset = datetime.datetime.fromisoformat(
        given_insert_date_time
    )
    given_update_date_time_offset = datetime.datetime.fromisoformat(
        given_update_date_time
    )

    given_request = {
        "name": given_name,
        "callbackUrl": given_callback_url,
        "statusUrl": given_status_url,
    }

    given_response = {
        "key": "3FC0C9CB4AFAEAC67E8FC6BA3B1E044A",
        "name": given_name,
        "callbackUrl": given_callback_url,
        "statusUrl": given_status_url,
        "insertDateTime": given_insert_date_time,
        "updateDateTime": given_update_date_time,
    }

    setup_request(
        httpserver,
        number_masking_configurations,
        given_response,
        "POST",
        200,
        given_request,
    )

    api = NumberMaskingApi(get_api_client)

    request = NumberMaskingSetupBody(
        name=given_name, callback_url=given_callback_url, status_url=given_status_url
    )

    response = api.create_number_masking_configuration(request)

    expected_response = NumberMaskingSetupResponse(
        key="3FC0C9CB4AFAEAC67E8FC6BA3B1E044A",
        name=given_name,
        callback_url=given_callback_url,
        status_url=given_status_url,
        insert_date_time=given_insert_date_time_offset,
        update_date_time=given_update_date_time_offset,
    )

    assert response == expected_response


def test_should_get_number_masking_configuration(
    httpserver: HTTPServer, get_api_client
):
    given_key = "3FC0C9CB4AFAEAC67E8FC6BA3B1E044A"
    given_name = "UniqueConfigurationName"
    given_callback_url = "https://example.com/1/callback"
    given_status_url = "https://example.com/1/status"
    given_insert_date_time = "2019-08-16T09:11:36.573"
    given_update_date_time = "2019-08-16T09:11:36.573"
    given_insert_date_time_offset = datetime.datetime.fromisoformat(
        given_insert_date_time
    )
    given_update_date_time_offset = datetime.datetime.fromisoformat(
        given_update_date_time
    )

    given_response = {
        "key": given_key,
        "name": given_name,
        "callbackUrl": given_callback_url,
        "statusUrl": given_status_url,
        "insertDateTime": given_insert_date_time,
        "updateDateTime": given_update_date_time,
    }

    endpoint = number_masking_configuration.replace("{key}", given_key)
    setup_request(httpserver, endpoint, given_response)

    api = NumberMaskingApi(get_api_client)

    response = api.get_number_masking_configuration(given_key)

    expected_response = NumberMaskingSetupResponse(
        key=given_key,
        name=given_name,
        callback_url=given_callback_url,
        status_url=given_status_url,
        insert_date_time=given_insert_date_time_offset,
        update_date_time=given_update_date_time_offset,
    )

    assert response == expected_response


def test_should_update_number_masking_configuration(
    httpserver: HTTPServer, get_api_client
):
    given_key = "3FC0C9CB4AFAEAC67E8FC6BA3B1E044A"
    given_name = "UniqueConfigurationName"
    given_callback_url = "https://example.com/1/callback"
    given_status_url = "https://example.com/1/status"
    given_insert_date_time = "2019-08-16T09:11:36.573"
    given_update_date_time = "2019-08-16T09:11:36.573"
    given_insert_date_time_offset = datetime.datetime.fromisoformat(
        given_insert_date_time
    )
    given_update_date_time_offset = datetime.datetime.fromisoformat(
        given_update_date_time
    )

    given_request = {
        "name": given_name,
        "callbackUrl": given_callback_url,
        "statusUrl": given_status_url,
    }

    given_response = {
        "key": given_key,
        "name": given_name,
        "callbackUrl": given_callback_url,
        "statusUrl": given_status_url,
        "insertDateTime": given_insert_date_time,
        "updateDateTime": given_update_date_time,
    }

    endpoint = number_masking_configuration.replace("{key}", given_key)
    setup_request(httpserver, endpoint, given_response, "PUT", 200, given_request)

    api = NumberMaskingApi(get_api_client)

    request = NumberMaskingSetupBody(
        name=given_name, callback_url=given_callback_url, status_url=given_status_url
    )

    response = api.update_number_masking_configuration(given_key, request)

    expected_response = NumberMaskingSetupResponse(
        key=given_key,
        name=given_name,
        callback_url=given_callback_url,
        status_url=given_status_url,
        insert_date_time=given_insert_date_time_offset,
        update_date_time=given_update_date_time_offset,
    )

    assert response == expected_response


def test_should_upload_audio_file(httpserver: HTTPServer, get_api_client):
    given_url = "https://www.example.com/example-audio-file.mp3"
    given_file_id = "cb702ae4-f356-4efd-b2dd-7a667b570af5"

    given_request = {"url": given_url}

    given_response = {"fileId": given_file_id}

    setup_request(
        httpserver,
        number_masking_upload_audio,
        given_response,
        "POST",
        200,
        given_request,
    )

    api = NumberMaskingApi(get_api_client)

    request = NumberMaskingUploadBody(url=given_url)

    response = api.upload_audio_files(request)

    expected_response = NumberMaskingUploadResponse(file_id=given_file_id)

    assert response == expected_response


def test_should_get_number_masking_credentials(httpserver: HTTPServer, get_api_client):
    given_api_id = "55ddccad2df62a4b615b7e3c472b2ab6"
    given_key = "5da086b6a8e4424993646b8699c333ca"

    given_response = {"apiId": given_api_id, "key": given_key}

    setup_request(httpserver, number_masking_credentials, given_response)

    api = NumberMaskingApi(get_api_client)

    response = api.get_number_masking_credentials()

    expected_response = NumberMaskingCredentialsResponse(
        api_id=given_api_id, key=given_key
    )

    assert response == expected_response


def test_should_update_number_masking_credentials(
    httpserver: HTTPServer, get_api_client
):
    given_api_id = "55ddccad2df62a4b615b7e3c472b2ab6"
    given_key = "5da086b6a8e4424993646b8699c333ca"

    given_request = {"apiId": given_api_id, "key": given_key}

    given_response = {"apiId": given_api_id, "key": given_key}

    setup_request(
        httpserver,
        number_masking_credentials,
        given_response,
        "PUT",
        200,
        given_request,
    )

    api = NumberMaskingApi(get_api_client)

    request = NumberMaskingCredentialsBody(api_id=given_api_id, key=given_key)

    response = api.update_number_masking_credentials(request)

    expected_response = NumberMaskingCredentialsResponse(
        api_id=given_api_id, key=given_key
    )

    assert response == expected_response


def test_should_create_number_masking_credentials(
    httpserver: HTTPServer, get_api_client
):
    given_api_id = "55ddccad2df62a4b615b7e3c472b2ab6"
    given_key = "5da086b6a8e4424993646b8699c333ca"

    given_request = {"apiId": given_api_id, "key": given_key}

    given_response = {"apiId": given_api_id, "key": given_key}

    setup_request(
        httpserver,
        number_masking_credentials,
        given_response,
        "POST",
        200,
        given_request,
    )

    api = NumberMaskingApi(get_api_client)

    request = NumberMaskingCredentialsBody(api_id=given_api_id, key=given_key)

    response = api.create_number_masking_credentials(request)

    expected_response = NumberMaskingCredentialsResponse(
        api_id=given_api_id, key=given_key
    )

    assert response == expected_response


@pytest.fixture
def get_api_client():
    configuration = Configuration(host="http://localhost:8088")
    configuration.api_key["APIKeyHeader"] = "GivenApiKey"
    configuration.api_key_prefix["APIKeyHeader"] = "App"
    return ApiClient(configuration)


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", 8088
