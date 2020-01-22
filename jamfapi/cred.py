import requests
from datetime import datetime, timedelta

class IdPasswd(object):
  def __init__(self, user_id, password):
    self._user_id = user_id
    self._password = password
  def get(self):
    return self._user_id, self._password

class Token(object):
  def __init__(self, user_id, password):
    self._user_id = user_id
    self._password = password
    self._token = None
    self._expires = None
  def _set_corp(self, corp):
    self._corp = corp
  def get(self):
    now = datetime.now()
    if not self._token or (now + timedelta(minutes=3)) >= self._expires:
      res = requests.post(f'https://{self._corp}.jamfcloud.com/uapi/auth/tokens', auth=(self._user_id, self._password))
      resd = res.json()
      self._token = resd['token']
      self._expires = datetime.fromtimestamp(resd['expires'] / 1000)
    return self._token

