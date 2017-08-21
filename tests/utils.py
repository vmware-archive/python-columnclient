# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause


class MockResponse(object):
    """Mock class for requests.Response
    """

    def __init__(self, text='', status_code=200):
        self.text = text
        self.status_code = status_code

    def text(self):
        return self.text
