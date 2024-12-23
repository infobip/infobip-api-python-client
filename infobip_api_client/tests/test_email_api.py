import datetime
import os
import pathlib
import pytest
from pathlib import Path
from pytest_httpserver import HTTPServer

from infobip_api_client import (
    ApiClient,
    Configuration,
    EmailApi,
    EmailDomainIpRequest,
    EmailDomainIpResponse,
    EmailDomainIp,
    EmailSimpleApiResponse,
    EmailAddDomainRequest,
    EmailDomainResponse,
    EmailTrackingResponse,
    EmailDnsRecordResponse,
    EmailAllDomainsResponse,
    EmailPaging,
    EmailValidationRequest,
    EmailValidationResponse,
    EmailBulkRescheduleResponse,
    EmailBulkScheduleResponse,
    EmailBulkInfo,
    EmailBulkStatusResponse,
    EmailBulkStatusInfo,
    EmailBulkStatus,
    EmailBulkRescheduleRequest,
    EmailBulkUpdateStatusRequest,
    EmailBulkUpdateStatusResponse,
    EmailReportsResult,
    EmailReport,
    MessageStatus,
    MessagePrice,
    MessageError,
    EmailReturnPathAddressRequest,
    EmailGetSuppressionType,
    EmailSuppressionInfoPageResponse,
    EmailSuppressionInfo,
    EmailPageDetails,
    EmailAddDeleteSuppressionType,
    EmailAddSuppressionRequest,
    EmailAddSuppression,
    EmailDeleteSuppressionRequest,
    EmailDeleteSuppression,
    EmailDomainAccess,
    EmailDomainInfoPageResponse,
    EmailDomainInfo,
)

DOMAIN_IPS = "/email/1/domain-ips"
DOMAINS = "/email/1/domains"
DOMAIN = "/email/1/domains/{domainName}"
DOMAIN_VERIFY = "/email/1/domains/{domainName}/verify"
IPS = "/email/1/ips"
VALIDATION = "/email/2/validation"
BULKS = "/email/1/bulks"
BULKS_STATUS = "/email/1/bulks/status"
EMAIL_SEND = "/email/3/send"
REPORTS = "/email/1/reports"
RETURN_PATH = "/email/1/domains/{domainName}/return-path"
EMAIL_SUPPRESSION = "/email/1/suppressions"
EMAIL_SUPPRESSION_DOMAINS = "/email/1/suppressions/domains"

TEMP_FILE_PATH = Path(os.path.dirname(__file__)) / "temp"


def test_should_get_all_domain_ips(httpserver: HTTPServer, get_api_client):
    given_domain_name = "example.com"
    given_ip_address = "11.11.11.1"
    given_dedicated = True
    given_assigned_domain_count = 1
    given_status = "ASSIGNABLE"

    given_response = {
        "result": [
            {
                "ipAddress": given_ip_address,
                "dedicated": given_dedicated,
                "assignedDomainCount": given_assigned_domain_count,
                "status": given_status,
            }
        ]
    }

    setup_request(httpserver, DOMAIN_IPS, given_response)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.get_all_domain_ips(given_domain_name)

    expected_response = EmailDomainIpResponse(
        result=[
            EmailDomainIp(
                ip_address=given_ip_address,
                dedicated=given_dedicated,
                assigned_domain_count=given_assigned_domain_count,
                status=given_status,
            )
        ]
    )

    assert api_response == expected_response


def test_should_assign_ip_to_domain(httpserver: HTTPServer, get_api_client):
    given_result = "OK"
    given_domain_name = "example.com"
    given_ip_address = "11.11.11.1"

    given_response = {"result": given_result}

    expected_request = {"domainName": given_domain_name, "ipAddress": given_ip_address}

    setup_request(
        httpserver, DOMAIN_IPS, given_response, "POST", request_body=expected_request
    )

    api_instance = EmailApi(get_api_client)
    request = EmailDomainIpRequest(
        domain_name=given_domain_name, ip_address=given_ip_address
    )
    api_response = api_instance.assign_ip_to_domain(request)

    expected_response = EmailSimpleApiResponse(result=given_result)

    assert api_response == expected_response


