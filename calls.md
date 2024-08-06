## Calls
Initialize Calls API client:
```python
    from infobip_api_client.api_client import ApiClient, Configuration
    from infobip_api_client.api import CallsApi
    
    client_config = Configuration(
        host="<YOUR_BASE_URL>",
        api_key={"APIKeyHeader": "<YOUR_API_KEY>"},
        api_key_prefix={"APIKeyHeader": "<YOUR_API_PREFIX>"},
    )
    
    calls_client = ApiClient(client_config)
    api_instance = CallsApi(calls_client)
```
Before starting a call or dialogue you need to set up the application.

#### Start call
After setting up the client you can start a call.
```python
    from infobip_api_client.models import CallRequest, CallsPhoneEndpoint, CallEndpointType, CallState

    request = CallRequest(
        endpoint=CallsPhoneEndpoint(phone_number="<TO_PHONE_NUMBER>", type=CallEndpointType.PHONE),
        var_from="<FROM_PHONE_NUMBER>",
        calls_configuration_id="ORION",
    )
    
    api_response = api_instance.create_call(call_request=request)
    
    call = api_instance.get_call(api_response.id)
    callId = call.id
    callState = call.state
 
    print("Waiting for CallState to be established...")
    while CallState.ESTABLISHED != callState:
        callState = api_instance.get_call(api_response.id).state
```

#### Executing call with text
After starting a call, you can execute text to be said.
```python
    from infobip_api_client.models import CallsSayRequest, CallsLanguage

    call_say_request = CallsSayRequest(
        text="<TEXT_TO_SAY>",
        language=CallsLanguage.EN,
    )
    
    api_response = api_instance.call_say_text(call_id=callId,
                                              calls_say_request=call_say_request)
    
```

#### Start dialogue
After starting a call, you can start a dialogue.
```python
    import time
    from infobip_api_client.models import CallsDialogRequest, CallsDialogCallRequest, CallsWebRtcEndpoint, CallEndpointType

    call_dialog_request = CallsDialogRequest(
        parent_call_id=callId,
        child_call_request=CallsDialogCallRequest(
            endpoint=CallsWebRtcEndpoint(type=CallEndpointType.WEBRTC, identity="<YOUR_IDENTITY>"),
            var_from="<FROM>",
        )
    )
    
    api_response = api_instance.create_dialog(calls_dialog_request=call_dialog_request)
    
    time.sleep(5)
    
    api_instance.hangup_dialog(api_response.id)

```

#### Starting a call for conference
Before starting a conference you need to start a call.
```python
    from infobip_api_client.models import CallRequest, CallEndpointType, CallState

    request = CallRequest(
        endpoint=CallsWebRtcEndpoint(identity="<YOUR_IDENTITY>", type=CallEndpointType.WEBRTC),
        var_from=<FROM>,
        calls_configuration_id="ORION",
    )
    
    api_response = api_instance.create_call(call_request=request)
    
    call = api_instance.get_call(api_response.id)
    callId = call.id
    callState = call.state
 
    print("Waiting for CallState to be established...")
    while CallState.ESTABLISHED != callState:
        callState = api_instance.get_call(api_response.id).state
```

#### Start conference
After starting a call, you can add it to the conference.
```python
    import time
    from infobip_api_client.models import CallsConferenceRequest, CallsAddExistingCallRequest
    
    conference_request = CallsConferenceRequest(
        name="<YOUR_CONFERENCE_NAME>",
        calls_configuration_id="ORION",
    )
    
    api_response = api_instance.create_conference(calls_conference_request=conference_request)
    
    conferenceId = api_response.id
    
    add_existing_call_request = CallsAddExistingCallRequest()
    
    api_instance.add_existing_conference_call(conference_id=conferenceId,
                                              call_id=callId,
                                              calls_add_existing_call_request=add_existing_call_request)

    time.sleep(5)

    api_instance.hangup_conference(conferenceId)
```