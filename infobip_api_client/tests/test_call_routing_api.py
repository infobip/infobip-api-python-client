import pytest
from pytest_httpserver import HTTPServer

from infobip_api_client import (
    ApiClient,
    Configuration,
    CallRoutingRouteResponsePage,
    CallRoutingRouteResponse,
    CallRoutingApi,
    CallRoutingEndpointDestination,
    CallRoutingSipEndpoint,
    CallRoutingRecording,
    CallRoutingRecordingType,
    PageInfo,
    CallRoutingPhoneEndpoint,
    CallRoutingRecordingComposition,
    CallRoutingRouteRequest,
)

routes = "/callrouting/1/routes"
route = "/callrouting/1/routes/{routeId}"


def test_should_get_call_routes(httpserver: HTTPServer, get_api_client):
    given_id = "f8fc8aca-786d-4943-9af2-e7ec01b5e80d"
    given_name = "SIP endpoint route"
    given_destinations_value_username = "41793026834"
    given_destinations_value_sip_trunk_id = "string"
    given_destinations_value_custom_headers_string = "string"
    given_destinations_value_type = "SIP"
    given_destinations_connect_timeout = 30
    given_destinations_recording_recording_type = "AUDIO"
    given_destinations_recording_recording_composition_enabled = True
    given_destinations_recording_custom_data_string = "string"
    given_destinations_recording_file_prefix = "string"
    given_destinations_type = "ENDPOINT"

    given_second_id = "f8fc8aca-786d-4943-9af2-e7ec01b5e80d"
    given_second_name = "Phone endpoint route"
    given_second_destinations_value_phone_number = "41793026834"
    given_second_destinations_value_type = "PHONE"
    given_second_destinations_connect_timeout = 30
    given_second_destinations_recording_recording_type = "AUDIO"
    given_second_destinations_recording_recording_composition_enabled = True
    given_second_destinations_recording_custom_data_string = "string"
    given_second_destinations_recording_file_prefix = "string"
    given_second_destinations_type = "ENDPOINT"

    given_paging_page = 0
    given_paging_size = 20
    given_paging_total_pages = 1
    given_paging_total_results = 2

    given_response = {
        "results": [
            {
                "id": given_id,
                "name": given_name,
                "destinations": [
                    {
                        "value": {
                            "username": given_destinations_value_username,
                            "sipTrunkId": given_destinations_value_sip_trunk_id,
                            "customHeaders": {
                                "string": given_destinations_value_custom_headers_string
                            },
                            "type": given_destinations_value_type,
                        },
                        "connectTimeout": given_destinations_connect_timeout,
                        "recording": {
                            "recordingType": given_destinations_recording_recording_type,
                            "recordingComposition": {
                                "enabled": given_destinations_recording_recording_composition_enabled
                            },
                            "customData": {
                                "string": given_destinations_recording_custom_data_string
                            },
                            "filePrefix": given_destinations_recording_file_prefix,
                        },
                        "type": given_destinations_type,
                    }
                ],
            },
            {
                "id": given_second_id,
                "name": given_second_name,
                "destinations": [
                    {
                        "value": {
                            "phoneNumber": given_second_destinations_value_phone_number,
                            "type": given_second_destinations_value_type,
                        },
                        "connectTimeout": given_second_destinations_connect_timeout,
                        "recording": {
                            "recordingType": given_second_destinations_recording_recording_type,
                            "recordingComposition": {
                                "enabled": given_second_destinations_recording_recording_composition_enabled
                            },
                            "customData": {
                                "string": given_second_destinations_recording_custom_data_string
                            },
                            "filePrefix": given_second_destinations_recording_file_prefix,
                        },
                        "type": given_second_destinations_type,
                    }
                ],
            },
        ],
        "paging": {
            "page": given_paging_page,
            "size": given_paging_size,
            "totalPages": given_paging_total_pages,
            "totalResults": given_paging_total_results,
        },
    }

    api_instance = CallRoutingApi(get_api_client)

    setup_request(httpserver, routes, given_response)

    api_response = api_instance.get_call_routes()

    expected_response: CallRoutingRouteResponsePage = CallRoutingRouteResponsePage(
        results=[
            CallRoutingRouteResponse(
                id=given_id,
                name=given_name,
                destinations=[
                    CallRoutingEndpointDestination(
                        type=given_destinations_type,
                        value=CallRoutingSipEndpoint(
                            type=given_destinations_value_type,
                            username=given_destinations_value_username,
                            sip_trunk_id=given_destinations_value_sip_trunk_id,
                            custom_headers={
                                "string": given_destinations_value_custom_headers_string
                            },
                        ),
                        connect_timeout=given_destinations_connect_timeout,
                        recording=CallRoutingRecording(
                            recording_type=CallRoutingRecordingType.AUDIO,
                            recording_composition=CallRoutingRecordingComposition(
                                enabled=given_destinations_recording_recording_composition_enabled
                            ),
                            custom_data={
                                "string": given_destinations_recording_custom_data_string
                            },
                            file_prefix=given_second_destinations_recording_file_prefix,
                        ),
                    )
                ],
            ),
            CallRoutingRouteResponse(
                id=given_second_id,
                name=given_second_name,
                destinations=[
                    CallRoutingEndpointDestination(
                        type=given_destinations_type,
                        value=CallRoutingPhoneEndpoint(
                            type=given_second_destinations_value_type,
                            phone_number=given_second_destinations_value_phone_number,
                        ),
                        connect_timeout=given_second_destinations_connect_timeout,
                        recording=CallRoutingRecording(
                            recording_type=CallRoutingRecordingType.AUDIO,
                            recording_composition=CallRoutingRecordingComposition(
                                enabled=given_destinations_recording_recording_composition_enabled
                            ),
                            custom_data={
                                "string": given_destinations_value_custom_headers_string
                            },
                            file_prefix=given_destinations_recording_file_prefix,
                        ),
                    )
                ],
            ),
        ],
        paging=PageInfo(
            page=given_paging_page,
            size=given_paging_size,
            total_pages=given_paging_total_pages,
            total_results=given_paging_total_results,
        ),
    )

    assert api_response == expected_response


