# Moments quickstart

This quick guide aims to help you start with [Infobip Moments API](https://www.infobip.com/docs/api/customer-engagement/moments). After reading it, you should know how to use Moments.

The first step is to create an `ApiClient` instance with some configuration.

```python
from infobip_api_client.api_client import ApiClient, Configuration

client_config = Configuration(
    host="<YOUR_BASE_URL>",
    api_key={"APIKeyHeader": "<YOUR_API_KEY>"},
    api_key_prefix={"APIKeyHeader": "<YOUR_API_PREFIX>"},
)

api_client = ApiClient(client_config)
```

## Flow API

You can now create an instance of `FlowApi` which allows you to manage your flows.

````python
from infobip_api_client.api import FlowApi

api_instance = FlowApi(api_client)
````
### Add participants to flow

To add participants to a flow, you can use the following code:

````python
from infobip_api_client import (
    FlowAddFlowParticipantsRequest,
    FlowParticipant,
    FlowPersonUniqueField,
    FlowPersonUniqueFieldType,
)

campaign_id = 200000000000001

request = FlowAddFlowParticipantsRequest(
        participants=[
            FlowParticipant(
                identify_by=FlowPersonUniqueField(
                    identifier="test@example.com", type=FlowPersonUniqueFieldType.EMAIL
                ),
                variables={"orderNumber": 1167873391},
            ),
        ],
        notify_url="https://example.com"
    )

api_response = api_instance.add_flow_participants(campaign_id, request)
````

### Get a report on participants added to flow

To fetch a report to confirm that all persons have been successfully added to the flow, you can use the following code:

````python
given_operation_id = "03f2d474-0508-46bf-9f3d-d8e2c28adaea"

api_response = api_instance.get_flow_participants_added_report(campaign_id, given_operation_id)
````

### Remove person from flow

To remove a person from a flow, you can use the following code:

````python
external_id = "8edb24b5-0319-48cd-a1d9-1e8bc5d577ab"

api_response = api_instance.remove_people_from_flow(campaign_id=campaign_id, external_id=external_id)
````


## Forms API

You can now create an instance of `FormsApi` which allows you to manage your forms.

````python
from infobip_api_client.api import FormsApi

api_instance = FormsApi(api_client)
````

### Get forms

To get all forms, you can use the following code:

````python
api_response = api_instance.get_forms()
````

### Get form by ID

To get a specific form by ID, you can use the following code:

````python
form_id = "cec5dfd2-4238-48e0-933b-9acbdb2e6f5f"

api_response = api_instance.get_form(form_id)
````

### Increment form view count

To increase the view counter of a specific form, you can use the following code:

````python
api_response = api_instance.increment_view_count(form_id)
````

### Submit form data

To submit data to a specific form, you can use the following code:

````python
form_data_request = {
    "first_name": "John",
    "last_name": "Doe",
    "company": "Infobip",
    "email": "info@example.com"
}
api_response = api_instance.submit_form_data(form_id, form_data_request)
````