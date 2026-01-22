import datetime

import pytest
from pytest_httpserver import HTTPServer
from infobip_api_client import (
    ApiClient,
    Configuration,
    EmailApi,
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
    MessageError,
    EmailSuppressionInfoPageResponse,
    EmailSuppressionInfo,
    EmailPageDetails,
    EmailAddSuppressionRequest,
    EmailAddSuppression,
    EmailDeleteSuppressionRequest,
    EmailDeleteSuppression,
    EmailDomainAccess,
    EmailDomainInfoPageResponse,
    EmailDomainInfo,
    EmailAddSuppressionType,
    EmailSuppressionType,
    EmailIpResponse,
    EmailIpDetailResponse,
    EmailIpPoolResponse,
    EmailIpPoolDetailResponse,
    EmailIpPoolAssignIpApiRequest,
    EmailIpDomainResponse,
    EmailDomainIpApiPool,
    EmailDomainIpPoolAssignApiRequest,
    EmailSendMimeRequestSchema,
    EmailSendResponse,
    EmailResponseDetails,
    EmailTemplateListPage,
    EmailTemplateListItem,
    EmailTemplate,
    EmailAttachment,
    PageInfo,
    EmailRequest,
    EmailMessage,
    EmailMessageContent,
    EmailGroupDestination,
    EmailToDestination,
    EmailResponse,
    EmailMessageResponseMessageResponseDetails,
    EmailMessageStatus,
    EmailMessageGeneralStatus,
    EmailValidationApiRisk,
    EmailMessagePrice,
    Platform,
)

DOMAINS = "/email/1/domains"
DOMAIN = "/email/1/domains/{domainName}"
DOMAIN_VERIFY = "/email/1/domains/{domainName}/verify"

VALIDATION = "/email/2/validation"
BULKS = "/email/1/bulks"
BULKS_STATUS = "/email/1/bulks/status"
EMAIL_SEND = "/email/3/send"
EMAIL_MESSAGES = "/email/4/messages"
REPORTS = "/email/4/reports"
RETURN_PATH = "/email/1/domains/{domainName}/return-path"
EMAIL_SUPPRESSION = "/email/1/suppressions"
EMAIL_SUPPRESSION_DOMAINS = "/email/1/suppressions/domains"

