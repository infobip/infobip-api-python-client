import datetime

import pytest
from infobip_api_client import (
    ApiClient,
    Configuration,
    FormsType,
    FormsStatus,
    FormsComponentType,
    FormsApi,
    FormsResponse,
    FormsResponseContent,
    FormsElement,
    FormsStatusResponse,
)
from pytest_httpserver import HTTPServer

FORMS = "/forms/1/forms"
FORM = "/forms/1/forms/{id}"
FORMS_VIEWS = "/forms/1/forms/{id}/views"
FORMS_SUBMIT = "/forms/1/forms/{id}/data"


def test_should_get_all_forms(httpserver: HTTPServer, get_api_client):
    given_form_id1 = "f23f0f7c-9898-4feb-8f21-5afe2c29db7e"
    given_form_name1 = "Test form"
    given_offset = 0
    given_limit = 25
    given_total = 1
    given_resubmit_enabled = True
    given_form_type = FormsType.OPT_IN
    given_form_status = FormsStatus.ACTIVE

    given_created_at = "2023-08-01T16:10:00+05:30"
    given_created_at_datetime = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )
    given_updated_at = "2023-08-01T16:10:00+05:30"
    given_updated_at_datetime = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )
    given_component = FormsComponentType.TEXT
    given_field_id = "last_name"
    given_person_field = ""
    given_label = ""
    given_is_hidden = True
    given_is_required = True
    given_placeholder = ""

    given_response = {
        "forms": [
            {
                "id": given_form_id1,
                "name": given_form_name1,
                "elements": [
                    {
                        "component": given_component,
                        "fieldId": given_field_id,
                        "personField": given_person_field,
                        "label": given_label,
                        "isRequired": given_is_required,
                        "isHidden": given_is_hidden,
                        "placeholder": given_placeholder,
                    }
                ],
                "createdAt": given_created_at,
                "updatedAt": given_updated_at,
                "resubmitEnabled": given_resubmit_enabled,
                "formType": given_form_type,
                "formStatus": given_form_status,
            }
        ],
        "offset": given_offset,
        "limit": given_limit,
        "total": given_total,
    }

    setup_request(httpserver, FORMS, given_response)

    api_instance = FormsApi(get_api_client)
    api_response = api_instance.get_forms()

    expected_response = FormsResponse(
        forms=[
            FormsResponseContent(
                id=given_form_id1,
                name=given_form_name1,
                elements=[
                    FormsElement(
                        component=given_component,
                        field_id=given_field_id,
                        person_field=given_person_field,
                        label=given_label,
                        is_required=given_is_required,
                        is_hidden=given_is_hidden,
                        placeholder=given_placeholder,
                    )
                ],
                created_at=given_created_at_datetime,
                updated_at=given_updated_at_datetime,
                resubmit_enabled=given_resubmit_enabled,
                form_type=given_form_type,
                form_status=given_form_status,
            )
        ],
        offset=given_offset,
        limit=given_limit,
        total=given_total,
    )

    assert api_response == expected_response


def test_should_get_form_by_id(httpserver: HTTPServer, get_api_client):
    given_form_id = "f23f0f7c-9898-4feb-8f21-5afe2c29db7e"
    given_form_name = "Test form"
    given_resubmit_enabled = True
    given_form_type = FormsType.OPT_IN
    given_form_status = FormsStatus.ACTIVE
    given_created_at = "2023-08-01T16:10:00+05:30"
    given_created_at_datetime = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )
    given_updated_at = "2023-08-01T16:10:00+05:30"
    given_updated_at_datetime = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )
    given_component = FormsComponentType.TEXT
    given_field_id = "last_name"
    given_person_field = ""
    given_label = ""
    given_is_hidden = True
    given_is_required = True
    given_placeholder = ""

    given_response = {
        "id": given_form_id,
        "name": given_form_name,
        "elements": [
            {
                "component": given_component,
                "fieldId": given_field_id,
                "personField": given_person_field,
                "label": given_label,
                "isRequired": given_is_required,
                "isHidden": given_is_hidden,
                "placeholder": given_placeholder,
            }
        ],
        "createdAt": given_created_at,
        "updatedAt": given_updated_at,
        "resubmitEnabled": given_resubmit_enabled,
        "formType": given_form_type,
        "formStatus": given_form_status,
    }

    setup_request(httpserver, FORM.replace("{id}", given_form_id), given_response)

    api_instance = FormsApi(get_api_client)
    api_response = api_instance.get_form(given_form_id)

    expected_response = FormsResponseContent(
        id=given_form_id,
        name=given_form_name,
        elements=[
            FormsElement(
                component=given_component,
                field_id=given_field_id,
                person_field=given_person_field,
                label=given_label,
                is_required=given_is_required,
                is_hidden=given_is_hidden,
                placeholder=given_placeholder,
            )
        ],
        created_at=given_created_at_datetime,
        updated_at=given_updated_at_datetime,
        resubmit_enabled=given_resubmit_enabled,
        form_type=given_form_type,
        form_status=given_form_status,
    )

    assert api_response == expected_response


def test_should_increment_form_view_count(httpserver: HTTPServer, get_api_client):
    form_id = "12345"
    given_status = "OK"

    given_response = {"status": given_status}

    setup_request(
        httpserver, FORMS_VIEWS.replace("{id}", form_id), given_response, "POST"
    )

    api_instance = FormsApi(get_api_client)
    api_response = api_instance.increment_view_count(form_id)

    expected_response = FormsStatusResponse(status=given_status)
    assert api_response == expected_response


def test_should_submit_form_data(httpserver: HTTPServer, get_api_client):
    form_id = "12345"
    given_status = "OK"

    given_response = {"status": given_status}

    given_number = 26
    given_boolean = True

    request_body = {
        "fields": {
            "number": {"value": given_number},
            "boolean": {"value": given_boolean},
        }
    }

    setup_request(
        httpserver,
        FORMS_SUBMIT.replace("{id}", form_id),
        given_response,
        "POST",
        request_body=request_body,
    )

    api_instance = FormsApi(get_api_client)
    api_response = api_instance.submit_form_data(form_id, request_body)

    expected_response = FormsStatusResponse(status=given_status)
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
