import requests
import base64

class JamfAPI(object):
  def __init__(self, corp, cred):
    self._corp = corp
    self._cred = cred
  @property
  def url(self):
    path = self.__class__.PATH
    basepath = self.__class__.BASEPATH
    host = f'https://{self._corp}.jamfcloud.com'
    return f'{host}{basepath}{path}'

  def get(self, **kwargs):
    qstr = '&'.join(f'{k}={v}' for k, v in kwargs.items())
    res = requests.get(f'{self.url}?{qstr}', headers={
      'Accept': 'application/json',
      'Authorization': self.authval
    })
    return res

class JamfClassicAPI(JamfAPI):
  BASEPATH = '/JSSResource'

  @property
  def authval(self):
    user_id, password = self._cred.get()
    v = base64.b64encode(f'{user_id}:{password}'.encode('ascii')).decode('ascii')
    return f'Basic {v}'

class JamfProAPI(JamfAPI):
  BASEPATH = '/uapi'
  def __init__(self, corp, cred):
    self._corp = corp
    cred._set_corp(corp)
    self._cred = cred
  @property
  def authval(self):
    token = self._cred.get()
    return f'Bearer {token}'

