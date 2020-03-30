import os

import pytest


@pytest.fixture
def fixtures_dir():
  return f'{os.path.dirname(os.path.realpath(__file__))}/fixtures'