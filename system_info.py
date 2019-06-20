"""Display information about the current system, Python, and Python packages."""

from __future__ import print_function


def system_info(file=None):
    import collections
    import importlib
    import os
    import platform
    import sys

    if file is None:
        file = sys.stdout

    mach_info = [('Platform', platform.platform()),
                 ('Hostname', platform.node()),
                 ('Machine Type', platform.machine()),
                 ('Processor', platform.processor()),
                 ('Byte Order', sys.byteorder + '-endian'),
                 ('Working Directory', os.getcwd()), ]

    py_info = [('Version', sys.version),
               ('Executable', sys.executable),
               ('Implementation', platform.python_implementation()),
               ('Search Path', '\n'.join(filter(None, sys.path[1:])).strip()), ]

    packages = [('NumPy', 'numpy'),
                ('SciPy', 'scipy'),
                ('TensorFlow', 'tensorflow'),
                ('Pillow', 'PIL'),
                ('pandas', 'pandas'),
                ('scikit-learn', 'sklearn'),
                ('Matplotlib', 'matplotlib'),
                ('seaborn', 'seaborn'), ]

    def version(package):
        try:
            module = importlib.import_module(package)
        except ImportError:
            return None

        v = getattr(module, '__version__', '???')
        return v

    package_info = [(name, version(package)) for name, package in packages]

    # Python dicts are ordered in Python 3.7:
    # https://mail.python.org/pipermail/python-dev/2017-December/151283.html
    # https://docs.python.org/3.7/library/stdtypes.html#typesmapping
    # But in previous versions, insertion order is not guarenteed to be
    # maintained (although it is in the CPython implementation of Python 3.6).
    mach_info = collections.OrderedDict(mach_info)
    py_info = collections.OrderedDict(py_info)
    package_info = collections.OrderedDict(package_info)

    all_keys = set().union(mach_info, py_info, package_info)
    padding = max(map(len, all_keys))
    separator = ': '

    def pprint_info(label, mapping):
        print('', label, '=' * len(label), sep='\n', file=file)
        for k, v in mapping.items():
            if not isinstance(v, str):
                v = str(v)
            if '\n' in v:
                v = v.replace('\n', '\n' + ' ' * (padding + len(separator)))
            print(k.rjust(padding), separator, v, sep='', file=file)

    pprint_info('Machine', mach_info)
    pprint_info('Python', py_info)
    pprint_info('Packages', package_info)


if __name__ == '__main__':
    system_info()
