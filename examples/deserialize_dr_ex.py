from infobip.api.model.sms.mt.reports.SMSReportResponse import SMSReportResponse

response_body = """{
  "results": [
    {
      "bulkId": "BULK-ID-123-xyz",
      "messageId": "c9823180-94d4-4ea0-9bf3-ec907e7534a6",
      "to": "41793026731",
      "sentAt": "2015-06-04T13:01:52.933+0000",
      "doneAt": "2015-06-04T13:02:00.134+0000",
      "smsCount": 1,
      "price": {
        "pricePerMessage": 0.0001000000,
        "currency": "EUR"
      },
      "status": {
        "groupId": 3,
        "groupName": "DELIVERED",
        "id": 5,
        "name": "DELIVERED_TO_HANDSET",
        "description": "Message delivered to handset"
      },
      "error": {
        "groupId": 0,
        "groupName": "OK",
        "id": 0,
        "name": "NO_ERROR",
        "description": "No Error",
        "permanent": false
      }
    },
    {
      "bulkId": "BULK-ID-123-xyz",
      "messageId": "MESSAGE-ID-123-xyz",
      "to": "41793026727",
      "sentAt": "2015-06-04T13:01:52.937+0000",
      "doneAt": "2015-06-04T13:02:01.204+0000",
      "smsCount": 1,
      "price": {
        "pricePerMessage": 0.0001000000,
        "currency": "EUR"
      },
      "status": {
        "groupId": 3,
        "groupName": "DELIVERED",
        "id": 5,
        "name": "DELIVERED_TO_HANDSET",
        "description": "Message delivered to handset"
      },
      "error": {
        "groupId": 0,
        "groupName": "OK",
        "id": 0,
        "name": "NO_ERROR",
        "description": "No Error",
        "permanent": false
      }
    }
  ]
}"""

reports = SMSReportResponse.from_JSON(response_body)
print(reports.results[0].status.name)
print(reports.results[0])
