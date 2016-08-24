# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class EnumTest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, enum_string=None, enum_integer=None, enum_number=None):
        """
        EnumTest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enum_string': 'str',
            'enum_integer': 'int',
            'enum_number': 'float'
        }

        self.attribute_map = {
            'enum_string': 'enum_string',
            'enum_integer': 'enum_integer',
            'enum_number': 'enum_number'
        }

        self._enum_string = enum_string
        self._enum_integer = enum_integer
        self._enum_number = enum_number


    @property
    def enum_string(self):
        """
        Gets the enum_string of this EnumTest.


        :return: The enum_string of this EnumTest.
        :rtype: str
        """
        return self._enum_string

    @enum_string.setter
    def enum_string(self, enum_string):
        """
        Sets the enum_string of this EnumTest.


        :param enum_string: The enum_string of this EnumTest.
        :type: str
        """
        allowed_values = ["UPPER", "lower"]
        if enum_string not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_string` ({0}), must be one of {1}"
                .format(enum_string, allowed_values)
            )

        self._enum_string = enum_string

    @property
    def enum_integer(self):
        """
        Gets the enum_integer of this EnumTest.


        :return: The enum_integer of this EnumTest.
        :rtype: int
        """
        return self._enum_integer

    @enum_integer.setter
    def enum_integer(self, enum_integer):
        """
        Sets the enum_integer of this EnumTest.


        :param enum_integer: The enum_integer of this EnumTest.
        :type: int
        """
        allowed_values = ["1", "-1"]
        if enum_integer not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_integer` ({0}), must be one of {1}"
                .format(enum_integer, allowed_values)
            )

        self._enum_integer = enum_integer

    @property
    def enum_number(self):
        """
        Gets the enum_number of this EnumTest.


        :return: The enum_number of this EnumTest.
        :rtype: float
        """
        return self._enum_number

    @enum_number.setter
    def enum_number(self, enum_number):
        """
        Sets the enum_number of this EnumTest.


        :param enum_number: The enum_number of this EnumTest.
        :type: float
        """
        allowed_values = ["1.1", "-1.2"]
        if enum_number not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_number` ({0}), must be one of {1}"
                .format(enum_number, allowed_values)
            )

        self._enum_number = enum_number

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
