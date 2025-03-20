# Infobip API Python Client

<img src="https://cdn-web.infobip.com/uploads/2023/01/Infobip-logo.svg" height="93px" alt="Infobip" />

[![Pypi index](https://badgen.net/pypi/v/infobip-api-python-client)](https://pypi.org/project/infobip-api-python-client/)
[![Snyk](https://snyk.io/test/github/infobip/infobip-api-python-client/badge.svg)](https://snyk.io/test/github/infobip/infobip-api-python-client)
[![MIT License](https://badgen.net/github/license/infobip/infobip-api-python-client)](https://opensource.org/licenses/MIT)

This is a Python package for Infobip API and you can use it as a dependency to add [Infobip APIs][apidocs] to your application.
To use the package you'll need an Infobip account. If you don't already have one, you can create a [free trial][freetrial] account [here][signup].

We use [OpenAPI Generator](https://openapi-generator.tech/) to generate the package code from the OpenAPI specification.


#### Table of contents:
* [API documentation](#api-documentation)
* [General Info](#general-info)
* [Installation](#installation)
* [Quickstart](#quickstart)
* [Ask for help](#ask-for-help)

## API documentation

Detailed documentation about Infobip API can be found here. The current version of this library includes this subset of Infobip products:

* [SMS](https://www.infobip.com/docs/api/channels/sms)
* [2FA](https://www.infobip.com/docs/api/platform/2fa)
* [Voice](https://www.infobip.com/docs/api/channels/voice)
* [Moments](https://www.infobip.com/docs/api/customer-engagement/moments).
* [Email](https://www.infobip.com/docs/api/channels/email)

## General Info
For `infobip-api-python-client` versioning we use [Semantic Versioning][semver] scheme.

Published under [MIT License][license].

Python 3.8 is minimum supported version by this library.

## Installation
Pull the library by using the following command:
```shell
pip install infobip-api-python-client
```

## Quickstart

Before initializing the client first thing you need to do is to set configuration and authentication.

#### Configuration

Let's first set the configuration. For that you will need your specific URL.
To see your base URL, log in to the [Infobip API Resource][apidocs] hub with your Infobip credentials.
```python
    from infobip_api_client.api_client import ApiClient, Configuration

    client_config = Configuration(
        host="<YOUR_BASE_URL>",
        api_key={"APIKeyHeader": "<YOUR_API_KEY>"},
        api_key_prefix={"APIKeyHeader": "<YOUR_API_PREFIX>"},
    )
```

#### Initialize the Client

With configuration set up you can initialize the API client.
```python
	api_client = ApiClient(client_config)
```

Now you are ready use the API.

#### Send an SMS
Here's a basic example of sending the SMS message.

```python
    from infobip_api_client.models import SmsRequest, SmsMessage, SmsMessageContent, SmsTextContent, SmsDestination, SmsResponse
    from infobip_api_client.api.sms_api import SmsApi

    sms_request = SmsRequest(
        messages=[
            SmsMessage(
                destinations=[
                    SmsDestination(
                        to="41793026727",
                    ),
                ],
                sender="InfoSMS",
                content=SmsMessageContent(actual_instance=SmsTextContent(text="This is a dummy SMS message sent using Python library"))
            )
        ]
    )

    api_instance = SmsApi(api_client)

    api_response: SmsResponse = api_instance.send_sms_messages(sms_request=sms_request)
    print(api_response)
```

To make your code more robust send the message in try block and handle the `ApiException` in catch block.
```python
    from infobip_api_client.exceptions import ApiException

    try:
        api_response: SmsResponse = api_instance.send_sms_messages(sms_request=sms_request)
    except ApiException as ex:
        print("Error occurred while trying to send SMS message.")
```

In case of failure you can inspect the `ApiException` for more information.
```python
    try:
        api_response: SmsResponse = api_instance.send_sms_messages(sms_request=sms_request)
    except ApiException as ex:
        print("Error occurred while trying to send SMS message.")
        print("Error status: %s\n" % ex.status)
        print("Error headers: %s\n" % ex.headers)
        print("Error body: %s\n" % ex.body)
```

Additionally, from the successful response (`SmsResponse` object) you can pull out the `bulk_id` and `message_id`(s) and use them to fetch a delivery report for given message or bulk.
Bulk ID will be received only when you send a message to more than one destination address or multiple messages in a single request.

```python
    bulk_id = api_response.bulk_id
    message_id = api_response.messages[0].message_id
```

#### Receive sent SMS report
All you need to do is specify your endpoint when sending SMS in the `webhooks.delivery.url` field of your request, or subscribe for reports by contacting our support team at support@infobip.com.
e.g. `https://{yourDomain}/delivery-reports`

Example of webhook implementation using Flask:

```python
    from infobip_api_client.models import SmsDeliveryResult

    @app.route("/api/delivery-reports", methods=["POST"])
    def delivery_report():
        delivery_results = SmsDeliveryResult(
            results=request.json["results"]
        )

        for result in delivery_results.results:
            print("message {0} sent at {1}".format(result.message_id, result.sent_at))
```
If you prefer to use your own serializer, please pay attention to the supported [date format](https://www.infobip.com/docs/essentials/api-essentials/integration-best-practices#date-formats-backward-compatibility).

#### Fetching delivery reports
If you are for any reason unable to receive real time delivery reports on your endpoint, you can use `message_id` or `bulk_id` to fetch them.
Each request will return a batch of delivery reports. Please be aware that these can be retrieved only once.

```python
    api_response = api_instance.get_outbound_sms_message_delivery_reports(bulk_id=bulk_id, message_id=message_id, limit=2)
    print(api_response)
```

#### Unicode & SMS preview
Infobip API supports Unicode characters and automatically detects encoding. Unicode and non-standard GSM characters use additional space, avoid unpleasant surprises and check how different message configurations will affect your message text, number of characters and message parts.

```python
    from infobip_api_client.models import SmsPreviewRequest

    sms_preview_request = SmsPreviewRequest(
        text="Let's see how many characters will remain unused in this message."
    )

    api_response = api_instance.preview_sms_message(sms_preview_request=sms_preview_request)
```

#### Receive incoming SMS
If you want to receive SMS messages from your subscribers we can have them delivered to you in real time. When you buy and configure a number capable of receiving SMS, specify your endpoint as explained [here](https://www.infobip.com/docs/api#channels/sms/receive-inbound-sms-messages).
e.g. `https://{yourDomain}/incoming-sms`.

Example of webhook implementation using Flask:

```python
    from infobip_api_client.models import SmsInboundMessageResult

    @app.route("/api/incoming-sms", methods=["POST"])
    def incoming_sms():
        message_results = SmsInboundMessageResult(
            message_count=request.json["message_count"],
            pending_message_count=request.json["pending_message_count"],
            results=request.json["results"]
        )

        for result in message_results.results:
            print("message text: {0}".format(result.clean_text))

```
#### Two-Factor Authentication (2FA)
For 2FA quick start guide please check [these examples](two-factor-authentication.md).

#### Calls
For Calls quick start guide please check [these examples](calls.md)

## Ask for help

Feel free to open issues on the repository for any encountered problem or feature request.

If you want to contribute to this library in any way, please follow the guidelines in [CONTRIBUTING][contributing] file.

For anything that requires our imminent attention, contact us @ [support@infobip.com](mailto:support@infobip.com).

[apidocs]: https://www.infobip.com/docs/api
[freetrial]: https://www.infobip.com/docs/essentials/getting-started/free-trial
[signup]: https://www.infobip.com/signup
[semver]: https://semver.org
[license]: LICENSE
[contributing]: CONTRIBUTING.md