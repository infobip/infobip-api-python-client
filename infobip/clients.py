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

    def execute(self, s_m_s_advanced_binary_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/binary/advanced", None, None, s_m_s_advanced_binary_request, SMSResponse)


class send_multiple_binary_sms(object):

    def __init__(self, configuration):
        super(send_multiple_binary_sms, self).__init__()
        self.configuration = configuration

    def execute(self, s_m_s_multi_binary_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/binary/multi", None, None, s_m_s_multi_binary_request, SMSResponse)


class send_single_binary_sms(object):

    def __init__(self, configuration):
        super(send_single_binary_sms, self).__init__()
        self.configuration = configuration

    def execute(self, s_m_s_binary_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/binary/single", None, None, s_m_s_binary_request, SMSResponse)


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

    def execute(self, s_m_s_advanced_textual_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/advanced", None, None, s_m_s_advanced_textual_request, SMSResponse)


class send_multiple_sms_textual(object):

    def __init__(self, configuration):
        super(send_multiple_sms_textual, self).__init__()
        self.configuration = configuration

    def execute(self, s_m_s_multi_textual_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/multi", None, None, s_m_s_multi_textual_request, SMSResponse)


class send_single_textual_sms(object):

    def __init__(self, configuration):
        super(send_single_textual_sms, self).__init__()
        self.configuration = configuration

    def execute(self, s_m_s_textual_request):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/single", None, None, s_m_s_textual_request, SMSResponse)


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


class get_account_balance(object):

    def __init__(self, configuration):
        super(get_account_balance, self).__init__()
        self.configuration = configuration

    def execute(self):
        from infobip.api.model.account.AccountBalance import AccountBalance

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/account/1/balance", None, None, None, AccountBalance)