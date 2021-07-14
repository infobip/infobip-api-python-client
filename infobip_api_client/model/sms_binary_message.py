"""
    Infobip Client API Libraries OpenAPI Specification

    OpenAPI specification containing public endpoints supported in client API libraries.  # noqa: E501

    The version of the OpenAPI document: 1.0.171
    Contact: support@infobip.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from infobip_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


def lazy_import():
    from infobip_api_client.model.sms_binary_content import SmsBinaryContent
    from infobip_api_client.model.sms_delivery_time_window import SmsDeliveryTimeWindow
    from infobip_api_client.model.sms_destination import SmsDestination
    from infobip_api_client.model.sms_regional_options import SmsRegionalOptions

    globals()["SmsBinaryContent"] = SmsBinaryContent
    globals()["SmsDeliveryTimeWindow"] = SmsDeliveryTimeWindow
    globals()["SmsDestination"] = SmsDestination
    globals()["SmsRegionalOptions"] = SmsRegionalOptions


class SmsBinaryMessage(ModelNormal):
    """
    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {
        ("destinations",): {
            "min_items": 1,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "binary": (SmsBinaryContent,),  # noqa: E501
            "callback_data": (str,),  # noqa: E501
            "delivery_time_window": (SmsDeliveryTimeWindow,),  # noqa: E501
            "destinations": ([SmsDestination],),  # noqa: E501
            "flash": (bool,),  # noqa: E501
            "_from": (str,),  # noqa: E501
            "intermediate_report": (bool,),  # noqa: E501
            "notify_content_type": (str,),  # noqa: E501
            "notify_url": (str,),  # noqa: E501
            "regional": (SmsRegionalOptions,),  # noqa: E501
            "send_at": (datetime,),  # noqa: E501
            "validity_period": (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "binary": "binary",  # noqa: E501
        "callback_data": "callbackData",  # noqa: E501
        "delivery_time_window": "deliveryTimeWindow",  # noqa: E501
        "destinations": "destinations",  # noqa: E501
        "flash": "flash",  # noqa: E501
        "_from": "from",  # noqa: E501
        "intermediate_report": "intermediateReport",  # noqa: E501
        "notify_content_type": "notifyContentType",  # noqa: E501
        "notify_url": "notifyUrl",  # noqa: E501
        "regional": "regional",  # noqa: E501
        "send_at": "sendAt",  # noqa: E501
        "validity_period": "validityPeriod",  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SmsBinaryMessage - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            binary (SmsBinaryContent): [optional]  # noqa: E501
            callback_data (str): Additional client's data that will be sent on the notifyUrl. The maximum value is 200 characters.. [optional]  # noqa: E501
            delivery_time_window (SmsDeliveryTimeWindow): Scheduling object that allows setting up detailed time windows in which the message can be sent. Consists of `from`, `to` and `days` properties. `Days` property is mandatory. `From` and `to` properties should be either both included, to allow finer time window granulation or both omitted, to include whole days in the delivery time window.. [optional]  # noqa: E501
            destinations ([SmsDestination]): [optional]  # noqa: E501
            flash (bool): Can be `true` or `false`. If the value is set to `true`, a flash SMS will be sent. Otherwise, a normal SMS will be sent. The default value is `false`.. [optional]  # noqa: E501
            _from (str): Represents a sender ID which can be alphanumeric or numeric. Alphanumeric sender ID length should be between 3 and 11 characters (Example: `CompanyName`). Numeric sender ID length should be between 3 and 14 characters.. [optional]  # noqa: E501
            intermediate_report (bool): The real-time Intermediate delivery report that will be sent on your callback server. Can be `true` or `false`.. [optional]  # noqa: E501
            notify_content_type (str): Preferred Delivery report content type. Can be `application/json` or `application/xml`.. [optional]  # noqa: E501
            notify_url (str): The URL on your call back server on which the Delivery report will be sent.. [optional]  # noqa: E501
            regional (SmsRegionalOptions): Region specific parameters, often specified by local laws. Use this if country or region that you are sending SMS to requires some extra parameters.. [optional]  # noqa: E501
            send_at (datetime): Date and time when the message is to be sent. Used for scheduled SMS (SMS not sent immediately, but at the scheduled time). Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.. [optional]  # noqa: E501
            validity_period (int): The message validity period in minutes. When the period expires, it will not be allowed for the message to be sent. Validity period longer than 48h is not supported (in this case, it will be automatically set to 48h).. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
