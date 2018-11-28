import base64

from .exception import ApiException, ApiRequestError, ApiRequestErrorDetails

__author__ = 'mstipanov'

import http.client
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urlparse
import json

class HttpClient:

    def deserialize(self, s, cls):
        vals = json.JSONDecoder().decode(s)
        return self.deserialize_map(vals, cls)

    def deserialize_map(self, vals, cls):
        obj = cls()

        if not hasattr(vals, 'items'):
            return vals

        for key, val in list(vals.items()):
            t = type(getattr(obj, key, None))
            value = self.deserialize_map(val, t)
            setattr(obj, key, value)

        return obj

    def serialize(self, bodyObject):
        return bodyObject.to_JSON()

    def getValue(self, httpMethod, configuration, methodPath, pathParams, context, bodyObject, valueType):
        if (pathParams):
            for key, value in list(pathParams.items()):
                methodPath = methodPath.replace("{" + key + "}", str(value))

        url = configuration.base_url + methodPath
        username = configuration.username
        password = configuration.password
        api_key = configuration.api_key
        token = configuration.token

        if context:
            if isinstance(context, dict):
                params = urllib.parse.urlencode(context)
            else:
                params = urllib.parse.urlencode(context.to_dict())
            url = url + ("?%s" % params)

        u = urlparse(url)
        if (u.scheme == "https"):
            connection = http.client.HTTPSConnection(u.netloc)
        else:
            connection = http.client.HTTPConnection(u.netloc)

        headers = {}
        if username:
            auth_bytes = ('%s:%s' % (username, password)).encode()
            auth = base64.encodestring(auth_bytes).replace(b'\n', b'').decode()
            headers["Authorization"] = "Basic %s" % auth

        if api_key:
            headers["Authorization"] = "App %s" % api_key

        if token:
            headers["Authorization"] = "IBSSO %s" % token

        body_content = None
        if bodyObject:
            body_content = self.serialize(bodyObject)
            headers["Accept"] = "application/json"

        headers["Content-Type"] = "application/json"
        headers["User-Agent"] = "Python-Client-Library"


        connection.request(httpMethod, url, body_content, headers)
        response = connection.getresponse()

        statusCode = response.status
        response_content = response.read().decode('utf8')
        if (statusCode < 200 or statusCode >= 300):
            contentType = response.getheader("Content-Type")
            if contentType and contentType.startswith("application/json"):
                raise self.deserialize(response_content, ApiException)

            raise ApiException(ApiRequestError(None, ApiRequestErrorDetails(response.reason + " - " + response_content)))

        contentType = response.getheader("Content-Type")
        if contentType and contentType.startswith("application/json") and not str == valueType:
            return valueType.from_JSON(response_content)

        return response_content
