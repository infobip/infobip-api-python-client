from infobip.api.model.sms.mt.send.DeliveryDay import DeliveryDay
from infobip.api.model.sms.mt.send.DeliveryTime import DeliveryTime
from infobip.api.model.sms.mt.send.DeliveryTimeWindow import DeliveryTimeWindow
from infobip.clients import send_multiple_textual_sms_advanced
from infobip.api.model.sms.mt.send.textual.SMSAdvancedTextualRequest import SMSAdvancedTextualRequest
from infobip.api.model.sms.mt.send.Message import Message
from infobip.api.model.Destination import Destination
from .__init__ import configuration

send_sms_client = send_multiple_textual_sms_advanced(configuration)

delivery_time_from = DeliveryTime()
delivery_time_from.hour = 0
delivery_time_from.minute = 0

delivery_time_to = DeliveryTime()
delivery_time_to.hour = 23
delivery_time_to.minute = 59

delivery_days_list = [
    DeliveryDay.MONDAY
]

delivery_time_window = DeliveryTimeWindow()
delivery_time_window.from_ = delivery_time_from
delivery_time_window.to = delivery_time_to
delivery_time_window.days = delivery_days_list

destination = Destination()
destination.message_id = "message_222"
destination.to = "41793026731"

message = Message()
message.from_ = "123412341234"
message.text = "This is a delivery time window message"
message.destinations = [destination]
message.set_delivery_time_window(delivery_time_window)

request = SMSAdvancedTextualRequest()
request.messages = [message]

response = send_sms_client.execute(request)

print(response)
