from configparser import ConfigParser


configure = ConfigParser()
print(configure.read('pytest.ini'))

import pytest