EMAIL_IPS = "/email/1/ip-management/ips"
EMAIL_IP = "/email/1/ip-management/ips/{ipId}"
EMAIL_IP_POOLS = "/email/1/ip-management/pools"
EMAIL_IP_POOL = "/email/1/ip-management/pools/{poolId}"
EMAIL_ASSIGN_IP_POOL = "/email/1/ip-management/pools/{poolId}/ips"
EMAIL_IP_DOMAIN = "/email/1/ip-management/domains/{domainId}"
EMAIL_ASSIGN_IP_DOMAIN_POOL = "/email/1/ip-management/domains/{domainId}/pools"
EMAIL_SEND_MIME = "/email/4/mime"
EMAIL_TEMPLATES = "/email/1/templates"
EMAIL_TEMPLATE = "/email/1/templates/{templateId}"
EMAIL_TEMPLATE_PREVIEW = "/email/1/templates/{templateId}/preview"
EMAIL_TEMPLATE_ATTACHMENTS = "/email/1/templates/{templateId}/attachments"
EMAIL_TEMPLATE_ATTACHMENT = "/email/1/templates/{templateId}/attachments/{attachmentId}"


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
    }

    expected_request = {
        "domainName": given_domain_name,
        "dkimKeyLength": given_dkim_key_length,
        "targetedDailyTraffic": given_target_daily_traffic,
    }

    setup_request(
        httpserver, DOMAINS, given_response, "POST", request_body=expected_request
    )

    api_instance = EmailApi(get_api_client)
    request = EmailAddDomainRequest(
        domain_name=given_domain_name,
        dkim_key_length=given_dkim_key_length,
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


def test_should_validate_email(httpserver: HTTPServer, get_api_client):
    given_to = "john.smith@abc.com"
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
        "risk": "LOW",
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
        risk=EmailValidationApiRisk.LOW,
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
    expected_request = {
        "messages": [
            {
                "sender": "jenny.smith@company.com",
                "destinations": [
                    {
                        "to": [
                            {
                                "destination": "john.smith@company.com",
                                "placeholders": '{"customer_name":"John Smith"}',
                            },
                            {
                                "destination": "mike.smith@company.com",
                                "placeholders": '{"customer_name":"Mike Smith"}',
                            },
                        ],
                        "preserveRecipients": False,
                    }
                ],
                "content": {
                    "templateId": "322307",
                    "defaultPlaceholders": '{"date":"20/03/2018","customer_name":"John Smith"}',
                    "templateLanguageVersion": "1",
                },
            }
        ]
    }

    given_response = {
        "bulkId": "a28dd97c-2222-4fcf-99f1-0b557ed381da",
        "messages": [
            {
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "status": {
                    "groupId": 1,
                    "groupName": "PENDING",
                    "id": 7,
                    "name": "PENDING_ENROUTE",
                    "description": "Message sent to next instance",
                },
                "destination": "john.smith@company.com",
            }
        ],
    }

    setup_request(
        httpserver, EMAIL_MESSAGES, given_response, "POST", 200, expected_request
    )

    api_instance = EmailApi(get_api_client)

    email_request = EmailRequest(
        messages=[
            EmailMessage(
                sender="jenny.smith@company.com",
                destinations=[
                    EmailGroupDestination(
                        to=[
                            EmailToDestination(
                                destination="john.smith@company.com",
                                placeholders='{"customer_name":"John Smith"}',
                            ),
                            EmailToDestination(
                                destination="mike.smith@company.com",
                                placeholders='{"customer_name":"Mike Smith"}',
                            ),
                        ]
                    )
                ],
                content=EmailMessageContent(
                    template_id="322307",
                    default_placeholders='{"date":"20/03/2018","customer_name":"John Smith"}',
                ),
            )
        ]
    )

    api_response = api_instance.send_email(email_request)

    expected_response = EmailResponse(
        bulk_id="a28dd97c-2222-4fcf-99f1-0b557ed381da",
        messages=[
            EmailMessageResponseMessageResponseDetails(
                destination="john.smith@company.com",
                message_id="a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                status=EmailMessageStatus(
                    group_id=1,
                    group_name=EmailMessageGeneralStatus.PENDING,
                    id=7,
                    name="PENDING_ENROUTE",
                    description="Message sent to next instance",
                ),
            ),
        ],
    )

    assert api_response == expected_response


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
    given_to = "john.doe@email.com"

    given_response = {
        "results": [
            {
                "bulkId": "string",
                "price": {"pricePerMessage": 0, "currency": "string"},
                "status": {
                    "groupId": 0,
                    "groupName": "ACCEPTED",
                    "id": 0,
                    "name": "string",
                    "description": "string",
                    "action": "string",
                },
                "error": {
                    "groupId": 0,
                    "groupName": "OK",
                    "id": 0,
                    "name": "string",
                    "description": "string",
                    "permanent": True,
                },
                "messageId": "string",
                "to": "string",
                "sender": "string",
                "sentAt": "2019-08-24T14:15:22Z",
                "doneAt": "2019-08-24T14:15:22Z",
                "messageCount": 0,
                "callbackData": "string",
                "platform": {"entityId": "string", "applicationId": "string"},
                "campaignReferenceId": "string",
                "attemptCount": 0,
                "timeToFirstAttempt": 0,
            }
        ]
    }

    setup_request(httpserver, REPORTS, given_response, "GET")

    api_instance = EmailApi(get_api_client)

    api_response = api_instance.get_email_delivery_reports(
        bulk_id=given_bulk_id, message_id=given_message_id, limit=1
    )

    expected_sent_at = datetime.datetime(
        2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
    )
    expected_done_at = datetime.datetime(
        2019, 8, 24, 14, 15, 22, tzinfo=datetime.timezone.utc
    )

    expected_response = EmailReportsResult(
        results=[
            EmailReport(
                bulk_id="string",
                message_id="string",
                to="string",
                sender="string",
                sent_at=expected_sent_at,
                done_at=expected_done_at,
                message_count=0,
                callback_data="string",
                campaign_reference_id="string",
                attempt_count=0,
                time_to_first_attempt=0,
                price=EmailMessagePrice(price_per_message=0, currency="string"),
                status=EmailMessageStatus(
                    group_id=0,
                    group_name=EmailMessageGeneralStatus.ACCEPTED,
                    id=0,
                    name="string",
                    description="string",
                    action="string",
                ),
                error=MessageError(
                    group_id=0,
                    group_name="OK",
                    id=0,
                    name="string",
                    description="string",
                    permanent=True,
                ),
                platform=Platform(
                    entity_id="string",
                    application_id="string",
                ),
            )
        ]
    )

    assert api_response == expected_response


