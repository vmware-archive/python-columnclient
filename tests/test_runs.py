# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

import json

from mock import patch
import testtools

from columnclient import client
from columnclient import runs

from tests import utils


class TestRunManager(testtools.TestCase):

    def setUp(self):
        super(TestRunManager, self).setUp()

    def tearDown(self):
        super(TestRunManager, self).tearDown()

    @patch('requests.session')
    def test_init(self, mock_session):
        base_url = 'http://127.0.0.1:48620'
        run_manager = runs.RunManager(mock_session, base_url)
        self.assertEqual(mock_session, run_manager.session)
        self.assertEqual(base_url + '/runs', run_manager.base_url)

    @patch('requests.session')
    def test_create(self, mock_session):
        instance = mock_session.return_value
        instance.post.return_value = utils.MockResponse(
            text='{"playbook_path":"/hello_world.yml",'
                 '"progress": 0,"state":"RUNNING",'
                 '"id":"0904eef0-563f-47c4-b586-851c6ea2ba88"}',
        )
        col_client = client.Client()
        result = col_client.runs.create('playbook_file',
                                        inventory_file='inventory_file',
                                        user='user',
                                        password='password',
                                        private_key_file='private_key_file')

        url = 'http://127.0.0.1:48620/runs'
        data = {
            'playbook_path': 'playbook_file',
            'inventory_file': 'inventory_file',
            'options': {
                'remote_user': 'user',
                'conn_pass': 'password',
                'become_pass': None,
                'private_key_file': 'private_key_file',
                'extra_vars': None,
                'subset': None,
                'tags': None,
                'verbosity': 0
            }
        }
        headers = {'content-type': 'application/json'}
        instance.post.assert_called_once_with(url, data=json.dumps(data),
                                              headers=headers)
        self.assertEqual('/hello_world.yml', result.playbook_path)
        self.assertEqual(0, result.progress)
        self.assertEqual('RUNNING', result.state)
        self.assertEqual('0904eef0-563f-47c4-b586-851c6ea2ba88', result.id)

    @patch('requests.session')
    def test_get(self, mock_session):
        instance = mock_session.return_value
        instance.get.return_value = utils.MockResponse(
            text='{"playbook_path":"/hello_world.yml",'
                 '"progress": 0,"state":"RUNNING",'
                 '"id":"0904eef0-563f-47c4-b586-851c6ea2ba88"}',
        )
        run_data = {'playbook_path': '/hello_world.yml',
                    'progress': 0,
                    'state': 'RUNNING',
                    'id': '0904eef0-563f-47c4-b586-851c6ea2ba88'}
        run = runs.Run('manager', run_data)
        col_client = client.Client()
        result = col_client.runs.get(run)

        url = ('http://127.0.0.1:48620/runs/'
               '0904eef0-563f-47c4-b586-851c6ea2ba88')
        instance.get.assert_called_once_with(url)
        self.assertEqual('/hello_world.yml', result.playbook_path)
        self.assertEqual(0, result.progress)
        self.assertEqual('RUNNING', result.state)
        self.assertEqual('0904eef0-563f-47c4-b586-851c6ea2ba88', result.id)

    @patch('requests.session')
    def test_list(self, mock_session):
        url = 'http://127.0.0.1:48620/runs'
        instance = mock_session.return_value
        instance.get.return_value = utils.MockResponse(
            text='[{"playbook_path":"/hello_world.yml",'
                 '"progress": 0,"state":"RUNNING",'
                 '"id":"0904eef0-563f-47c4-b586-851c6ea2ba88"}]',
            status_code=200
        )

        col_client = client.Client()
        result = col_client.runs.list()
        instance.get.assert_called_once_with(url)
        self.assertEqual('/hello_world.yml', result[0].playbook_path)
        self.assertEqual(0, result[0].progress)
        self.assertEqual('RUNNING', result[0].state)
        self.assertEqual('0904eef0-563f-47c4-b586-851c6ea2ba88', result[0].id)

    @patch('requests.session')
    def test_delete(self, mock_session):
        instance = mock_session.return_value
        instance.delete.return_value = utils.MockResponse(status_code=204)
        run_data = {'playbook_path': '/hello_world.yml',
                    'progress': 0,
                    'state': 'RUNNING',
                    'id': '0904eef0-563f-47c4-b586-851c6ea2ba88'}
        run = runs.Run('manager', run_data)
        col_client = client.Client()
        col_client.runs.delete(run)

        url = ('http://127.0.0.1:48620/runs/'
               '0904eef0-563f-47c4-b586-851c6ea2ba88')
        instance.delete.assert_called_once_with(url)