def test_should_remove_ip_from_domain(httpserver: HTTPServer, get_api_client):
    given_result = "OK"
    given_domain_name = "example.com"
    given_ip_address = "11.11.11.1"

    given_response = {"result": given_result}

    setup_request(httpserver, DOMAIN_IPS, given_response, "DELETE")

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.remove_ip_from_domain(
        given_domain_name, given_ip_address
    )

    expected_response = EmailSimpleApiResponse(result=given_result)

    assert api_response == expected_response


def test_should_add_domain(httpserver: HTTPServer, get_api_client):
    given_domain_name = "example.com"
    given_dkim_key_length = 1024
    given_domain_id = 1
    given_active = False
    given_tracking = True
    given_dns_records = "string"
    given_verified = True
    given_blocked = False
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
    given_return_path_address = "pathAddress"
    given_target_daily_traffic = 10000

    given_response = {
        "domainId": given_domain_id,
        "domainName": given_domain_name,
        "active": given_active,
        "tracking": {
            "clicks": given_tracking,
            "opens": given_tracking,
            "unsubscribe": given_tracking,
        },
        "dnsRecords": [
            {
                "recordType": given_dns_records,
                "name": given_dns_records,
                "expectedValue": given_dns_records,
                "verified": given_verified,
            }
        ],
        "blocked": given_blocked,
        "createdAt": given_created_at,
        "returnPathAddress": given_return_path_address,
    }

    expected_request = {
        "domainName": given_domain_name,
        "dkimKeyLength": given_dkim_key_length,
        "returnPathAddress": given_return_path_address,
        "targetedDailyTraffic": given_target_daily_traffic,
    }

    setup_request(
        httpserver, DOMAINS, given_response, "POST", request_body=expected_request
    )

    api_instance = EmailApi(get_api_client)
    request = EmailAddDomainRequest(
        domain_name=given_domain_name,
        dkim_key_length=given_dkim_key_length,
        return_path_address=given_return_path_address,
        targeted_daily_traffic=given_target_daily_traffic,
    )
    api_response = api_instance.add_domain(request)

    expected_response = EmailDomainResponse(
        domain_id=given_domain_id,
        domain_name=given_domain_name,
        active=given_active,
        tracking=EmailTrackingResponse(
            clicks=given_tracking, opens=given_tracking, unsubscribe=given_tracking
        ),
        dns_records=[
            EmailDnsRecordResponse(
                record_type=given_dns_records,
                name=given_dns_records,
                expected_value=given_dns_records,
                verified=given_verified,
            )
        ],
        blocked=given_blocked,
        created_at=given_created_at_datetime,
        return_path_address=given_return_path_address,
    )

    assert api_response == expected_response