def test_should_get_email_suppressions(httpserver: HTTPServer, get_api_client):
    given_domain_name = "example.com"
    given_email_address = "jane.smith@somecompany.com"
    given_type = "BOUNCE"
    given_created_date = "2024-08-14T14:02:17.366"
    given_reason = "550 5.1.1 <jane.smith@somecompany.com>: user does not exist"
    given_page = 0
    given_size = 100

    given_response = {
        "results": [
            {
                "domainName": given_domain_name,
                "emailAddress": given_email_address,
                "type": given_type,
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
    given_email_addresses1 = ["jane.smith@somecompany.com", "john.doe@somecompany.com"]
    given_type = EmailAddSuppressionType.BOUNCE

    given_domain_name2 = "example.com"
    given_email_addresses2 = ["john.smith@somecompany.com", "john.perry@gmail.com"]

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
    given_email_addresses1 = ["jane.smith@somecompany.com", "john.doe@somecompany.com"]
    given_type = EmailSuppressionType.BOUNCE

    given_domain_name2 = "example.com"
    given_email_addresses2 = ["john.smith@somecompany.com", "john.perry@gmail.com"]

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
    given_delete_overquotas1 = True

    given_domain_name2 = "example.com"
    given_data_access2 = EmailDomainAccess.GRANTED
    given_read_bounces2 = True
    given_create_bounces2 = True
    given_delete_bounces2 = False
    given_read_complaints2 = True
    given_create_complaints2 = False
    given_delete_complaints2 = False
    given_read_overquotas2 = False
    given_delete_overquotas2 = False

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
                "deleteOverquotas": given_delete_overquotas1,
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
                "deleteOverquotas": given_delete_overquotas2,
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
                delete_overquotas=given_delete_overquotas1,
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
                delete_overquotas=given_delete_overquotas2,
            ),
        ],
        paging=EmailPageDetails(page=given_page, size=given_size),
    )

    assert response == expected_response


def test_should_get_ips(httpserver: HTTPServer, get_api_client):
    given_id = "DB3F9D439088BF73F5560443C8054AC4"
    given_ip = "198.51.100.0"
    given_ip_addresses = ["198.51.100.0"]
    given_pool_id = "08A3A7608750CC6E6080325A6ADF45B6"
    given_pool_name = "IP pool name"

    given_response = [
        {
            "id": given_id,
            "ip": given_ip,
            "ipAddresses": given_ip_addresses,
            "pools": [{"id": given_pool_id, "name": given_pool_name}],
        }
    ]

    setup_request(httpserver, EMAIL_IPS, given_response, "GET", 200)

    api_instance = EmailApi(get_api_client)

    api_response = api_instance.get_all_ips()

    expected_response = [
        EmailIpDetailResponse(
            id=given_id,
            ip=given_ip,
            ip_addresses=given_ip_addresses,
            pools=[EmailIpPoolResponse(id=given_pool_id, name=given_pool_name)],
        )
    ]

    assert api_response == expected_response


def test_should_get_ip_details(httpserver: HTTPServer, get_api_client):
    given_id = "DB3F9D439088BF73F5560443C8054AC4"
    given_ip = "198.51.100.0"
    given_ip_addresses = ["198.51.100.0"]
    given_pool_id = "08A3A7608750CC6E6080325A6ADF45B6"
    given_pool_name = "IP pool name"

    given_response = {
        "id": given_id,
        "ip": given_ip,
        "ipAddresses": given_ip_addresses,
        "pools": [{"id": given_pool_id, "name": given_pool_name}],
    }

    setup_request(
        httpserver, EMAIL_IP.replace("{ipId}", given_id), given_response, "GET", 200
    )

    api_instance = EmailApi(get_api_client)

    api_response = api_instance.get_ip_details(given_id)

    expected_response = EmailIpDetailResponse(
        id=given_id,
        ip=given_ip,
        ip_addresses=given_ip_addresses,
        pools=[EmailIpPoolResponse(id=given_pool_id, name=given_pool_name)],
    )

    assert api_response == expected_response


def test_should_get_ip_pools(httpserver: HTTPServer, get_api_client):
    given_id = "08A3A7608750CC6E6080325A6ADF45B6"
    given_name = "IP pool name"
    given_ip_id = "DB3F9D439088BF73F5560443C8054AC4"
    given_ip = "198.51.100.0"
    given_ip_addresses = ["198.51.100.0"]

    given_response = [
        {
            "id": given_id,
            "name": given_name,
            "ips": [
                {"id": given_ip_id, "ip": given_ip, "ipAddresses": given_ip_addresses}
            ],
        }
    ]

    setup_request(httpserver, EMAIL_IP_POOLS, given_response, "GET", 200)

    api_instance = EmailApi(get_api_client)

    api_response = api_instance.get_ip_pools()

    expected_response = [
        EmailIpPoolDetailResponse(
            id=given_id,
            name=given_name,
            ips=[
                EmailIpResponse(
                    id=given_ip_id, ip=given_ip, ip_addresses=given_ip_addresses
                )
            ],
        )
    ]

    assert api_response == expected_response


