"""Get information about Python and the system."""

from sys import modules as _modules
from types import ModuleType as _ModuleType

from .py_info import py_info

__package__ = 'py_info'
__version__ = '0.0.0'


# Below is a hack to make this module callable
class _PyInfo(_ModuleType):
    def __init__(self):
        super().__init__(name=__name__, doc=__doc__)
        self.__dict__.update(_modules[__name__].__dict__)

    def __call__(self):
        return py_info()


_modules[__name__] = _PyInfo()
