# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

from mock import patch
import testtools

from columnclient import client


class TestClient(testtools.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()

    def tearDown(self):
        super(TestClient, self).tearDown()

    @patch('requests.session')
    def test_init(self, mock_session):
        col_client = client.Client()
        self.assertEqual('http://127.0.0.1:48620', col_client.base_url)
