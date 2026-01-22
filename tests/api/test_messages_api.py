import datetime

import pytest
from pytest_httpserver import HTTPServer

from infobip_api_client import (
    ApiClient,
    Configuration,
    MessagesApi,
    MessagesApiRequest,
    MessagesApiRequestMessagesInner,
    MessagesApiMessage,
    MessagesApiOutboundMessageChannel,
    MessagesApiMessageDestination,
    MessagesApiToDestination,
    MessagesApiMessageContent,
    MessagesApiMessageTextBody,
    MessagesApiMessageBodyType,
    MessagesApiMessageButtonType,
    MessagesApiMessageReplyButton,
    MessagesApiMessageOpenUrlButton,
    MessagesApiMessageDialPhoneButton,
    MessagesApiMessageShowLocationButton,
    MessagesApiMessageRequestLocationButton,
    MessagesApiMessageAddCalendarEventButton,
    MessagesApiMessageImageBody,
    MessagesApiValidationOkResponse,
    MessagesApiTemplateMessage,
    MessagesApiOutboundTemplateChannel,
    MessagesApiTemplate,
    MessagesApiTemplateMessageContent,
    MessagesApiTemplateTextBody,
    MessagesApiTemplateBodyType,
    MessagesApiTemplateButtonType,
    MessagesApiTemplateOpenUrlButton,
    MessagesApiTemplateQuickReplyButton,
    MessagesApiTemplatePhoneNumberButton,
    MessagesApiTemplateCopyCodeButton,
    MessagesApiTemplateFlowButton,
    MessagesApiTemplateCatalogButton,
    MessagesApiTemplateMultiProductButton,
    MessagesApiTemplateMultiProductButtonSection,
    MessagesApiEventRequest,
    MessagesApiOutboundTypingStartedEvent,
    MessagesApiOutboundEventChannel,
    MessagesApiOutboundEventType,
    MessagesApiDeliveryReport,
    MessagesApiInboundDlrChannel,
    MessagesApiIncomingMessage,
    MessagesApiWebhookEvent,
    MessagesApiWebhookEventTextContent,
    MessagesApiInboundMoEventChannel,
    MessagesApiInboundEventType,
    MessageResponse,
)

messages_endpoint = "/messages-api/1/messages"
events_endpoint = "/messages-api/1/events"
validate_endpoint = "/messages-api/1/messages/validate"