def test_should_create_a_call_route(httpserver: HTTPServer, get_api_client):
    given_name = "SIP endpoint route"
    given_destinations_value_username = "41793026834"
    given_destinations_value_sip_trunk_id = "string"
    given_destinations_value_custom_headers_string = "string"
    given_destinations_value_type = "SIP"
    given_destinations_connect_timeout = 30
    given_destinations_recording_recording_type = CallRoutingRecordingType.AUDIO
    given_destinations_recording_recording_composition_enabled = True
    given_destinations_recording_custom_data_string = "string"
    given_destinations_recording_file_prefix = "string"
    given_destinations_type = "ENDPOINT"

    given_second_destinations_recording_file_prefix = "string"

    given_request = {
        "name": given_name,
        "destinations": [
            {
                "value": {
                    "username": given_destinations_value_username,
                    "sipTrunkId": given_destinations_value_sip_trunk_id,
                    "customHeaders": {
                        "string": given_destinations_value_custom_headers_string
                    },
                    "type": given_destinations_value_type,
                },
                "connectTimeout": given_destinations_connect_timeout,
                "recording": {
                    "recordingType": given_destinations_recording_recording_type,
                    "recordingComposition": {
                        "enabled": given_destinations_recording_recording_composition_enabled
                    },
                    "customData": {
                        "string": given_destinations_recording_custom_data_string
                    },
                    "filePrefix": given_destinations_recording_file_prefix,
                },
                "type": given_destinations_type,
            }
        ],
    }

    given_id = "f8fc8aca-786d-4943-9af2-e7ec01b5e80d"

    given_response = {
        "id": given_id,
        "name": given_name,
        "destinations": [
            {
                "value": {
                    "username": given_destinations_value_username,
                    "sipTrunkId": given_destinations_value_sip_trunk_id,
                    "customHeaders": {
                        "string": given_destinations_value_custom_headers_string
                    },
                    "type": given_destinations_value_type,
                },
                "connectTimeout": given_destinations_connect_timeout,
                "recording": {
                    "recordingType": given_destinations_recording_recording_type,
                    "recordingComposition": {
                        "enabled": given_destinations_recording_recording_composition_enabled
                    },
                    "customData": {
                        "string": given_destinations_recording_custom_data_string
                    },
                    "filePrefix": given_destinations_recording_file_prefix,
                },
                "type": given_destinations_type,
            }
        ],
    }

    api_instance = CallRoutingApi(get_api_client)

    setup_request(httpserver, routes, given_response, "POST", 201, given_request)

    request: CallRoutingRouteRequest = CallRoutingRouteRequest(
        name=given_name,
        destinations=[
            CallRoutingEndpointDestination(
                type=given_destinations_type,
                value=CallRoutingSipEndpoint(
                    type=given_destinations_value_type,
                    username=given_destinations_value_username,
                    sip_trunk_id=given_destinations_value_sip_trunk_id,
                    custom_headers={
                        "string": given_destinations_value_custom_headers_string
                    },
                ),
                connect_timeout=given_destinations_connect_timeout,
                recording=CallRoutingRecording(
                    recording_type=CallRoutingRecordingType.AUDIO,
                    recording_composition=CallRoutingRecordingComposition(
                        enabled=given_destinations_recording_recording_composition_enabled
                    ),
                    custom_data={
                        "string": given_destinations_recording_custom_data_string
                    },
                    file_prefix=given_second_destinations_recording_file_prefix,
                ),
            )
        ],
    )

    api_response = api_instance.create_call_route(call_routing_route_request=request)

    expected_response: CallRoutingRouteResponse = CallRoutingRouteResponse(
        id=given_id,
        name=given_name,
        destinations=[
            CallRoutingEndpointDestination(
                type=given_destinations_type,
                value=CallRoutingSipEndpoint(
                    type=given_destinations_value_type,
                    username=given_destinations_value_username,
                    sip_trunk_id=given_destinations_value_sip_trunk_id,
                    custom_headers={
                        "string": given_destinations_value_custom_headers_string
                    },
                ),
                connect_timeout=given_destinations_connect_timeout,
                recording=CallRoutingRecording(
                    recording_type=CallRoutingRecordingType.AUDIO,
                    recording_composition=CallRoutingRecordingComposition(
                        enabled=given_destinations_recording_recording_composition_enabled
                    ),
                    custom_data={
                        "string": given_destinations_recording_custom_data_string
                    },
                    file_prefix=given_second_destinations_recording_file_prefix,
                ),
            )
        ],
    )

    assert api_response == expected_response


