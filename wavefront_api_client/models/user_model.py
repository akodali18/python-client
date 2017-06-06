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


class UserModel(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, identifier=None, customer=None, groups=None):
        """
        UserModel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'identifier': 'str',
            'customer': 'str',
            'groups': 'list[str]'
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'customer': 'customer',
            'groups': 'groups'
        }

        self._identifier = identifier
        self._customer = customer
        self._groups = groups

    @property
    def identifier(self):
        """
        Gets the identifier of this UserModel.
        The unique identifier of this user, which must be their valid email address

        :return: The identifier of this UserModel.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this UserModel.
        The unique identifier of this user, which must be their valid email address

        :param identifier: The identifier of this UserModel.
        :type: str
        """

        self._identifier = identifier

    @property
    def customer(self):
        """
        Gets the customer of this UserModel.
        The id of the customer to which this user belongs

        :return: The customer of this UserModel.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this UserModel.
        The id of the customer to which this user belongs

        :param customer: The customer of this UserModel.
        :type: str
        """

        self._customer = customer

    @property
    def groups(self):
        """
        Gets the groups of this UserModel.
        The permissions granted to this user

        :return: The groups of this UserModel.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this UserModel.
        The permissions granted to this user

        :param groups: The groups of this UserModel.
        :type: list[str]
        """

        self._groups = groups

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
        if not isinstance(other, UserModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
