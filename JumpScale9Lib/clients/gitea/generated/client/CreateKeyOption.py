"""
Auto-generated class for CreateKeyOption
"""
from six import string_types

from . import client_support


class CreateKeyOption(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type key: str
        :type title: str
        :rtype: CreateKeyOption
        """

        return CreateKeyOption(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'CreateKeyOption'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.key = client_support.set_property('key', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.title = client_support.set_property('title', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
