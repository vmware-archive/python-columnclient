# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

import json

from six.moves.urllib import parse


class Run(object):

    def __init__(self, manager, data):
        self.manager = manager
        for (key, value) in data.items():
            try:
                setattr(self, key, value)
            except AttributeError:
                pass

    def __repr__(self):
        """Return string representation of run attributes."""
        reprkeys = sorted(k
                          for k in self.__dict__.keys()
                          if k[0] != '_' and k != 'manager')
        info = ", ".join("%s=%s" % (k, getattr(self, k)) for k in reprkeys)
        return "<%s %s>" % (self.__class__.__name__, info)

    def delete(self):
        return self.manager.delete(self)


class RunManager(object):

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = parse.urljoin(base_url, 'runs')

    def create(self, playbook_file, **kwargs):
        data = {
            'playbook_path': playbook_file,
            'inventory_file': kwargs.get('inventory_file'),
            'options': {
                'remote_user': kwargs.get('user'),
                'conn_pass': kwargs.get('password'),
                'become_pass': kwargs.get('become_pass'),
                'private_key_file': kwargs.get('private_key_file'),
                'extra_vars': kwargs.get('extra_vars'),
                'subset': kwargs.get('subset'),
                'tags': kwargs.get('tags'),
                'verbosity': kwargs.get('verbosity', 0)
            }
        }
        headers = {'content-type': 'application/json'}
        response = self.session.post(
            self.base_url, data=json.dumps(data), headers=headers)
        return Run(self, json.loads(response.text))

    def get(self, run):
        runs_url = parse.urljoin(self.base_url + '/', run.id)
        response = self.session.get(runs_url)
        return Run(self, json.loads(response.text))

    def list(self):
        response = self.session.get(self.base_url)
        return [Run(self, run) for run in json.loads(response.text)]

    def delete(self, run):
        runs_url = parse.urljoin(self.base_url + '/', run.id)
        self.session.delete(runs_url)
