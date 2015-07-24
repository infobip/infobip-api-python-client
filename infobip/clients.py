# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""
from util.http import HttpClient

# SMS API

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


class send_single_textual_sms(object):

    def __init__(self, configuration):
        super(send_single_textual_sms, self).__init__()
        self.configuration = configuration

    def execute(self, textual):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/single", None, None, textual, SMSResponse)


class send_multiple_textual_sms_advanced(object):

    def __init__(self, configuration):
        super(send_multiple_textual_sms_advanced, self).__init__()
        self.configuration = configuration

    def execute(self, textual):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/advanced", None, None, textual, SMSResponse)


class send_multiple_sms_textual(object):

    def __init__(self, configuration):
        super(send_multiple_sms_textual, self).__init__()
        self.configuration = configuration

    def execute(self, textual):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/text/multi", None, None, textual, SMSResponse)


class send_singe_binary_sms(object):

    def __init__(self, configuration):
        super(send_singe_binary_sms, self).__init__()
        self.configuration = configuration

    def execute(self, binary):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/binary/single", None, None, binary, SMSResponse)


class send_multiple_sms_binary_advanced(object):

    def __init__(self, configuration):
        super(send_multiple_sms_binary_advanced, self).__init__()
        self.configuration = configuration

    def execute(self, binary):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/binary/advanced", None, None, binary, SMSResponse)


class send_multiple_binary_sms(object):

    def __init__(self, configuration):
        super(send_multiple_binary_sms, self).__init__()
        self.configuration = configuration

    def execute(self, binary):
        from infobip.api.model.sms.mt.send.SMSResponse import SMSResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/sms/1/binary/multi", None, None, binary, SMSResponse)


class number_context_query(object):

    def __init__(self, configuration):
        super(number_context_query, self).__init__()
        self.configuration = configuration

    def execute(self, n_c_request):
        from infobip.api.model.sms.nc.lookup.sync.NCResponse import NCResponse

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/number/1/query", None, None, n_c_request, NCResponse)


class number_context_notify(object):

    def __init__(self, configuration):
        super(number_context_notify, self).__init__()
        self.configuration = configuration

    def execute(self, n_c_request_async):
        from infobip.api.model.sms.nc.lookup.async.NCResponseAsync import NCResponseAsync

        http_client = HttpClient()
        return http_client.getValue("POST", self.configuration, "/number/1/notify", None, None, n_c_request_async, NCResponseAsync)


class get_number_context_logs(object):

    def __init__(self, configuration):
        super(get_number_context_logs, self).__init__()
        self.configuration = configuration

    def execute(self, context):
        from infobip.api.model.sms.nc.logs.NCLogsResponse import NCLogsResponse

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/number/1/logs", None, context, None, NCLogsResponse)


# CUSTOMER API

class get_account_balance(object):

    def __init__(self, configuration):
        super(get_account_balance, self).__init__()
        self.configuration = configuration

    def execute(self):
        from infobip.api.model.account.AccountBalance import AccountBalance

        http_client = HttpClient()
        return http_client.getValue("GET", self.configuration, "/account/1/balance", None, None, None, AccountBalance)
