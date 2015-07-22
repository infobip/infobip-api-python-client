__author__ = 'mstipanov'


class ApiRequestErrorDetails(object):
    messageId = ""
    text = ""
    variables = ""
    additionalDescription = ""

    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return "ApiRequestErrorDetails: {" \
               "messageId = \"" + str(self.messageId) + "\", " \
                                                        "text = \"" + str(self.text) + "\", " \
                                                                                       "variables = \"" + str(
            self.variables) + "\", " \
                              "additionalDescription = \"" + str(self.additionalDescription) + "\"" \
                                                                                               "}"


class ApiRequestError(object):
    clientCorrelator = ""
    serviceException = ApiRequestErrorDetails()

    def __init__(self, clientCorrelator="", serviceException=ApiRequestErrorDetails()):
        self.clientCorrelator = clientCorrelator
        self.serviceException = serviceException

    def __str__(self):
        return "ApiRequestError: {" \
               "clientCorrelator = \"" + str(self.clientCorrelator) + "\", " \
                                                                      "serviceException = " + str(
            self.serviceException) + "" \
                                     "}"


class ApiException(Exception):
    requestError = ApiRequestError()

    def __init__(self, requestError=ApiRequestError()):
        self.requestError = requestError

    def __str__(self):
        return "ApiException: {" \
               "requestError = " + str(self.requestError) + "" \
                                                            "}"