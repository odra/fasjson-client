import json

from fasjson_client.client import Client, ApiOperation


def test_client(fixtures_dir):
  with open(f'{fixtures_dir}/spec.yaml') as f:
    data = f.read()
  client = Client.from_spec(data)
  code, headers, data = client.api.ip(server_name='default')

  assert 'Fedora Account Service JSON API'== client.info.title
  assert  'GPLv3' == client.info.license.name
  assert  'https://www.gnu.org/licenses/quick-guide-gplv3.en.html' == client.info.license.url
  assert 'https://httpbin.org' == client.servers[0]['url']
  assert 200 == code
  assert 'origin' in json.loads(data)
