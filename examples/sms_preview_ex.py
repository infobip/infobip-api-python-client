# -*- coding: utf-8 -*-
from examples import configuration
from infobip.api.model.sms.mt.send.preview.PreviewRequest import PreviewRequest
from infobip.clients import preview_sms

preview_sms_client = preview_sms(configuration)

preview_request = PreviewRequest()
preview_request.text = "Artık Ulusal Dil Tanımlayıcısı ile Türkçe karakterli smslerinizi rahatlıkla iletebilirsiniz."
preview_request.language_code = "TR"
preview_request.transliteration = "TURKISH"

preview_response = preview_sms_client.execute(preview_request)

print "Original message: " + preview_response.original_text + "\n"

print "Your previews: "
for preview in preview_response.previews:
    print "\t" + preview.text_preview
    print "\tNumber of messages: " + str(preview.message_count)
    print "\tCharacters remaining: " + str(preview.characters_remaining) + "\n"
