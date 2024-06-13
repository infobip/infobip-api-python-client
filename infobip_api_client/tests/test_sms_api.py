import datetime

import pytest
from dateutil.tz import tzoffset
from pytest_httpserver import HTTPServer

from infobip_api_client import (
    ApiClient,
    Configuration,
    SmsAdvancedTextualRequest,
    SmsTextualMessage,
    SmsDestination,
    SmsApi,
    SmsResponse,
    SmsResponseDetails,
    MessageStatus,
    SmsBulkResponse,
    SmsBulkStatusResponse,
    SmsBulkStatus,
    SmsBulkRequest,
    SmsUpdateStatusRequest,
    SmsDeliveryResult,
    SmsReport,
    MessageError,
    MessagePrice,
    SmsLogsResponse,
    SmsLog,
    SmsInboundMessageResult,
    SmsInboundMessage,
    SmsDeliveryTimeWindow,
    SmsDeliveryDay,
    SmsDeliveryTimeFrom,
    SmsDeliveryTimeTo,
    SmsLanguage,
    SmsUrlOptions,
    SmsSendingSpeedLimit,
    SmsSpeedLimitTimeUnit,
    SmsTracking,
    SmsRegionalOptions,
    SmsIndiaDltOptions,
    SmsTurkeyIysOptions,
    SmsAdvancedBinaryRequest,
    SmsBinaryMessage,
    SmsBinaryContent,
    SmsPreviewRequest,
    SmsPreviewResponse,
    SmsPreview,
    SmsLanguageConfiguration,
)

sms_advanced_textual_endpoint = "/sms/2/text/advanced"
sms_advanced_binary_endpoint = "/sms/2/binary/advanced"
sms_preview_endpoint = "/sms/1/preview"
sms_bulks_endpoint = "/sms/1/bulks"
sms_bulks_status_endpoint = "/sms/1/bulks/status"
sms_outbound_reports_endpoint = "/sms/1/reports"
sms_outbound_logs_endpoint = "/sms/1/logs"
sms_inbound_messages_endpoint = "/sms/1/inbox/reports"


