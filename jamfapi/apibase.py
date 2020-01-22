import requests
import base64
import re

PATH_PARAM_PAT = re.compile(r'{([^}][^}]*)}')

class JamfAPI(object):
  def __init__(self, corp, cred):
    self._corp = corp
    self._cred = cred
    self._url = None
  @property
  def url(self):
    if self._url:
      return self._url
    path = self.__class__.PATH
    basepath = self.__class__.BASEPATH
    host = f'https://{self._corp}.jamfcloud.com'
    self._url = f'{host}{basepath}{path}'
    return self._url

  @url.setter
  def url(self, _url):
    self._url = _url

  def _invoke(self, params, cont):
    url = self.url
    keys = re.findall(PATH_PARAM_PAT, url)
    for key in keys:
      url = url.replace('{' + key + '}', params[key])
      del params[key]
    headers = {
      'Accept': 'application/json',
      'Authorization': self.authval
    }
    if 'accept' in params:
      headers['Accept'] = params['accept']
      del params['accept']
    if 'content_type' in params:
      headers['Content-Type'] = params['content_type']
      del params['content_type']
    return cont(url, params, headers)

  def get(self, **kwargs):
    def _callback(_url, _params, _headers):
      qstr = '&'.join(f'{k}={v}' for k, v in _params.items())
      res = requests.get(f'{_url}?{qstr}', headers=_headers)
      return res
    return self._invoke(kwargs, _callback)

  def _prep_postparam(self, params, content_type=None):
    if content_type == 'application/json':
      return json.dumps(params)
    elif content_type == 'application/xml':
      return params['xml']
    return params

  def post(self, **kwargs):
    def _callback(_url, _params, _headers):
      if len(_params.keys()):
        data = self._prep_postparam(_params, _headers.get('Content-Type', None))
        res = requests.post(_url, data=data, headers=_headers)
    return self._invoke(kwargs, _callback)

  def put(self, **kwargs):
    def _callback(_url, _params, _headers):
      if len(_params.keys()):
        data = self._prep_postparam(_params, _headers.get('Content-Type', None))
        res = requests.put(_url, data=data, headers=_headers)
    return self._invoke(kwargs, _callback)

  def delete(self, **kwargs):
    def _callback(_url, _params, _headers):
      if len(_params.keys()):
        data = self._prep_postparam(_params, _headers.get('Content-Type', None))
        res = requests.delete(_url, data=data, headers=_headers)
    return self._invoke(kwargs, _callback)

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
    self._url = None
  @property
  def authval(self):
    token = self._cred.get()
    return f'Bearer {token}'

