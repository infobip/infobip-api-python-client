import datetime

import pytest
from dateutil.tz import tzoffset
from pytest_httpserver import HTTPServer

from infobip_api_client import (
    ApiClient,
    Configuration,
    SmsDestination,
    SmsApi,
    SmsResponse,
    SmsResponseDetails,
    SmsBulkResponse,
    SmsBulkStatusResponse,
    SmsBulkStatus,
    SmsBulkRequest,
    SmsUpdateStatusRequest,
    SmsDeliveryResult,
    MessagePrice,
    SmsLogsResponse,
    SmsLog,
    SmsInboundMessageResult,
    SmsInboundMessage,
    SmsTracking,
    SmsBinaryContent,
    SmsPreviewRequest,
    SmsPreviewResponse,
    SmsPreview,
    SmsLanguageConfiguration,
    SmsRequest,
    SmsMessage,
    SmsMessageContent,
    SmsTextContent,
    SmsMessageOptions,
    Platform,
    SmsMessageStatus,
    MessageGeneralStatus,
    SmsMessageResponseDetails,
    SmsTransliterationCode,
    ValidityPeriod,
    ValidityPeriodTimeUnit,
    SmsWebhooks,
    SmsMessageDeliveryReporting,
    DeliveryTimeWindow,
    DeliveryDay,
    DeliveryTime,
    SmsMessageRequestOptions,
    UrlOptions,
    SmsRequestSchedulingSettings,
    SmsPreviewLanguage,
    SmsDeliveryReport,
    SmsMessageError,
    MessageErrorGroup,
)

