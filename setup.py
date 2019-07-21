from __future__ import print_function

import os
import re

from setuptools import setup, find_packages

HERE = os.path.dirname(__file__)


def resolve_path(*parts):
    return os.path.join(HERE, *parts)


def read(*parts):
    filename = resolve_path(*parts)
    with open(filename, 'r') as f:
        return f.read()


def get_variable(name, parts):
    source = read(*parts)
    pattern = r'^%s = [\'"](?P<value>[^\'"]*)[\'"]' % name
    regex = re.compile(pattern, flags=re.M)
    result = regex.search(source)
    if result:
        return result.group('value')
    error = 'Can\'t find variable %s in %s' % (name, resolve_path(*parts))
    raise RuntimeError(error)


def get_version(*parts):
    return get_variable('__version__', parts)


def get_package_name(*parts):
    return get_variable('__package__', parts)


setup(
    name=get_package_name('src', 'py_info', '__init__.py'),
    version=get_version('src', 'py_info', '__init__.py'),
    description='Get information about Python and the system',
    url='https://github.com/artemmavrin/py_info',
    author='Artem Mavrin',
    author_email='artemvmavrin@gmail.com',
    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
    entry_points={
        'console_scripts': [
            'py_info = py_info:py_info',
        ],
    },
    zip_safe=False,
)
