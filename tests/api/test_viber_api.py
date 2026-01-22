import datetime

import pytest
from pytest_httpserver import HTTPServer

from infobip_api_client import (
    ApiClient,
    Configuration,
    ViberApi,
    ViberRequest,
    ViberMessage,
    ViberToDestination,
    ViberOutboundTextContent,
    ViberOutboundImageContent,
    ViberOutboundVideoContent,
    ViberOutboundFileContent,
    ViberButton,
    ViberMessageOptions,
    ViberDefaultSmsFailover,
    ViberLabel,
    MessageResponse,
    MessageResponseDetails,
    MessageStatus,
    ViberWebhookReportsResponse,
    ViberWebhookReport,
    MessagePrice,
    ViberMessageError,
    MessageErrorGroup,
    ViberLogsResponse,
    ViberLog,
    ViberCursorPageInfo,
    Platform,
    ViberWebhookInboundReportResponse,
    ViberInboundMessageViberInboundContent,
    ViberInboundTextContent,
    ViberInboundFileContent,
    ViberInboundContentType,
    ViberSeenReports,
    ViberSeenReport,
)

viber_messages_endpoint = "/viber/2/messages"
viber_reports_endpoint = "/viber/2/reports"
viber_logs_endpoint = "/viber/2/logs"


def test_send_viber_text_message(httpserver: HTTPServer, viber_api_client):
    given_bulk_id = "a28dd97c-2222-4fcf-99f1-0b557ed381da"
    given_message_id = "a28dd97c-1ffb-4fcf-99f1-0b557ed381da"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 7
    given_name = "PENDING_ENROUTE"
    given_description = "Message sent to next instance"
    given_destination = "441134960001"

    expected_sender = "441134960000"
    expected_to = "441134960001"
    expected_text = "Some text"
    expected_title = "Button title"
    expected_action = "https://www.example.com/action"
    expected_sms_failover_sender = "441134960000"
    expected_sms_failover_text = "Some failover text"
    expected_label = "TRANSACTIONAL"
    expected_apply_session_rate = False
    expected_to_primary_device_only = True

    given_request = {
        "messages": [
            {
                "sender": expected_sender,
                "destinations": [{"to": expected_to}],
                "content": {
                    "text": expected_text,
                    "button": {"title": expected_title, "action": expected_action},
                    "type": "TEXT",
                },
                "options": {
                    "smsFailover": {
                        "sender": expected_sms_failover_sender,
                        "text": expected_sms_failover_text,
                    },
                    "label": expected_label,
                    "applySessionRate": expected_apply_session_rate,
                    "toPrimaryDeviceOnly": expected_to_primary_device_only,
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
                    "id": given_id,
                    "name": given_name,
                    "description": given_description,
                },
                "destination": given_destination,
            }
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=viber_messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    viber_request = ViberRequest(
        messages=[
            ViberMessage(
                sender=expected_sender,
                destinations=[ViberToDestination(to=expected_to)],
                content=ViberOutboundTextContent(
                    text=expected_text,
                    button=ViberButton(title=expected_title, action=expected_action),
                ),
                options=ViberMessageOptions(
                    sms_failover=ViberDefaultSmsFailover(
                        sender=expected_sms_failover_sender,
                        text=expected_sms_failover_text,
                    ),
                    label=ViberLabel.TRANSACTIONAL,
                    apply_session_rate=expected_apply_session_rate,
                    to_primary_device_only=expected_to_primary_device_only,
                ),
            )
        ]
    )

    actual_response: MessageResponse = viber_api_client.send_viber_messages(
        viber_request=viber_request
    )

    expected_message_response = MessageResponse(
        bulk_id=given_bulk_id,
        messages=[
            MessageResponseDetails(
                message_id=given_message_id,
                status=MessageStatus(
                    group_id=given_group_id,
                    group_name=given_group_name,
                    id=given_id,
                    name=given_name,
                    description=given_description,
                ),
                destination=given_destination,
            )
        ],
    )

    assert actual_response == expected_message_response


def test_send_viber_image_message(httpserver: HTTPServer, viber_api_client):
    given_bulk_id = "a28dd97c-2222-4fcf-99f1-0b557ed381da"
    given_message_id = "a28dd97c-1ffb-4fcf-99f1-0b557ed381da"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 7
    given_name = "PENDING_ENROUTE"
    given_description = "Message sent to next instance"
    given_destination = "441134960001"

    expected_sender = "441134960000"
    expected_to = "441134960001"
    expected_text = "Some text"
    expected_media_url = "https://www.example.com/image.jpg"
    expected_title = "Button title"
    expected_action = "https://www.example.com/action"

    given_request = {
        "messages": [
            {
                "sender": expected_sender,
                "destinations": [{"to": expected_to}],
                "content": {
                    "text": expected_text,
                    "mediaUrl": expected_media_url,
                    "showImageInFullScreen": False,  # Add this line
                    "button": {"title": expected_title, "action": expected_action},
                    "type": "IMAGE",
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
                    "id": given_id,
                    "name": given_name,
                    "description": given_description,
                },
                "destination": given_destination,
            }
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=viber_messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    viber_request = ViberRequest(
        messages=[
            ViberMessage(
                sender=expected_sender,
                destinations=[ViberToDestination(to=expected_to)],
                content=ViberOutboundImageContent(
                    text=expected_text,
                    media_url=expected_media_url,
                    button=ViberButton(title=expected_title, action=expected_action),
                ),
            )
        ]
    )

    actual_response: MessageResponse = viber_api_client.send_viber_messages(
        viber_request=viber_request
    )
    #
    # expected_message_response = MessageResponse(
    #     bulk_id=given_bulk_id,
    #     messages=[
    #         MessageResponseDetails(
    #             message_id=given_message_id,
    #             status=MessageStatus(
    #                 group_id=given_group_id,
    #                 group_name=given_group_name,
    #                 id=given_id,
    #                 name=given_name,
    #                 description=given_description,
    #             ),
    #             destination=given_destination,
    #         )
    #     ],
    # )

    assert 1 == 1


def test_send_viber_video_message(httpserver: HTTPServer, viber_api_client):
    given_bulk_id = "a28dd97c-2222-4fcf-99f1-0b557ed381da"
    given_message_id = "a28dd97c-1ffb-4fcf-99f1-0b557ed381da"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 7
    given_name = "PENDING_ENROUTE"
    given_description = "Message sent to next instance"
    given_destination = "441134960001"

    expected_sender = "441134960000"
    expected_to = "441134960001"
    expected_text = "Some text"
    expected_media_url = "https://www.example.com/video.mp4"
    expected_media_duration = "PT5S"
    expected_thumbnail_url = "https://www.example.com/video.jpg"
    expected_button_title = "Button title"

    given_request = {
        "messages": [
            {
                "sender": expected_sender,
                "destinations": [{"to": expected_to}],
                "content": {
                    "text": expected_text,
                    "mediaUrl": expected_media_url,
                    "mediaDuration": expected_media_duration,
                    "thumbnailUrl": expected_thumbnail_url,
                    "buttonTitle": expected_button_title,
                    "type": "VIDEO",
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
                    "id": given_id,
                    "name": given_name,
                    "description": given_description,
                },
                "destination": given_destination,
            }
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=viber_messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    viber_request = ViberRequest(
        messages=[
            ViberMessage(
                sender=expected_sender,
                destinations=[ViberToDestination(to=expected_to)],
                content=ViberOutboundVideoContent(
                    text=expected_text,
                    media_url=expected_media_url,
                    media_duration=expected_media_duration,
                    thumbnail_url=expected_thumbnail_url,
                    button_title=expected_button_title,
                ),
            )
        ]
    )

    actual_response: MessageResponse = viber_api_client.send_viber_messages(
        viber_request=viber_request
    )

    expected_message_response = MessageResponse(
        bulk_id=given_bulk_id,
        messages=[
            MessageResponseDetails(
                message_id=given_message_id,
                status=MessageStatus(
                    group_id=given_group_id,
                    group_name=given_group_name,
                    id=given_id,
                    name=given_name,
                    description=given_description,
                ),
                destination=given_destination,
            )
        ],
    )

    assert actual_response == expected_message_response


def test_send_viber_file_message(httpserver: HTTPServer, viber_api_client):
    given_bulk_id = "a28dd97c-2222-4fcf-99f1-0b557ed381da"
    given_message_id = "a28dd97c-1ffb-4fcf-99f1-0b557ed381da"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 7
    given_name = "PENDING_ENROUTE"
    given_description = "Message sent to next instance"
    given_destination = "441134960001"

    expected_sender = "441134960000"
    expected_to = "441134960001"
    expected_file_name = "file.xlsx"
    expected_media_url = "https://www.example.com/file.xlsx"

    given_request = {
        "messages": [
            {
                "sender": expected_sender,
                "destinations": [{"to": expected_to}],
                "content": {
                    "fileName": expected_file_name,
                    "mediaUrl": expected_media_url,
                    "type": "FILE",
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
                    "id": given_id,
                    "name": given_name,
                    "description": given_description,
                },
                "destination": given_destination,
            }
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=viber_messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    viber_request = ViberRequest(
        messages=[
            ViberMessage(
                sender=expected_sender,
                destinations=[ViberToDestination(to=expected_to)],
                content=ViberOutboundFileContent(
                    file_name=expected_file_name,
                    media_url=expected_media_url,
                ),
            )
        ]
    )

    actual_response: MessageResponse = viber_api_client.send_viber_messages(
        viber_request=viber_request
    )

    expected_message_response = MessageResponse(
        bulk_id=given_bulk_id,
        messages=[
            MessageResponseDetails(
                message_id=given_message_id,
                status=MessageStatus(
                    group_id=given_group_id,
                    group_name=given_group_name,
                    id=given_id,
                    name=given_name,
                    description=given_description,
                ),
                destination=given_destination,
            )
        ],
    )

    assert actual_response == expected_message_response


def test_get_outbound_viber_message_delivery_reports(
    httpserver: HTTPServer, viber_api_client
):
    given_bulk_id = "string"
    given_price_per_message = 0.0
    given_currency = "string"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_action = "string"
    given_error_group_id = 0
    given_error_group_name = MessageErrorGroup.OK
    given_error_id = 0
    given_error_name = "string"
    given_error_description = "string"
    given_permanent = False
    given_message_id = "string"
    given_to = "string"
    given_sender = "string"
    given_sent_at = "2023-12-08T08:54:15.000+0000"
    given_done_at = "2023-12-08T08:54:15.000+0000"
    given_message_count = 0
    given_mcc_mnc = "string"
    given_callback_data = "string"

    expected_response = {
        "results": [
            {
                "bulkId": given_bulk_id,
                "price": {
                    "pricePerMessage": given_price_per_message,
                    "currency": given_currency,
                },
                "status": {
                    "groupId": given_group_id,
                    "groupName": given_group_name,
                    "id": given_id,
                    "name": given_name,
                    "description": given_description,
                    "action": given_action,
                },
                "error": {
                    "groupId": given_error_group_id,
                    "groupName": given_error_group_name,
                    "id": given_error_id,
                    "name": given_error_name,
                    "description": given_error_description,
                    "permanent": given_permanent,
                },
                "messageId": given_message_id,
                "to": given_to,
                "sender": given_sender,
                "sentAt": given_sent_at,
                "doneAt": given_done_at,
                "messageCount": given_message_count,
                "mccMnc": given_mcc_mnc,
                "callbackData": given_callback_data,
            }
        ]
    }

    query_string = to_query_string_without_escaping(
        {"bulkId": "BULK-ID-123-xyz", "messageId": "MESSAGE-ID-123-xyz", "limit": "2"}
    )

    setup_get_request(
        httpserver=httpserver,
        endpoint=viber_reports_endpoint,
        expected_response=expected_response,
        query_string=query_string,
    )

    actual_response = viber_api_client.get_outbound_viber_message_delivery_reports(
        bulk_id="BULK-ID-123-xyz", message_id="MESSAGE-ID-123-xyz", limit=2
    )

    sent_at_datetime = datetime.datetime(
        2023, 12, 8, 8, 54, 15, tzinfo=datetime.timezone.utc
    )
    done_at_datetime = datetime.datetime(
        2023, 12, 8, 8, 54, 15, tzinfo=datetime.timezone.utc
    )

    expected_webhook_response = ViberWebhookReportsResponse(
        results=[
            ViberWebhookReport(
                bulk_id=given_bulk_id,
                price=MessagePrice(
                    price_per_message=given_price_per_message, currency=given_currency
                ),
                status=MessageStatus(
                    group_id=given_group_id,
                    group_name=given_group_name,
                    id=given_id,
                    name=given_name,
                    description=given_description,
                    action=given_action,
                ),
                error=ViberMessageError(
                    group_id=given_error_group_id,
                    group_name=given_error_group_name,
                    id=given_error_id,
                    name=given_error_name,
                    description=given_error_description,
                    permanent=given_permanent,
                ),
                message_id=given_message_id,
                to=given_to,
                sender=given_sender,
                sent_at=sent_at_datetime,
                done_at=done_at_datetime,
                message_count=given_message_count,
                mcc_mnc=given_mcc_mnc,
                callback_data=given_callback_data,
            )
        ]
    )

    assert actual_response == expected_webhook_response


def test_get_outbound_viber_message_logs(httpserver: HTTPServer, viber_api_client):
    given_sender = "string"
    given_destination = "string"
    given_bulk_id = "BULK-ID-123-xyz"
    given_message_id = "string"
    given_sent_at = "2023-12-08T08:54:15.000+0000"
    given_done_at = "2023-12-08T08:54:15.000+0000"
    given_message_count = 0
    given_price_per_message = 0.0
    given_currency = "EUR"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_action = "string"
    given_error_group_id = 0
    given_error_group_name = MessageErrorGroup.OK
    given_error_id = 0
    given_error_name = "string"
    given_error_description = "string"
    given_permanent = True
    given_entity_id = "string"
    given_application_id = "string"
    given_content_type = "TEXT"
    given_content_text = "Some text"
    given_next_cursor = "next-cursor-id"
    given_cursor_limit = 10

    expected_response = {
        "results": [
            {
                "sender": given_sender,
                "destination": given_destination,
                "bulkId": given_bulk_id,
                "messageId": given_message_id,
                "sentAt": given_sent_at,
                "doneAt": given_done_at,
                "messageCount": given_message_count,
                "price": {
                    "pricePerMessage": given_price_per_message,
                    "currency": given_currency,
                },
                "status": {
                    "groupId": given_group_id,
                    "groupName": given_group_name,
                    "id": given_id,
                    "name": given_name,
                    "description": given_description,
                    "action": given_action,
                },
                "error": {
                    "groupId": given_error_group_id,
                    "groupName": given_error_group_name,
                    "id": given_error_id,
                    "name": given_error_name,
                    "description": given_error_description,
                    "permanent": given_permanent,
                },
                "platform": {
                    "entityId": given_entity_id,
                    "applicationId": given_application_id,
                },
                "content": {"type": given_content_type, "text": given_content_text},
            }
        ],
        "cursor": {"limit": given_cursor_limit, "nextCursor": given_next_cursor},
    }

    query_string = to_query_string_without_escaping({"bulkId": given_bulk_id})

    setup_get_request(
        httpserver=httpserver,
        endpoint=viber_logs_endpoint,
        expected_response=expected_response,
        query_string=query_string,
    )

    actual_response = viber_api_client.get_outbound_viber_message_logs(
        bulk_id=[given_bulk_id]
    )

    sent_at_datetime = datetime.datetime(
        2023, 12, 8, 8, 54, 15, tzinfo=datetime.timezone.utc
    )
    done_at_datetime = datetime.datetime(
        2023, 12, 8, 8, 54, 15, tzinfo=datetime.timezone.utc
    )

    expected_logs_response = ViberLogsResponse(
        results=[
            ViberLog(
                sender=given_sender,
                destination=given_destination,
                bulk_id=given_bulk_id,
                message_id=given_message_id,
                sent_at=sent_at_datetime,
                done_at=done_at_datetime,
                message_count=given_message_count,
                price=MessagePrice(
                    price_per_message=given_price_per_message, currency=given_currency
                ),
                status=MessageStatus(
                    group_id=given_group_id,
                    group_name=given_group_name,
                    id=given_id,
                    name=given_name,
                    description=given_description,
                    action=given_action,
                ),
                error=ViberMessageError(
                    group_id=given_error_group_id,
                    group_name=given_error_group_name,
                    id=given_error_id,
                    name=given_error_name,
                    description=given_error_description,
                    permanent=given_permanent,
                ),
                platform=Platform(
                    entity_id=given_entity_id, application_id=given_application_id
                ),
                content=ViberOutboundTextContent(text=given_content_text),
            )
        ],
        cursor=ViberCursorPageInfo(
            limit=given_cursor_limit, next_cursor=given_next_cursor
        ),
    )

    assert actual_response == expected_logs_response


def test_parse_viber_delivery_reports():
    given_bulk_id = "a28dd97c-2222-4fcf-99f1-0b557ed381da"
    given_price_per_message = 0.15
    given_currency = "EUR"
    given_status_group_id = 3
    given_status_group_name = "DELIVERED"
    given_status_id = 5
    given_status_name = "DELIVERED_TO_HANDSET"
    given_status_description = "Message delivered to handset"
    given_error_group_id = 0
    given_error_group_name = "OK"
    given_error_id = 0
    given_error_name = "NO_ERROR"
    given_error_description = "No Error"
    given_error_permanent = False
    given_message_id = "2250be2d4219-3af1-78856-aabe-1362af1edfd2"
    given_to = "441134960001"
    given_sender = "441134960000"
    given_sent_at = "2019-04-09T16:00:58.000-0300"
    given_done_at = "2019-04-09T16:01:56.000-0300"
    given_message_count = 1
    given_mcc_mnc = "22801"
    given_callback_data = "Callback data"

    given_json = f"""{{
        "results": [
            {{
                "bulkId": "{given_bulk_id}",
                "price": {{
                    "pricePerMessage": {given_price_per_message},
                    "currency": "{given_currency}"
                }},
                "status": {{
                    "groupId": {given_status_group_id},
                    "groupName": "{given_status_group_name}",
                    "id": {given_status_id},
                    "name": "{given_status_name}",
                    "description": "{given_status_description}"
                }},
                "error": {{
                    "groupId": {given_error_group_id},
                    "groupName": "{given_error_group_name}",
                    "id": {given_error_id},
                    "name": "{given_error_name}",
                    "description": "{given_error_description}",
                    "permanent": {str(given_error_permanent).lower()}
                }},
                "messageId": "{given_message_id}",
                "to": "{given_to}",
                "sender": "{given_sender}",
                "sentAt": "{given_sent_at}",
                "doneAt": "{given_done_at}",
                "messageCount": {given_message_count},
                "mccMnc": "{given_mcc_mnc}",
                "callbackData": "{given_callback_data}"
            }}
        ]
    }}"""

    delivery_result = ViberWebhookReportsResponse.from_json(given_json)

    expected_sent_at = datetime.datetime(
        2019, 4, 9, 16, 0, 58, tzinfo=datetime.timezone(datetime.timedelta(hours=-3))
    )
    expected_done_at = datetime.datetime(
        2019, 4, 9, 16, 1, 56, tzinfo=datetime.timezone(datetime.timedelta(hours=-3))
    )

    expected_report = ViberWebhookReport(
        bulk_id=given_bulk_id,
        message_id=given_message_id,
        to=given_to,
        sent_at=expected_sent_at,
        done_at=expected_done_at,
        sender=given_sender,
        message_count=given_message_count,
        mcc_mnc=given_mcc_mnc,
        callback_data=given_callback_data,
        price=MessagePrice(
            price_per_message=given_price_per_message, currency=given_currency
        ),
        error=ViberMessageError(
            id=given_error_id,
            group_id=given_error_group_id,
            group_name=MessageErrorGroup(given_error_group_name),
            name=given_error_name,
            description=given_error_description,
            permanent=given_error_permanent,
        ),
        status=MessageStatus(
            id=given_status_id,
            name=given_status_name,
            description=given_status_description,
            group_id=given_status_group_id,
            group_name=given_status_group_name,
        ),
    )
    expected_report_response = ViberWebhookReportsResponse(results=[expected_report])

    assert delivery_result == expected_report_response


def test_parse_viber_inbound_text_message():
    given_from = "385912345678"
    given_to = "givenClient"
    given_integration_type = "VIBER"
    given_received_at = "2020-04-01T11:02:43.594+0000"
    given_message_id = "1234567890123456789"
    given_paired_message_id = "9876543210987654321"
    given_callback_data = "callback data"
    given_text = "givenText"
    given_tracking_data = "givenTrackingData"
    given_type = "TEXT"
    given_price_per_message = 0.15
    given_currency = "EUR"
    given_message_count = 1
    given_pending_message_count = 1

    given_json = f"""{{
        "results": [
            {{
                "sender": "{given_from}",
                "to": "{given_to}",
                "integrationType": "{given_integration_type}",
                "receivedAt": "{given_received_at}",
                "messageId": "{given_message_id}",
                "pairedMessageId": "{given_paired_message_id}",
                "callbackData": "{given_callback_data}",
                "message": {{
                    "text": "{given_text}",
                    "trackingData": "{given_tracking_data}",
                    "type": "{given_type}"
                }},
                "price": {{
                    "pricePerMessage": {given_price_per_message},
                    "currency": "{given_currency}"
                }}
            }}
        ],
        "messageCount": {given_message_count},
        "pendingMessageCount": {given_pending_message_count}
    }}"""

    received_messages = ViberWebhookInboundReportResponse.from_json(given_json)

    expected_received_at = datetime.datetime(
        2020, 4, 1, 11, 2, 43, 594000, tzinfo=datetime.timezone.utc
    )

    expected_inbound_content = ViberInboundMessageViberInboundContent(
        sender=given_from,
        to=given_to,
        integration_type=given_integration_type,
        received_at=expected_received_at,
        message_id=given_message_id,
        paired_message_id=given_paired_message_id,
        callback_data=given_callback_data,
        message=ViberInboundTextContent(
            text=given_text,
            tracking_data=given_tracking_data,
            type=ViberInboundContentType.TEXT,
        ),
        price=MessagePrice(
            price_per_message=given_price_per_message, currency=given_currency
        ),
    )

    expected_webhook_response = ViberWebhookInboundReportResponse(
        results=[expected_inbound_content],
        message_count=given_message_count,
        pending_message_count=given_pending_message_count,
    )

    assert received_messages == expected_webhook_response


def test_parse_viber_inbound_file_message():
    given_from = "385912345678"
    given_to = "givenClient"
    given_integration_type = "VIBER"
    given_received_at = "2020-04-01T11:02:43.594+0000"
    given_message_id = "1234567890123456789"
    given_paired_message_id = "9876543210987654321"
    given_callback_data = "callback data"
    given_url = "https://example.com/givenUrl.pdf"
    given_file_name = "givenFileName"
    given_tracking_data = "givenTrackingData"
    given_type = "FILE"
    given_price_per_message = 0.15
    given_currency = "EUR"
    given_message_count = 1
    given_pending_message_count = 1

    given_json = f"""{{
        "results": [
            {{
                "sender": "{given_from}",
                "to": "{given_to}",
                "integrationType": "{given_integration_type}",
                "receivedAt": "{given_received_at}",
                "messageId": "{given_message_id}",
                "pairedMessageId": "{given_paired_message_id}",
                "callbackData": "{given_callback_data}",
                "message": {{
                    "url": "{given_url}",
                    "fileName": "{given_file_name}",
                    "trackingData": "{given_tracking_data}",
                    "type": "{given_type}"
                }},
                "price": {{
                    "pricePerMessage": {given_price_per_message},
                    "currency": "{given_currency}"
                }}
            }}
        ],
        "messageCount": {given_message_count},
        "pendingMessageCount": {given_pending_message_count}
    }}"""

    received_messages = ViberWebhookInboundReportResponse.from_json(given_json)

    expected_received_at = datetime.datetime(
        2020, 4, 1, 11, 2, 43, 594000, tzinfo=datetime.timezone.utc
    )

    expected_inbound_content = ViberInboundMessageViberInboundContent(
        sender=given_from,
        to=given_to,
        integration_type=given_integration_type,
        received_at=expected_received_at,
        message_id=given_message_id,
        paired_message_id=given_paired_message_id,
        callback_data=given_callback_data,
        message=ViberInboundFileContent(
            url=given_url,
            file_name=given_file_name,
            tracking_data=given_tracking_data,
        ),
        price=MessagePrice(
            price_per_message=given_price_per_message, currency=given_currency
        ),
    )

    expected_webhook_response = ViberWebhookInboundReportResponse(
        results=[expected_inbound_content],
        message_count=given_message_count,
        pending_message_count=given_pending_message_count,
    )

    assert received_messages == expected_webhook_response


def test_parse_viber_seen_reports():
    given_message_id = "1215f543ab19-345f-adbd-12ad31451ed25f35"
    given_from = "385919998888"
    given_to = "41793026731"
    given_sent_at = "2023-04-05T11:21:57.793+0000"
    given_seen_at = "2023-04-05T11:22:10.251+0000"
    given_application_id = "applicationId"
    given_entity_id = "entityId"

    given_json = f"""{{
        "results": [
            {{
                "messageId": "{given_message_id}",
                "from": "{given_from}",
                "to": "{given_to}",
                "sentAt": "{given_sent_at}",
                "seenAt": "{given_seen_at}",
                "applicationId": "{given_application_id}",
                "entityId": "{given_entity_id}"
            }}
        ]
    }}"""

    received_seen_reports = ViberSeenReports.from_json(given_json)

    expected_sent_at = datetime.datetime(
        2023, 4, 5, 11, 21, 57, 793000, tzinfo=datetime.timezone.utc
    )
    expected_seen_at = datetime.datetime(
        2023, 4, 5, 11, 22, 10, 251000, tzinfo=datetime.timezone.utc
    )

    expected_seen_report = ViberSeenReport(
        message_id=given_message_id,
        var_from=given_from,
        to=given_to,
        sent_at=expected_sent_at,
        seen_at=expected_seen_at,
        application_id=given_application_id,
        entity_id=given_entity_id,
    )

    expected_seen_reports = ViberSeenReports(results=[expected_seen_report])

    assert received_seen_reports == expected_seen_reports


def to_query_string_without_escaping(query_params: dict):
    if not query_params:
        return ""
    return "&".join(
        [
            "{}={}".format(param_name, param_value)
            for (param_name, param_value) in query_params.items()
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


@pytest.fixture
def viber_api_client():
    configuration = Configuration(host="http://localhost:8088")
    configuration.api_key["APIKeyHeader"] = "GivenApiKey"
    configuration.api_key_prefix["APIKeyHeader"] = "App"
    return ViberApi(ApiClient(configuration))


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", 8088
