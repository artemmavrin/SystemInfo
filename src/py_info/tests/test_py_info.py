import subprocess
import sys


def test_module_inside_python():
    import py_info
    py_info()


def test_function_inside_python():
    import py_info
    py_info.py_info()


def test_module_inside_python_with_positional_arguments(capsys):
    import py_info
    packages = ['numpy', 'scipy']
    py_info(*packages)
    captured1 = capsys.readouterr()
    py_info(packages)
    captured2 = capsys.readouterr()
    assert captured1.out == captured2.out


def test_function_inside_python_with_positional_arguments(capsys):
    import py_info
    packages = ['numpy', 'scipy']
    py_info.py_info(*packages)
    captured1 = capsys.readouterr()
    py_info.py_info(packages)
    captured2 = capsys.readouterr()
    assert captured1.out == captured2.out


def test_script_inside_terminal():
    python = sys.executable
    script_parts = ['py_info']
    module_parts = [python, '-m', 'py_info']
    script_output = subprocess.check_output(script_parts).decode('utf-8')
    module_output = subprocess.check_output(module_parts).decode('utf-8')
    assert script_output == module_output
