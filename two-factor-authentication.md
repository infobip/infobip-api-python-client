## Two-Factor Authentication (2FA)
Initialize 2FA API client:
```python
    from infobip_api_client.api_client import Configuration
    
    client_config = Configuration(
        host="<YOUR_BASE_URL>",
        api_key={"APIKeyHeader": "<YOUR_API_KEY>"},
        api_key_prefix={"APIKeyHeader": "<YOUR_API_PREFIX>"},
    )
    
    tfa_client = ApiClient(api_instance)
    api_instance = TfaApi(tfa_client)
```
Before sending one-time PIN codes you need to set up application and message template.

#### Application setup
The application represents your service. It’s good practice to have separate applications for separate services.
```python

    application_request = TfaApplicationRequest(
        name="My 2FA application",
        configuration=TfaApplicationConfiguration(
            allow_multiple_pin_verifications=True,
            pin_attempts=5,
            pin_time_to_live="10m",
            send_pin_per_application_limit="2/4s",
            send_pin_per_phone_number_limit="2/1d",
            verify_pin_limit="5000/12h"
        ) 
    )
    
    api_response = api_instance.create_tfa_application(tfa_application_request=application_request)
    
    application_id = api_response.application_id
```

#### Message template setup
Message template is the message body with the PIN placeholder that is sent to end users.
```python
    message_request = TfaCreateMessageRequest(
            message_text="Your pin is {{pin}}",
            pin_length=4,
            pin_type=TfaPinType("NUMERIC"),
            language=TfaLanguage("en")
        )
    
    api_response = api_instance.create_tfa_message_template(app_id=application_id,
                                                            tfa_create_message_request=message_request)
    
    message_id == api_response.message_id
```

#### Send 2FA code via SMS
After setting up the application and message template, you can start generating and sending PIN codes via SMS to the provided destination address.
```python
    start_auth_request = TfaStartAuthenticationRequest(
        application_id=application_id,
        message_id=message_id,
        to="41793026727",
        _from="InfoSMS",
        placeholders={"firstName": "John"}
    )
    
    api_response = api_instance.send_tfa_pin_code_over_sms(tfa_start_authentication_request=start_auth_request)
    
    is_success = api_esponse.sms_status == "MESSAGE_SENT";
    pin_id = api_response.pin_id
```

#### Verify phone number
Verify a phone number to confirm successful 2FA authentication.
```python
    verify_pin_request = TfaVerifyPinRequest(pin="1598")

    api_response = api_instance.verify_tfa_phone_number(pin_id=pin_id, tfa_verify_pin_request=verify_pin_request)
    
    verified = api_response.verified
```
