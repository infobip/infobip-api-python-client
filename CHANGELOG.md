# Change Log of `infobip_api_client`

All notable changes to the library will be documented in this file.

The format of the file is based on [Keep a Changelog](http://keepachangelog.com/)
and this library adheres to [Semantic Versioning](http://semver.org/) as mentioned in [README.md][readme] file.

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

[readme]: README.mustache