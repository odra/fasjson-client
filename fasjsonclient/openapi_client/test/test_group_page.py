# coding: utf-8

"""
    Fedora Account Service JSON API

    fajson rest api  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.group_page import GroupPage  # noqa: E501
from openapi_client.rest import ApiException

class TestGroupPage(unittest.TestCase):
    """GroupPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GroupPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.group_page.GroupPage()  # noqa: E501
        if include_optional :
            return GroupPage(
                data = [
                    openapi_client.models.group.group(
                        cn = '0', )
                    ], 
                pagination = openapi_client.models.user_ref_page_pagination.user_ref_page_pagination(
                    current = 56, 
                    previous = 56, 
                    next = 56, )
            )
        else :
            return GroupPage(
        )

    def testGroupPage(self):
        """Test GroupPage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
