# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

import json

from mock import patch
import testtools

from columnclient import client
from columnclient import credentials

from tests import utils


DECRYPTED = 'secret'
ENCRYPTED = ('$ANSIBLE_VAULT;1.1;AES256'
             '3261343834623738623036306235646334333831346630346466303839646263'
             '3361336338303330333661323563336465376332303362366163356666656363'
             '0a37383063623339383537336165393533346133353736646462663939393430'
             '3438343038323734663636646362616437383663383166396334393233393663'
             '620a396665383530653738653865336236623935363638616234353734393565'
             '3630')


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
    def test_vault_decrypt(self, mock_session):
        instance = mock_session.return_value
        instance.get.return_value = utils.MockResponse(
            text='{"value": "' + DECRYPTED + '"}')
        col_client = client.Client()
        col_client.credentials.vault_decrypt(ENCRYPTED)

        url = ('http://127.0.0.1:48620/credentials?value=' + ENCRYPTED)
        instance.get.assert_called_once_with(url)

    @patch('requests.session')
    def test_vault_encrypt(self, mock_session):
        instance = mock_session.return_value
        instance.put.return_value = utils.MockResponse(
            text='{"value": "' + ENCRYPTED + '"}')
        col_client = client.Client()
        col_client.credentials.vault_encrypt(DECRYPTED)

        url = 'http://127.0.0.1:48620/credentials'
        data = {'value': DECRYPTED}
        headers = {'content-type': 'application/json'}
        instance.put.assert_called_once_with(url, data=json.dumps(data),
                                             headers=headers)
