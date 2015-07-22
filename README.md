Infobip API Python client
============================

Running examples
----------------

First, setup your username and password in `examples/__init__.py`. Then, you can run provided examples in `examples` folder by running:

    python example.py deserialize_dr_example # provided argument is <file_name_of_example>

Basic messaging example
-----------------------

First, initialize the messaging client using your username and password:

    send_sms_client = send_single_textual_sms(Configuration("https://api.infobip.com", "username", "password"))

Prepare the message:

    request = SMSTextualRequest()
    request.text = "This is an example message"
    request.to = ["xxxxxxxx", "yyyyyyy"]
    
Send the message:

    response = send_sms_client.execute(request)

Later you can query for the delivery status of the message:

    get_delivery_reports_client = get_sent_sms_delivery_reports(Configuration("https://api.infobip.com", "username", "password"))
    response = get_delivery_reports_client.execute({"limit": 5})

Messaging with delivery report push to notification URL example
-----------------------

Similar to standard messaging example, but when preparing your message, use `SMSAdvancedTextualRequest`:

    send_sms_client = send_multiple_textual_sms_advanced(Configuration("https://api.infobip.com", "username", "password"))
    
    dest = Destination()
    dest.message_id = "message_111"
    dest.to = "number1aaa"
    
    message = SMSData()
    message.text = "This is an example message."
    message.notify_url = "https://test.com/url_for_delivery_reports"
    message.destinations = [dest]
    
    dest2 = Destination()
    dest2.message_id = "message_222"
    dest2.to = "number2bbb"
    
    message2 = SMSData()
    message2.text = "This is an example message #2."
    message2.notify_url = "https://test.com/url_for_delivery_reports_2"
    message2.destinations = [dest2]
    
    request = SMSAdvancedTextualRequest()
    request.messages = [message, message2]
    
    response = send_sms_client.execute(request)


When the delivery notification is pushed to your server as a HTTP POST request, you can process the body of the message with the following code:

    delivery_status = reports = SMSReportResponse.from_JSON(http_body)

License
-------

This library is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
