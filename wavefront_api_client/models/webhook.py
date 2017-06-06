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


class Webhook(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, content_type=None, description=None, created_epoch_millis=None, updated_epoch_millis=None, updater_id=None, creator_id=None, triggers=None, recipient=None, custom_http_headers=None, title=None, template=None, customer_id=None):
        """
        Webhook - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'content_type': 'str',
            'description': 'str',
            'created_epoch_millis': 'int',
            'updated_epoch_millis': 'int',
            'updater_id': 'str',
            'creator_id': 'str',
            'triggers': 'list[str]',
            'recipient': 'str',
            'custom_http_headers': 'dict(str, str)',
            'title': 'str',
            'template': 'str',
            'customer_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'content_type': 'contentType',
            'description': 'description',
            'created_epoch_millis': 'createdEpochMillis',
            'updated_epoch_millis': 'updatedEpochMillis',
            'updater_id': 'updaterId',
            'creator_id': 'creatorId',
            'triggers': 'triggers',
            'recipient': 'recipient',
            'custom_http_headers': 'customHttpHeaders',
            'title': 'title',
            'template': 'template',
            'customer_id': 'customerId'
        }

        self._id = id
        self._content_type = content_type
        self._description = description
        self._created_epoch_millis = created_epoch_millis
        self._updated_epoch_millis = updated_epoch_millis
        self._updater_id = updater_id
        self._creator_id = creator_id
        self._triggers = triggers
        self._recipient = recipient
        self._custom_http_headers = custom_http_headers
        self._title = title
        self._template = template
        self._customer_id = customer_id

    @property
    def id(self):
        """
        Gets the id of this Webhook.

        :return: The id of this Webhook.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Webhook.

        :param id: The id of this Webhook.
        :type: str
        """

        self._id = id

    @property
    def content_type(self):
        """
        Gets the content_type of this Webhook.
        The value of the Content-Type header of the webhook POST request.

        :return: The content_type of this Webhook.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this Webhook.
        The value of the Content-Type header of the webhook POST request.

        :param content_type: The content_type of this Webhook.
        :type: str
        """
        allowed_values = ["application/json", "text/html", "text/plain", "application/x-www-form-urlencoded"]
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def description(self):
        """
        Gets the description of this Webhook.
        Webhook description

        :return: The description of this Webhook.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Webhook.
        Webhook description

        :param description: The description of this Webhook.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def created_epoch_millis(self):
        """
        Gets the created_epoch_millis of this Webhook.

        :return: The created_epoch_millis of this Webhook.
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """
        Sets the created_epoch_millis of this Webhook.

        :param created_epoch_millis: The created_epoch_millis of this Webhook.
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def updated_epoch_millis(self):
        """
        Gets the updated_epoch_millis of this Webhook.

        :return: The updated_epoch_millis of this Webhook.
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """
        Sets the updated_epoch_millis of this Webhook.

        :param updated_epoch_millis: The updated_epoch_millis of this Webhook.
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """
        Gets the updater_id of this Webhook.

        :return: The updater_id of this Webhook.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """
        Sets the updater_id of this Webhook.

        :param updater_id: The updater_id of this Webhook.
        :type: str
        """

        self._updater_id = updater_id

    @property
    def creator_id(self):
        """
        Gets the creator_id of this Webhook.

        :return: The creator_id of this Webhook.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this Webhook.

        :param creator_id: The creator_id of this Webhook.
        :type: str
        """

        self._creator_id = creator_id

    @property
    def triggers(self):
        """
        Gets the triggers of this Webhook.
        A list of occurrences on which this webhook will be fired.  Valid values are ALERT_OPENED, ALERT_UPDATED, ALERT_RESOLVED, ALERT_MAINTENANCE, ALERT_SNOOZED

        :return: The triggers of this Webhook.
        :rtype: list[str]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """
        Sets the triggers of this Webhook.
        A list of occurrences on which this webhook will be fired.  Valid values are ALERT_OPENED, ALERT_UPDATED, ALERT_RESOLVED, ALERT_MAINTENANCE, ALERT_SNOOZED

        :param triggers: The triggers of this Webhook.
        :type: list[str]
        """
        allowed_values = ["ALERT_OPENED", "ALERT_UPDATED", "ALERT_RESOLVED", "ALERT_MAINTENANCE", "ALERT_SNOOZED", "ALERT_INVALID", "ALERT_NO_LONGER_INVALID", "ALERT_TESTING", "ALERT_RETRIGGERED"]
        if not set(triggers).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `triggers` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(triggers)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._triggers = triggers

    @property
    def recipient(self):
        """
        Gets the recipient of this Webhook.
        The URL to which this webhook will be delivered

        :return: The recipient of this Webhook.
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """
        Sets the recipient of this Webhook.
        The URL to which this webhook will be delivered

        :param recipient: The recipient of this Webhook.
        :type: str
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")

        self._recipient = recipient

    @property
    def custom_http_headers(self):
        """
        Gets the custom_http_headers of this Webhook.
        A string->string map specifying the custom HTTP header key / value pairs that will be sent in the requests of this web hook

        :return: The custom_http_headers of this Webhook.
        :rtype: dict(str, str)
        """
        return self._custom_http_headers

    @custom_http_headers.setter
    def custom_http_headers(self, custom_http_headers):
        """
        Sets the custom_http_headers of this Webhook.
        A string->string map specifying the custom HTTP header key / value pairs that will be sent in the requests of this web hook

        :param custom_http_headers: The custom_http_headers of this Webhook.
        :type: dict(str, str)
        """

        self._custom_http_headers = custom_http_headers

    @property
    def title(self):
        """
        Gets the title of this Webhook.
        Webhook Title

        :return: The title of this Webhook.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Webhook.
        Webhook Title

        :param title: The title of this Webhook.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def template(self):
        """
        Gets the template of this Webhook.
        A mustache template that will form the body of the POST request sent as the web hook.

        :return: The template of this Webhook.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this Webhook.
        A mustache template that will form the body of the POST request sent as the web hook.

        :param template: The template of this Webhook.
        :type: str
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")

        self._template = template

    @property
    def customer_id(self):
        """
        Gets the customer_id of this Webhook.

        :return: The customer_id of this Webhook.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this Webhook.

        :param customer_id: The customer_id of this Webhook.
        :type: str
        """

        self._customer_id = customer_id

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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
