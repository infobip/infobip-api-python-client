from datetime import datetime, timedelta

from __init__ import configuration
from infobip.api.model.Destination import Destination
from infobip.api.model.sms.mt.bulks.BulkRequest import BulkRequest
from infobip.api.model.sms.mt.bulks.status.UpdateStatusRequest import UpdateStatusRequest
from infobip.api.model.sms.mt.bulks.status.BulkStatus import BulkStatus
from infobip.api.model.sms.mt.send.Message import Message
from infobip.api.model.sms.mt.send.textual.SMSAdvancedTextualRequest import SMSAdvancedTextualRequest
from infobip.clients import send_multiple_textual_sms_advanced, get_bulks, reschedule_bulk, get_bulk_status, \
    manage_bulk_status

# defining clients
send_sms_client = send_multiple_textual_sms_advanced(configuration)
get_bulks_client = get_bulks(configuration)
reschedule_bulk_client = reschedule_bulk(configuration)
get_bulk_status_client = get_bulk_status(configuration)
manage_bulk_status_client = manage_bulk_status(configuration)


def send_scheduled_message():
    destination = Destination()
    destination.to = "41793026731"

    message = Message()
    message.from_ = "Infobip"
    message.text = "This is a scheduled message"
    message.destinations = [destination]
    message.send_at = (datetime.utcnow() + timedelta(minutes=10)).isoformat()

    request = SMSAdvancedTextualRequest()
    request.messages = [message]

    return send_sms_client.execute(request)


def get_bulk():
    return get_bulks_client.execute(context)


def reschedule_message():
    reschedule_request = BulkRequest()
    reschedule_request.send_at = (datetime.utcnow() + timedelta(minutes=30)).isoformat()

    reschedule_bulk_client.execute(context, reschedule_request)


def get_bulk_status():
    return get_bulk_status_client.execute(context)


def cancel_bulk_status():
    update_status_request = UpdateStatusRequest()
    update_status_request.status = BulkStatus.CANCELED

    return manage_bulk_status_client.execute(context, update_status_request)


response = send_scheduled_message()
context = {"bulkId": response.bulk_id}
sent_message_info = response.messages[0]

print "------------------------------------------------"
print "Scheduled SMS"
print "Message ID: " + sent_message_info.message_id
print "Bulk ID: " + response.bulk_id
print "Receiver: " + sent_message_info.to
print "Message status: " + sent_message_info.status.name
print "------------------------------------------------"

# Fetching bulk via bulkId
bulk_response = get_bulk()
print "Fetched scheduling date."
print "Bulk ID: " + bulk_response.bulk_id
print "SendAt: " + bulk_response.send_at.isoformat()
print "------------------------------------------------"

# Rescheduling the message via the bulkId
reschedule_message()
print "Rescheduling message."
print "------------------------------------------------"

# Fetching bulk via bulkId after rescheduling
bulk_response = get_bulk()
print "Fetched scheduling date after rescheduling."
print "Bulk ID: " + bulk_response.bulk_id
print "SendAt: " + bulk_response.send_at.isoformat()
print "------------------------------------------------"

# Fetching bulk status via bulkId
status_response = get_bulk_status()
print "Fetched bulk status."
print "Bulk status: " + status_response.status
print "------------------------------------------------"

# Change the PENDING status of the scheduled message bulk to CANCELED to cancel the scheduled message
if status_response.status == BulkStatus.PENDING:
    print "Fetched bulk is in PENDING status, attempting to cancel bulk."
    print "------------------------------------------------"

    cancel_bulk_status()

    status_response = get_bulk_status()
    print "Fetched bulk status after update."
    print "Bulk status: " + status_response.status

else:
    print "Fetched bulk is not in PENDING status, aborting update."

print "------------------------------------------------"