def test_should_get_all_domains(httpserver: HTTPServer, get_api_client):
    given_domain_name = "example.com"
    given_paging = 0
    given_domain_id = 1
    given_active = False
    given_tracking = True
    given_dns_records = "string"
    given_verified = True
    given_blocked = False
    given_created_at = "2022-05-05T17:32:28.777+01:00"
    given_created_at_offset = datetime.datetime(
        2022,
        5,
        5,
        17,
        32,
        28,
        777000,
        tzinfo=datetime.timezone(datetime.timedelta(hours=1, minutes=0)),
    )

    given_response = {
        "paging": {
            "page": given_paging,
            "size": given_paging,
            "totalPages": given_paging,
            "totalResults": given_paging,
        },
        "results": [
            {
                "domainId": given_domain_id,
                "domainName": given_domain_name,
                "active": given_active,
                "tracking": {
                    "clicks": given_tracking,
                    "opens": given_tracking,
                    "unsubscribe": given_tracking,
                },
                "dnsRecords": [
                    {
                        "recordType": given_dns_records,
                        "name": given_dns_records,
                        "expectedValue": given_dns_records,
                        "verified": given_verified,
                    }
                ],
                "blocked": given_blocked,
                "createdAt": given_created_at,
            }
        ],
    }

    setup_request(httpserver, DOMAINS, given_response)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.get_all_domains()

    expected_response = EmailAllDomainsResponse(
        results=[
            EmailDomainResponse(
                domain_id=given_domain_id,
                domain_name=given_domain_name,
                active=given_active,
                tracking=EmailTrackingResponse(
                    clicks=given_tracking,
                    opens=given_tracking,
                    unsubscribe=given_tracking,
                ),
                dns_records=[
                    EmailDnsRecordResponse(
                        record_type=given_dns_records,
                        name=given_dns_records,
                        expected_value=given_dns_records,
                        verified=given_verified,
                    )
                ],
                blocked=given_blocked,
                created_at=given_created_at_offset,
            )
        ],
        paging=EmailPaging(
            page=given_paging,
            size=given_paging,
            total_pages=given_paging,
            total_results=given_paging,
        ),
    )

    assert api_response == expected_response


def test_should_get_domain_details(httpserver: HTTPServer, get_api_client):
    given_domain_name = "example.com"
    given_domain_id = 1
    given_active = False
    given_tracking = True
    given_dns_records = "string"
    given_verified = True
    given_blocked = False
    given_created_at = "2022-05-05T17:32:28.777+01:00"
    given_created_at_offset = datetime.datetime(
        2022,
        5,
        5,
        17,
        32,
        28,
        777000,
        tzinfo=datetime.timezone(datetime.timedelta(hours=1, minutes=0)),
    )

    given_response = {
        "domainId": given_domain_id,
        "domainName": given_domain_name,
        "active": given_active,
        "tracking": {
            "clicks": given_tracking,
            "opens": given_tracking,
            "unsubscribe": given_tracking,
        },
        "dnsRecords": [
            {
                "recordType": given_dns_records,
                "name": given_dns_records,
                "expectedValue": given_dns_records,
                "verified": given_verified,
            }
        ],
        "blocked": given_blocked,
        "createdAt": given_created_at,
    }

    setup_request(
        httpserver, DOMAIN.replace("{domainName}", given_domain_name), given_response
    )

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.get_domain_details(given_domain_name)

    expected_response = EmailDomainResponse(
        domain_id=given_domain_id,
        domain_name=given_domain_name,
        active=given_active,
        tracking=EmailTrackingResponse(
            clicks=given_tracking, opens=given_tracking, unsubscribe=given_tracking
        ),
        dns_records=[
            EmailDnsRecordResponse(
                record_type=given_dns_records,
                name=given_dns_records,
                expected_value=given_dns_records,
                verified=given_verified,
            )
        ],
        blocked=given_blocked,
        created_at=given_created_at_offset,
    )

    assert api_response == expected_response


def test_should_verify_domain(httpserver: HTTPServer, get_api_client):
    given_domain_name = "example.com"
    given_status_code = 202

    setup_request(
        httpserver,
        DOMAIN_VERIFY.replace("{domainName}", given_domain_name),
        None,
        "POST",
        status_code=given_status_code,
    )

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.verify_domain(given_domain_name)

    assert api_response == None


def test_should_get_all_ips(httpserver: HTTPServer, get_api_client):
    given_ip_address = "11.11.11.1"
    given_dedicated = True
    given_assigned_domain_count = 1
    given_status = "ASSIGNABLE"

    given_response = {
        "result": [
            {
                "ipAddress": given_ip_address,
                "dedicated": given_dedicated,
                "assignedDomainCount": given_assigned_domain_count,
                "status": given_status,
            }
        ]
    }

    setup_request(httpserver, IPS, given_response)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.get_all_ips()

    expected_response = EmailDomainIpResponse(
        result=[
            EmailDomainIp(
                ip_address=given_ip_address,
                dedicated=given_dedicated,
                assigned_domain_count=given_assigned_domain_count,
                status=given_status,
            )
        ]
    )

    assert api_response == expected_response


