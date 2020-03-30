from types import SimpleNamespace as NS

import yaml
import requests


class ApiOperation(object):
  def __init__(self, name, path, servers, method='GET'):
    self.name = name
    self.path = path
    self.method = method
    self.servers = servers

  def server(self, description):
    for server in self.servers:
      if server['description'] == description:
        return server['url']
    return None

  def __call__(self, server_name=None, server_url=None, headers=None, body=None):
    if server_name:
      server_url = self.server(server_name)
    url = f'{server_url}{self.path}'
    res = requests.request(self.method, url,
      headers=headers,
      data=body)
    return (res.status_code, res.headers, res.text)


class ClientApi(object):
  def __init__(self, operations=None):
    self.__operations = operations if operations else {}

  @classmethod
  def from_paths(cls, paths, servers):
    data = {}
    for kpath, vpath in paths.items():
      for kmethod, vmethod in vpath.items():
        data[vmethod['operationId']] = ApiOperation(vmethod['operationId'],
          kpath,
          servers,
          method=kmethod.upper())
    return cls(operations=data)

  def __getattr__(self, name):
    return self.__operations.get(name)


class Client(object):
  info = NS(title=None, description=None, version=None, license=NS(name=None, url=None))
  api = ClientApi()
  servers = []

  def __init__(self, info=None, servers=None, api_spec=None):
    self.info = info
    self.servers = servers
    self.api = ClientApi.from_paths(api_spec, servers)

  @classmethod
  def from_spec(cls, data):
    parsed = yaml.load(data, Loader=yaml.SafeLoader)

    info = parsed.get('info', dict())
    servers = parsed.get('servers', list())
    license = info.get('license', dict())
    
    return cls(
      info=NS(
        title=info.get('title'),
        description=info.get('description'),
        version=info.get('version'),
        license=NS(name=license.get('name'), url=license.get('url'))),
      servers=servers,
      api_spec=parsed.get('paths')
    )
