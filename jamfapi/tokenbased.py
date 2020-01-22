from .apibase import JamfProAPI

class Computers(JamfProAPI):
  PATH = '/preview/computers'

class Departments(JamfProAPI):
  PATH = '/v1/departments'

class Buildings(JamfProAPI):
  PATH = '/v1/buildings'

class Building(JamfProAPI):
  PATH = '/v1/buildings/{id}'
