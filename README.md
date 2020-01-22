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
from jamfapi.classic import Computers

cred = IdPasswd(os.environ['JAMF_USER_ID'], os.environ['JAMF_PASSWORD'])
api = Computers(os.environ['JAMF_CORP'], cred)

res = api.get() # /JSSResource/computers
res = api.get(basic=True) # /JSSResource/computers/subset/basic

api = Computer(os.environ['JAMF_CORP'], cred)
res = api.get(id='1') # /JSSResource/computers/id/1
```

```python
import os
from jamfapi.cred import IdPasswd
from jamfapi.classic import Computer

cred = IdPasswd(os.environ['JAMF_USER_ID'], os.environ['JAMF_PASSWORD'])
api = Computers(os.environ['JAMF_CORP'], cred)

xmlstr = """<?xml version="1.0" encoding="UTF-8"?>
<computer>
  <general>
    <id>1</id>
    <name>Koneko MacBook Pro</name>
    <username>Nekomura, Koneko</username>
  </general>
</computer>
"""

res = api.post(id='1', content_type='application/xml', xml=xmlstr)
"""
POST /JSSResource/computers/id/1
...
Content-Type: application/xml
...

<?xml version="1.0" encoding="UTF-8"?>
<computer>
  <general>
    <id>1</id>
    <name>Koneko MacBook Pro</name>
    <username>Nekomura, Koneko</username>
  </general>
</computer>
"""
```

### Jamf Pro API (Token-based)

```python
import os
from jamfapi.cred import Token
from jamfapi.tokenbased import Computers

cred = Token(os.environ['JAMF_USER_ID'], os.environ['JAMF_PASSWORD'])
api = Computers(os.environ['JAMF_CORP'], cred)
res = api.get(size=5) # /uapi/preview/computers?size=5
res = api.get(size=5, page=1) # /uapi/preview/computers?size=5&page=1
```