def test_should_get_a_call_route(httpserver: HTTPServer, get_api_client):
    given_name = "SIP endpoint route"
    given_destinations_value_username = "41793026834"
    given_destinations_value_sip_trunk_id = "string"
    given_destinations_value_custom_headers_string = "string"
    given_destinations_value_type = "SIP"
    given_destinations_connect_timeout = 30
    given_destinations_recording_recording_type = "AUDIO"
    given_destinations_recording_recording_composition_enabled = True
    given_destinations_recording_custom_data_string = "string"
    given_destinations_recording_file_prefix = "string"
    given_destinations_type = "ENDPOINT"

    given_second_destinations_recording_file_prefix = "string"

    given_id = "f8fc8aca-786d-4943-9af2-e7ec01b5e80d"

    given_response = {
        "id": given_id,
        "name": given_name,
        "destinations": [
            {
                "value": {
                    "username": given_destinations_value_username,
                    "sipTrunkId": given_destinations_value_sip_trunk_id,
                    "customHeaders": {
                        "string": given_destinations_value_custom_headers_string
                    },
                    "type": given_destinations_value_type,
                },
                "connectTimeout": given_destinations_connect_timeout,
                "recording": {
                    "recordingType": given_destinations_recording_recording_type,
                    "recordingComposition": {
                        "enabled": given_destinations_recording_recording_composition_enabled
                    },
                    "customData": {
                        "string": given_destinations_recording_custom_data_string
                    },
                    "filePrefix": given_destinations_recording_file_prefix,
                },
                "type": given_destinations_type,
            }
        ],
    }

    endpoint = route.replace("{routeId}", given_id)

    setup_request(httpserver, endpoint, given_response)

    api_instance = CallRoutingApi(get_api_client)
    api_response = api_instance.get_call_route(route_id=given_id)

    expected_response: CallRoutingRouteResponse = CallRoutingRouteResponse(
        id=given_id,
        name=given_name,
        destinations=[
            CallRoutingEndpointDestination(
                type=given_destinations_type,
                value=CallRoutingSipEndpoint(
                    type=given_destinations_value_type,
                    username=given_destinations_value_username,
                    sip_trunk_id=given_destinations_value_sip_trunk_id,
                    custom_headers={
                        "string": given_destinations_value_custom_headers_string
                    },
                ),
                connect_timeout=given_destinations_connect_timeout,
                recording=CallRoutingRecording(
                    recording_type=CallRoutingRecordingType.AUDIO,
                    recording_composition=CallRoutingRecordingComposition(
                        enabled=given_destinations_recording_recording_composition_enabled
                    ),
                    custom_data={
                        "string": given_destinations_recording_custom_data_string
                    },
                    file_prefix=given_second_destinations_recording_file_prefix,
                ),
            )
        ],
    )

    assert api_response == expected_response


