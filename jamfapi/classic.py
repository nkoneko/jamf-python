from .apibase import JamfClassicAPI

class Computers(JamfClassicAPI):
  PATH = '/computers'

  def get(self, **kwargs):
    if 'basic' in kwargs:
      if type(kwargs['basic']) is bool and kwargs['basic']:
        self.url = self.url.replace('/JSSResource/computers', '/JSSResource/computers/subset/basic')
      del kwargs['basic']
    else:
      if self.url.endswith('basic'):
        self.url = self.url.replace('/subset/basic', '')
    return super().get(**kwargs)

class Computer(JamfClassicAPI):
  PATH = '/computers/id/{id}'
