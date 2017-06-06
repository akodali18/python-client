# coding: utf-8

"""
    Wavefront Public API

    <p>Wavefront public APIs enable you to interact with Wavefront servers using standard web service API tools. You can use the APIs to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront UI you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DashboardParameterValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, default_value=None, label=None, description=None, values_to_readable_strings=None, dynamic_field_type=None, query_value=None, hide_from_view=None, tag_key=None, parameter_type=None, multivalue=None, allow_all=None):
        """
        DashboardParameterValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'default_value': 'str',
            'label': 'str',
            'description': 'str',
            'values_to_readable_strings': 'dict(str, str)',
            'dynamic_field_type': 'str',
            'query_value': 'str',
            'hide_from_view': 'bool',
            'tag_key': 'str',
            'parameter_type': 'str',
            'multivalue': 'bool',
            'allow_all': 'bool'
        }

        self.attribute_map = {
            'default_value': 'defaultValue',
            'label': 'label',
            'description': 'description',
            'values_to_readable_strings': 'valuesToReadableStrings',
            'dynamic_field_type': 'dynamicFieldType',
            'query_value': 'queryValue',
            'hide_from_view': 'hideFromView',
            'tag_key': 'tagKey',
            'parameter_type': 'parameterType',
            'multivalue': 'multivalue',
            'allow_all': 'allowAll'
        }

        self._default_value = default_value
        self._label = label
        self._description = description
        self._values_to_readable_strings = values_to_readable_strings
        self._dynamic_field_type = dynamic_field_type
        self._query_value = query_value
        self._hide_from_view = hide_from_view
        self._tag_key = tag_key
        self._parameter_type = parameter_type
        self._multivalue = multivalue
        self._allow_all = allow_all

    @property
    def default_value(self):
        """
        Gets the default_value of this DashboardParameterValue.

        :return: The default_value of this DashboardParameterValue.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this DashboardParameterValue.

        :param default_value: The default_value of this DashboardParameterValue.
        :type: str
        """

        self._default_value = default_value

    @property
    def label(self):
        """
        Gets the label of this DashboardParameterValue.

        :return: The label of this DashboardParameterValue.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this DashboardParameterValue.

        :param label: The label of this DashboardParameterValue.
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """
        Gets the description of this DashboardParameterValue.

        :return: The description of this DashboardParameterValue.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DashboardParameterValue.

        :param description: The description of this DashboardParameterValue.
        :type: str
        """

        self._description = description

    @property
    def values_to_readable_strings(self):
        """
        Gets the values_to_readable_strings of this DashboardParameterValue.

        :return: The values_to_readable_strings of this DashboardParameterValue.
        :rtype: dict(str, str)
        """
        return self._values_to_readable_strings

    @values_to_readable_strings.setter
    def values_to_readable_strings(self, values_to_readable_strings):
        """
        Sets the values_to_readable_strings of this DashboardParameterValue.

        :param values_to_readable_strings: The values_to_readable_strings of this DashboardParameterValue.
        :type: dict(str, str)
        """

        self._values_to_readable_strings = values_to_readable_strings

    @property
    def dynamic_field_type(self):
        """
        Gets the dynamic_field_type of this DashboardParameterValue.

        :return: The dynamic_field_type of this DashboardParameterValue.
        :rtype: str
        """
        return self._dynamic_field_type

    @dynamic_field_type.setter
    def dynamic_field_type(self, dynamic_field_type):
        """
        Sets the dynamic_field_type of this DashboardParameterValue.

        :param dynamic_field_type: The dynamic_field_type of this DashboardParameterValue.
        :type: str
        """
        allowed_values = ["SOURCE", "SOURCE_TAG", "METRIC_NAME", "TAG_KEY", "MATCHING_SOURCE_TAG"]
        if dynamic_field_type not in allowed_values:
            raise ValueError(
                "Invalid value for `dynamic_field_type` ({0}), must be one of {1}"
                .format(dynamic_field_type, allowed_values)
            )

        self._dynamic_field_type = dynamic_field_type

    @property
    def query_value(self):
        """
        Gets the query_value of this DashboardParameterValue.

        :return: The query_value of this DashboardParameterValue.
        :rtype: str
        """
        return self._query_value

    @query_value.setter
    def query_value(self, query_value):
        """
        Sets the query_value of this DashboardParameterValue.

        :param query_value: The query_value of this DashboardParameterValue.
        :type: str
        """

        self._query_value = query_value

    @property
    def hide_from_view(self):
        """
        Gets the hide_from_view of this DashboardParameterValue.

        :return: The hide_from_view of this DashboardParameterValue.
        :rtype: bool
        """
        return self._hide_from_view

    @hide_from_view.setter
    def hide_from_view(self, hide_from_view):
        """
        Sets the hide_from_view of this DashboardParameterValue.

        :param hide_from_view: The hide_from_view of this DashboardParameterValue.
        :type: bool
        """

        self._hide_from_view = hide_from_view

    @property
    def tag_key(self):
        """
        Gets the tag_key of this DashboardParameterValue.

        :return: The tag_key of this DashboardParameterValue.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        """
        Sets the tag_key of this DashboardParameterValue.

        :param tag_key: The tag_key of this DashboardParameterValue.
        :type: str
        """

        self._tag_key = tag_key

    @property
    def parameter_type(self):
        """
        Gets the parameter_type of this DashboardParameterValue.

        :return: The parameter_type of this DashboardParameterValue.
        :rtype: str
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type):
        """
        Sets the parameter_type of this DashboardParameterValue.

        :param parameter_type: The parameter_type of this DashboardParameterValue.
        :type: str
        """
        allowed_values = ["SIMPLE", "LIST", "DYNAMIC"]
        if parameter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `parameter_type` ({0}), must be one of {1}"
                .format(parameter_type, allowed_values)
            )

        self._parameter_type = parameter_type

    @property
    def multivalue(self):
        """
        Gets the multivalue of this DashboardParameterValue.

        :return: The multivalue of this DashboardParameterValue.
        :rtype: bool
        """
        return self._multivalue

    @multivalue.setter
    def multivalue(self, multivalue):
        """
        Sets the multivalue of this DashboardParameterValue.

        :param multivalue: The multivalue of this DashboardParameterValue.
        :type: bool
        """

        self._multivalue = multivalue

    @property
    def allow_all(self):
        """
        Gets the allow_all of this DashboardParameterValue.

        :return: The allow_all of this DashboardParameterValue.
        :rtype: bool
        """
        return self._allow_all

    @allow_all.setter
    def allow_all(self, allow_all):
        """
        Sets the allow_all of this DashboardParameterValue.

        :param allow_all: The allow_all of this DashboardParameterValue.
        :type: bool
        """

        self._allow_all = allow_all

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DashboardParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
