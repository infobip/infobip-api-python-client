# Change Log of `infobip_api_client`

All notable changes to the library will be documented in this file.

The format of the file is based on [Keep a Changelog](http://keepachangelog.com/)
and this library adheres to [Semantic Versioning](http://semver.org/) as mentioned in [README.md][readme] file.

## [Unreleased]

⚠ IMPORTANT NOTE: From this point onward Python 3.7 is no longer supported. The minimum supported version is Python 3.8 due to dependency updates.

### Added
- `calls.md` which contains examples and explanations for the Calls API

### Security
* Bumped werkzeug dependency from 2.1.2 to 3.0.3
* Bumped pytest-httpserver dependency from 1.0.4 to 1.0.8

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