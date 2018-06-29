# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

import json

from six.moves.urllib import parse


class CredentialsManager(object):

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = parse.urljoin(base_url, 'credentials')

    def vault_decrypt(self, value):
        creds_url = '{0}?value={1}'.format(self.base_url, value)
        response = self.session.get(creds_url)
        return json.loads(response.text)

    def vault_encrypt(self, value):
        data_in_json = json.dumps({'value': value})
        headers = {'content-type': 'application/json'}
        response = self.session.put(self.base_url, data=data_in_json,
                                    headers=headers)
        return json.loads(response.text)