def test_should_validate_email(httpserver: HTTPServer, get_api_client):
    given_to = "john.smith@example.com"
    given_valid_syntax = True
    given_did_you_mean = None

    expected_request = {"to": given_to}

    given_response = {
        "to": given_to,
        "validMailbox": "true",
        "validSyntax": given_valid_syntax,
        "catchAll": False,
        "didYouMean": given_did_you_mean,
        "disposable": False,
        "roleBased": True,
    }

    setup_request(
        httpserver, VALIDATION, given_response, "POST", request_body=expected_request
    )

    api_instance = EmailApi(get_api_client)
    request = EmailValidationRequest(to=given_to)
    api_response = api_instance.validate_email_addresses(request)

    expected_response = EmailValidationResponse(
        to=given_to,
        valid_syntax=given_valid_syntax,
        did_you_mean=given_did_you_mean,
        valid_mailbox="true",
        catch_all=False,
        disposable=False,
        role_based=True,
    )

    assert api_response == expected_response


def test_should_get_scheduled_emails(httpserver: HTTPServer, get_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_external_bulk_id = "SOME_USER_DEFINE_BULK_123"

    given_response = {
        "externalBulkId": given_external_bulk_id,
        "bulks": [{"bulkId": given_bulk_id, "sendAt": "2021-08-25T16:00:00.000+0000"}],
    }

    setup_request(httpserver, BULKS, given_response, "GET")

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.get_scheduled_emails(given_external_bulk_id)

    expected_response = EmailBulkScheduleResponse(
        external_bulk_id=given_external_bulk_id,
        bulks=[
            EmailBulkInfo(
                bulk_id=given_bulk_id,
                send_at=datetime.datetime(
                    2021, 8, 25, 16, 0, 0, 0, tzinfo=datetime.timezone.utc
                ),
            )
        ],
    )

    assert api_response == expected_response


def test_should_get_scheduled_emails_statuses(httpserver: HTTPServer, get_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_external_bulk_id = "SOME_USER_DEFINE_BULK_123"
    given_status = EmailBulkStatus.PENDING

    given_response = {
        "externalBulkId": given_external_bulk_id,
        "bulks": [{"bulkId": given_bulk_id, "status": given_status}],
    }

    setup_request(httpserver, BULKS_STATUS, given_response, "GET")

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.get_scheduled_email_statuses(given_external_bulk_id)

    expected_response = EmailBulkStatusResponse(
        external_bulk_id=given_external_bulk_id,
        bulks=[EmailBulkStatusInfo(bulk_id=given_bulk_id, status=given_status)],
    )

    assert api_response == expected_response


def test_should_reschedule_emails(httpserver: HTTPServer, get_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_send_at = "2023-08-01T16:10:00+05:30"
    given_send_at_datetime = datetime.datetime(
        2023,
        8,
        1,
        16,
        10,
        0,
        tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)),
    )
    given_request = {"sendAt": given_send_at}

    given_response = {"bulkId": given_bulk_id, "sendAt": given_send_at}

    setup_request(httpserver, BULKS, given_response, "PUT", request_body=given_request)

    api_instance = EmailApi(get_api_client)
    request = EmailBulkRescheduleRequest(send_at=given_send_at_datetime)
    api_response = api_instance.reschedule_emails(given_bulk_id, request)

    expected_response = EmailBulkRescheduleResponse(
        bulk_id=given_bulk_id, send_at=given_send_at_datetime
    )

    assert api_response == expected_response


def test_should_update_scheduled_email_statuses(httpserver: HTTPServer, get_api_client):
    given_bulk_id = "string"
    given_status = EmailBulkStatus.PENDING

    given_response = {"bulkId": given_bulk_id, "status": given_status}
    expected_request = {"status": given_status}

    setup_request(
        httpserver, BULKS_STATUS, given_response, "PUT", request_body=expected_request
    )

    api_instance = EmailApi(get_api_client)
    request = EmailBulkUpdateStatusRequest(status=given_status)
    api_response = api_instance.update_scheduled_email_statuses(given_bulk_id, request)

    expected_response = EmailBulkUpdateStatusResponse(
        bulk_id=given_bulk_id, status=given_status
    )

    assert api_response == expected_response


def test_should_send_fully_featured_email(httpserver: HTTPServer, get_api_client):
    given_to = "john.smith@example.com"
    given_another_to = "alice.grey@example.com"
    given_bulk_id = "snxemd8u52v7v84iiu69"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 1
    given_name = "PENDING_ACCEPTED"
    given_description = "Message accepted, pending for delivery."
    given_attachment_text = "Test file text"
    given_message_id = "somExternalMessageId0"
    given_another_message_id = "someExternalMessageId1"
    given_from = "Jane Smith <jane.smith@example.com>"
    given_reply_to = "all.replies@example.com"
    given_subject = "Mail subject text"
    given_text = "Mail body text"
    given_html = "<h1>Html body</h1><p>Rich HTML message body.</p>"
    intermediate_report = True
    given_notify_url = "https://www.example.com/email/advanced"
    given_notify_content_type = "application/json"
    given_callback_data = "DLR callback data"

    given_response = {
        "bulkId": given_bulk_id,
        "messages": [
            {
                "to": given_to,
                "messageId": given_message_id,
                "status": {
                    "groupId": given_group_id,
                    "groupName": given_group_name,
                    "id": given_id,
                    "name": given_name,
                    "description": given_description,
                },
            },
            {
                "to": given_another_to,
                "messageId": given_another_message_id,
                "status": {
                    "groupId": given_group_id,
                    "groupName": given_group_name,
                    "id": given_id,
                    "name": given_name,
                    "description": given_description,
                },
            },
        ],
    }

    setup_multipart_request(httpserver, EMAIL_SEND, given_response, 200)

    temp_path = Path(TEMP_FILE_PATH)
    temp_path.mkdir(parents=True, exist_ok=True)
    attachment_file_path = create_temp_file_with_content(temp_path, "attachment.txt", given_attachment_text)

    try:
        api_instance = EmailApi(get_api_client)
        api_response = api_instance.send_email(
            to=[given_to, given_another_to],
            var_from=given_from,
            subject=given_subject,
            reply_to=given_reply_to,
            html=given_html,
            text=given_text,
            attachment=[read_temp_file(attachment_file_path)],
            intermediate_report=intermediate_report,
            notify_url=given_notify_url,
            notify_content_type=given_notify_content_type,
            callback_data=given_callback_data,
        )
    finally:
        attachment_file_path.unlink()
        temp_path.rmdir()

    assert api_response.bulk_id == given_bulk_id


def test_should_get_email_delivery_reports(httpserver: HTTPServer, get_api_client):
    given_sent_at = "2022-05-05T17:32:28.777+01:00"
    given_sent_at_offset = datetime.datetime(
        2022,
        5,
        5,
        17,
        32,
        28,
        777000,
        tzinfo=datetime.timezone(datetime.timedelta(hours=1, minutes=0)),
    )

    given_done_at = "2022-05-05T17:32:28.777+01:00"
    given_done_at_offset = datetime.datetime(
        2022,
        5,
        5,
        17,
        32,
        28,
        777000,
        tzinfo=datetime.timezone(datetime.timedelta(hours=1, minutes=0)),
    )

    given_bulk_id = "csdstgteet4fath2pclbq"
    given_message_id = "45653761-3a88-4060-869e-ae372adc7a51"
    given_to = "john.doe@example.com"

    given_response = {
        "results": [
            {
                "bulkId": given_bulk_id,
                "messageId": given_message_id,
                "to": given_to,
                "sentAt": given_sent_at,
                "doneAt": given_done_at,
                "messageCount": 1,
                "price": {"pricePerMessage": 0, "currency": "UNKNOWN"},
                "status": {
                    "groupId": 3,
                    "groupName": "DELIVERED",
                    "id": 5,
                    "name": "DELIVERED_TO_HANDSET",
                    "description": "Message delivered to handset",
                },
                "error": {
                    "groupId": 0,
                    "groupName": "OK",
                    "id": 0,
                    "name": "NO_ERROR",
                    "description": "No Error",
                    "permanent": False,
                },
            }
        ]
    }

    setup_request(httpserver, REPORTS, given_response, "GET")

    api_instance = EmailApi(get_api_client)

    api_response = api_instance.get_email_delivery_reports(
        bulk_id=given_bulk_id, message_id=given_message_id, limit=1
    )

    expected_response = EmailReportsResult(
        results=[
            EmailReport(
                bulk_id=given_bulk_id,
                message_id=given_message_id,
                to=given_to,
                sent_at=given_sent_at_offset,
                done_at=given_done_at_offset,
                message_count=1,
                price=MessagePrice(price_per_message=0, currency="UNKNOWN"),
                status=MessageStatus(
                    group_id=3,
                    group_name="DELIVERED",
                    id=5,
                    name="DELIVERED_TO_HANDSET",
                    description="Message delivered to handset",
                ),
                error=MessageError(
                    group_id=0,
                    group_name="OK",
                    id=0,
                    name="NO_ERROR",
                    description="No Error",
                    permanent=False,
                ),
            )
        ]
    )

    assert api_response == expected_response


def test_should_update_return_path(httpserver: HTTPServer, get_api_client):
    given_domain_id = 1
    given_domain_name = "example.com"
    given_active = False
    given_tracking = True
    given_opens = True
    given_unsubscribe = True
    given_record_type = "string"
    given_name = "string"
    given_expected_value = "string"
    given_verified = True
    given_blocked = False
    given_created_at = "2022-05-05T17:32:28.777+01:00"
    given_created_at_offset = datetime.datetime(
        2022,
        5,
        5,
        17,
        32,
        28,
        777000,
        tzinfo=datetime.timezone(datetime.timedelta(hours=1, minutes=0)),
    )
    given_return_path_address = "returnpath@example.com"

    given_response = {
        "domainId": given_domain_id,
        "domainName": given_domain_name,
        "active": given_active,
        "tracking": {
            "clicks": given_tracking,
            "opens": given_opens,
            "unsubscribe": given_unsubscribe,
        },
        "dnsRecords": [
            {
                "recordType": given_record_type,
                "name": given_name,
                "expectedValue": given_expected_value,
                "verified": given_verified,
            }
        ],
        "blocked": given_blocked,
        "createdAt": given_created_at,
        "returnPathAddress": given_return_path_address,
    }

    expected_request = {"returnPathAddress": given_return_path_address}

    setup_request(
        httpserver,
        RETURN_PATH.replace("{domainName}", given_domain_name),
        given_response,
        "PUT",
        request_body=expected_request,
    )

    api_instance = EmailApi(get_api_client)
    request = EmailReturnPathAddressRequest(
        return_path_address=given_return_path_address
    )
    api_response = api_instance.update_return_path(given_domain_name, request)

    expected_response = EmailDomainResponse(
        domain_id=given_domain_id,
        domain_name=given_domain_name,
        active=given_active,
        tracking=EmailTrackingResponse(
            clicks=given_tracking, opens=given_opens, unsubscribe=given_unsubscribe
        ),
        dns_records=[
            EmailDnsRecordResponse(
                record_type=given_record_type,
                name=given_name,
                expected_value=given_expected_value,
                verified=given_verified,
            )
        ],
        blocked=given_blocked,
        created_at=given_created_at_offset,
        return_path_address=given_return_path_address,
    )

    assert api_response == expected_response


def test_should_get_email_suppressions(httpserver: HTTPServer, get_api_client):
    given_domain_name = "example.com"
    given_email_address = "jane.smith@example.com"
    given_type = EmailGetSuppressionType.BOUNCE
    given_created_date = "2024-08-14T14:02:17.366"
    given_reason = "550 5.1.1 <jane.smith@example.com>: user does not exist"
    given_page = 0
    given_size = 100

    given_response = {
        "results": [
            {
                "domainName": given_domain_name,
                "emailAddress": given_email_address,
                "type": given_type.value,
                "createdDate": given_created_date,
                "reason": given_reason,
            }
        ],
        "paging": {"page": given_page, "size": given_size},
    }

    setup_request(httpserver, EMAIL_SUPPRESSION, given_response)

    api_instance = EmailApi(get_api_client)
    response = api_instance.get_suppressions(given_domain_name, given_type)

    expected_response = EmailSuppressionInfoPageResponse(
        results=[
            EmailSuppressionInfo(
                domain_name=given_domain_name,
                email_address=given_email_address,
                type=given_type,
                created_date=given_created_date,
                reason=given_reason,
            )
        ],
        paging=EmailPageDetails(page=given_page, size=given_size),
    )

    assert response == expected_response


def test_should_add_email_suppressions(httpserver: HTTPServer, get_api_client):
    given_domain_name1 = "example.com"
    given_email_addresses1 = ["jane.smith@example.com", "john.doe@example.com"]
    given_type = EmailAddDeleteSuppressionType.BOUNCE

    given_domain_name2 = "example.com"
    given_email_addresses2 = ["john.smith@example.com", "john.perry@example.com"]

    expected_request = {
        "suppressions": [
            {
                "domainName": given_domain_name1,
                "emailAddress": given_email_addresses1,
                "type": given_type.value,
            },
            {
                "domainName": given_domain_name2,
                "emailAddress": given_email_addresses2,
                "type": given_type.value,
            },
        ]
    }

    setup_request(
        httpserver, EMAIL_SUPPRESSION, None, "POST", 204, request_body=expected_request
    )

    api_instance = EmailApi(get_api_client)
    request = EmailAddSuppressionRequest(
        suppressions=[
            EmailAddSuppression(
                domain_name=given_domain_name1,
                email_address=given_email_addresses1,
                type=given_type,
            ),
            EmailAddSuppression(
                domain_name=given_domain_name2,
                email_address=given_email_addresses2,
                type=given_type,
            ),
        ]
    )
    response = api_instance.add_suppressions(request)
    assert response is None


def test_should_delete_email_suppressions(httpserver: HTTPServer, get_api_client):
    given_domain_name1 = "example.com"
    given_email_addresses1 = ["jane.smith@example.com", "john.doe@xample.com"]
    given_type = EmailAddDeleteSuppressionType.BOUNCE

    given_domain_name2 = "example.com"
    given_email_addresses2 = ["john.smith@example.com", "john.perry@example.com"]

    expected_request = {
        "suppressions": [
            {
                "domainName": given_domain_name1,
                "emailAddress": given_email_addresses1,
                "type": given_type.value,
            },
            {
                "domainName": given_domain_name2,
                "emailAddress": given_email_addresses2,
                "type": given_type.value,
            },
        ]
    }

    setup_request(
        httpserver,
        EMAIL_SUPPRESSION,
        None,
        "DELETE",
        204,
        request_body=expected_request,
    )

    api_instance = EmailApi(get_api_client)
    request = EmailDeleteSuppressionRequest(
        suppressions=[
            EmailDeleteSuppression(
                domain_name=given_domain_name1,
                email_address=given_email_addresses1,
                type=given_type,
            ),
            EmailDeleteSuppression(
                domain_name=given_domain_name2,
                email_address=given_email_addresses2,
                type=given_type,
            ),
        ]
    )

    response = api_instance.delete_suppressions(request)
    assert response is None


def test_should_get_suppression_domains(httpserver: HTTPServer, get_api_client):
    given_domain_name1 = "example.com"
    given_data_access1 = EmailDomainAccess.OWNER
    given_read_bounces1 = True
    given_create_bounces1 = True
    given_delete_bounces1 = True
    given_read_complaints1 = True
    given_create_complaints1 = True
    given_delete_complaints1 = True
    given_read_overquotas1 = True

    given_domain_name2 = "example.com"
    given_data_access2 = EmailDomainAccess.GRANTED
    given_read_bounces2 = True
    given_create_bounces2 = True
    given_delete_bounces2 = False
    given_read_complaints2 = True
    given_create_complaints2 = False
    given_delete_complaints2 = False
    given_read_overquotas2 = False

    given_page = 0
    given_size = 100

    given_response = {
        "results": [
            {
                "domainName": given_domain_name1,
                "dataAccess": given_data_access1.value,
                "readBounces": given_read_bounces1,
                "createBounces": given_create_bounces1,
                "deleteBounces": given_delete_bounces1,
                "readComplaints": given_read_complaints1,
                "createComplaints": given_create_complaints1,
                "deleteComplaints": given_delete_complaints1,
                "readOverquotas": given_read_overquotas1,
            },
            {
                "domainName": given_domain_name2,
                "dataAccess": given_data_access2.value,
                "readBounces": given_read_bounces2,
                "createBounces": given_create_bounces2,
                "deleteBounces": given_delete_bounces2,
                "readComplaints": given_read_complaints2,
                "createComplaints": given_create_complaints2,
                "deleteComplaints": given_delete_complaints2,
                "readOverquotas": given_read_overquotas2,
            },
        ],
        "paging": {"page": given_page, "size": given_size},
    }

    setup_request(httpserver, EMAIL_SUPPRESSION_DOMAINS, given_response)

    api_instance = EmailApi(get_api_client)
    response = api_instance.get_domains()

    expected_response = EmailDomainInfoPageResponse(
        results=[
            EmailDomainInfo(
                domain_name=given_domain_name1,
                data_access=given_data_access1,
                read_bounces=given_read_bounces1,
                create_bounces=given_create_bounces1,
                delete_bounces=given_delete_bounces1,
                read_complaints=given_read_complaints1,
                create_complaints=given_create_complaints1,
                delete_complaints=given_delete_complaints1,
                read_overquotas=given_read_overquotas1,
            ),
            EmailDomainInfo(
                domain_name=given_domain_name2,
                data_access=given_data_access2,
                read_bounces=given_read_bounces2,
                create_bounces=given_create_bounces2,
                delete_bounces=given_delete_bounces2,
                read_complaints=given_read_complaints2,
                create_complaints=given_create_complaints2,
                delete_complaints=given_delete_complaints2,
                read_overquotas=given_read_overquotas2,
            ),
        ],
        paging=EmailPageDetails(page=given_page, size=given_size),
    )

    assert response == expected_response


def setup_multipart_request(
        httpserver, endpoint: str, expected_response=None, status_code: int = 200
):
    httpserver.expect_request(uri=endpoint, method="POST").respond_with_json(
        expected_response, status=status_code
    )


def create_temp_file_with_content(temp_path: Path, filename: str, content: str):
    temp_file_path = temp_path / filename
    with open(temp_file_path, "w") as temp_file:
        temp_file.write(content)
    return temp_file_path


def read_temp_file(temp_file_path: str):
    with open(temp_file_path, "rb") as temp_file:
        return temp_file.read()


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