def test_should_get_ip_pool_details(httpserver: HTTPServer, get_api_client):
    given_id = "08A3A7608750CC6E6080325A6ADF45B6"
    given_name = "IP pool name"
    given_ip_id = "DB3F9D439088BF73F5560443C8054AC4"
    given_ip = "198.51.100.0"
    given_ip_addresses = ["198.51.100.0"]

    given_response = {
        "id": given_id,
        "name": given_name,
        "ips": [{"id": given_ip_id, "ip": given_ip, "ipAddresses": given_ip_addresses}],
    }

    setup_request(
        httpserver,
        EMAIL_IP_POOL.replace("{poolId}", given_id),
        given_response,
        "GET",
        200,
    )

    api_instance = EmailApi(get_api_client)

    api_response = api_instance.get_ip_pool(given_id)

    expected_response = EmailIpPoolDetailResponse(
        id=given_id,
        name=given_name,
        ips=[
            EmailIpResponse(
                id=given_ip_id, ip=given_ip, ip_addresses=given_ip_addresses
            )
        ],
    )

    assert api_response == expected_response


def test_should_assign_ip_to_pool(httpserver: HTTPServer, get_api_client):
    pool_id = "08A3A7608750CC6E6080325A6ADF45B6"
    ip_id = "DB3F9D439088BF73F5560443C8054AC4"

    expected_request = {"ipId": ip_id}

    setup_request(
        httpserver,
        EMAIL_ASSIGN_IP_POOL.replace("{poolId}", pool_id),
        None,
        "POST",
        204,
        request_body=expected_request,
    )

    given_request = EmailIpPoolAssignIpApiRequest(ip_id=ip_id)

    api_instance = EmailApi(get_api_client)
    response = api_instance.assign_ip_to_pool(pool_id, given_request)

    assert response is None


def test_should_get_ip_domain_details(httpserver: HTTPServer, get_api_client):
    given_domain_id = 1
    given_domain_name = "example.com"
    given_pool_id = "08A3A7608750CC6E6080325A6ADF45B6"
    given_pool_name = "IP pool name"
    given_priority = 0
    given_ip_id = "DB3F9D439088BF73F5560443C8054AC4"
    given_ip = "198.51.100.0"
    given_ip_addresses = ["198.51.100.0"]

    given_response = {
        "id": given_domain_id,
        "name": given_domain_name,
        "pools": [
            {
                "id": given_pool_id,
                "name": given_pool_name,
                "priority": given_priority,
                "ips": [
                    {
                        "id": given_ip_id,
                        "ip": given_ip,
                        "ipAddresses": given_ip_addresses,
                    }
                ],
            }
        ],
    }

    setup_request(
        httpserver,
        EMAIL_IP_DOMAIN.replace("{domainId}", str(given_domain_id)),
        given_response,
        "GET",
        200,
    )

    api_instance = EmailApi(get_api_client)

    api_response = api_instance.get_ip_domain(given_domain_id)

    expected_response = EmailIpDomainResponse(
        id=given_domain_id,
        name=given_domain_name,
        pools=[
            EmailDomainIpApiPool(
                id=given_pool_id,
                name=given_pool_name,
                priority=given_priority,
                ips=[
                    EmailIpResponse(
                        id=given_ip_id, ip=given_ip, ip_addresses=given_ip_addresses
                    )
                ],
            )
        ],
    )

    assert api_response == expected_response


def test_should_assign_pool_to_domain(httpserver: HTTPServer, get_api_client):
    domain_id = 1
    pool_id = "08A3A7608750CC6E6080325A6ADF45B6"
    priority = 0

    expected_request = {"poolId": pool_id, "priority": priority}

    setup_request(
        httpserver,
        EMAIL_ASSIGN_IP_DOMAIN_POOL.replace("{domainId}", str(domain_id)),
        None,
        "POST",
        204,
        request_body=expected_request,
    )

    given_request = EmailDomainIpPoolAssignApiRequest(
        pool_id=pool_id, priority=priority
    )

    api_instance = EmailApi(get_api_client)
    response = api_instance.assign_pool_to_domain(domain_id, given_request)

    assert response is None


