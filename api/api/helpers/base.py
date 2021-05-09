
class Base(object):
  def __init__(self):
    self._configuration = None

  @property
  def configuration(self):
      return self._configuration

  @configuration.setter
  def configuration(self, config):
    self._configuration = config
