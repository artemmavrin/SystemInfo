from sys import modules as _modules
from types import ModuleType as _ModuleType

from .py_info import py_info

__package__ = 'py_info'
__version__ = '0.0.0'
__author__ = 'Artem Mavrin'
__author_email__ = 'artemvmavrin@gmail.com'
__description__ = 'Get information about Python and the system.'
__url__ = 'https://github.com/artemmavrin/py_info'
__doc__ = __description__


# Below is a hack to make this module callable
class _PyInfo(_ModuleType):
    def __init__(self):
        super().__init__(name=__name__, doc=__doc__)
        self.__dict__.update(_modules[__name__].__dict__)

    def __call__(self, *args, **kwargs):
        return py_info(*args, **kwargs)


_modules[__name__] = _PyInfo()