def test_should_send_mime_email(httpserver: HTTPServer, get_api_client):
    given_message_id = "requestMessageId"
    given_from = "jenny.smith@company.com"
    given_destinations = ["john.smith@company.com"]
    given_mime_message = "RGF0ZTogV2VkLCAxOCBKdW4gMjAyNSAxMjo0ODoyMyArMDIwMCAoQ0VTVCkNCkZyb206IGplbm55LnNtaXRoQGNvbXBhbnkuY29tDQpUbzogam9obi5zbWl0aEBjb21wYW55LmNvbQ0KTWVzc2FnZS1JRDogPG1lc3NhZ2VAaWQ+DQpTdWJqZWN0OiBUaGlzIGlzIHN1YmplY3QNCk1JTUUtVmVyc2lvbjogMS4wDQpDb250ZW50LVR5cGU6IG11bHRpcGFydC9taXhlZDsgDQoJYm91bmRhcnk9Ii0tLS09X1BhcnRfMF8xNDkzMzcyMS4xNzUwMjQzNzAzMTY0Ig0KWC1JQi1idWxrLWlkOiBkZWZhdWx0QnVsa0lkDQoNCi0tLS0tLT1fUGFydF8wXzE0OTMzNzIxLjE3NTAyNDM3MDMxNjQNCkNvbnRlbnQtVHlwZTogdGV4dC9wbGFpbjsgY2hhcnNldD11cy1hc2NpaQ0KQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogN2JpdA0KDQpIZWxsbyB3b3JsZA0KLS0tLS0tPV9QYXJ0XzBfMTQ5MzM3MjEuMTc1MDI0MzcwMzE2NA0KQ29udGVudC1UeXBlOiB0ZXh0L2h0bWw7IGNoYXJzZXQ9dXMtYXNjaWkNCkNvbnRlbnQtVHJhbnNmZXItRW5jb2Rpbmc6IDdiaXQNCg0KPGRpdj5IZWxsbyB3b3JsZDwvZGl2Pg0KLS0tLS0tPV9QYXJ0XzBfMTQ5MzM3MjEuMTc1MDI0MzcwMzE2NC0tDQo="

    given_bulk_id = "snxemd8u52v7v84iiu69"
    given_to = "john.smith@company.com"
    given_response_message_id = "jgzra46v9zi1ztvd62t5"
    given_group_id = 1
    given_group_name = "PENDING"
    given_id = 26
    given_name = "PENDING_ACCEPTED"
    given_description = "Message accepted, pending for delivery."

    given_client_priority = "STANDARD"

    expected_request = {
        "messageId": given_message_id,
        "from": given_from,
        "destinations": given_destinations,
        "mimeMessage": given_mime_message,
        "clientPriority": given_client_priority,
    }

    given_response = {
        "bulkId": given_bulk_id,
        "messages": [
            {
                "to": given_to,
                "messageId": given_response_message_id,
                "status": {
                    "groupId": given_group_id,
                    "groupName": given_group_name,
                    "id": given_id,
                    "name": given_name,
                    "description": given_description,
                },
            }
        ],
    }

    setup_request(
        httpserver, EMAIL_SEND_MIME, given_response, "POST", 200, expected_request
    )

    api_instance = EmailApi(get_api_client)

    request = EmailSendMimeRequestSchema(
        message_id=given_message_id,
        var_from=given_from,
        destinations=given_destinations,
        mime_message=given_mime_message,
    )

    api_response = api_instance.send_mime_email(request)

    expected_response = EmailSendResponse(
        bulk_id=given_bulk_id,
        messages=[
            EmailResponseDetails(
                to=given_to,
                message_id=given_response_message_id,
                status=MessageStatus(
                    group_id=given_group_id,
                    group_name=given_group_name,
                    id=given_id,
                    name=given_name,
                    description=given_description,
                ),
            )
        ],
    )

    assert api_response == expected_response


def test_should_create_email_template(httpserver: HTTPServer, get_api_client):
    given_id = 1000000000000000001
    given_name = "Welcome email"
    given_from = "Infobip <noreply@example.com>"
    given_reply_to = "support@example.com"
    given_subject = "Welcome to Infobip"
    given_preheader = "Welcome to Infobip"
    given_html = "<html><head></head><body><h2>Welcome to Infobip</h2></body></html>"
    given_is_html_editable = True
    given_landing_page_id = "1_2345"
    given_image_preview_url = "/email/1/templates/1000000000000000001/preview.png"
    given_created_at = "2024-01-01T12:00:00.000+0000"
    given_created_at_datetime = datetime.datetime(
        2024, 1, 1, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )
    given_updated_at = "2024-01-02T12:00:00.000+0000"
    given_updated_at_datetime = datetime.datetime(
        2024, 1, 2, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )

    given_response = {
        "id": given_id,
        "name": given_name,
        "from": given_from,
        "replyTo": given_reply_to,
        "subject": given_subject,
        "preheader": given_preheader,
        "html": given_html,
        "isHtmlEditable": given_is_html_editable,
        "landingPageId": given_landing_page_id,
        "imagePreviewUrl": given_image_preview_url,
        "createdAt": given_created_at,
        "updatedAt": given_updated_at,
    }

    setup_multipart_request(httpserver, EMAIL_TEMPLATES, given_response, 201)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.create_email_template(
        name=given_name,
        var_from=given_from,
        reply_to=given_reply_to,
        subject=given_subject,
        preheader=given_preheader,
        html=given_html,
        landing_page=given_landing_page_id,
    )

    expected_response = EmailTemplate(
        id=given_id,
        name=given_name,
        var_from=given_from,
        reply_to=given_reply_to,
        subject=given_subject,
        preheader=given_preheader,
        html=given_html,
        is_html_editable=given_is_html_editable,
        landing_page_id=given_landing_page_id,
        image_preview_url=given_image_preview_url,
        created_at=given_created_at_datetime,
        updated_at=given_updated_at_datetime,
    )

    assert api_response == expected_response


