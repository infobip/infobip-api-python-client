# Change Log of `infobip_api_client`

All notable changes to the library will be documented in this file.

The format of the file is based on [Keep a Changelog](http://keepachangelog.com/)
and this library adheres to [Semantic Versioning](http://semver.org/) as mentioned in [README.md][readme] file.

## [ [6.0.0](https://github.com/infobip/infobip-api-python-client/releases/tag/6.0.0) ] - 2026-01-22

🎉 **NEW Major Version of `infobip-api-python-client`.**

⚠️ **IMPORTANT NOTE:** This release contains breaking changes.
All changes, including breaking changes, are addressed and explained in the list bellow.
If you find out that something was not addressed properly, please submit an issue.

From this point onward Python 3.8 is no longer supported. The minimum supported version is Python 3.9 due to dependency updates.

### Added
* Most recent feature set for:
  * [Infobip SMS API](https://www.infobip.com/docs/api/channels/sms)
  * [Infobip 2FA](https://www.infobip.com/docs/api/platform/2fa)
  * [Infobip Voice API](https://www.infobip.com/docs/api/channels/voice)
  * [Infobip Moments API](https://www.infobip.com/docs/api/customer-engagement/moments).
  * [Infobip Email API](https://www.infobip.com/docs/api/channels/email)
    * Introduced `/email/4/messages (V4)`  replacing the `/email/3/send (V3)` endpoint.
    * Introduced `/email/4/logs (V4)` replacing `/email/1/logs (V1)` endpoint.
    * Introduced `/email/4/reports (V4)` replacing `/email/1/reports (V1)` endpoint.
    * Added `Email Templates` support. This should resolve the following issue: [#31](https://github.com/infobip/infobip-api-python-client/issues/31)
* Support for:
  * [Infobip Viber](https://www.infobip.com/docs/api/channels/viber)
    * This should resolve the following issue: [#26](https://github.com/infobip/infobip-api-python-client/issues/26)
  * [Infobip Messages API](https://www.infobip.com/docs/api/platform/messages-api)
* **HTTPS enforcement:** The SDK now automatically ensures HTTPS is used for API host URLs. If `http://` is explicitly provided, a `ValueError` is raised. URLs without a protocol are automatically prefixed with `https://`.


### Changed

**General / Dependencies:**
* **Breaking Change:** The minimum Python supported version bumped to `3.9`.
* Deprecated `API_KEY_PREFIX` in client configuration. It is no longer needed when providing `API_KEY` and `BASE_URL`.[See latest configuration quickstart](README.md#quickstart)
* Bumped `urllib` version support (>= 2.1.0). This should resolve the following issue: [#21](https://github.com/infobip/infobip-api-python-client/issues/21) and close the related pull requests: [#36](https://github.com/infobip/infobip-api-python-client/pull/36), [#35](https://github.com/infobip/infobip-api-python-client/pull/35), [#33](https://github.com/infobip/infobip-api-python-client/pull/33).
* Bumped `python-dateutil` to `2.8.2`.
* Extended `ApiException` for handling `409` and `422` exceptions.
* Extended `MessageStatus` with `action` support.
* `ValidityPeriod` and `SendingSpeedLimit` `time_unit` default value is now set to `MINUTES`.

**Voice:**
* Discriminator type no longer needs to be specified for the following classes:
  * `CallsUrlPlayContent`, `CallsTextPlayContent`, `CallsGenesysCloudProvider`, `CallsBulkPhoneEndpoint`, `CallsCiscoWebexProvider`, `CallsFreshworksProvider`, `CallsFilePlayContent`, `CallsRegisteredSipTrunkRequest`, `CallsRecordingPlayContent`, `CallsRegisteredSipTrunkRequest`, `CallsRegisteredSipTrunkResponse`, `CallsStaticSipTrunkUpdateRequest`, `CallsStaticSipTrunkRequest`, `CallRoutingEndpointDestinationResponse`, `CallRoutingEndpointDestination`, `CallRoutingPhoneCriteria`, `CallRoutingPhoneEndpoint`, `CallRoutingSipCriteria`, `CallRoutingUrlDestination`, `CallRoutingViberEndpoint`, `CallRoutingWebRTCCriteria`, `CallRoutingWebRtcEndpoint`, `CallRoutingWebSocketEndpoint`, `CallsAudioCallbackResponse`, `CallsCreateProviderSipTrunkResponse`, `CallsCreateRegisteredSipTrunkResponse`, `CallsCreateStaticSipTrunkResponse`, `CallsDialCallbackResponse`, `CallsDtmfTermination`, `CallsFreshworksProvide`, `CallsGenesysCloudProvide`, `CallsMediaStreamingConfigRequest`, `CallsMediaStreamingConfigResponse`, `CallsPhoneEndpoint`, `CallsProviderSipTrunkRequest`, `CallsProviderSipTrunkResponse`, `CallsProviderSipTrunkUpdateRequest`, `CallsSipEndpoint`, `CallsStaticSipTrunkResponse`, `CallsWebsocketEndpoint`, `CallsWebsocketEndpointConfigResponse`, `CallsWebsocketEndpointConfigRequest`, `CallsWebRtcEndpoint`, `CallsViberEndpoint`.
* `CallsCreateRegisteredSipTrunkResponse`, `CallsRegisteredSipTrunkRequest`, `CallsRegisteredSipTrunkUpdateRequest`, and `CallsSipTrunkResponse` now have default values set for `dtmf`, `fax`, and `anonymisation` fields.
* `CallsCreateStaticSipTrunkResponse`, `CallsStaticSipTrunkRequest`, and `CallsStaticSipTrunkUpdateRequest` now have default values set for `dtmf`, `fax`, `strategy`, and `anonymisation` fields.
* `CallsStaticSipTrunkResponse` strategy field default is now set to `FAILOVER`.
* Extended `CallEndpoint` and `CallRoutingEndpoint` with `WHATSAPP` support.
* Extended `CallRoutingCriteria` with `APPLICATION` type support.
* Extended `CallRoutingDestination` with `ApplicationDestination` support.
* Extended `CallRoutingRouteResponse` with `status` and `order` field support.
* Extended `CallRoutingSipEndpoint` with `from` field support.
* Extended `CallRoutingWebSocketEndpoint` with `custom_data` field support.
* Extended `Call` with `external_id` field support.
* Extended `CallsAddExistingCallRequest` with `role` and `custom_data` field support.
* Extended `CallsAddNewCallRequest` with `role` field support.
* Extended `CallsDialCallbackResponse` with `machine_detection` support.
* Extended `CallsDialogLogResponse` with `hangup_source` support.
* Extended `CallsDialogState` with `TRANSFERRING` state support.
* Extended `CallsMachineDetectionProperties` with `confidence_rating` field support.
* Extended `CallsParticipant` with `role` support.
* Extended `CallsProviderTrunkType` and `CallsProvide` with `OPENAI_REALTIME` support.
* Extended `CallsSearchResponse`, `CallsUpdateScenarioResponse`, and `CallsUpdateScenarioRequest` with `notify_url`, `notify_content_type`, and `record` fields.
* Extended `CallsSpeechCaptureRequest` with `terminate_on_key_phrase`, `custom_dictionary`, and `advanced_formatting` support.
* Extended `CallsTranscription` with `custom_dictionary`, and `advanced_formatting` support.
* Extended `CallsVoiceData` with `answered_by` and `call_recording_file_id` field support.
* Extended `CallsVideoMediaProperties` and `CallsUpdateRequest` with `blind` field support.
* Extended `CallVoice` with additional voices.
* Extended `CallsLanguage` with different languages.
* Extended `CallsMachineDetectionRequest` with `detection_time` support.
* **Breaking Change:** `CallsMediaStreamConfigRequest` type is now required to construct the class.
* `CallsSpeechCaptureRequest` `key_phrases` is now an optional field.

**SMS:**
* Unified `SmsWebhookInboundReport` with the existing `SmsInboundMessage` model.
* Extended `SmsLogsResponse` with cursor-based pagination support.
* Extended `SmsRequestSchedulingSettings` with `bulk_id` validation.
* Extended `SmsDestination` with `message_id` validation.

**2FA (TFA):**
* Extended `TfaStartEmailAuthenticationRequest` with `landing_page_placeholders` support.
* Extended `TfaStartAuthenticationResponse` with `external_message_id` support.
* Extended `TfaStartAuthenticationRequest` and `TfaResendPinRequest` with `track_delivery` support.
* Extended `TfaMessage`, `TfaEmailMessage`, `TfaUpdateEmailMessageRequest`, and `TfaCreateEmailMessageRequest` with `landing_page_id` support.

**Email:**
* **Breaking Change:** `EmailResponseDetails` `to` and `status` fields are now **required**.
* **Breaking Change:** `EmailBulkUpdateStatusResponse` `bulk_id` and `status` fields are now **required**.
* **Breaking Change:** `EmailBulkStatusResponse`, `EmailBulkStatusInfo`, and `EmailBulkScheduleResponse` `external_bulk_id` and `bulks` fields are now **required**.
* **Breaking Change:** `EmailBulkRescheduleResponse` and `EmailBulkInfo` `bulk_id` and `send_at` fields are now **required**.
* **Breaking Change:** `EmailReport` class changes based on the new API specification after the migration to V4 endpoint. Introduced `sender`, `callback_data`, `platform`, `campaign_refence_id`, `attempt_count`, `time_to_first_attempt` and removed `application_id` and `entity_id` fields.
* **Breaking Change:** `EmailWebhookTrackResponse` class changes based on the new API specification after the migration to V4 endpoint. Introduced `eventId`, `sender` and changed `message_id` type from `StrictStr` to `Union[StrictFloat, StrictInt]`.
* Extended `EmailLogsResponse` with cursor-based pagination support.
* Extended `EmailReportsResult` with `email_results` field.
* Extended `EmailDomainResponse` model with `blocklist_configration_level` field.
* Extended `EmailIpDetailResponse` and `EmailIpResponse` model with `ip_addresses` field.

**Number Masking:**
* Extended `NumberMaskingStatusRequest` with `machine_detection_result` field support.

### Removed

**Voice:**
* Removed `creation_method` support from `CallsFile`.
* Removed `UNKNOWN` type support from `CallsDetectionResult`.
* Removed `record` field support from `CallsIvrMessage`.
* Removed `JOHANNESBURG_11` support from `CallsRecordingLocation`.
* Removed `return_path_address` from `EmailDomainResponse` and `EmailAddDomainRequest`.

**General:**
* Removed unused `CallsCreationMethod`, `CallsRegionList`, `EmailReturnPathAddressRequest`, `WebhookMessageCount` classes.

These changes align the SDK with the current API specification, ensuring consistency and reliability in future updates.

## [ [5.1.1](https://github.com/infobip/infobip-api-python-client/releases/tag/5.1.1) ] - 2025-05-09

### Added
* [FileParameter](https://github.com/infobip/infobip-api-python-client/blob/master/infobip_api_client/models/file_parameter.py) class that represents a File passed to the API as a Parameter, allows using different backends for files.

### Fixed
* Adding trackingPixelPosition to Send fully featured email API method (https://github.com/infobip/infobip-api-python-client/issues/29).

## [ [5.1.0](https://github.com/infobip/infobip-api-python-client/releases/tag/5.1.0) ] - 2025-03-21

⚠️ **IMPORTANT NOTE:** This release contains breaking changes.
All changes, including breaking changes, are addressed and explained in the list bellow.
If you find out that something was not addressed properly, please submit an issue.

### Added
* Most recent feature set for:
    * [Infobip Voice API](https://www.infobip.com/docs/api/channels/voice).
        * Support for Calls Configuration.
    * [Infobip SMS API](https://www.infobip.com/docs/api/channels/sms).
    * [Infobip 2FA API](https://www.infobip.com/docs/api/platform/2fa).
    * [Infobip Email API](https://www.infobip.com/docs/api/channels/email).
        * Support for Email IP Management instead of set of deprecated Email IP endpoints. Check [Email API documentation](https://www.infobip.com/docs/api/channels/email) for additional details.
    * [Infobip Moments](https://www.infobip.com/docs/api/customer-engagement/moments).
* **Added** support for `WEBSOCKET` option in call routing endpoint.
* **Added** new Calls error code type: `MACHINE_DETECTED`.
* **Added** support for `CallsProviderSipTrunkUpdateRequest`.

### Changed

- General
  - **Unified** `message_response`, `message_response_details`, `message_group_error`, `sending_speed_limit`, `security_config_type`, `api_exception` and `speed_limit_time_unit`.

- Voice API
  - **Updated** `calls_update_scenario_response.last_usage_date` field type from `datetime` → `date`.
  - **Updated** `calls_search_response.last_usage_date` field type from `datetime` → `date`.
  - **Removed** `priority` and `weight` duplicated fields from `call_routing_endpoint_destination`.
  - **Removed** `priority` and `weight` duplicated fields from `call_routing_url_destination`.
  - Adjusted Sip Trunk models in location processing. Location is now implemented as a string to increase usability of the feature. Locations should be passed as strings to the Sip Trunk request model in all upcoming SDK versions.
      - **Updated** `call_sip_trunk_response.location` field type from `Optional[CallsSipTrunkLocation]` → `Optional[StrictStr]`.
  - **Updated** `calls_transcription.language` field type from `CallsLanguage` → `CallTranscriptionLanguage`.
  - **Updated** `calls_speech_capture_request.language` field type from `CallsLanguage` → `CallTranscriptionLanguage`.
  - **Removed** `calls_voice` – Certain fields removed due to API updates.
  - **Fixed** Number Masking UTC date-time deserialization in setup response model.
  - **Fixed** Number Masking content schema when uploading audio files.
  - Adjusted IVR models in script processing. Scenario scripting is now implemented as a raw string to increase usability of the feature. Scripts should be passed as strings to the IVR request model in all upcoming SDK versions.
        - **Updated** `calls_update_scenario_response.script` field type from `Optional[Dict[str, Any]]` → `Optional[StrictStr]`.
        - **Updated** `calls_update_scenario_request.script` field type from `List[CallsScriptInner]` → `StrictStr`.
        - **Updated** `calls_search_response.script` and `else` fields type from `Optional[Dict[str, Any]]` → `Optional[StrictStr]`.
  - **Updated** `calls_get_voices_response.voices` field type from `Optional[List[CallsVoice]]` → `Optional[List[CallsSynthesisVoice]]`.
  - **Removed** `call_routing_url_security_config_type` – Unified into `security_config_type` enumeration class.
  - **Removed** `call_url_security_config_type` – Unified into `security_config_type` enumeration class.

- Email API
  - **Updated** `email_supression_info.created_date` field type from `StrictStr` → `datetime`.
  - **Removed** `email_single_message_status` – Now integrated into the unified `MessageStatus` class.
  - Email suppression type enum models are now consolidated. Use `email_suppression_type` and `email_add_suppression_type` instead of `email_add_delete_suppression_type` and `email_get_suppression_type`.

### Removed:
- All the Calls IVR script related class and from now on all the scripts are processed as `String`:
  - `calls_call_api`
  - `calls_capture`
  - `calls_collect`
  - `calls_dial`
  - `calls_dial_to_many`
  - `calls_dial_to_webrtc`
  - `calls_dial_to_conversations`
  - `calls_for_each`
  - `calls_go_to`
  - `calls_hangup`
  - `calls_if_then_else`
  - `calls_machine_detection`
  - `calls_pause`
  - `calls_play`
  - `calls_play_from_recording`
  - `calls_record`
  - `calls_repeat_until`
  - `calls_repeat_while`
  - `calls_say`
  - `calls_send_sms`
  - `calls_set_variable`
  - `calls_switch_case`
  - `calls_while_do`

- **Removed** `DISCONNECTED` option from `call_state`.

These changes align the SDK with the current API specification, ensuring consistency and reliability in future updates.

## [ [5.0.0](https://github.com/infobip/infobip-api-python-client/releases/tag/5.0.0) ] - 2024-12-23

🎉 **NEW Major Version of `infobip-api-python-client`.**

⚠️ **IMPORTANT NOTE:** This release contains compile time breaking changes.
All changes, including breaking changes, are addressed and explained in the list bellow.
If you find out that something was not addressed properly, please submit an issue.

From this point onward Python 3.7 is no longer supported. The minimum supported version is Python 3.8 due to dependency updates.

### Added
* Most recent feature set for:
  * [Infobip SMS API](https://www.infobip.com/docs/api/channels/sms)
    * Introduced `/sms/3/messages (V3)`  replacing the `/sms/2/text/advanced (V2)` and `/sms/2/binary/advanced (V2)` endpoints.
    * Introduced `/sms/3/reports (V3)` replacing `/sms/1/reports (V1)` endpoint.
    * Introduced `/sms/3/logs (V3)` replacing `/sms/1/logs (V1)` endpoint.
  * [Infobip 2FA](https://www.infobip.com/docs/api/platform/2fa)
  * [Infobip Voice API](https://www.infobip.com/docs/api/channels/voice)
* Support for:
  * [Infobip Moments API](https://www.infobip.com/docs/api/customer-engagement/moments).
  * [Infobip Email API](https://www.infobip.com/docs/api/channels/email)
* `calls.md` which contains examples and explanations for the Calls API.
* `build.yml` workflow to ensure project build and test integrity.
* `snyk.yml` workflow, which serves the purpose of identifying and addressing dependency vulnerabilities in the project.
* `sonar.yml` workflow to analyze the source code, enhancing code quality and maintainability.

### Changed
* **Fixes and changes**
  * Across all voice models, the 'applicationId' field has been removed and replaced with the `platform` field, as it better reflects the state of the endpoint.
  * Introduced the new [sms_message](infobip_api_client/models/sms_message.py) class to replace `sms_textual_message` and `sms_binary_message`, providing a unified structure for SMS messaging.
  * Added a content field within `sms_message` to define the message content. This supports both textual and binary messages, which can be created using [sms_text_content](infobip_api_client/models/sms_text_content.py) or [sms_binary_content](infobip_api_client/models/sms_binary_content.py), respectively.
  * Unified request classes by replacing `sms_advaned_textual_request` and `sms_advaned_binary_request` with the new [sms_request](infobip_api_client/models/sms_request.py) class.
  * Consolidated sending functions: use `send_sms_messages` instead of the `send_sms_message` and `send_binary_sms_message` functions.
  * Removed delivery time window configuration classes (`sms_delivery_time_window`, `call_routing_allowed_time_window`, `calls_delivery_time_window`, `calls_time_window`) in favor of a unified class: [delivery_time_window](infobip_api_client/models/delivery_time_window.py)
  * Removed delivery time configuration classes (`sms_delivery_time_to`, `sms_delivery_time_from`, `calls_time_windows_point`, `call_routing_allowed_time_from`, `call_routing_allowed_time_to`) in favor of a unified class: [delivery_time](infobip_api_client/models/delivery_time.py)
  * Removed URL options configuration class (`sms_url_options`) in favor of a unified class: [url_options](infobip_api_client/models/url_options.py)
  * Removed TurkeyIys options configuration class (`sms_turkey_iys_options`) in favor of a unified class: [turkey_iys_options](infobip_api_client/models/turkey_iys_options.py)
  * Removed delivery day enumeration classes (`sms_delivery_day`, `calls_delivery_day`, `call_routing_allowed_day`) in favor of a unified class: [delivery_day](infobip_api_client/models/delivery_day.py)
  * Removed speed limit time unit enumeration class (`sms_speed_limit_time_unit`) in favor of a unified class: [speed_limit_time_unit](infobip_api_client/models/speed_limit_time_unit.py)
  * Renamed class from `calls_public_conference_recording` to `calls_conference_recording`.
  * Renamed class from `calls_pegasus_provider` to `calls_provider`.
  * Renamed class from `calls_pegasus_provider_trunk_type` to `calls_provider_trunk_type`.

### Security
- Bumped werkzeug dependency from `2.1.2` to `3.0.3`.
- Bumped pytest-httpserver dependency from `1.0.4` to `1.0.8`.
- Bumped setuptools dependency to `72.1.0`.

### Removed
- `wheel` dependency due to an upgrade of `setuptools` to version `72.0.1`. As of `setuptools` version `70.1`, it is no longer necessary to have `wheel` installed for functionality.

## [ [4.0.0](https://github.com/infobip/infobip-api-python-client/releases/tag/4.0.0) ] - 2024-06-13
🎉 **NEW Major Version of `infobip_api_client`.**

⚠ IMPORTANT NOTE: This release contains breaking changes!

In this release, we updated and modernized the `infobip_api_client` library. It is auto-generated and different from the previous version.

### Added
- Support for [Infobip Calls API](https://www.infobip.com/docs/api/channels/voice/calls)
- Support for [Infobip Click To Call API](https://www.infobip.com/docs/api/channels/voice/click-to-call)
- Support for [Infobip Call Routing API](https://www.infobip.com/docs/api/channels/voice/routing)

## [ [3.0.3](https://github.com/infobip/infobip-api-python-client/releases/tag/3.0.3) ] - 2023-07-03

### General
- Added test infrastructure and a simple test

## [ [3.0.2](https://github.com/infobip/infobip-api-python-client/releases/tag/3.0.2) ] - 2023-07-03

### Fixed
- ApiAttributeError when deserializing response that contains unknown fields

## [ [3.0.0](https://github.com/infobip/infobip-api-python-client/releases/tag/3.0.0) ] - 2021-07-14

🎉 **NEW Major Version of `infobip_api_client`.**

⚠ **IMPORTANT NOTE:** This release contains breaking changes!

In this release, we updated and modernized the `infobip_api_client` library. It is auto-generated and completely different from the previous version.

### Added
- Support for [Infobip Two-factor Authentication API](https://www.infobip.com/docs/api#channels/sms/send-2fa-pin-code-over-sms)
- `CONTRIBUTING.md` which contains guidelines for creating GitHub issues

### Changed
- Targeting minimum Python version 3.6
- Models, structure, examples, etc. for [Infobip SMS API](https://www.infobip.com/docs/api#channels/sms)
- Library dependencies
- `README.md` which contains necessary data and examples for quickstart as well as some other important information about versioning, licensing, etc.

### Removed
- Support for [Infobip Omni API](https://www.infobip.com/docs/api#channels/omni-failover) (to be included back in one of the next releases)
- Support for [Infobip Account API](https://www.infobip.com/docs/api#platform-&-connectivity/account-management) `getAccountBalance` method (to be included back in one of the next releases)
- Support for [Infobip Number Context API](https://www.infobip.com/docs/api#platform-&-connectivity/number-lookup) methods (to be included back in one of the next releases)
- Support for [Infobip SMS Tracking API](https://www.infobip.com/docs/sms/tracking) methods (to be included back in one of the next releases)
- `examples` directory

[readme]: README.md