# Python and System Info

[![GitHub last commit](https://img.shields.io/github/last-commit/artemmavrin/py_info)](https://github.com/artemmavrin/py_info)
[![Build Status](https://github.com/artemmavrin/py_info/workflows/Python%20package/badge.svg)](https://github.com/artemmavrin/py_info/actions?query=workflow%3A%22Python+package%22)
[![Code Coverage](https://codecov.io/gh/artemmavrin/py_info/branch/master/graph/badge.svg)](https://codecov.io/gh/artemmavrin/py_info)

Get information about the current system, Python, and Python packages.

## Installation

1. Use `pip` to install directly from GitHub:

   ```bash
   pip install git+https://github.com/artemmavrin/py_info.git
   ```

2. Alternatively, clone the repo and install manually:

   ```bash
   git clone https://github.com/artemmavrin/py_info.git
   cd py_info
   make install
   ```

Either method will install install the `py_info` Python package in your current
environment and create a script called `py_info` on your system path.

## Usage

### Using the `py_info` script

From a terminal, run the `py_info` script:

```bash
$ py_info

System
======
         Platform: Linux-4.9.184-linuxkit-x86_64-with-debian-10.2
         Hostname: 52a9020e146b
     Machine Type: x86_64
        Processor: ???
       Byte Order: little-endian
Working Directory: /home/py_info
             Path: /usr/local/bin
                   /usr/local/sbin
                   /usr/local/bin
                   /usr/sbin
                   /usr/bin
                   /sbin
                   /bin

Python
======
          Version: 3.7.6 (default, Feb  2 2020, 09:00:14) 
                   [GCC 8.3.0]
       Executable: /usr/local/bin/python
   Implementation: CPython
      Python Path: /usr/local/lib/python37.zip
                   /usr/local/lib/python3.7
                   /usr/local/lib/python3.7/lib-dynload
                   /usr/local/lib/python3.7/site-packages

Packages
========
       matplotlib: 3.1.3
            numpy: 1.18.1
           pandas: 1.0.1
            scipy: 1.4.1
          sklearn: 0.22.1
       tensorflow: 2.1.0
```

Run with the `-h` or `--help` flag to view usage instructions:

```bash
$ py_info --help
usage: py_info [-h] [package [package ...]]

Get information about Python and the system.

positional arguments:
  package     One or more Python packages. (default: ['matplotlib', 'numpy', 'pandas', 'scipy', 'sklearn', 'tensorflow'])

optional arguments:
  -h, --help  show this help message and exit
``` 

Specify which packages you care about by listing them as command line arguments:

```bash
$ py_info numpy tensorflow

System
======
...
Packages
========
            numpy: 1.18.1
       tensorflow: None

```

### Running the `py_info` package

From a terminal, run `python -m py_info`:

```bash
$ python -m py_info

System
======
...
```

You may also specify command line package names here.

### Using `py_info` inside a Python interpreter or script

The module `py_info` can be imported and called, e.g., from the Python
interpreter:

```text
>>> import py_info
>>> py_info()

System
======
...
>>> py_info('sklearn', 'scipy')  # Specify packages as positional arguments

System
======
...
Packages
========
          sklearn: 0.22.1
            scipy: 1.4.1
>>> py_info(['sklearn', 'scipy'])  # Specify a list of packages

System
======
...
Packages
========
          sklearn: 0.22.1
            scipy: 1.4.1
```


## Docker Image

The output shown above was generated in a Docker container based on the
[Dockerfile](Dockerfile) in this repo.
To reproduce it, ensure that [Docker](https://www.docker.com/) is installed, and
run

```bash
make image
make run
```
