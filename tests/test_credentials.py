# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

from mock import patch
import testtools

from columnclient import credentials


class MockResponse(object):
    """Mock class for requests.Response
    """

    def __init__(self, text='', status_code=200):
        self.text = text
        self.status_code = status_code

    def text(self):
        return self.text


class TestCredentialsManager(testtools.TestCase):

    def setUp(self):
        super(TestCredentialsManager, self).setUp()

    def tearDown(self):
        super(TestCredentialsManager, self).tearDown()

    @patch('requests.session')
    def test_init(self, mock_session):
        base_url = 'http://127.0.0.1:48620'
        cred_manager = credentials.CredentialsManager(mock_session, base_url)
        self.assertEqual(mock_session, cred_manager.session)
        self.assertEqual(base_url + '/credentials', cred_manager.base_url)

    @patch('requests.session')
    def test_get(self, mock_session):
        pass

    @patch('requests.session')
    def test_put(self, mock_session):
        pass
