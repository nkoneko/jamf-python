Python client library for Jamf Pro APIs
========================================

Installation
--------------

```
$ git clone https://github.com/nkoneko/jamf-python.git
$ cd jamf-python
$ python setup.py install
```

Examples
---------------

### Classic API (JSSResouce)

```python
import os
from jamfapi.cred import IdPasswd
from jamfapi.classic import GetComputers

cred = IdPasswd(os.environ['JAMF_USER_ID'], os.environ['JAMF_PASSWORD'])
api = GetComputers(os.environ['JAMF_CORP'], cred)
res = api.get()
```


### Jamf Pro API (Token-based)

```python
import os
from jamfapi.cred import Token
from jamfapi.tokenbased import Computers

cred = Token(os.environ['JAMF_USER_ID'], os.environ['JAMF_PASSWORD'])
api = Computers(os.environ['JAMF_CORP'], cred)
res = api.get(size=5)
res = api.get(size=5, page=1)
```
