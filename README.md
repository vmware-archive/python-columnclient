![Column](https://github.com/vmware/python-columnclient/blob/master/column.png "python-columnclient")

[![Build Status](https://travis-ci.org/vmware/python-columnclient.svg?branch=master)](https://travis-ci.org/vmware/python-columnclient)
[![codecov](https://codecov.io/gh/vmware/python-columnclient/branch/master/graph/badge.svg)](https://codecov.io/gh/vmware/python-columnclient)
[![Latest Version](https://img.shields.io/pypi/v/columnclient.svg)](https://pypi.org/project/columnclient/)
[![Python Versions](https://img.shields.io/pypi/pyversions/columnclient.svg)](https://pypi.org/project/columnclient/)
[![Format](https://img.shields.io/pypi/format/columnclient.svg)](https://pypi.org/project/columnclient/)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://github.com/vmware/python-columnclient/blob/master/LICENSE)
[![Slack](https://img.shields.io/badge/slack-join%20chat%20%E2%86%92-e01563.svg)](https://code.vmware.com/web/code/join)

## Overview

## Try it out

### Install & Run

Install with pip:
```bash
pip install python-columnclient
```
and in your python code do the following to list runs:
```python
from columnclient import client

col_client = client.Client()
col_client.runs.list()
```

## Documentation
Coming soon...

## Releases & Major Branches
Column client is still in alpha state, currently at version 0.1.0.

## Contributing

The python-columnclient project team welcomes contributions from the community. Before you start working with python-columnclient, please read our [Developer Certificate of Origin](https://cla.vmware.com/dco). All contributions to this repository must be signed as described on that page. Your signature certifies that you wrote the patch or have the right to pass it on as an open-source patch. For more detailed information, refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License
Refer to [LICENSE](LICENSE)