def test_should_update_a_call_route(httpserver: HTTPServer, get_api_client):
    given_name = "SIP endpoint route"
    given_destinations_value_username = "41793026834"
    given_destinations_value_sip_trunk_id = "string"
    given_destinations_value_custom_headers_string = "string"
    given_destinations_value_type = "SIP"
    given_destinations_connect_timeout = 30
    given_destinations_recording_recording_type = "AUDIO"
    given_destinations_recording_recording_composition_enabled = True
    given_destinations_recording_custom_data_string = "string"
    given_destinations_recording_file_prefix = "string"
    given_destinations_type = "ENDPOINT"

    given_second_destinations_recording_file_prefix = "string"

    given_request = {
        "name": given_name,
        "destinations": [
            {
                "value": {
                    "username": given_destinations_value_username,
                    "sipTrunkId": given_destinations_value_sip_trunk_id,
                    "customHeaders": {
                        "string": given_destinations_value_custom_headers_string
                    },
                    "type": given_destinations_value_type,
                },
                "connectTimeout": given_destinations_connect_timeout,
                "recording": {
                    "recordingType": given_destinations_recording_recording_type,
                    "recordingComposition": {
                        "enabled": given_destinations_recording_recording_composition_enabled
                    },
                    "customData": {
                        "string": given_destinations_recording_custom_data_string
                    },
                    "filePrefix": given_destinations_recording_file_prefix,
                },
                "type": given_destinations_type,
            }
        ],
    }

    given_id = "f8fc8aca-786d-4943-9af2-e7ec01b5e80d"

    given_response = {
        "id": given_id,
        "name": given_name,
        "destinations": [
            {
                "value": {
                    "username": given_destinations_value_username,
                    "sipTrunkId": given_destinations_value_sip_trunk_id,
                    "customHeaders": {
                        "string": given_destinations_value_custom_headers_string
                    },
                    "type": given_destinations_value_type,
                },
                "connectTimeout": given_destinations_connect_timeout,
                "recording": {
                    "recordingType": given_destinations_recording_recording_type,
                    "recordingComposition": {
                        "enabled": given_destinations_recording_recording_composition_enabled
                    },
                    "customData": {
                        "string": given_destinations_recording_custom_data_string
                    },
                    "filePrefix": given_destinations_recording_file_prefix,
                },
                "type": given_destinations_type,
            }
        ],
    }

    api_instance = CallRoutingApi(get_api_client)

    endpoint = route.replace("{routeId}", given_id)

    setup_request(httpserver, endpoint, given_response, "PUT", 200, given_request)

    request: CallRoutingRouteRequest = CallRoutingRouteRequest(
        name=given_name,
        destinations=[
            CallRoutingEndpointDestination(
                type=given_destinations_type,
                value=CallRoutingSipEndpoint(
                    type=given_destinations_value_type,
                    username=given_destinations_value_username,
                    sip_trunk_id=given_destinations_value_sip_trunk_id,
                    custom_headers={
                        "string": given_destinations_value_custom_headers_string
                    },
                ),
                connect_timeout=given_destinations_connect_timeout,
                recording=CallRoutingRecording(
                    recording_type=CallRoutingRecordingType.AUDIO,
                    recording_composition=CallRoutingRecordingComposition(
                        enabled=given_destinations_recording_recording_composition_enabled
                    ),
                    custom_data={
                        "string": given_destinations_recording_custom_data_string
                    },
                    file_prefix=given_second_destinations_recording_file_prefix,
                ),
            )
        ],
    )

    api_response = api_instance.update_call_route(
        call_routing_route_request=request, route_id=given_id
    )

    expected_response: CallRoutingRouteResponse = CallRoutingRouteResponse(
        id=given_id,
        name=given_name,
        destinations=[
            CallRoutingEndpointDestination(
                type=given_destinations_type,
                value=CallRoutingSipEndpoint(
                    type=given_destinations_value_type,
                    username=given_destinations_value_username,
                    sip_trunk_id=given_destinations_value_sip_trunk_id,
                    custom_headers={
                        "string": given_destinations_value_custom_headers_string
                    },
                ),
                connect_timeout=given_destinations_connect_timeout,
                recording=CallRoutingRecording(
                    recording_type=CallRoutingRecordingType.AUDIO,
                    recording_composition=CallRoutingRecordingComposition(
                        enabled=given_destinations_recording_recording_composition_enabled
                    ),
                    custom_data={
                        "string": given_destinations_recording_custom_data_string
                    },
                    file_prefix=given_second_destinations_recording_file_prefix,
                ),
            )
        ],
    )

    assert api_response == expected_response


