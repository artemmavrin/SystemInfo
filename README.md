# Python and System Info


[![Build Status](https://github.com/artemmavrin/py_info/workflows/Python%20package/badge.svg)](https://github.com/artemmavrin/py_info/actions?query=workflow%3A%22Python+package%22)

Get information about the current system, Python, and Python packages.

## Installation

After cloning the repo, either

```bash
make install
```

or

```bash
python setup.py install
```

will install install the `py_info` Python package in your current environment
and create a script called `py_info` on your system path.

## Usage

### Using the `py_info` script

From a terminal, run the `py_info` script:

```bash
$ py_info

System
======
         Platform: Linux-4.9.125-linuxkit-x86_64-with-debian-9.9
         Hostname: cb441e9a1fc5
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
          Version: 3.7.3 (default, Jun 11 2019, 01:05:09) 
                   [GCC 6.3.0 20170516]
       Executable: /usr/local/bin/python
   Implementation: CPython
      Python Path: /usr/local/lib/python37.zip
                   /usr/local/lib/python3.7
                   /usr/local/lib/python3.7/lib-dynload
                   /usr/local/lib/python3.7/site-packages
                   /usr/local/lib/python3.7/site-packages/py_info-0.0.0-py3.7.egg

Packages
========
            NumPy: 1.16.4
            SciPy: 1.3.0
           pandas: 0.25.0
       Matplotlib: 3.1.1
          seaborn: 0.9.0
     scikit-learn: 0.21.2
       TensorFlow: 1.14.0
           Pillow: None
```

### Running the `py_info` package

From a terminal, run `python -m py_info`:

```bash
$ python -m py_info

System
======
...
```

### Using `py_info` inside a Python interpreter or script

The module `py_info` can be imported and called, e.g., from the Python
interpreter:

```text
>>> import py_info
>>> py_info()

System
======
...
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