def test_should_get_email_templates(httpserver: HTTPServer, get_api_client):
    given_id = 1000000000000000001
    given_name = "Welcome email"
    given_image_preview_url = "/email/1/templates/1000000000000000001/preview.png"
    given_created_at = "2024-01-01T12:00:00.000+0000"
    given_created_at_datetime = datetime.datetime(
        2024, 1, 1, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )
    given_updated_at = "2024-01-02T12:00:00.000+0000"
    given_updated_at_datetime = datetime.datetime(
        2024, 1, 2, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )
    given_page = 0
    given_size = 20
    given_total_pages = 1
    given_total_results = 1

    given_response = {
        "results": [
            {
                "id": given_id,
                "name": given_name,
                "imagePreviewUrl": given_image_preview_url,
                "createdAt": given_created_at,
                "updatedAt": given_updated_at,
            }
        ],
        "paging": {
            "page": given_page,
            "size": given_size,
            "totalPages": given_total_pages,
            "totalResults": given_total_results,
        },
    }

    setup_request(httpserver, EMAIL_TEMPLATES, given_response)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.get_email_templates()

    expected_response = EmailTemplateListPage(
        results=[
            EmailTemplateListItem(
                id=given_id,
                name=given_name,
                image_preview_url=given_image_preview_url,
                created_at=given_created_at_datetime,
                updated_at=given_updated_at_datetime,
            )
        ],
        paging=PageInfo(
            page=given_page,
            size=given_size,
            total_pages=given_total_pages,
            total_results=given_total_results,
        ),
    )

    assert api_response == expected_response


def test_should_get_email_template(httpserver: HTTPServer, get_api_client):
    given_id = 1000000000000000001
    given_name = "Welcome email"
    given_from = "Infobip <noreply@example.com>"
    given_reply_to = "support@example.com"
    given_subject = "Welcome to Infobip"
    given_preheader = "Welcome to Infobip"
    given_html = "<html><head></head><body><h2>Welcome to Infobip</h2></body></html>"
    given_is_html_editable = True
    given_landing_page_id = "1_2345"
    given_image_preview_url = "/email/1/templates/1000000000000000001/preview.png"
    given_created_at = "2024-01-01T12:00:00.000+0000"
    given_created_at_datetime = datetime.datetime(
        2024, 1, 1, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )
    given_updated_at = "2024-01-02T12:00:00.000+0000"
    given_updated_at_datetime = datetime.datetime(
        2024, 1, 2, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )
    given_attachment_id = "7BE07D39-C7DA-4ED4-9F45-33BDB8643AA1"
    given_attachment_content_type = "application/pdf"
    given_attachment_file_name = "attachment.pdf"
    given_attachment_size = 1024
    given_attachment_url = "/email/1/templates/1000000000000000001/attachments/7BE07D39-C7DA-4ED4-9F45-33BDB8643AA1/download"

    given_response = {
        "id": given_id,
        "name": given_name,
        "from": given_from,
        "replyTo": given_reply_to,
        "subject": given_subject,
        "preheader": given_preheader,
        "html": given_html,
        "isHtmlEditable": given_is_html_editable,
        "attachments": [
            {
                "id": given_attachment_id,
                "contentType": given_attachment_content_type,
                "fileName": given_attachment_file_name,
                "size": given_attachment_size,
                "url": given_attachment_url,
            }
        ],
        "landingPageId": given_landing_page_id,
        "imagePreviewUrl": given_image_preview_url,
        "createdAt": given_created_at,
        "updatedAt": given_updated_at,
    }

    endpoint = EMAIL_TEMPLATE.replace("{templateId}", str(given_id))
    setup_request(httpserver, endpoint, given_response)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.get_email_template(template_id=given_id)

    expected_response = EmailTemplate(
        id=given_id,
        name=given_name,
        var_from=given_from,
        reply_to=given_reply_to,
        subject=given_subject,
        preheader=given_preheader,
        html=given_html,
        is_html_editable=given_is_html_editable,
        attachments=[
            EmailAttachment(
                id=given_attachment_id,
                content_type=given_attachment_content_type,
                file_name=given_attachment_file_name,
                size=given_attachment_size,
                url=given_attachment_url,
            )
        ],
        landing_page_id=given_landing_page_id,
        image_preview_url=given_image_preview_url,
        created_at=given_created_at_datetime,
        updated_at=given_updated_at_datetime,
    )

    assert api_response == expected_response