def test_send_text_messages(httpserver: HTTPServer, messages_api_client):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "SMS"
    given_sender = "447491163443"
    given_to = "111111111"
    given_text = "May the Force be with you."

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "content": {
                    "body": {
                        "text": given_text,
                        "type": "TEXT",
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiMessage(
                    channel=MessagesApiOutboundMessageChannel.SMS,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    content=MessagesApiMessageContent(
                        body=MessagesApiMessageTextBody(
                            type=MessagesApiMessageBodyType.TEXT, text=given_text
                        )
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1
    message = actual_response.messages[0]
    assert message.message_id == given_message_id
    assert message.status is not None
    assert message.status.group_id == given_group_id
    assert message.status.group_name == given_group_name
    assert message.status.id == given_id
    assert message.status.name == given_name
    assert message.status.description == given_description


def test_send_text_messages_with_reply_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "SMS"
    given_sender = "447491163443"
    given_to = "111111111"
    given_text = "May the Force be with you."
    given_button_text = "Yes, I agree!"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "content": {
                    "body": {
                        "text": given_text,
                        "type": "TEXT",
                    },
                    "buttons": [
                        {
                            "text": given_button_text,
                            "type": "REPLY",
                        }
                    ],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiMessage(
                    channel=MessagesApiOutboundMessageChannel.SMS,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    content=MessagesApiMessageContent(
                        body=MessagesApiMessageTextBody(
                            type=MessagesApiMessageBodyType.TEXT, text=given_text
                        ),
                        buttons=[
                            MessagesApiMessageReplyButton(
                                type=MessagesApiMessageButtonType.REPLY,
                                text=given_button_text,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1
    message = actual_response.messages[0]
    assert message.message_id == given_message_id
    assert message.status.group_id == given_group_id
    assert message.status.name == given_name


def test_send_text_messages_with_open_url_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "SMS"
    given_sender = "447491163443"
    given_to = "111111111"
    given_text = "May the Force be with you."
    given_button_text = "Yes, I agree!"
    given_open_url = "http://example.com/agree"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "content": {
                    "body": {
                        "text": given_text,
                        "type": "TEXT",
                    },
                    "buttons": [
                        {
                            "text": given_button_text,
                            "url": given_open_url,
                            "type": "OPEN_URL",
                        }
                    ],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiMessage(
                    channel=MessagesApiOutboundMessageChannel.SMS,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    content=MessagesApiMessageContent(
                        body=MessagesApiMessageTextBody(
                            type=MessagesApiMessageBodyType.TEXT, text=given_text
                        ),
                        buttons=[
                            MessagesApiMessageOpenUrlButton(
                                type=MessagesApiMessageButtonType.OPEN_URL,
                                text=given_button_text,
                                url=given_open_url,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1
    message = actual_response.messages[0]
    assert message.message_id == given_message_id
    assert message.status.group_id == given_group_id


def test_send_text_messages_with_dial_phone_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "SMS"
    given_sender = "447491163443"
    given_to = "111111111"
    given_text = "May the Force be with you."
    given_button_text = "Yes, I agree!"
    given_phone_number = "+1234567890"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "content": {
                    "body": {
                        "text": given_text,
                        "type": "TEXT",
                    },
                    "buttons": [
                        {
                            "text": given_button_text,
                            "phoneNumber": given_phone_number,
                            "type": "DIAL_PHONE",
                        }
                    ],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiMessage(
                    channel=MessagesApiOutboundMessageChannel.SMS,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    content=MessagesApiMessageContent(
                        body=MessagesApiMessageTextBody(
                            type=MessagesApiMessageBodyType.TEXT, text=given_text
                        ),
                        buttons=[
                            MessagesApiMessageDialPhoneButton(
                                type=MessagesApiMessageButtonType.DIAL_PHONE,
                                text=given_button_text,
                                phone_number=given_phone_number,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_text_messages_with_show_location_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "SMS"
    given_sender = "447491163443"
    given_to = "111111111"
    given_text = "May the Force be with you."
    given_button_text = "Yes, I agree!"
    given_latitude = 37.7749
    given_longitude = -122.4194

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "content": {
                    "body": {
                        "text": given_text,
                        "type": "TEXT",
                    },
                    "buttons": [
                        {
                            "text": given_button_text,
                            "latitude": given_latitude,
                            "longitude": given_longitude,
                            "type": "SHOW_LOCATION",
                        }
                    ],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiMessage(
                    channel=MessagesApiOutboundMessageChannel.SMS,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    content=MessagesApiMessageContent(
                        body=MessagesApiMessageTextBody(
                            type=MessagesApiMessageBodyType.TEXT, text=given_text
                        ),
                        buttons=[
                            MessagesApiMessageShowLocationButton(
                                type=MessagesApiMessageButtonType.SHOW_LOCATION,
                                text=given_button_text,
                                latitude=given_latitude,
                                longitude=given_longitude,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_text_messages_with_request_location_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "SMS"
    given_sender = "447491163443"
    given_to = "111111111"
    given_text = "May the Force be with you."
    given_button_text = "Yes, I agree!"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "content": {
                    "body": {
                        "text": given_text,
                        "type": "TEXT",
                    },
                    "buttons": [
                        {
                            "text": given_button_text,
                            "type": "REQUEST_LOCATION",
                        }
                    ],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiMessage(
                    channel=MessagesApiOutboundMessageChannel.SMS,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    content=MessagesApiMessageContent(
                        body=MessagesApiMessageTextBody(
                            type=MessagesApiMessageBodyType.TEXT, text=given_text
                        ),
                        buttons=[
                            MessagesApiMessageRequestLocationButton(
                                type=MessagesApiMessageButtonType.REQUEST_LOCATION,
                                text=given_button_text,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_text_messages_with_add_calendar_event_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "SMS"
    given_sender = "447491163443"
    given_to = "111111111"
    given_text = "May the Force be with you."
    given_button_text = "Yes, I agree!"
    given_start_time = datetime.datetime(
        2024, 7, 1, 10, 0, 0, tzinfo=datetime.timezone.utc
    )
    given_end_time = datetime.datetime(
        2024, 7, 1, 11, 0, 0, tzinfo=datetime.timezone.utc
    )
    given_start_time_str = "2024-07-01T10:00:00+00:00"
    given_end_time_str = "2024-07-01T11:00:00+00:00"
    given_event_title = "Meeting"
    given_event_description = "Discuss project updates"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "content": {
                    "body": {
                        "text": given_text,
                        "type": "TEXT",
                    },
                    "buttons": [
                        {
                            "text": given_button_text,
                            "startTime": given_start_time_str,
                            "endTime": given_end_time_str,
                            "title": given_event_title,
                            "description": given_event_description,
                            "type": "ADD_CALENDAR_EVENT",
                        }
                    ],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiMessage(
                    channel=MessagesApiOutboundMessageChannel.SMS,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    content=MessagesApiMessageContent(
                        body=MessagesApiMessageTextBody(
                            type=MessagesApiMessageBodyType.TEXT, text=given_text
                        ),
                        buttons=[
                            MessagesApiMessageAddCalendarEventButton(
                                type=MessagesApiMessageButtonType.ADD_CALENDAR_EVENT,
                                text=given_button_text,
                                start_time=given_start_time,
                                end_time=given_end_time,
                                title=given_event_title,
                                description=given_event_description,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_image_messages(httpserver: HTTPServer, messages_api_client):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "SMS"
    given_sender = "447491163443"
    given_to = "111111111"
    given_image_url = "https://example.com/image.jpg"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "content": {
                    "body": {
                        "url": given_image_url,
                        "type": "IMAGE",
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiMessage(
                    channel=MessagesApiOutboundMessageChannel.SMS,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    content=MessagesApiMessageContent(
                        body=MessagesApiMessageImageBody(
                            type=MessagesApiMessageBodyType.IMAGE, url=given_image_url
                        )
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1
    message = actual_response.messages[0]
    assert message.message_id == given_message_id
    assert message.status.group_id == given_group_id


def test_validate_messages_api_message(httpserver: HTTPServer, messages_api_client):
    given_channel = "SMS"
    given_sender = "447491163443"
    given_to = "111111111"
    given_message_text = "May the Force be with you."
    given_description = "Request can be sent through '/messages' endpoint and should be accepted by our platform."
    given_action = "No action is required, but it is recommended to check and address any violations."
    given_property = "messages[0].metadata"
    given_violation = "Unknown property"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "content": {
                    "body": {
                        "text": given_message_text,
                        "type": "TEXT",
                    }
                },
            }
        ]
    }

    expected_response = {
        "description": given_description,
        "action": given_action,
        "skippableViolations": [
            {"property": given_property, "violation": given_violation}
        ],
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=validate_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiMessage(
                    channel=MessagesApiOutboundMessageChannel.SMS,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    content=MessagesApiMessageContent(
                        body=MessagesApiMessageTextBody(
                            type=MessagesApiMessageBodyType.TEXT,
                            text=given_message_text,
                        )
                    ),
                )
            )
        ]
    )

    actual_response: MessagesApiValidationOkResponse = (
        messages_api_client.validate_messages_api_message(messages_api_request=request)
    )

    assert actual_response.description == given_description
    assert actual_response.action == given_action
    assert actual_response.skippable_violations is not None
    assert len(actual_response.skippable_violations) == 1
    violation = actual_response.skippable_violations[0]
    assert violation.var_property == given_property
    assert violation.violation == given_violation


def test_send_template_message(httpserver: HTTPServer, messages_api_client):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "WHATSAPP"
    given_sender = "447860099299"
    given_to = "111111111"
    given_template_name = "registration_success"
    given_language = "en_GB"
    given_suffix = "search?q=007"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "template": {
                    "templateName": given_template_name,
                    "language": given_language,
                },
                "content": {
                    "body": {"type": "TEXT"},
                    "buttons": [{"suffix": given_suffix, "type": "OPEN_URL"}],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiTemplateMessage(
                    channel=MessagesApiOutboundTemplateChannel.WHATSAPP,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    template=MessagesApiTemplate(
                        template_name=given_template_name, language=given_language
                    ),
                    content=MessagesApiTemplateMessageContent(
                        body=MessagesApiTemplateTextBody(
                            type=MessagesApiTemplateBodyType.TEXT
                        ),
                        buttons=[
                            MessagesApiTemplateOpenUrlButton(
                                type=MessagesApiTemplateButtonType.OPEN_URL,
                                suffix=given_suffix,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1
    message = actual_response.messages[0]
    assert message.message_id == given_message_id
    assert message.status.group_id == given_group_id
    assert message.status.name == given_name


def test_send_template_message_with_quick_reply_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "WHATSAPP"
    given_sender = "447860099299"
    given_to = "111111111"
    given_template_name = "registration_success"
    given_language = "en_GB"
    given_postback_data = "postback_data_123"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "template": {
                    "templateName": given_template_name,
                    "language": given_language,
                },
                "content": {
                    "body": {"type": "TEXT"},
                    "buttons": [
                        {"postbackData": given_postback_data, "type": "QUICK_REPLY"}
                    ],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiTemplateMessage(
                    channel=MessagesApiOutboundTemplateChannel.WHATSAPP,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    template=MessagesApiTemplate(
                        template_name=given_template_name, language=given_language
                    ),
                    content=MessagesApiTemplateMessageContent(
                        body=MessagesApiTemplateTextBody(
                            type=MessagesApiTemplateBodyType.TEXT
                        ),
                        buttons=[
                            MessagesApiTemplateQuickReplyButton(
                                type=MessagesApiTemplateButtonType.QUICK_REPLY,
                                postback_data=given_postback_data,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_template_message_with_phone_number_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "WHATSAPP"
    given_sender = "447860099299"
    given_to = "111111111"
    given_template_name = "registration_success"
    given_language = "en_GB"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "template": {
                    "templateName": given_template_name,
                    "language": given_language,
                },
                "content": {
                    "body": {"type": "TEXT"},
                    "buttons": [{"type": "PHONE_NUMBER"}],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiTemplateMessage(
                    channel=MessagesApiOutboundTemplateChannel.WHATSAPP,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    template=MessagesApiTemplate(
                        template_name=given_template_name, language=given_language
                    ),
                    content=MessagesApiTemplateMessageContent(
                        body=MessagesApiTemplateTextBody(
                            type=MessagesApiTemplateBodyType.TEXT
                        ),
                        buttons=[
                            MessagesApiTemplatePhoneNumberButton(
                                type=MessagesApiTemplateButtonType.PHONE_NUMBER
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_template_message_with_copy_code_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "WHATSAPP"
    given_sender = "447860099299"
    given_to = "111111111"
    given_template_name = "registration_success"
    given_language = "en_GB"
    given_code = "code"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "template": {
                    "templateName": given_template_name,
                    "language": given_language,
                },
                "content": {
                    "body": {"type": "TEXT"},
                    "buttons": [{"code": given_code, "type": "COPY_CODE"}],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiTemplateMessage(
                    channel=MessagesApiOutboundTemplateChannel.WHATSAPP,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    template=MessagesApiTemplate(
                        template_name=given_template_name, language=given_language
                    ),
                    content=MessagesApiTemplateMessageContent(
                        body=MessagesApiTemplateTextBody(
                            type=MessagesApiTemplateBodyType.TEXT
                        ),
                        buttons=[
                            MessagesApiTemplateCopyCodeButton(
                                type=MessagesApiTemplateButtonType.COPY_CODE,
                                code=given_code,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_template_message_with_flow_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "WHATSAPP"
    given_sender = "447860099299"
    given_to = "111111111"
    given_template_name = "registration_success"
    given_language = "en_GB"
    given_token = "flow_token"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "template": {
                    "templateName": given_template_name,
                    "language": given_language,
                },
                "content": {
                    "body": {"type": "TEXT"},
                    "buttons": [{"token": given_token, "type": "FLOW"}],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiTemplateMessage(
                    channel=MessagesApiOutboundTemplateChannel.WHATSAPP,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    template=MessagesApiTemplate(
                        template_name=given_template_name, language=given_language
                    ),
                    content=MessagesApiTemplateMessageContent(
                        body=MessagesApiTemplateTextBody(
                            type=MessagesApiTemplateBodyType.TEXT
                        ),
                        buttons=[
                            MessagesApiTemplateFlowButton(
                                type=MessagesApiTemplateButtonType.FLOW,
                                token=given_token,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_template_message_with_catalog_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "WHATSAPP"
    given_sender = "447860099299"
    given_to = "111111111"
    given_template_name = "registration_success"
    given_language = "en_GB"
    given_product_id = "product_id"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "template": {
                    "templateName": given_template_name,
                    "language": given_language,
                },
                "content": {
                    "body": {"type": "TEXT"},
                    "buttons": [{"productId": given_product_id, "type": "CATALOG"}],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiTemplateMessage(
                    channel=MessagesApiOutboundTemplateChannel.WHATSAPP,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    template=MessagesApiTemplate(
                        template_name=given_template_name, language=given_language
                    ),
                    content=MessagesApiTemplateMessageContent(
                        body=MessagesApiTemplateTextBody(
                            type=MessagesApiTemplateBodyType.TEXT
                        ),
                        buttons=[
                            MessagesApiTemplateCatalogButton(
                                type=MessagesApiTemplateButtonType.CATALOG,
                                product_id=given_product_id,
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_template_message_with_multi_product_button(
    httpserver: HTTPServer, messages_api_client
):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "WHATSAPP"
    given_sender = "447860099299"
    given_to = "111111111"
    given_template_name = "registration_success"
    given_language = "en_GB"
    given_product_id = "product_id"
    given_product_id_2 = "product_id_2"
    given_title = "title"

    given_request = {
        "messages": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "template": {
                    "templateName": given_template_name,
                    "language": given_language,
                },
                "content": {
                    "body": {"type": "TEXT"},
                    "buttons": [
                        {
                            "sections": [
                                {
                                    "title": given_title,
                                    "productIds": [
                                        given_product_id,
                                        given_product_id_2,
                                    ],
                                }
                            ],
                            "type": "MULTI_PRODUCT",
                        }
                    ],
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
        endpoint=messages_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiRequest(
        messages=[
            MessagesApiRequestMessagesInner(
                MessagesApiTemplateMessage(
                    channel=MessagesApiOutboundTemplateChannel.WHATSAPP,
                    sender=given_sender,
                    destinations=[
                        MessagesApiMessageDestination(
                            MessagesApiToDestination(to=given_to)
                        )
                    ],
                    template=MessagesApiTemplate(
                        template_name=given_template_name, language=given_language
                    ),
                    content=MessagesApiTemplateMessageContent(
                        body=MessagesApiTemplateTextBody(
                            type=MessagesApiTemplateBodyType.TEXT
                        ),
                        buttons=[
                            MessagesApiTemplateMultiProductButton(
                                type=MessagesApiTemplateButtonType.MULTI_PRODUCT,
                                sections=[
                                    MessagesApiTemplateMultiProductButtonSection(
                                        title=given_title,
                                        product_ids=[
                                            given_product_id,
                                            given_product_id_2,
                                        ],
                                    )
                                ],
                            )
                        ],
                    ),
                )
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_message(
        messages_api_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1


def test_send_messages_event(httpserver: HTTPServer, messages_api_client):
    given_bulk_id = "1688025180464000013"
    given_message_id = "1688025180464000014"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "MESSAGE_ACCEPTED"
    given_description = "Message sent to next instance"
    given_destination = "48600700800"
    given_channel = "APPLE_MB"
    given_sender = "447491163443"
    given_to = "111111111"

    given_request = {
        "events": [
            {
                "channel": given_channel,
                "sender": given_sender,
                "destinations": [{"to": given_to}],
                "event": "TYPING_STARTED",
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
        endpoint=events_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
    )

    request = MessagesApiEventRequest(
        events=[
            MessagesApiOutboundTypingStartedEvent(
                event=MessagesApiOutboundEventType.TYPING_STARTED,
                channel=MessagesApiOutboundEventChannel.APPLE_MB,
                sender=given_sender,
                destinations=[MessagesApiToDestination(to=given_to)],
            )
        ]
    )

    actual_response: MessageResponse = messages_api_client.send_messages_api_events(
        messages_api_event_request=request
    )

    assert actual_response.bulk_id == given_bulk_id
    assert actual_response.messages is not None
    assert len(actual_response.messages) == 1
    message = actual_response.messages[0]
    assert message.message_id == given_message_id
    assert message.status.group_id == given_group_id
    assert message.status.name == given_name


# Webhook tests


def test_parse_delivery_reports():
    expected_event = "DELIVERY"
    expected_channel = "SMS"
    expected_sender = "string"
    expected_destination = "string"
    expected_sent_at = "string"
    expected_done_at = "string"
    expected_bulk_id = "bulk123"
    expected_message_id = "string"
    expected_callback_data = "string"
    expected_message_count = 0
    expected_group_id = 0
    expected_group_name = "string"
    expected_id = 0
    expected_name = "string"
    expected_description = "string"
    expected_error_group_id = 0
    expected_error_group_name = "OK"
    expected_error_id = 0
    expected_error_name = "string"
    expected_error_description = "string"
    expected_permanent = True
    expected_application_id = "string"
    expected_entity_id = "string"
    expected_mcc_mnc = 0

    json_payload = f"""{{
        "results": [
            {{
                "event": "{expected_event}",
                "channel": "{expected_channel}",
                "sender": "{expected_sender}",
                "destination": "{expected_destination}",
                "sentAt": "{expected_sent_at}",
                "doneAt": "{expected_done_at}",
                "bulkId": "{expected_bulk_id}",
                "messageId": "{expected_message_id}",
                "callbackData": "{expected_callback_data}",
                "messageCount": {expected_message_count},
                "status": {{
                    "groupId": {expected_group_id},
                    "groupName": "{expected_group_name}",
                    "id": {expected_id},
                    "name": "{expected_name}",
                    "description": "{expected_description}"
                }},
                "error": {{
                    "groupId": {expected_error_group_id},
                    "groupName": "{expected_error_group_name}",
                    "id": {expected_error_id},
                    "name": "{expected_error_name}",
                    "description": "{expected_error_description}",
                    "permanent": {str(expected_permanent).lower()}
                }},
                "platform": {{
                    "applicationId": "{expected_application_id}",
                    "entityId": "{expected_entity_id}"
                }},
                "mccMnc": {expected_mcc_mnc}
            }}
        ]
    }}"""

    dlr_report = MessagesApiDeliveryReport.from_json(json_payload)

    assert dlr_report.results is not None
    assert len(dlr_report.results) == 1
    dlr_event = dlr_report.results[0]
    assert dlr_event.event == expected_event
    assert dlr_event.channel == MessagesApiInboundDlrChannel.SMS
    assert dlr_event.sender == expected_sender
    assert dlr_event.destination == expected_destination
    assert dlr_event.sent_at == expected_sent_at
    assert dlr_event.done_at == expected_done_at
    assert dlr_event.message_id == expected_message_id
    assert dlr_event.callback_data == expected_callback_data
    assert dlr_event.message_count == expected_message_count
    assert dlr_event.status.group_id == expected_group_id
    assert dlr_event.status.group_name == expected_group_name
    assert dlr_event.status.id == expected_id
    assert dlr_event.status.name == expected_name
    assert dlr_event.status.description == expected_description
    assert dlr_event.error.group_id == expected_error_group_id
    assert dlr_event.error.group_name == expected_error_group_name
    assert dlr_event.error.id == expected_error_id
    assert dlr_event.error.name == expected_error_name
    assert dlr_event.error.description == expected_error_description
    assert dlr_event.error.permanent == expected_permanent
    assert dlr_event.platform.application_id == expected_application_id
    assert dlr_event.platform.entity_id == expected_entity_id
    assert dlr_event.mcc_mnc == expected_mcc_mnc


def test_parse_incoming_messages():
    expected_channel = "SMS"
    expected_sender = "48123234567"
    expected_destination = "48123098765"
    expected_text = "Text message 123"
    expected_clean_text = "Text message"
    expected_received_at = "2020-02-06T14:18:29.797+0000"
    expected_message_id = "ABEGVUGWh3gEAgo-sLTvmQCS5kwjhsy"
    expected_application_id = "my-application-id"
    expected_entity_id = "my-entity-id"
    expected_event = "MO"
    expected_message_count = 1

    json_payload = f"""{{
        "results": [
            {{
                "channel": "{expected_channel}",
                "sender": "{expected_sender}",
                "destination": "{expected_destination}",
                "content": [
                    {{
                        "text": "{expected_text}",
                        "cleanText": "{expected_clean_text}",
                        "type": "TEXT"
                    }}
                ],
                "receivedAt": "{expected_received_at}",
                "messageId": "{expected_message_id}",
                "messageCount": {expected_message_count},
                "platform": {{
                    "applicationId": "{expected_application_id}",
                    "entityId": "{expected_entity_id}"
                }},
                "event": "{expected_event}"
            }}
        ]
    }}"""

    incoming_message = MessagesApiIncomingMessage.from_json(json_payload)

    assert incoming_message.results is not None
    assert len(incoming_message.results) == 1
    webhook_event = incoming_message.results[0]
    assert isinstance(webhook_event, MessagesApiWebhookEvent)
    assert webhook_event.channel == MessagesApiInboundMoEventChannel.SMS
    assert webhook_event.sender == expected_sender
    assert webhook_event.destination == expected_destination
    assert webhook_event.content is not None
    assert len(webhook_event.content) == 1
    content = webhook_event.content[0]
    assert isinstance(content, MessagesApiWebhookEventTextContent)
    assert content.text == expected_text
    assert content.clean_text == expected_clean_text
    assert webhook_event.message_id == expected_message_id
    assert webhook_event.platform.application_id == expected_application_id
    assert webhook_event.platform.entity_id == expected_entity_id
    assert webhook_event.event == MessagesApiInboundEventType.MO


def setup_post_request_ok(
    httpserver: HTTPServer,
    endpoint: str,
    expected_request: dict = None,
    expected_response: dict = None,
):
    httpserver.expect_request(
        uri=endpoint, method="POST", json=expected_request
    ).respond_with_json(expected_response)


@pytest.fixture
def messages_api_client():
    configuration = Configuration(host="http://localhost:8088")
    configuration.api_key["APIKeyHeader"] = "GivenApiKey"
    configuration.api_key_prefix["APIKeyHeader"] = "App"
    return MessagesApi(ApiClient(configuration))


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", 8088
