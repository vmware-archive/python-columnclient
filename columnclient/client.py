# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

import urlparse

import requests

from columnclient import credentials
from columnclient import runs


class Client(object):

    def __init__(self, **kwargs):
        self.session = requests.session()
        protocol = kwargs.get('protocol', 'http')
        netloc = '%s:%d' % (kwargs.get('hostname', '127.0.0.1'),
                            kwargs.get('port', 48620))
        self.base_url = urlparse.urlunparse((protocol, netloc, '', '', '', ''))
        self.credentials = credentials.CredentialsManager(
            self.session, self.base_url)
        self.runs = runs.RunManager(self.session, self.base_url)


if __name__ == '__main__':
    client = Client(hostname='10.146.29.200')
    for run in client.runs.list():
        print(run.id)
        last_run = run

    print(client.runs.get(last_run))
    print(last_run.delete())
