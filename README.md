# Infobip API Python Client

[![Pypi index](https://badgen.net/pypi/v/infobip-api-python-client)](https://pypi.org/project/infobip-api-python-client/)
[![MIT License](https://badgen.net/github/license/infobip/infobip-api-python-client)](https://opensource.org/licenses/MIT)

This is a Python package for Infobip API and you can use it as a dependency to add [Infobip APIs][apidocs] to your application.
To use the package you'll need an Infobip account. If you don't already have one, you can create a [free trial][freetrial] account [here][signup].

We use [OpenAPI Generator](https://openapi-generator.tech/) to generate the package code from the OpenAPI specification.

<img src="https://udesigncss.com/wp-content/uploads/2020/01/Infobip-logo-transparent.png" height="124px" alt="Infobip" />

#### Table of contents:
* [API documentation](#documentation)
* [General Info](#general-info)
* [Installation](#installation)
* [Quickstart](#quickstart)
* [Ask for help](#ask-for-help)

## API documentation

Infobip API Documentation can be found [here][apidocs].

## General Info
For `infobip-api-python-client` versioning we use [Semantic Versioning][semver] scheme.

Published under [MIT License][license].

Python 3.6 is minimum supported version by this library.

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
    sms_request = SmsAdvancedTextualRequest(
        messages=[
            SmsTextualMessage(
                destinations=[
                    SmsDestination(
                        to="41793026727",
                    ),
                ],
                _from="InfoSMS",
                text="This is a dummy SMS message sent using Python library",
            )
        ])
        
    api_instance = SendSmsApi(api_client)

    api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
    pprint(api_response)
```

To make your code more robust send the message in try block and handle the `ApiException` in catch block.
```python
    from infobip_api_client.exceptions import ApiException
    
    try:
        api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
    except ApiException as ex:
        print("Error occurred while trying to send SMS message.")
```

In case of failure you can inspect the `ApiException` for more information.
```python
    try:
        api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_binary_request=sms_advanced_binary_request)
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
For each SMS that you send out, we can send you a message delivery report in real time. All you need to do is specify your endpoint when sending SMS in `notify_url` field of `SmsTextualMessage`, or subscribe for reports by contacting our support team.
e.g. `https://{yourDomain}/delivery-reports`

Example of webhook implementation using Flask:

```python
    @app.route("/api/delivery-reports", methods=["POST"])
    def delivery_report():
        delivery_result = SmsDeliveryResult(
            results=request.json["results"]
        )
        
        for result in delivery_results.results:
            print("message {0} sent at {1}".format(result.message_id, result.sent_at))
```
If you prefer to use your own serializer, please pay attention to the supported [date format](https://www.infobip.com/docs/essentials/integration-best-practices#date-formats).

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

## Ask for help

Feel free to open issues on the repository for any issue or feature request. As per pull requests, for details check the `CONTRIBUTING` [file][contributing] related to it - in short, we will not merge any pull requests, this code is auto-generated.

If it's something that requires our imminent attention feel free to contact us @ [support@infobip.com](mailto:support@infobip.com).

[apidocs]: https://www.infobip.com/docs/api
[freetrial]: https://www.infobip.com/docs/freetrial
[signup]: https://www.infobip.com/signup
[semver]: https://semver.org
[license]: LICENSE
[contributing]: CONTRIBUTING.md
