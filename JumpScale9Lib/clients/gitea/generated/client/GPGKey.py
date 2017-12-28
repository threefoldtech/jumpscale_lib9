"""
Auto-generated class for GPGKey
"""
from .GPGKeyEmail import GPGKeyEmail
from datetime import datetime
from six import string_types

from . import client_support


class GPGKey(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type can_certify: bool
        :type can_encrypt_comms: bool
        :type can_encrypt_storage: bool
        :type can_sign: bool
        :type created_at: datetime
        :type emails: list[GPGKeyEmail]
        :type expires_at: datetime
        :type id: int
        :type key_id: str
        :type primary_key_id: str
        :type public_key: str
        :rtype: GPGKey
        """

        return GPGKey(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'GPGKey'
        data = json or kwargs

        # set attributes
        data_types = [bool]
        self.can_certify = client_support.set_property(
            'can_certify', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.can_encrypt_comms = client_support.set_property(
            'can_encrypt_comms', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.can_encrypt_storage = client_support.set_property(
            'can_encrypt_storage', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.can_sign = client_support.set_property('can_sign', data, data_types, False, [], False, False, class_name)
        data_types = [datetime]
        self.created_at = client_support.set_property(
            'created_at', data, data_types, False, [], False, False, class_name)
        data_types = [GPGKeyEmail]
        self.emails = client_support.set_property('emails', data, data_types, False, [], True, False, class_name)
        data_types = [datetime]
        self.expires_at = client_support.set_property(
            'expires_at', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.key_id = client_support.set_property('key_id', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.primary_key_id = client_support.set_property(
            'primary_key_id', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.public_key = client_support.set_property(
            'public_key', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