def test_should_delete_a_call_route(httpserver: HTTPServer, get_api_client):
    given_name = "SIP endpoint route"
    given_destinations_value_username = "41793026834"
    given_destinations_value_sip_trunk_id = "string"
    given_destinations_value_custom_headers_string = "string"
    given_destinations_value_type = "SIP"
    given_destinations_connect_timeout = 30
    given_destinations_recording_recording_type = "AUDIO"
    given_destinations_recording_recording_composition_enabled = True
    given_destinations_recording_custom_data_string = "string"
    given_destinations_recording_file_prefix = "string"
    given_destinations_type = "ENDPOINT"

    given_second_destinations_recording_file_prefix = "string"

    given_id = "f8fc8aca-786d-4943-9af2-e7ec01b5e80d"

    given_response = {
        "id": given_id,
        "name": given_name,
        "destinations": [
            {
                "value": {
                    "username": given_destinations_value_username,
                    "sipTrunkId": given_destinations_value_sip_trunk_id,
                    "customHeaders": {
                        "string": given_destinations_value_custom_headers_string
                    },
                    "type": given_destinations_value_type,
                },
                "connectTimeout": given_destinations_connect_timeout,
                "recording": {
                    "recordingType": given_destinations_recording_recording_type,
                    "recordingComposition": {
                        "enabled": given_destinations_recording_recording_composition_enabled
                    },
                    "customData": {
                        "string": given_destinations_recording_custom_data_string
                    },
                    "filePrefix": given_destinations_recording_file_prefix,
                },
                "type": given_destinations_type,
            }
        ],
    }

    endpoint = route.replace("{routeId}", given_id)

    setup_request(httpserver, endpoint, given_response, http_verb="DELETE")

    api_instance = CallRoutingApi(get_api_client)
    api_response = api_instance.delete_call_route(route_id=given_id)

    expected_response: CallRoutingRouteResponse = CallRoutingRouteResponse(
        id=given_id,
        name=given_name,
        destinations=[
            CallRoutingEndpointDestination(
                type=given_destinations_type,
                value=CallRoutingSipEndpoint(
                    type=given_destinations_value_type,
                    username=given_destinations_value_username,
                    sip_trunk_id=given_destinations_value_sip_trunk_id,
                    custom_headers={
                        "string": given_destinations_value_custom_headers_string
                    },
                ),
                connect_timeout=given_destinations_connect_timeout,
                recording=CallRoutingRecording(
                    recording_type=CallRoutingRecordingType.AUDIO,
                    recording_composition=CallRoutingRecordingComposition(
                        enabled=given_destinations_recording_recording_composition_enabled
                    ),
                    custom_data={
                        "string": given_destinations_recording_custom_data_string
                    },
                    file_prefix=given_second_destinations_recording_file_prefix,
                ),
            )
        ],
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
