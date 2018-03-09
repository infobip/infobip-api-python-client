# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""

from util.http import HttpClient


class get_received_sms_logs(object):

    def __init__(self, configuration):
        super(get_received_sms_logs, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.sms.mo.logs.MOLogsResponse import MOLogsResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/sms/1/inbox/logs", None, context, None, MOLogsResponse)


class get_received_messages(object):

    def __init__(self, configuration):
        super(get_received_messages, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.sms.mo.reports.MOReportResponse import MOReportResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/sms/1/inbox/reports", None, context, None, MOReportResponse)


class get_bulks(object):

    def __init__(self, configuration):
        super(get_bulks, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.sms.mt.bulks.BulkResponse import BulkResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/sms/1/bulks", None, context, None, BulkResponse)


class reschedule_bulk(object):

    def __init__(self, configuration):
        super(reschedule_bulk, self).__init__()
        self.configuration = configuration

    def execute(self, context, bulk_request):
        from infobip.api.model.sms.mt.bulks.BulkResponse import BulkResponse

        http_client = HttpClient()
        return http_client.getValue("PUT", self.configuration, "/sms/1/bulks", None, context, bulk_request, BulkResponse)


class get_bulk_status(object):

    def __init__(self, configuration):
        super(get_bulk_status, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.sms.mt.bulks.status.BulkStatusResponse import BulkStatusResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/sms/1/bulks/status", None, context, None, BulkStatusResponse)


class manage_bulk_status(object):

    def __init__(self, configuration):
        super(manage_bulk_status, self).__init__()
        self.configuration = configuration

    def execute(self, context, update_status_request):
        from infobip.api.model.sms.mt.bulks.status.BulkStatusResponse import BulkStatusResponse

        http_client = HttpClient()
        return http_client.getValue("PUT", self.configuration, "/sms/1/bulks/status", None, context, update_status_request, BulkStatusResponse)


class get_sent_sms_logs(object):

    def __init__(self, configuration):
        super(get_sent_sms_logs, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.sms.mt.logs.SMSLogsResponse import SMSLogsResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/sms/1/logs", None, context, None, SMSLogsResponse)


class get_sent_sms_delivery_reports(object):

    def __init__(self, configuration):
        super(get_sent_sms_delivery_reports, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.sms.mt.reports.SMSReportResponse import SMSReportResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/sms/1/reports", None, context, None, SMSReportResponse)


class send_multiple_sms_binary_advanced(object):

    def __init__(self, configuration):
        super(send_multiple_sms_binary_advanced, self).__init__()
        self.configuration = configuration

    def execute(self, sms_advanced_binary_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/binary/advanced", None, None, sms_advanced_binary_request, SMSResponse)


class send_multiple_binary_sms(object):

    def __init__(self, configuration):
        super(send_multiple_binary_sms, self).__init__()
        self.configuration = configuration

    def execute(self, sms_multi_binary_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/binary/multi", None, None, sms_multi_binary_request, SMSResponse)


class send_single_binary_sms(object):

    def __init__(self, configuration):
        super(send_single_binary_sms, self).__init__()
        self.configuration = configuration

    def execute(self, sms_binary_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/binary/single", None, None, sms_binary_request, SMSResponse)


class preview_sms(object):

    def __init__(self, configuration):
        super(preview_sms, self).__init__()
        self.configuration = configuration

    def execute(self, preview_request):
        from infobip.api.model.sms.mt.send.preview.PreviewResponse import PreviewResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/preview", None, None, preview_request, PreviewResponse)


class send_multiple_textual_sms_advanced(object):

    def __init__(self, configuration):
        super(send_multiple_textual_sms_advanced, self).__init__()
        self.configuration = configuration

    def execute(self, sms_advanced_textual_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/advanced", None, None, sms_advanced_textual_request, SMSResponse)


class send_multiple_sms_textual(object):

    def __init__(self, configuration):
        super(send_multiple_sms_textual, self).__init__()
        self.configuration = configuration

    def execute(self, sms_multi_textual_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/multi", None, None, sms_multi_textual_request, SMSResponse)


class send_sms_textual_query_post(object):

    def __init__(self, configuration):
        super(send_sms_textual_query_post, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/query", None, context, None, SMSResponse)


class send_single_textual_sms(object):

    def __init__(self, configuration):
        super(send_single_textual_sms, self).__init__()
        self.configuration = configuration

    def execute(self, sms_textual_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/single", None, None, sms_textual_request, SMSResponse)


class get_number_context_logs(object):

    def __init__(self, configuration):
        super(get_number_context_logs, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.nc.logs.NumberContextLogsResponse import NumberContextLogsResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/number/1/logs", None, context, None, NumberContextLogsResponse)


class number_context_notify(object):

    def __init__(self, configuration):
        super(number_context_notify, self).__init__()
        self.configuration = configuration

    def execute(self, number_context_request):
        from infobip.api.model.nc.notify.NumberContextResponse import NumberContextResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/number/1/notify", None, None, number_context_request, NumberContextResponse)


class number_context_query(object):

    def __init__(self, configuration):
        super(number_context_query, self).__init__()
        self.configuration = configuration

    def execute(self, number_context_request):
        from infobip.api.model.nc.query.NumberContextResponse import NumberContextResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/number/1/query", None, None, number_context_request, NumberContextResponse)


class log_end_tag(object):

    def __init__(self, configuration):
        super(log_end_tag, self).__init__()
        self.configuration = configuration

    def execute(self, messageId):
        from infobip.api.model.conversion.EndTagResponse import EndTagResponse

        pathParams = {
            "messageId": messageId
        }
        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/ct/1/log/end/{messageId}", pathParams, None, None, EndTagResponse)


class add_destination(object):

    def __init__(self, configuration):
        super(add_destination, self).__init__()
        self.configuration = configuration

    def execute(self, campaignKey, destination):
        from infobip.api.model.omni.campaign.Campaign import Campaign

        pathParams = {
            "campaignKey": campaignKey
        }
        http_client = HttpClient()
        return http_client.getValue("PUT", self.configuration, "/omni/1/campaigns/{campaignKey}/destinations", pathParams, None, destination, Campaign)


class add_destination(object):

    def __init__(self, configuration):
        super(add_destination, self).__init__()
        self.configuration = configuration

    def execute(self, campaignKey, destinations):
        from infobip.api.model.omni.campaign.Campaign import Campaign

        pathParams = {
            "campaignKey": campaignKey
        }
        http_client = HttpClient()
        return http_client.getValue("PUT", self.configuration, "/omni/2/campaigns/{campaignKey}/destinations", pathParams, None, destinations, Campaign)


class get_campaign_details(object):

    def __init__(self, configuration):
        super(get_campaign_details, self).__init__()
        self.configuration = configuration

    def execute(self, campaignKey):
        from infobip.api.model.omni.campaign.Campaign import Campaign

        pathParams = {
            "campaignKey": campaignKey
        }
        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/omni/1/campaigns/{campaignKey}", pathParams, None, None, Campaign)


class get_campaigns(object):

    def __init__(self, configuration):
        super(get_campaigns, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.omni.campaign.CampaignsResponse import CampaignsResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/omni/1/campaigns", None, context, None, CampaignsResponse)


class get_omni_logs(object):

    def __init__(self, configuration):
        super(get_omni_logs, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.omni.logs.OmniLogsResponse import OmniLogsResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/omni/1/logs", None, context, None, OmniLogsResponse)


class get_omni_reports(object):

    def __init__(self, configuration):
        super(get_omni_reports, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.omni.reports.OMNIReportsResponse import OMNIReportsResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/omni/1/reports", None, context, None, OMNIReportsResponse)


class get_scenarios(object):

    def __init__(self, configuration):
        super(get_scenarios, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.omni.scenarios.ScenariosResponse import ScenariosResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/omni/1/scenarios", None, context, None, ScenariosResponse)


class get_specific_scenario(object):

    def __init__(self, configuration):
        super(get_specific_scenario, self).__init__()
        self.configuration = configuration

    def execute(self, scenarioKey):
        from infobip.api.model.omni.scenarios.Scenario import Scenario

        pathParams = {
            "scenarioKey": scenarioKey
        }
        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/omni/1/scenarios/{scenarioKey}", pathParams, None, None, Scenario)


class create_scenario(object):

    def __init__(self, configuration):
        super(create_scenario, self).__init__()
        self.configuration = configuration

    def execute(self, scenario):
        from infobip.api.model.omni.scenarios.Scenario import Scenario

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/omni/1/scenarios", None, None, scenario, Scenario)


class update_scenario(object):

    def __init__(self, configuration):
        super(update_scenario, self).__init__()
        self.configuration = configuration

    def execute(self, scenarioKey, scenario):
        from infobip.api.model.omni.scenarios.Scenario import Scenario

        pathParams = {
            "scenarioKey": scenarioKey
        }
        http_client = HttpClient()
        return http_client.getValue("PUT", self.configuration, "/omni/1/scenarios/{scenarioKey}", pathParams, None, scenario, Scenario)


class send_advanced_omni_message(object):

    def __init__(self, configuration):
        super(send_advanced_omni_message, self).__init__()
        self.configuration = configuration

    def execute(self, omni_advanced_request):
        from infobip.api.model.omni.send.OmniResponse import OmniResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/omni/1/advanced", None, None, omni_advanced_request, OmniResponse)


class send_simple_omni_message(object):

    def __init__(self, configuration):
        super(send_simple_omni_message, self).__init__()
        self.configuration = configuration

    def execute(self, omni_simple_request):
        from infobip.api.model.omni.send.OmniResponse import OmniResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/omni/1/text", None, None, omni_simple_request, OmniResponse)


class get_account_balance(object):

    def __init__(self, configuration):
        super(get_account_balance, self).__init__()
        self.configuration = configuration

    def execute(self):
        from infobip.api.model.account.AccountBalance import AccountBalance

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/account/1/balance", None, None, None, AccountBalance)