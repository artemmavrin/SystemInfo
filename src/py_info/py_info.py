"""Display information about the current system, Python, and Python packages."""

from __future__ import print_function


def py_info(file=None):
    import collections
    import importlib
    import os
    import platform
    import sys

    # String to use for missing data
    unknown = '???'

    # System search path
    path = os.environ.get('PATH', None)
    if path is None:
        path = unknown
    else:
        # Convert path to a multi-line string, one line per component
        path = '\n'.join(map(str.strip, path.split(os.pathsep)))

    # Non-Python information about the current system
    system_info = [
        ('Platform', platform.platform() or unknown),
        ('Hostname', platform.node() or unknown),
        ('Machine Type', platform.machine() or unknown),
        ('Processor', platform.processor() or unknown),
        ('Byte Order', sys.byteorder + '-endian'),
        ('Working Directory', os.getcwd()),
        ('Path', path),
    ]

    # Python information
    python_info = [
        ('Version', sys.version),
        ('Executable', sys.executable),
        ('Implementation', platform.python_implementation()),
        ('Python Path', '\n'.join(filter(None, sys.path[1:])).strip()),
    ]

    # Tuples of the form (official name, import name) for important packages
    packages = [
        ('NumPy', 'numpy'),
        ('SciPy', 'scipy'),
        ('pandas', 'pandas'),
        ('scikit-learn', 'sklearn'),
        ('Matplotlib', 'matplotlib'),
        ('seaborn', 'seaborn'),
        ('TensorFlow', 'tensorflow'),
        ('Pillow', 'PIL'),
    ]

    def version(package):
        """Try to get the version string of a package."""
        try:
            module = importlib.import_module(package)
        except ImportError:
            return None

        v = getattr(module, '__version__', unknown)
        return v

    package_info = [(name, version(package)) for name, package in packages]

    # Python dicts are ordered in Python 3.7:
    # https://mail.python.org/pipermail/python-dev/2017-December/151283.html
    # https://docs.python.org/3.7/library/stdtypes.html#typesmapping
    # But in previous versions, insertion order is not guaranteed to be
    # maintained (although it is in the CPython implementation of Python 3.6).
    system_info = collections.OrderedDict(system_info)
    python_info = collections.OrderedDict(python_info)
    package_info = collections.OrderedDict(package_info)

    # Setup for pretty-printing
    all_keys = set().union(system_info, python_info, package_info)
    padding = max(map(len, all_keys))
    separator = ': '

    def pprint_info(label, mapping):
        """Pretty-print an information mapping, including alignment and
        indentation stuff.
        """
        print('', label, '=' * len(label), sep='\n', file=file)
        for k, v in mapping.items():
            if not isinstance(v, str):
                v = str(v)
            if '\n' in v:
                # Make each new line start at the appropriate indentation level
                v = v.replace('\n', '\n' + (' ' * (padding + len(separator))))
            print(k.rjust(padding), separator, v, sep='', file=file)

    pprint_info('System', system_info)
    pprint_info('Python', python_info)
    pprint_info('Packages', package_info)


if __name__ == '__main__':
    py_info()
