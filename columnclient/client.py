# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

import requests
from six.moves.urllib import parse

from columnclient import credentials
from columnclient import runs


class Client(object):

    def __init__(self, **kwargs):
        self.session = requests.session()
        protocol = kwargs.get('protocol', 'http')
        netloc = '%s:%d' % (kwargs.get('hostname', '127.0.0.1'),
                            kwargs.get('port', 48620))
        self.base_url = parse.urlunparse((protocol, netloc, '', '', '', ''))
        self.credentials = credentials.CredentialsManager(
            self.session, self.base_url)
        self.runs = runs.RunManager(self.session, self.base_url)
