![Column](https://github.com/vmware/python-columnclient/blob/master/column.png "python-columnclient")

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
Column client is still in alpha state, currently at version 0.0.1.

## Contributing

The python-columnclient project team welcomes contributions from the community. If you wish to contribute code and you have not
signed our contributor license agreement (CLA), our bot will update the issue when you open a Pull Request. For any
questions about the CLA process, please refer to our [FAQ](https://cla.vmware.com/faq). For more detailed information,
refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License
Refer to [LICENSE](LICENSE)