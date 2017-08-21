![Column](https://github.com/vmware/python-columnclient/blob/master/column.png "python-columnclient")

[![Build Status](https://travis-ci.org/vmware/python-columnclient.svg?branch=master)](https://travis-ci.org/vmware/python-columnclient)
[![codecov](https://codecov.io/gh/vmware/python-columnclient/branch/master/graph/badge.svg)](https://codecov.io/gh/vmware/python-columnclient)
[![Latest Version](https://img.shields.io/pypi/v/python-columnclient.svg)](https://pypi.python.org/pypi/python-columnclient/)
[![Python Versions](https://img.shields.io/pypi/pyversions/python-columnclient.svg)](https://pypi.python.org/pypi/python-columnclient/)
[![Format](https://img.shields.io/pypi/format/python-columnclient.svg)](https://pypi.python.org/pypi/python-columnclient/)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://github.com/vmware/python-columnclient/blob/master/LICENSE)

## Overview

## Try it out

### Prerequisites

* python 2.7
* requests

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

The python-columnclient project team welcomes contributions from the community. If you wish to contribute code and you have not
signed our contributor license agreement (CLA), our bot will update the issue when you open a Pull Request. For any
questions about the CLA process, please refer to our [FAQ](https://cla.vmware.com/faq). For more detailed information,
refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License
Refer to [LICENSE](LICENSE)