sms_messages = "/sms/3/messages"
sms_outbound_reports_endpoint = "/sms/3/reports"
sms_outbound_logs_endpoint = "/sms/3/logs"
sms_preview_endpoint = "/sms/1/preview"
sms_bulks_endpoint = "/sms/1/bulks"
sms_bulks_status_endpoint = "/sms/1/bulks/status"
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
    given_group_name = MessageGeneralStatus.PENDING
    given_status_id = 26
    given_status_name = "MESSAGE_ACCEPTED"
    given_status_description = "Message sent to next instance"
    given_application_id = "given_application_id"
    given_entity_id = "given_entity_id"
    given_message_count = 1

    given_request = {
        "messages": [
            {
                "sender": given_from,
                "destinations": [{"to": given_to}],
                "content": {
                    "text": given_text,
                },
                "options": {
                    "platform": {
                        "applicationId": given_application_id,
                        "entityId": given_entity_id,
                    }
                },
            }
        ]
    }

    expected_response = {
        "bulkId": given_bulk_id,
        "messages": [
            {
                "messageId": given_message_id,
                "status": {
                    "groupId": given_group_id,
                    "groupName": given_group_name,
                    "id": given_status_id,
                    "name": given_status_name,
                    "description": given_status_description,
                },
                "destination": given_to,
                "details": {
                    "messageCount": given_message_count,
                },
            }
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=sms_messages,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = SmsRequest(
        messages=[
            SmsMessage(
                destinations=[
                    SmsDestination(
                        to=given_to,
                    ),
                ],
                sender=given_from,
                content=SmsMessageContent(actual_instance=SmsTextContent(text=given_text)),
                options=SmsMessageOptions(
                    platform=Platform(
                        application_id=given_application_id, entity_id=given_entity_id
                    )
                ),
            )
        ]
    )

    actual_response: SmsResponse = sms_api_client.send_sms_messages(sms_request=request)

    expected_sms_response = SmsResponse(
        bulk_id=given_bulk_id,
        messages=[
            SmsResponseDetails(
                message_id=given_message_id,
                status=SmsMessageStatus(
                    group_id=given_group_id,
                    group_name=given_group_name,
                    id=given_status_id,
                    name=given_status_name,
                    description=given_status_description,
                ),
                destination=given_to,
                details=SmsMessageResponseDetails(message_count=given_message_count),
            )
        ],
    )

    assert actual_response == expected_sms_response


def test_send_fully_featured_sms(httpserver: HTTPServer, sms_api_client):
    sender_1 = "InfoSMS"
    sender_2 = "41793026700"
    destination_1 = "41793026727"
    destination_2 = "41793026834"
    destination_3 = "41793026700"
    message_id_1 = "MESSAGE-ID-123-xyz"
    text_1 = "Artık Ulusal Dil Tanımlayıcısı ile Türkçe karakterli smslerinizi rahatlıkla iletebilirsiniz."
    text_2 = "A long time ago, in a galaxy far, far away... It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire."
    transliteration = SmsTransliterationCode.TURKISH
    validity_period_amount = 720
    validity_period_unit = ValidityPeriodTimeUnit.HOURS
    campaign_reference_id = "summersale"
    delivery_url = "https://www.example.com/sms/advanced"
    intermediate_report = True
    content_type = "application/json"
    callback_data = "DLR callback data"
    delivery_days = [
        DeliveryDay.MONDAY,
        DeliveryDay.TUESDAY,
        DeliveryDay.WEDNESDAY,
        DeliveryDay.THURSDAY,
        DeliveryDay.FRIDAY,
        DeliveryDay.SATURDAY,
        DeliveryDay.SUNDAY,
    ]
    delivery_from_hour = 6
    delivery_from_minute = 0
    delivery_to_hour = 15
    delivery_to_minute = 30
    bulk_id = "BULK-ID-123-xyz"
    send_at = "2023-08-01T16:10:00.000+05:30"

    send_at_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )
    shorten_url = True
    track_clicks = True
    tracking_url = "https://example.com/click-report"
    remove_protocol = True
    custom_domain = "example.com"
    include_sms_count_in_response = True
    use_conversion_tracking = True
    conversion_tracking_name = "MY_CAMPAIGN"

    # Response values
    bulk_id_response = "2034072219640523072"
    message_id_response_1 = "2250be2d4219-3af1-78856-aabe-1362af1edfd2"
    message_id_response_2 = "3350be2d4219-3af1-23343-bbbb-1362af1edfd3"
    status_group_id = 1
    status_group_name = MessageGeneralStatus.PENDING
    status_id = 26
    status_name = "PENDING_ACCEPTED"
    status_description = "Message sent to next instance"
    message_count = 1

    given_request = {
        "messages": [
            {
                "sender": sender_1,
                "destinations": [
                    {"to": destination_1, "messageId": message_id_1},
                    {"to": destination_2},
                ],
                "content": {"text": text_1, "transliteration": transliteration},
                "options": {
                    "validityPeriod": {
                        "amount": validity_period_amount,
                        "timeUnit": validity_period_unit,
                    },
                    "campaignReferenceId": campaign_reference_id,
                },
                "webhooks": {
                    "delivery": {
                        "url": delivery_url,
                        "intermediateReport": intermediate_report,
                    },
                    "contentType": content_type,
                    "callbackData": callback_data,
                },
            },
            {
                "sender": sender_2,
                "destinations": [{"to": destination_3}],
                "content": {"text": text_2},
                "options": {
                    "deliveryTimeWindow": {
                        "days": delivery_days,
                        "from": {
                            "hour": delivery_from_hour,
                            "minute": delivery_from_minute,
                        },
                        "to": {"hour": delivery_to_hour, "minute": delivery_to_minute},
                    }
                },
            },
        ],
        "options": {
            "schedule": {"bulkId": bulk_id, "sendAt": send_at},
            "tracking": {
                "shortenUrl": shorten_url,
                "trackClicks": track_clicks,
                "trackingUrl": tracking_url,
                "removeProtocol": remove_protocol,
                "customDomain": custom_domain,
            },
            "includeSmsCountInResponse": include_sms_count_in_response,
            "conversionTracking": {
                "useConversionTracking": use_conversion_tracking,
                "conversionTrackingName": conversion_tracking_name,
            },
        },
    }

    given_response = {
        "bulkId": bulk_id_response,
        "messages": [
            {
                "messageId": message_id_response_1,
                "status": {
                    "groupId": status_group_id,
                    "groupName": status_group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "destination": destination_1,
                "details": {"messageCount": message_count},
            },
            {
                "messageId": message_id_response_2,
                "status": {
                    "groupId": status_group_id,
                    "groupName": status_group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "destination": destination_2,
                "details": {"messageCount": message_count},
            },
        ],
    }

    setup_post_request_ok(httpserver, sms_messages, given_request, given_response)

    request = SmsRequest(
        messages=[
            SmsMessage(
                sender=sender_1,
                destinations=[
                    SmsDestination(to=destination_1, message_id=message_id_1),
                    SmsDestination(to=destination_2),
                ],
                content=SmsMessageContent(
                    actual_instance=SmsTextContent(
                        text=text_1, transliteration=transliteration
                    )
                ),
                options=SmsMessageOptions(
                    validity_period=ValidityPeriod(
                        amount=validity_period_amount, time_unit=validity_period_unit
                    ),
                    campaign_reference_id=campaign_reference_id,
                ),
                webhooks=SmsWebhooks(
                    delivery=SmsMessageDeliveryReporting(
                        url=delivery_url, intermediate_report=intermediate_report
                    ),
                    content_type=content_type,
                    callback_data=callback_data,
                ),
            ),
            SmsMessage(
                sender=sender_2,
                destinations=[SmsDestination(to=destination_3)],
                content=SmsMessageContent(actual_instance=SmsTextContent(text=text_2)),
                options=SmsMessageOptions(
                    delivery_time_window=DeliveryTimeWindow(
                        days=delivery_days,
                        var_from=DeliveryTime(
                            hour=delivery_from_hour, minute=delivery_from_minute
                        ),
                        to=DeliveryTime(
                            hour=delivery_to_hour, minute=delivery_to_minute
                        ),
                    )
                ),
            ),
        ],
        options=SmsMessageRequestOptions(
            schedule=SmsRequestSchedulingSettings(
                bulk_id=bulk_id, send_at=send_at_offset
            ),
            tracking=UrlOptions(
                shorten_url=shorten_url,
                track_clicks=track_clicks,
                tracking_url=tracking_url,
                remove_protocol=remove_protocol,
                custom_domain=custom_domain,
            ),
            include_sms_count_in_response=include_sms_count_in_response,
            conversion_tracking=SmsTracking(
                use_conversion_tracking=use_conversion_tracking,
                conversion_tracking_name=conversion_tracking_name,
            ),
        ),
    )

    response = sms_api_client.send_sms_messages(sms_request=request)

    expected_response = SmsResponse(
        bulk_id=bulk_id_response,
        messages=[
            SmsResponseDetails(
                message_id=message_id_response_1,
                status=SmsMessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                destination=destination_1,
                details=SmsMessageResponseDetails(message_count=message_count),
            ),
            SmsResponseDetails(
                message_id=message_id_response_2,
                status=SmsMessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                destination=destination_2,
                details=SmsMessageResponseDetails(message_count=message_count),
            ),
        ],
    )

    assert response == expected_response


def test_send_fully_featured_binary_sms(httpserver: HTTPServer, sms_api_client):
    sender_1 = "InfoSMS"
    sender_2 = "41793026700"
    destination_1 = "41793026727"
    destination_2 = "41793026834"
    destination_3 = "41793026700"
    message_id_1 = "MESSAGE-ID-123-xyz"
    validity_period_amount = 720
    validity_period_unit = ValidityPeriodTimeUnit.HOURS
    campaign_reference_id = "summersale"
    delivery_url = "https://www.example.com/sms/advanced"
    intermediate_report = True
    content_type = "application/json"
    callback_data = "DLR callback data"
    delivery_days = [
        DeliveryDay.MONDAY,
        DeliveryDay.TUESDAY,
        DeliveryDay.WEDNESDAY,
        DeliveryDay.THURSDAY,
        DeliveryDay.FRIDAY,
        DeliveryDay.SATURDAY,
        DeliveryDay.SUNDAY,
    ]
    delivery_from_hour = 6
    delivery_from_minute = 0
    delivery_to_hour = 15
    delivery_to_minute = 30
    bulk_id = "BULK-ID-123-xyz"
    send_at = "2023-08-01T16:10:00.000+05:30"
    data_coding = 0
    esm_class = 0
    given_hex = "41 20 6C 6F 6E 67 20 74 …20 45 6D 70 69 72 65 2E"

    send_at_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )
    shorten_url = True
    track_clicks = True
    tracking_url = "https://example.com/click-report"
    remove_protocol = True
    custom_domain = "example.com"
    include_sms_count_in_response = True
    use_conversion_tracking = True
    conversion_tracking_name = "MY_CAMPAIGN"

    # Response values
    bulk_id_response = "2034072219640523072"
    message_id_response_1 = "2250be2d4219-3af1-78856-aabe-1362af1edfd2"
    message_id_response_2 = "3350be2d4219-3af1-23343-bbbb-1362af1edfd3"
    status_group_id = 1
    status_group_name = MessageGeneralStatus.PENDING
    status_id = 26
    status_name = "PENDING_ACCEPTED"
    status_description = "Message sent to next instance"
    message_count = 1

    given_request = {
        "messages": [
            {
                "sender": sender_1,
                "destinations": [
                    {"to": destination_1, "messageId": message_id_1},
                    {"to": destination_2},
                ],
                "content": {
                    "dataCoding": data_coding,
                    "esmClass": esm_class,
                    "hex": given_hex,
                },
                "options": {
                    "validityPeriod": {
                        "amount": validity_period_amount,
                        "timeUnit": validity_period_unit,
                    },
                    "campaignReferenceId": campaign_reference_id,
                },
                "webhooks": {
                    "delivery": {
                        "url": delivery_url,
                        "intermediateReport": intermediate_report,
                    },
                    "contentType": content_type,
                    "callbackData": callback_data,
                },
            },
            {
                "sender": sender_2,
                "destinations": [{"to": destination_3}],
                "content": {
                    "dataCoding": data_coding,
                    "esmClass": esm_class,
                    "hex": given_hex,
                },
                "options": {
                    "deliveryTimeWindow": {
                        "days": delivery_days,
                        "from": {
                            "hour": delivery_from_hour,
                            "minute": delivery_from_minute,
                        },
                        "to": {"hour": delivery_to_hour, "minute": delivery_to_minute},
                    }
                },
            },
        ],
        "options": {
            "schedule": {"bulkId": bulk_id, "sendAt": send_at},
            "tracking": {
                "shortenUrl": shorten_url,
                "trackClicks": track_clicks,
                "trackingUrl": tracking_url,
                "removeProtocol": remove_protocol,
                "customDomain": custom_domain,
            },
            "includeSmsCountInResponse": include_sms_count_in_response,
            "conversionTracking": {
                "useConversionTracking": use_conversion_tracking,
                "conversionTrackingName": conversion_tracking_name,
            },
        },
    }

    given_response = {
        "bulkId": bulk_id_response,
        "messages": [
            {
                "messageId": message_id_response_1,
                "status": {
                    "groupId": status_group_id,
                    "groupName": status_group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "destination": destination_1,
                "details": {"messageCount": message_count},
            },
            {
                "messageId": message_id_response_2,
                "status": {
                    "groupId": status_group_id,
                    "groupName": status_group_name,
                    "id": status_id,
                    "name": status_name,
                    "description": status_description,
                },
                "destination": destination_2,
                "details": {"messageCount": message_count},
            },
        ],
    }

    setup_post_request_ok(httpserver, sms_messages, given_request, given_response)

    request = SmsRequest(
        messages=[
            SmsMessage(
                sender=sender_1,
                destinations=[
                    SmsDestination(to=destination_1, message_id=message_id_1),
                    SmsDestination(to=destination_2),
                ],
                content=SmsMessageContent(
                    actual_instance=SmsBinaryContent(
                        esm_class=esm_class, data_coding=data_coding, hex=given_hex
                    )
                ),
                options=SmsMessageOptions(
                    validity_period=ValidityPeriod(
                        amount=validity_period_amount, time_unit=validity_period_unit
                    ),
                    campaign_reference_id=campaign_reference_id,
                ),
                webhooks=SmsWebhooks(
                    delivery=SmsMessageDeliveryReporting(
                        url=delivery_url, intermediate_report=intermediate_report
                    ),
                    content_type=content_type,
                    callback_data=callback_data,
                ),
            ),
            SmsMessage(
                sender=sender_2,
                destinations=[SmsDestination(to=destination_3)],
                content=SmsMessageContent(
                    actual_instance=SmsBinaryContent(
                        esm_class=esm_class, data_coding=data_coding, hex=given_hex
                    )
                ),
                options=SmsMessageOptions(
                    delivery_time_window=DeliveryTimeWindow(
                        days=delivery_days,
                        var_from=DeliveryTime(
                            hour=delivery_from_hour, minute=delivery_from_minute
                        ),
                        to=DeliveryTime(
                            hour=delivery_to_hour, minute=delivery_to_minute
                        ),
                    )
                ),
            ),
        ],
        options=SmsMessageRequestOptions(
            schedule=SmsRequestSchedulingSettings(
                bulk_id=bulk_id, send_at=send_at_offset
            ),
            tracking=UrlOptions(
                shorten_url=shorten_url,
                track_clicks=track_clicks,
                tracking_url=tracking_url,
                remove_protocol=remove_protocol,
                custom_domain=custom_domain,
            ),
            include_sms_count_in_response=include_sms_count_in_response,
            conversion_tracking=SmsTracking(
                use_conversion_tracking=use_conversion_tracking,
                conversion_tracking_name=conversion_tracking_name,
            ),
        ),
    )

    response = sms_api_client.send_sms_messages(sms_request=request)

    expected_response = SmsResponse(
        bulk_id=bulk_id_response,
        messages=[
            SmsResponseDetails(
                message_id=message_id_response_1,
                status=SmsMessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                destination=destination_1,
                details=SmsMessageResponseDetails(message_count=message_count),
            ),
            SmsResponseDetails(
                message_id=message_id_response_2,
                status=SmsMessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                destination=destination_2,
                details=SmsMessageResponseDetails(message_count=message_count),
            ),
        ],
    )

    assert response == expected_response


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
                    "language": {
                        "languageCode": "AUTODETECT",
                    },
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
                    language=SmsPreviewLanguage(language_code="AUTODETECT"),
                    transliteration="CENTRAL_EUROPEAN",
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
    given_send_at_message_request = "2023-03-08T17:42:05.390+01:00"
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
    send_at_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )

    expected_deserialized_report = SmsDeliveryResult(
        results=[
            SmsDeliveryReport(
                bulk_id="BULK-ID-123-xyz",
                price=MessagePrice(price_per_message=0.01, currency="EUR"),
                status=SmsMessageStatus(
                    group_id=3,
                    group_name=MessageGeneralStatus.DELIVERED,
                    id=5,
                    name="DELIVERED_TO_HANDSET",
                    description="Message delivered to handset",
                ),
                error=SmsMessageError(
                    group_id=0,
                    group_name=MessageErrorGroup.OK,
                    id=0,
                    name="NO_ERROR",
                    description="No Error",
                    permanent=False,
                ),
                message_id="MESSAGE-ID-123-xyz",
                to="41793026727",
                sender="InfoSMS",
                sent_at=send_at_offset,
                done_at=send_at_offset,
                message_count=1,
                platform=Platform(
                    application_id="marketing-automation-application",
                    entity_id="promotional-traffic-entity",
                ),
            )
        ]
    )
    delivery_result_payload = """
    {
      "results": [
        {
          "bulkId": "BULK-ID-123-xyz",
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
            "groupName": "OK",
            "id": 0,
            "name": "NO_ERROR",
            "description": "No Error",
            "permanent": false
          },
          "messageId": "MESSAGE-ID-123-xyz",
          "to": "41793026727",
          "sender": "InfoSMS",
          "sentAt": "2023-08-01T16:10:00+05:30",
          "doneAt": "2023-08-01T16:10:00+05:30",
          "messageCount": 1,
          "platform": {
            "entityId": "promotional-traffic-entity",
            "applicationId": "marketing-automation-application"
          }
        }
      ]
    }
    """

    actual_deserialized_report = SmsDeliveryResult.from_json(delivery_result_payload)

    assert actual_deserialized_report == expected_deserialized_report


def test_inbound_reports_webhook_model():
    received_at_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )

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
            "receivedAt": "2023-08-01T16:10:00+05:30",
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
                received_at=received_at_offset,
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
    message_id_1 = "MESSAGE-ID-123-xyz"
    message_id_2 = "12db39c3-7822-4e72-a3ec-c87442c0ffc5"
    to_1 = "41793026727"
    to_2 = "41793026834"
    sender = "InfoSMS"
    sent_at = "2023-08-01T16:10:00+05:30"
    done_at = "2023-08-01T16:10:00+05:30"

    sent_at_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )

    done_at_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )
    sms_count = 1
    price_per_message = 0.01
    currency = "EUR"
    application_id = "marketing-automation-application"
    entity_id = "promotional-traffic-entity"

    status_group_id = 3
    status_group_name = MessageGeneralStatus.DELIVERED
    status_id = 5
    status_name = "DELIVERED_TO_HANDSET"
    status_description = "Message delivered to handset"

    error_group_id = 0
    error_group_name = MessageErrorGroup.OK
    error_id = 0
    error_name = "NO_ERROR"
    error_description = "No Error"
    error_permanent = False

    expected_response = {
        "results": [
            {
                "bulkId": bulk_id,
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
                "messageId": message_id_1,
                "to": to_1,
                "sender": sender,
                "sentAt": sent_at,
                "doneAt": done_at,
                "messageCount": sms_count,
                "platform": {"entityId": entity_id, "applicationId": application_id},
            },
            {
                "bulkId": bulk_id,
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
                "messageId": message_id_2,
                "to": to_2,
                "sender": sender,
                "sentAt": sent_at,
                "doneAt": done_at,
                "messageCount": sms_count,
                "platform": {"entityId": entity_id, "applicationId": application_id},
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

    actual_response = sms_api_client.get_outbound_sms_message_delivery_reports(
        bulk_id=bulk_id
    )

    expected_deserialized_report = SmsDeliveryResult(
        results=[
            SmsDeliveryReport(
                bulk_id=bulk_id,
                price=MessagePrice(
                    price_per_message=price_per_message, currency=currency
                ),
                status=SmsMessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                error=SmsMessageError(
                    group_id=error_group_id,
                    group_name=error_group_name,
                    id=error_id,
                    name=error_name,
                    description=error_description,
                    permanent=error_permanent,
                ),
                message_id=message_id_1,
                to=to_1,
                sender=sender,
                sent_at=sent_at_offset,
                done_at=done_at_offset,
                message_count=sms_count,
                platform=Platform(application_id=application_id, entity_id=entity_id),
            ),
            SmsDeliveryReport(
                bulk_id=bulk_id,
                price=MessagePrice(
                    price_per_message=price_per_message, currency=currency
                ),
                status=SmsMessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                error=SmsMessageError(
                    group_id=error_group_id,
                    group_name=error_group_name,
                    id=error_id,
                    name=error_name,
                    description=error_description,
                    permanent=error_permanent,
                ),
                message_id=message_id_2,
                to=to_2,
                sender=sender,
                sent_at=sent_at_offset,
                done_at=done_at_offset,
                message_count=sms_count,
                platform=Platform(application_id=application_id, entity_id=entity_id),
            ),
        ]
    )

    assert actual_response == expected_deserialized_report


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
    message_id_1 = "MESSAGE-ID-123-xyz"
    message_id_2 = "12db39c3-7822-4e72-a3ec-c87442c0ffc5"
    destination_1 = "41793026727"
    destination_2 = "41793026834"
    sent_at = "2023-08-01T16:10:00+05:30"
    done_at = "2023-08-01T16:10:00+05:30"

    sent_at_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(seconds=19800)),
    )

    done_at_offset = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(seconds=19800)),
    )
    sms_count = 1
    price_per_message = 0.01
    currency = "EUR"
    application_id = "marketing-automation-application"
    entity_id = "promotional-traffic-entity"
    mcc_mnc = "22801"
    text = "This is a sample message"

    status_group_id = 3
    status_group_name = MessageGeneralStatus.DELIVERED
    status_id = 5
    status_name = "DELIVERED_TO_HANDSET"
    status_description = "Message delivered to handset"

    error_group_id = 0
    error_group_name = MessageErrorGroup.OK
    error_id = 0
    error_name = "NO_ERROR"
    error_description = "No Error"
    error_permanent = False

    expected_response = {
        "results": [
            {
                "destination": destination_1,
                "bulkId": bulk_id,
                "messageId": message_id_1,
                "sentAt": sent_at,
                "doneAt": done_at,
                "messageCount": sms_count,
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
                "platform": {"entityId": entity_id, "applicationId": application_id},
                "content": {"text": text},
                "mccMnc": mcc_mnc,
            },
            {
                "destination": destination_2,
                "bulkId": bulk_id,
                "messageId": message_id_2,
                "sentAt": sent_at,
                "doneAt": done_at,
                "messageCount": sms_count,
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
                "platform": {"entityId": entity_id, "applicationId": application_id},
                "content": {"text": text},
                "mccMnc": mcc_mnc,
            },
        ]
    }

    query_string = to_query_string_without_escaping({"bulkId": bulk_id})

    setup_get_request(
        httpserver=httpserver,
        endpoint=sms_outbound_logs_endpoint,
        expected_response=expected_response,
        query_string=query_string,
    )

    actual_response = sms_api_client.get_outbound_sms_message_logs(bulk_id=[bulk_id])

    expected_deserialized_logs = SmsLogsResponse(
        results=[
            SmsLog(
                destination=destination_1,
                bulk_id=bulk_id,
                message_id=message_id_1,
                sent_at=sent_at_offset,
                done_at=done_at_offset,
                message_count=sms_count,
                price=MessagePrice(
                    price_per_message=price_per_message, currency=currency
                ),
                status=SmsMessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                error=SmsMessageError(
                    group_id=error_group_id,
                    group_name=error_group_name,
                    id=error_id,
                    name=error_name,
                    description=error_description,
                    permanent=error_permanent,
                ),
                platform=Platform(application_id=application_id, entity_id=entity_id),
                content=SmsMessageContent(actual_instance=SmsTextContent(text=text)),
                mcc_mnc=mcc_mnc,
            ),
            SmsLog(
                destination=destination_2,
                bulk_id=bulk_id,
                message_id=message_id_2,
                sent_at=sent_at_offset,
                done_at=done_at_offset,
                message_count=sms_count,
                price=MessagePrice(
                    price_per_message=price_per_message, currency=currency
                ),
                status=SmsMessageStatus(
                    group_id=status_group_id,
                    group_name=status_group_name,
                    id=status_id,
                    name=status_name,
                    description=status_description,
                ),
                error=SmsMessageError(
                    group_id=error_group_id,
                    group_name=error_group_name,
                    id=error_id,
                    name=error_name,
                    description=error_description,
                    permanent=error_permanent,
                ),
                platform=Platform(application_id=application_id, entity_id=entity_id),
                content=SmsMessageContent(actual_instance=SmsTextContent(text=text)),
                mcc_mnc=mcc_mnc,
            ),
        ]
    )

    assert actual_response == expected_deserialized_logs


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