def test_should_delete_email_template(httpserver: HTTPServer, get_api_client):
    given_id = 1000000000000000001

    endpoint = EMAIL_TEMPLATE.replace("{templateId}", str(given_id))
    setup_request(httpserver, endpoint, None, "DELETE", 204)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.delete_email_template(template_id=given_id)

    assert api_response == ""


def test_should_update_email_template(httpserver: HTTPServer, get_api_client):
    given_id = 1000000000000000001
    given_name = "Updated Welcome email"
    given_from = "Infobip <noreply@example.com>"
    given_reply_to = "support@example.com"
    given_subject = "Updated Welcome to Infobip"
    given_preheader = "Updated Welcome to Infobip"
    given_html = (
        "<html><head></head><body><h2>Updated Welcome to Infobip</h2></body></html>"
    )
    given_is_html_editable = True
    given_landing_page_id = "1_2345"
    given_image_preview_url = "/email/1/templates/1000000000000000001/preview.png"
    given_created_at = "2024-01-01T12:00:00.000+0000"
    given_created_at_datetime = datetime.datetime(
        2024, 1, 1, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )
    given_updated_at = "2024-01-03T12:00:00.000+0000"
    given_updated_at_datetime = datetime.datetime(
        2024, 1, 3, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )

    given_response = {
        "id": given_id,
        "name": given_name,
        "from": given_from,
        "replyTo": given_reply_to,
        "subject": given_subject,
        "preheader": given_preheader,
        "html": given_html,
        "isHtmlEditable": given_is_html_editable,
        "landingPageId": given_landing_page_id,
        "imagePreviewUrl": given_image_preview_url,
        "createdAt": given_created_at,
        "updatedAt": given_updated_at,
    }

    endpoint = EMAIL_TEMPLATE.replace("{templateId}", str(given_id))
    setup_multipart_request(httpserver, endpoint, given_response, 200, "PUT")

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.update_email_template(
        template_id=given_id,
        name=given_name,
        var_from=given_from,
        reply_to=given_reply_to,
        subject=given_subject,
        preheader=given_preheader,
        html=given_html,
        landing_page=given_landing_page_id,
    )

    expected_response = EmailTemplate(
        id=given_id,
        name=given_name,
        var_from=given_from,
        reply_to=given_reply_to,
        subject=given_subject,
        preheader=given_preheader,
        html=given_html,
        is_html_editable=given_is_html_editable,
        landing_page_id=given_landing_page_id,
        image_preview_url=given_image_preview_url,
        created_at=given_created_at_datetime,
        updated_at=given_updated_at_datetime,
    )

    assert api_response == expected_response


def test_should_patch_email_template(httpserver: HTTPServer, get_api_client):
    given_id = 1000000000000000001
    given_name = "Patched Welcome email"
    given_from = "Infobip <noreply@example.com>"
    given_reply_to = "support@example.com"
    given_subject = "Patched Welcome to Infobip"
    given_preheader = "Patched Welcome to Infobip"
    given_html = (
        "<html><head></head><body><h2>Patched Welcome to Infobip</h2></body></html>"
    )
    given_is_html_editable = True
    given_landing_page_id = "1_2345"
    given_image_preview_url = "/email/1/templates/1000000000000000001/preview.png"
    given_created_at = "2024-01-01T12:00:00.000+0000"
    given_created_at_datetime = datetime.datetime(
        2024, 1, 1, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )
    given_updated_at = "2024-01-04T12:00:00.000+0000"
    given_updated_at_datetime = datetime.datetime(
        2024, 1, 4, 12, 0, 0, 0, tzinfo=datetime.timezone.utc
    )

    given_response = {
        "id": given_id,
        "name": given_name,
        "from": given_from,
        "replyTo": given_reply_to,
        "subject": given_subject,
        "preheader": given_preheader,
        "html": given_html,
        "isHtmlEditable": given_is_html_editable,
        "landingPageId": given_landing_page_id,
        "imagePreviewUrl": given_image_preview_url,
        "createdAt": given_created_at,
        "updatedAt": given_updated_at,
    }

    endpoint = EMAIL_TEMPLATE.replace("{templateId}", str(given_id))
    setup_multipart_request(httpserver, endpoint, given_response, 200, "PATCH")

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.patch_email_template(
        template_id=given_id,
        html=given_html,
        name=given_name,
    )

    expected_response = EmailTemplate(
        id=given_id,
        name=given_name,
        var_from=given_from,
        reply_to=given_reply_to,
        subject=given_subject,
        preheader=given_preheader,
        html=given_html,
        is_html_editable=given_is_html_editable,
        landing_page_id=given_landing_page_id,
        image_preview_url=given_image_preview_url,
        created_at=given_created_at_datetime,
        updated_at=given_updated_at_datetime,
    )

    assert api_response == expected_response


