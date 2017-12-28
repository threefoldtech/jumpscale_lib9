"""
Auto-generated class for Permission52
"""

from . import client_support


class Permission52(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type admin: bool
        :type pull: bool
        :type push: bool
        :rtype: Permission52
        """

        return Permission52(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Permission52'
        data = json or kwargs

        # set attributes
        data_types = [bool]
        self.admin = client_support.set_property('admin', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.pull = client_support.set_property('pull', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.push = client_support.set_property('push', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
