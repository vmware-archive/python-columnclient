# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

import urlparse


class CredentialsManager(object):

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = urlparse.urljoin(base_url, 'credentials')

    def get(self, credential):
        pass

    def put(self):
        pass