def test_should_generate_email_template_preview(httpserver: HTTPServer, get_api_client):
    given_id = 1000000000000000001
    given_placeholders = {
        "firstName": {"value": "John"},
        "lastName": {"value": "Doe"},
    }
    given_preview_html = (
        "<html><head></head><body><h2>Welcome John Doe to Infobip</h2></body></html>"
    )

    endpoint = EMAIL_TEMPLATE_PREVIEW.replace("{templateId}", str(given_id))
    setup_multipart_request(httpserver, endpoint, given_preview_html, 200)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.generate_email_template_preview(
        template_id=given_id,
        placeholders=given_placeholders,
    )

    assert api_response == given_preview_html


def test_should_get_email_template_attachments(httpserver: HTTPServer, get_api_client):
    given_id = 1000000000000000001
    given_attachment_id = "7BE07D39-C7DA-4ED4-9F45-33BDB8643AA1"
    given_attachment_content_type = "application/pdf"
    given_attachment_file_name = "attachment.pdf"
    given_attachment_size = 1024
    given_attachment_url = "/email/1/templates/1000000000000000001/attachments/7BE07D39-C7DA-4ED4-9F45-33BDB8643AA1/download"

    given_response = [
        {
            "id": given_attachment_id,
            "contentType": given_attachment_content_type,
            "fileName": given_attachment_file_name,
            "size": given_attachment_size,
            "url": given_attachment_url,
        }
    ]

    endpoint = EMAIL_TEMPLATE_ATTACHMENTS.replace("{templateId}", str(given_id))
    setup_request(httpserver, endpoint, given_response)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.get_email_template_attachments(template_id=given_id)

    expected_response = [
        EmailAttachment(
            id=given_attachment_id,
            content_type=given_attachment_content_type,
            file_name=given_attachment_file_name,
            size=given_attachment_size,
            url=given_attachment_url,
        )
    ]

    assert api_response == expected_response


def test_should_upload_email_template_attachment(
    httpserver: HTTPServer, get_api_client
):
    given_template_id = 1000000000000000001
    given_attachment_id = "7BE07D39-C7DA-4ED4-9F45-33BDB8643AA1"
    given_attachment_content_type = "application/pdf"
    given_attachment_file_name = "attachment.pdf"
    given_attachment_size = 1024
    given_attachment_url = "/email/1/templates/1000000000000000001/attachments/7BE07D39-C7DA-4ED4-9F45-33BDB8643AA1/download"
    given_attachment_data = "SGVsbG8gV29ybGQh"

    given_response = {
        "id": given_attachment_id,
        "contentType": given_attachment_content_type,
        "fileName": given_attachment_file_name,
        "size": given_attachment_size,
        "url": given_attachment_url,
    }

    endpoint = EMAIL_TEMPLATE_ATTACHMENTS.replace(
        "{templateId}", str(given_template_id)
    )
    setup_multipart_request(httpserver, endpoint, given_response, 201)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.upload_email_template_attachment(
        template_id=given_template_id,
        content_type=given_attachment_content_type,
        file_name=given_attachment_file_name,
        data=given_attachment_data,
    )

    expected_response = EmailAttachment(
        id=given_attachment_id,
        content_type=given_attachment_content_type,
        file_name=given_attachment_file_name,
        size=given_attachment_size,
        url=given_attachment_url,
    )

    assert api_response == expected_response


def test_should_delete_email_template_attachment(
    httpserver: HTTPServer, get_api_client
):
    given_template_id = 1000000000000000001
    given_attachment_id = "7BE07D39-C7DA-4ED4-9F45-33BDB8643AA1"

    endpoint = EMAIL_TEMPLATE_ATTACHMENT.replace(
        "{templateId}", str(given_template_id)
    ).replace("{attachmentId}", given_attachment_id)
    setup_request(httpserver, endpoint, None, "DELETE", 204)

    api_instance = EmailApi(get_api_client)
    api_response = api_instance.delete_email_template_attachment(
        template_id=given_template_id,
        attachment_id=given_attachment_id,
    )

    assert api_response == ""


def setup_multipart_request(
    httpserver,
    endpoint: str,
    expected_response=None,
    status_code: int = 200,
    http_verb: str = "POST",
):
    httpserver.expect_request(uri=endpoint, method=http_verb).respond_with_json(
        expected_response, status=status_code
    )


def create_temp_file_with_content(filename: str, content: str):
    with open(filename, "w") as temp_file:
        temp_file.write(content)
    with open(filename, "rb") as temp_file:
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