def test_send_basic_sms_with_application_and_entity(
    httpserver: HTTPServer, sms_api_client
):
    given_bulk_id = "2034072219640523072"
    given_to = "41793026727"
    given_message_id = "2250be2d4219-3af1-78856-aabe-1362af1edfd2"
    given_from = "InfoSMS"
    given_text = "This is a sample message"
    given_group_id = 1
    given_group_name = "PENDING"
    given_status_id = 26
    given_status_name = "MESSAGE_ACCEPTED"
    given_status_description = "Message sent to next instance"
    given_application_id = "given_application_id"
    given_entity_id = "given_entity_id"

    given_request = {
        "messages": [
            {
                "destinations": [{"to": given_to}],
                "flash": False,
                "text": given_text,
                "from": given_from,
                "applicationId": given_application_id,
                "entityId": given_entity_id,
            }
        ],
        "includeSmsCountInResponse": False,
    }

    expected_response = {
        "bulkId": given_bulk_id,
        "messages": [
            {
                "to": given_to,
                "status": {
                    "groupId": given_group_id,
                    "groupName": given_group_name,
                    "id": given_status_id,
                    "name": given_status_name,
                    "description": given_status_description,
                },
                "messageId": given_message_id,
            }
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=sms_advanced_textual_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    sms_advanced_textual_request = SmsAdvancedTextualRequest(
        messages=[
            SmsTextualMessage(
                destinations=[
                    SmsDestination(
                        to=given_to,
                    ),
                ],
                var_from=given_from,
                text=given_text,
                application_id=given_application_id,
                entity_id=given_entity_id,
            )
        ]
    )

    actual_response: SmsResponse = sms_api_client.send_sms_message(
        sms_advanced_textual_request=sms_advanced_textual_request
    )

    expected_sms_response = SmsResponse(
        bulk_id=given_bulk_id,
        messages=[
            SmsResponseDetails(
                message_id=given_message_id,
                status=MessageStatus(
                    groupId=given_group_id,
                    groupName=given_group_name,
                    id=given_status_id,
                    name=given_status_name,
                    description=given_status_description,
                ),
                to=given_to,
            )
        ],
    )

    assert actual_response == expected_sms_response


def test_send_fully_featured_sms(httpserver: HTTPServer, sms_api_client):
    bulk_id = "2034072219640523072"
    first_to = "41793026727"
    second_to = "41793026834"
    first_message_id = "MESSAGE-ID-123-xyz"
    second_message_id = "2250be2d4219-3af1-78856-aabe-1362af1edfd2"
    given_from = "InfoSMS"
    application_id = "application_id"
    entity_id = "entity_id"

    flash = False
    callback_data = "my-callback-data"
    first_delivery_day = "MONDAY"
    second_delivery_day = "THURSDAY"
    delivery_from_hours = 11
    delivery_from_minutes = 10
    delivery_to_hours = 12
    delivery_to_minutes = 15
    intermediate_report = True
    language_code = "AUTODETECT"
    notify_content_type = "application/json"
    notify_url = "https://example.com/mms-webhook"
    validity_period = 10
    text = "Laku noć"
    transliteration = "CENTRAL_EUROPEAN"

    india_dlt_content_template_id = "content-template-id"
    india_dlt_principal_entity_id = "principal-entity-id"
    turkey_iys_brand_code = 123123
    turkey_iys_recipient_type = "TACIR"
    send_at = "2023-08-01T16:10:00+05:30"

    sending_speed_limit_amount = 10
    sending_speed_limit_time_unit = "HOUR"
    url_options_shorten_url = True
    url_options_track_clicks = False
    url_options_tracking_url = "https://ib.com"
    url_options_remove_protocol = True
    url_options_custom_domain = "example.com"
    tracking = "SMS"
    tracking_type = "MY_CAMPAIGN"
    tracking_base_url = "https://example.com"
    tracking_process_key = "123"

    expected_request = {
        "bulkId": bulk_id,
        "messages": [
            {
                "callbackData": callback_data,
                "deliveryTimeWindow": {
                    "days": [first_delivery_day, second_delivery_day],
                    "from": {
                        "hour": delivery_from_hours,
                        "minute": delivery_from_minutes,
                    },
                    "to": {"hour": delivery_to_hours, "minute": delivery_to_minutes},
                },
                "destinations": [
                    {"to": first_to, "messageId": first_message_id},
                    {"to": second_to},
                ],
                "flash": flash,
                "from": given_from,
                "intermediateReport": intermediate_report,
                "language": {"languageCode": language_code},
                "notifyContentType": notify_content_type,
                "notifyUrl": notify_url,
                "regional": {
                    "indiaDlt": {
                        "contentTemplateId": india_dlt_content_template_id,
                        "principalEntityId": india_dlt_principal_entity_id,
                    },
                    "turkeyIys": {
                        "brandCode": turkey_iys_brand_code,
                        "recipientType": turkey_iys_recipient_type,
                    },
                },
                "sendAt": send_at,
                "text": text,
                "transliteration": transliteration,
                "validityPeriod": validity_period,
                "applicationId": application_id,
                "entityId": entity_id,
            }
        ],
        "sendingSpeedLimit": {
            "amount": sending_speed_limit_amount,
            "timeUnit": sending_speed_limit_time_unit,
        },
        "urlOptions": {
            "shortenUrl": url_options_shorten_url,
            "trackClicks": url_options_track_clicks,
            "trackingUrl": url_options_tracking_url,
            "removeProtocol": url_options_remove_protocol,
            "customDomain": url_options_custom_domain,
        },
        "tracking": {
            "baseUrl": tracking_base_url,
            "processKey": tracking_process_key,
            "track": tracking,
            "type": tracking_type,
        },
        "includeSmsCountInResponse": False,
    }

    group_id = 1
    group_name = "PENDING"
    status_id = 26
    status_name = "MESSAGE_ACCEPTED"
    status_description = "Message sent to next instance"

    expected_response = {
        "bulkId": bulk_id,
        "messages": [
            {
                "to": first_to,
                "status": {
                    "groupId": group_id,
                    "groupName": group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "messageId": first_message_id,
            },
            {
                "to": second_to,
                "status": {
                    "groupId": group_id,
                    "groupName": group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "messageId": second_message_id,
            },
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=sms_advanced_textual_endpoint,
        expected_request=expected_request,
        expected_response=expected_response,
    )

    sms_advanced_textual_request = SmsAdvancedTextualRequest(
        bulk_id=bulk_id,
        messages=[
            SmsTextualMessage(
                callback_data=callback_data,
                delivery_time_window=SmsDeliveryTimeWindow(
                    days=[SmsDeliveryDay.MONDAY, SmsDeliveryDay.THURSDAY],
                    var_from=SmsDeliveryTimeFrom(
                        hour=delivery_from_hours, minute=delivery_from_minutes
                    ),
                    to=SmsDeliveryTimeTo(
                        hour=delivery_to_hours, minute=delivery_to_minutes
                    ),
                ),
                destinations=[
                    SmsDestination(
                        message_id=first_message_id,
                        to=first_to,
                    ),
                    SmsDestination(to=second_to),
                ],
                var_from=given_from,
                flash=flash,
                intermediate_report=intermediate_report,
                language=SmsLanguage(language_code=language_code),
                notify_content_type=notify_content_type,
                notify_url=notify_url,
                regional=SmsRegionalOptions(
                    india_dlt=SmsIndiaDltOptions(
                        content_template_id=india_dlt_content_template_id,
                        principal_entity_id=india_dlt_principal_entity_id,
                    ),
                    turkey_iys=SmsTurkeyIysOptions(
                        brand_code=turkey_iys_brand_code,
                        recipient_type=turkey_iys_recipient_type,
                    ),
                ),
                send_at=datetime.datetime(
                    2023,
                    8,
                    1,
                    16,
                    10,
                    0,
                    tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
                ),
                text=text,
                transliteration=transliteration,
                validity_period=validity_period,
                application_id=application_id,
                entity_id=entity_id,
            )
        ],
        sending_speed_limit=SmsSendingSpeedLimit(
            amount=sending_speed_limit_amount, time_unit=SmsSpeedLimitTimeUnit.HOUR
        ),
        url_options=SmsUrlOptions(
            shorten_url=url_options_shorten_url,
            track_clicks=url_options_track_clicks,
            tracking_url=url_options_tracking_url,
            remove_protocol=url_options_remove_protocol,
            custom_domain=url_options_custom_domain,
        ),
        tracking=SmsTracking(
            base_url=tracking_base_url,
            process_key=tracking_process_key,
            track=tracking,
            type=tracking_type,
        ),
    )

    actual_response = sms_api_client.send_sms_message(
        sms_advanced_textual_request=sms_advanced_textual_request
    )

    expected_sms_result = SmsResponse(
        bulk_id=bulk_id,
        messages=[
            SmsResponseDetails(
                message_id=first_message_id,
                status=MessageStatus(
                    group_id=group_id,
                    group_name=group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                to=first_to,
            ),
            SmsResponseDetails(
                message_id=second_message_id,
                status=MessageStatus(
                    group_id=group_id,
                    group_name=group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                to=second_to,
            ),
        ],
    )

    assert actual_response == expected_sms_result


def test_send_fully_featured_binary_sms(httpserver: HTTPServer, sms_api_client):
    bulk_id = "2034072219640523072"
    first_to = "41793026727"
    second_to = "41793026834"
    first_message_id = "MESSAGE-ID-123-xyz"
    second_message_id = "2250be2d4219-3af1-78856-aabe-1362af1edfd2"
    given_from = "InfoSMS"
    application_id = "application_id"
    entity_id = "entity_id"

    flash = False
    callback_data = "my-callback-data"
    first_delivery_day = "MONDAY"
    second_delivery_day = "THURSDAY"
    delivery_from_hours = 11
    delivery_from_minutes = 10
    delivery_to_hours = 12
    delivery_to_minutes = 15
    intermediate_report = True
    notify_content_type = "application/json"
    notify_url = "https://example.com/mms-webhook"
    validity_period = 10
    hex_message = "54 65 73 74 20 6d 65 73 73 61 67 65 2e"
    data_coding = 0
    esm_class = 0

    india_dlt_content_template_id = "content-template-id"
    india_dlt_principal_entity_id = "principal-entity-id"
    turkey_iys_brand_code = 123123
    turkey_iys_recipient_type = "TACIR"
    send_at = "2023-08-01T16:10:00+05:30"

    sending_speed_limit_amount = 10
    sending_speed_limit_time_unit = "HOUR"

    expected_request = {
        "bulkId": bulk_id,
        "messages": [
            {
                "callbackData": callback_data,
                "deliveryTimeWindow": {
                    "days": [first_delivery_day, second_delivery_day],
                    "from": {
                        "hour": delivery_from_hours,
                        "minute": delivery_from_minutes,
                    },
                    "to": {"hour": delivery_to_hours, "minute": delivery_to_minutes},
                },
                "destinations": [
                    {"to": first_to, "messageId": first_message_id},
                    {"to": second_to},
                ],
                "flash": flash,
                "from": given_from,
                "intermediateReport": intermediate_report,
                "notifyContentType": notify_content_type,
                "notifyUrl": notify_url,
                "regional": {
                    "indiaDlt": {
                        "contentTemplateId": india_dlt_content_template_id,
                        "principalEntityId": india_dlt_principal_entity_id,
                    },
                    "turkeyIys": {
                        "brandCode": turkey_iys_brand_code,
                        "recipientType": turkey_iys_recipient_type,
                    },
                },
                "sendAt": send_at,
                "binary": {
                    "hex": hex_message,
                    "dataCoding": data_coding,
                    "esmClass": esm_class,
                },
                "validityPeriod": validity_period,
                "applicationId": application_id,
                "entityId": entity_id,
            }
        ],
        "sendingSpeedLimit": {
            "amount": sending_speed_limit_amount,
            "timeUnit": sending_speed_limit_time_unit,
        },
    }

    group_id = 1
    group_name = "PENDING"
    status_id = 26
    status_name = "MESSAGE_ACCEPTED"
    status_description = "Message sent to next instance"

    expected_sms_response = {
        "bulkId": bulk_id,
        "messages": [
            {
                "to": first_to,
                "status": {
                    "groupId": group_id,
                    "groupName": group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "messageId": first_message_id,
            },
            {
                "to": second_to,
                "status": {
                    "groupId": group_id,
                    "groupName": group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "messageId": second_message_id,
            },
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=sms_advanced_binary_endpoint,
        expected_request=expected_request,
        expected_response=expected_sms_response,
    )

    sms_advanced_binary_request = SmsAdvancedBinaryRequest(
        bulk_id=bulk_id,
        messages=[
            SmsBinaryMessage(
                callback_data=callback_data,
                delivery_time_window=SmsDeliveryTimeWindow(
                    days=[SmsDeliveryDay.MONDAY, SmsDeliveryDay.THURSDAY],
                    var_from=SmsDeliveryTimeFrom(
                        hour=delivery_from_hours, minute=delivery_from_minutes
                    ),
                    to=SmsDeliveryTimeTo(
                        hour=delivery_to_hours, minute=delivery_to_minutes
                    ),
                ),
                destinations=[
                    SmsDestination(
                        message_id=first_message_id,
                        to=first_to,
                    ),
                    SmsDestination(to=second_to),
                ],
                var_from=given_from,
                flash=flash,
                intermediate_report=intermediate_report,
                notify_content_type=notify_content_type,
                notify_url=notify_url,
                regional=SmsRegionalOptions(
                    india_dlt=SmsIndiaDltOptions(
                        content_template_id=india_dlt_content_template_id,
                        principal_entity_id=india_dlt_principal_entity_id,
                    ),
                    turkey_iys=SmsTurkeyIysOptions(
                        brand_code=turkey_iys_brand_code,
                        recipient_type=turkey_iys_recipient_type,
                    ),
                ),
                send_at=datetime.datetime(
                    2023,
                    8,
                    1,
                    16,
                    10,
                    0,
                    tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
                ),
                binary=SmsBinaryContent(
                    hex=hex_message, data_coding=data_coding, esm_class=esm_class
                ),
                validity_period=validity_period,
                application_id=application_id,
                entity_id=entity_id,
            )
        ],
        sending_speed_limit=SmsSendingSpeedLimit(
            amount=sending_speed_limit_amount, time_unit=SmsSpeedLimitTimeUnit.HOUR
        ),
    )

    actual_response = sms_api_client.send_binary_sms_message(
        sms_advanced_binary_request=sms_advanced_binary_request
    )

    expected_sms_response = SmsResponse(
        bulk_id=bulk_id,
        messages=[
            SmsResponseDetails(
                message_id=first_message_id,
                status=MessageStatus(
                    group_id=group_id,
                    group_name=group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                to=first_to,
            ),
            SmsResponseDetails(
                message_id=second_message_id,
                status=MessageStatus(
                    group_id=group_id,
                    group_name=group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                to=second_to,
            ),
        ],
    )

    assert actual_response == expected_sms_response


def test_preview_sms(httpserver: HTTPServer, sms_api_client):
    expected_request = {
        "text": "Let's see how many characters remain unused in this message.",
        "languageCode": "AUTODETECT",
        "transliteration": "CENTRAL_EUROPEAN",
    }

    expected_response = {
        "originalText": "Let's see how many characters remain unused in this message.",
        "previews": [
            {
                "textPreview": "Let's see how many characters remain unused in this message.",
                "messageCount": 1,
                "charactersRemaining": 96,
                "configuration": {
                    "languageCode": "AUTODETECT",
                    "transliteration": "CENTRAL_EUROPEAN",
                },
            }
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=sms_preview_endpoint,
        expected_request=expected_request,
        expected_response=expected_response,
    )

    sms_preview_request = SmsPreviewRequest(
        text="Let's see how many characters remain unused in this message.",
        language_code="AUTODETECT",
        transliteration="CENTRAL_EUROPEAN",
    )

    actual_response = sms_api_client.preview_sms_message(
        sms_preview_request=sms_preview_request
    )

    expected_preview_response = SmsPreviewResponse(
        original_text="Let's see how many characters remain unused in this message.",
        previews=[
            SmsPreview(
                text_preview="Let's see how many characters remain unused in this message.",
                message_count=1,
                characters_remaining=96,
                configuration=SmsLanguageConfiguration(
                    language_code="AUTODETECT", transliteration="CENTRAL_EUROPEAN"
                ),
            )
        ],
    )

    assert actual_response == expected_preview_response


def test_get_scheduled_sms_messages(httpserver: HTTPServer, sms_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_send_at_message = "2023-03-08T17:42:05.390+0100"

    expected_response = {"bulkId": given_bulk_id, "sendAt": given_send_at_message}

    query_string = to_query_string_without_escaping({"bulkId": given_bulk_id})

    setup_get_request(
        httpserver=httpserver,
        endpoint=sms_bulks_endpoint,
        expected_response=expected_response,
        query_string=query_string,
    )

    actual_response: SmsBulkResponse = sms_api_client.get_scheduled_sms_messages(
        bulk_id=given_bulk_id
    )

    expected_sms_bulk_response = SmsBulkResponse(
        bulk_id=given_bulk_id,
        send_at=datetime.datetime(
            2023, 3, 8, 17, 42, 5, 390000, tzinfo=tzoffset(None, 3600)
        ),
    )

    assert actual_response == expected_sms_bulk_response


def test_reschedule_sms_messages(httpserver: HTTPServer, sms_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_send_at_message_request = "2023-03-08T17:42:05.390000+01:00"
    given_send_at_message_response = "2023-03-08T17:42:05.390+0100"
    given_send_at_message_datetime = datetime.datetime(
        2023, 3, 8, 17, 42, 5, 390000, tzinfo=tzoffset(None, 3600)
    )

    expected_request = {"sendAt": given_send_at_message_request}

    expected_response = {
        "bulkId": given_bulk_id,
        "sendAt": given_send_at_message_response,
    }

    query_string = to_query_string_without_escaping({"bulkId": given_bulk_id})

    setup_put_request_ok(
        httpserver=httpserver,
        endpoint=sms_bulks_endpoint,
        expected_request=expected_request,
        expected_response=expected_response,
        query_string=query_string,
    )

    sms_bulk_request = SmsBulkRequest(send_at=given_send_at_message_datetime)

    actual_response: SmsBulkResponse = sms_api_client.reschedule_sms_messages(
        bulk_id=given_bulk_id, sms_bulk_request=sms_bulk_request
    )

    expected_sms_bulk_response = SmsBulkResponse(
        bulk_id=given_bulk_id, send_at=given_send_at_message_datetime
    )

    assert actual_response == expected_sms_bulk_response


def test_get_scheduled_sms_messages_status(httpserver: HTTPServer, sms_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_status = "PAUSED"

    expected_response = {"bulkId": given_bulk_id, "status": given_status}

    query_string = to_query_string_without_escaping({"bulkId": given_bulk_id})

    setup_get_request(
        httpserver=httpserver,
        endpoint=sms_bulks_status_endpoint,
        expected_response=expected_response,
        query_string=query_string,
    )

    actual_response: SmsBulkStatusResponse = (
        sms_api_client.get_scheduled_sms_messages_status(bulk_id=given_bulk_id)
    )

    expected_sms_bulk_status_response = SmsBulkStatusResponse(
        bulk_id=given_bulk_id, status=SmsBulkStatus.PAUSED
    )

    assert actual_response == expected_sms_bulk_status_response


def test_update_scheduled_sms_messages_status(httpserver: HTTPServer, sms_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_status = "CANCELED"

    expected_request = {"status": given_status}

    expected_response = {"bulkId": given_bulk_id, "status": given_status}

    query_string = to_query_string_without_escaping({"bulkId": given_bulk_id})

    setup_put_request_ok(
        httpserver=httpserver,
        endpoint=sms_bulks_status_endpoint,
        expected_request=expected_request,
        expected_response=expected_response,
        query_string=query_string,
    )

    sms_update_status_request = SmsUpdateStatusRequest(status=SmsBulkStatus.CANCELED)

    actual_response: SmsBulkStatusResponse = (
        sms_api_client.update_scheduled_sms_messages_status(
            bulk_id=given_bulk_id, sms_update_status_request=sms_update_status_request
        )
    )

    expected_sms_bulk_response = SmsBulkStatusResponse(
        bulk_id=given_bulk_id, status=SmsBulkStatus.CANCELED
    )

    assert actual_response == expected_sms_bulk_response


def test_outbound_delivery_reports_webhook_model():
    delivery_result_payload = """
    {
        "results": [
        {
            "bulkId": "BULK-ID-123-xyz",
            "messageId": "MESSAGE-ID-123-xyz",
            "to": "41793026727",
            "from": "InfoSMS",
            "sentAt": "2019-11-09T16:00:00.000+0000",
            "doneAt": "2019-11-09T16:01:00.000+0000",
            "smsCount": 1,
            "mccMnc": "code",
            "callbackData": "my-callback-data",
            "price": {
                "pricePerMessage": 0.01,
                "currency": "EUR"
            },
            "status": {
                "groupId": 3,
                "groupName": "DELIVERED",
                "id": 5,
                "name": "DELIVERED_TO_HANDSET",
                "description": "Message delivered to handset"
            },
            "error": {
                "groupId": 0,
                "groupName": "Ok",
                "id": 0,
                "name": "NO_ERROR",
                "description": "No Error",
                "permanent": false
            },
            "entityId": "entity_id",
            "applicationId": "application_id"
        }
        ]
    }
    """

    expected_deserialized_report = SmsDeliveryResult(
        results=[
            SmsReport(
                bulk_id="BULK-ID-123-xyz",
                message_id="MESSAGE-ID-123-xyz",
                to="41793026727",
                var_from="InfoSMS",
                sent_at="2019-11-09T16:00:00.000+0000",
                done_at="2019-11-09T16:01:00.000+0000",
                sms_count=1,
                mcc_mnc="code",
                callback_data="my-callback-data",
                price=MessagePrice(price_per_message=0.01, currency="EUR"),
                status=MessageStatus(
                    group_id=3,
                    group_name="DELIVERED",
                    id=5,
                    name="DELIVERED_TO_HANDSET",
                    description="Message delivered to handset",
                ),
                error=MessageError(
                    group_id=0,
                    group_name="Ok",
                    id=0,
                    name="NO_ERROR",
                    description="No Error",
                    permanent=False,
                ),
                entity_id="entity_id",
                application_id="application_id",
            )
        ]
    )

    actual_deserialized_report = SmsDeliveryResult.from_json(delivery_result_payload)

    assert actual_deserialized_report == expected_deserialized_report


def test_inbound_reports_webhook_model():
    inbound_report_payload = """
    {
        "results": [
        {
            "messageId": "817790313235066447",
            "from": "385916242493",
            "to": "385921004026",
            "text": "QUIZ Correct answer is Paris",
            "cleanText": "Correct answer is Paris",
            "keyword": "QUIZ",
            "receivedAt": "2016-10-06T09:28:39.220+0000",
            "smsCount": 1,
            "price": {
                "pricePerMessage": 0.00,
                "currency": "EUR"
            },
            "callbackData": "callbackData"
        }
        ],
        "messageCount": 1,
        "pendingMessageCount": 0
    }
    """

    expected_inbound_report = SmsInboundMessageResult(
        results=[
            SmsInboundMessage(
                message_id="817790313235066447",
                to="385921004026",
                var_from="385916242493",
                text="QUIZ Correct answer is Paris",
                clean_text="Correct answer is Paris",
                keyword="QUIZ",
                received_at="2016-10-06T09:28:39.220+0000",
                sms_count=1,
                callback_data="callbackData",
                price=MessagePrice(price_per_message=0.0, currency="EUR"),
            )
        ],
        message_count=1,
        pending_message_count=0,
    )

    actual_inbound_report = SmsInboundMessageResult.from_json(inbound_report_payload)

    assert actual_inbound_report == expected_inbound_report


def test_outbound_delivery_reports(httpserver: HTTPServer, sms_api_client):
    bulk_id = "BULK-ID-123-xyz"
    message_id = "MESSAGE-ID-123-xyz"
    message_id2 = "12db39c3-7822-4e72-a3ec-c87442c0ffc5"
    to = "41793026727"
    sent_at = "2019-11-09T16:00:00.000+0000"
    done_at = "2019-11-09T16:00:00.000+0000"
    sms_count = 1
    price_per_message = 0.01
    currency = "EUR"
    application_id = "test_application_id"
    entity_id = "test_entity_id"

    status_group_id = 3
    status_group_name = "DELIVERED"
    status_id = 5
    status_name = "DELIVERED_TO_HANDSET"
    status_description = "Message delivered to handset"

    error_group_id = 0
    error_group_name = "Ok"
    error_id = 0
    error_name = "NO_ERROR"
    error_description = "No Error"
    error_permanent = False

    expected_response = {
        "results": [
            {
                "bulkId": bulk_id,
                "messageId": message_id,
                "to": to,
                "sentAt": sent_at,
                "doneAt": done_at,
                "smsCount": sms_count,
                "price": {"pricePerMessage": price_per_message, "currency": currency},
                "status": {
                    "groupId": status_group_id,
                    "groupName": status_group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "error": {
                    "groupId": error_group_id,
                    "groupName": error_group_name,
                    "id": error_id,
                    "name": error_name,
                    "description": error_description,
                    "permanent": error_permanent,
                },
                "applicationId": application_id,
                "entityId": entity_id,
            },
            {
                "bulkId": bulk_id,
                "messageId": message_id2,
                "to": to,
                "sentAt": sent_at,
                "doneAt": done_at,
                "smsCount": sms_count,
                "price": {"pricePerMessage": price_per_message, "currency": currency},
                "status": {
                    "groupId": status_group_id,
                    "groupName": status_group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "error": {
                    "groupId": error_group_id,
                    "groupName": error_group_name,
                    "id": error_id,
                    "name": error_name,
                    "description": error_description,
                    "permanent": error_permanent,
                },
                "applicationId": application_id,
                "entityId": entity_id,
            },
        ]
    }

    query_string = to_query_string_without_escaping({"bulkId": bulk_id})

    setup_get_request(
        httpserver=httpserver,
        endpoint=sms_outbound_reports_endpoint,
        expected_response=expected_response,
        query_string=query_string,
    )

    actual_response: SmsDeliveryResult = (
        sms_api_client.get_outbound_sms_message_delivery_reports(bulk_id=bulk_id)
    )

    expected_report_response = SmsDeliveryResult(
        results=[
            SmsReport(
                bulk_id=bulk_id,
                message_id=message_id,
                to=to,
                sent_at=sent_at,
                done_at=done_at,
                sms_count=sms_count,
                price=MessagePrice(
                    price_per_message=price_per_message, currency=currency
                ),
                status=MessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                error=MessageError(
                    group_id=error_group_id,
                    group_name=error_group_name,
                    id=error_id,
                    name=error_name,
                    description=error_description,
                    permanent=error_permanent,
                ),
                application_id=application_id,
                entity_id=entity_id,
            ),
            SmsReport(
                bulk_id=bulk_id,
                message_id=message_id2,
                to=to,
                sent_at=sent_at,
                done_at=done_at,
                sms_count=sms_count,
                price=MessagePrice(
                    price_per_message=price_per_message, currency=currency
                ),
                status=MessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                error=MessageError(
                    group_id=error_group_id,
                    group_name=error_group_name,
                    id=error_id,
                    name=error_name,
                    description=error_description,
                    permanent=error_permanent,
                ),
                application_id=application_id,
                entity_id=entity_id,
            ),
        ]
    )

    assert actual_response == expected_report_response


def test_get_inbound_sms_messages(httpserver: HTTPServer, sms_api_client):
    expected_response = {
        "results": [
            {
                "messageId": "817790313235066447",
                "from": "385916242493",
                "to": "385921004026",
                "text": "QUIZ Correct answer is Paris",
                "cleanText": "Correct answer is Paris",
                "keyword": "QUIZ",
                "receivedAt": "2016-10-06T09:28:39.220+0000",
                "smsCount": 1,
                "price": {"pricePerMessage": 0.0, "currency": "EUR"},
                "callbackData": "callbackData",
            }
        ],
        "messageCount": 1,
        "pendingMessageCount": 0,
    }

    query_string = to_query_string_without_escaping({"limit": 2})

    setup_get_request(
        httpserver=httpserver,
        endpoint=sms_inbound_messages_endpoint,
        expected_response=expected_response,
        query_string=query_string,
    )

    expected_inbound_report = SmsInboundMessageResult(
        results=[
            SmsInboundMessage(
                message_id="817790313235066447",
                to="385921004026",
                var_from="385916242493",
                text="QUIZ Correct answer is Paris",
                clean_text="Correct answer is Paris",
                keyword="QUIZ",
                received_at="2016-10-06T09:28:39.220+0000",
                sms_count=1,
                callback_data="callbackData",
                price=MessagePrice(price_per_message=0.0, currency="EUR"),
            )
        ],
        message_count=1,
        pending_message_count=0,
    )

    actual_inbound_report = sms_api_client.get_inbound_sms_messages(limit=2)

    assert actual_inbound_report == expected_inbound_report


def test_outbound_logs(httpserver: HTTPServer, sms_api_client):
    bulk_id = "BULK-ID-123-xyz"
    message_id = "MESSAGE-ID-123-xyz"
    message_id2 = "12db39c3-7822-4e72-a3ec-c87442c0ffc5"
    to = "41793026727"
    sent_at = "2023-03-09T16:00:00.000+0000"
    done_at = "2023-03-09T16:01:00.000+0000"
    sms_count = 1
    mcc_mnc = "22801"
    price_per_message = 0.01
    currency = "EUR"
    status_group_id = 3
    status_group_name = "DELIVERED"
    status_id = 5
    status_name = "DELIVERED_TO_HANDSET"
    status_description = "Message delivered to handset"
    error_group_id = 0
    error_group_name = "Ok"
    error_id = 0
    error_name = "NO_ERROR"
    error_description = "No Error"
    error_permanent = False

    expected_response = {
        "results": [
            {
                "bulkId": bulk_id,
                "messageId": message_id,
                "to": to,
                "sentAt": sent_at,
                "doneAt": done_at,
                "smsCount": sms_count,
                "mccMnc": mcc_mnc,
                "price": {"pricePerMessage": price_per_message, "currency": currency},
                "status": {
                    "groupId": status_group_id,
                    "groupName": status_group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "error": {
                    "groupId": error_group_id,
                    "groupName": error_group_name,
                    "id": error_id,
                    "name": error_name,
                    "description": error_description,
                    "permanent": error_permanent,
                },
            },
            {
                "bulkId": bulk_id,
                "messageId": message_id2,
                "to": to,
                "sentAt": sent_at,
                "doneAt": done_at,
                "smsCount": sms_count,
                "mccMnc": mcc_mnc,
                "price": {"pricePerMessage": price_per_message, "currency": currency},
                "status": {
                    "groupId": status_group_id,
                    "groupName": status_group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "error": {
                    "groupId": error_group_id,
                    "groupName": error_group_name,
                    "id": error_id,
                    "name": error_name,
                    "description": error_description,
                    "permanent": error_permanent,
                },
            },
        ]
    }

    query_string = to_query_string_without_escaping(
        {"bulkId": bulk_id, "sentSince": "2023-03-09T14%3A00%3A00%2B00%3A00"}
    )

    setup_get_request(
        httpserver=httpserver,
        endpoint=sms_outbound_logs_endpoint,
        expected_response=expected_response,
    )

    actual_response: SmsLogsResponse = sms_api_client.get_outbound_sms_message_logs(
        bulk_id=[bulk_id],
        sent_since=datetime.datetime(
            2023, 3, 9, 14, 0, 0, 0, tzinfo=datetime.timezone.utc
        ),
    )

    expected_logs_response = SmsLogsResponse(
        results=[
            SmsLog(
                bulk_id=bulk_id,
                message_id=message_id,
                to=to,
                sent_at=sent_at,
                done_at=done_at,
                sms_count=sms_count,
                mcc_mnc=mcc_mnc,
                price=MessagePrice(
                    price_per_message=price_per_message, currency=currency
                ),
                status=MessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                error=MessageError(
                    group_id=error_group_id,
                    group_name=error_group_name,
                    id=error_id,
                    name=error_name,
                    description=error_description,
                    permanent=error_permanent,
                ),
            ),
            SmsLog(
                bulk_id=bulk_id,
                message_id=message_id2,
                to=to,
                sent_at=sent_at,
                done_at=done_at,
                sms_count=sms_count,
                mcc_mnc=mcc_mnc,
                price=MessagePrice(
                    price_per_message=price_per_message, currency=currency
                ),
                status=MessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                error=MessageError(
                    group_id=error_group_id,
                    group_name=error_group_name,
                    id=error_id,
                    name=error_name,
                    description=error_description,
                    permanent=error_permanent,
                ),
            ),
        ]
    )

    assert actual_response == expected_logs_response


def to_query_string_without_escaping(query_params: dict):
    if not query_params:
        return ""
    return "&".join(
        [
            "{}={}".format(paramName, paramValue)
            for (paramName, paramValue) in query_params.items()
        ]
    )


def setup_post_request_ok(
    httpserver: HTTPServer,
    endpoint: str,
    expected_request: dict = None,
    expected_response: dict = None,
):
    httpserver.expect_request(
        uri=endpoint, method="POST", json=expected_request
    ).respond_with_json(expected_response)


def setup_get_request(
    httpserver: HTTPServer,
    endpoint: str,
    expected_response: dict,
    query_string: str = None,
):
    httpserver.expect_request(
        uri=endpoint, method="GET", query_string=query_string
    ).respond_with_json(status=200, response_json=expected_response)


def setup_put_request_ok(
    httpserver: HTTPServer,
    endpoint: str,
    expected_request: dict,
    expected_response: dict,
    query_string: str,
):
    httpserver.expect_request(
        uri=endpoint, method="PUT", json=expected_request, query_string=query_string
    ).respond_with_json(status=200, response_json=expected_response)


@pytest.fixture
def sms_api_client():
    configuration = Configuration(host="http://localhost:8088")
    configuration.api_key["APIKeyHeader"] = "GivenApiKey"
    configuration.api_key_prefix["APIKeyHeader"] = "App"
    return SmsApi(ApiClient(configuration))


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", 8088
