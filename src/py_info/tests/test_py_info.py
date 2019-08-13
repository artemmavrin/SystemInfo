import subprocess
import sys


def test_inside_python():
    import py_info
    py_info()
    py_info.py_info()


def test_inside_terminal():
    python = sys.executable
    script_parts = ['py_info']
    module_parts = [python, '-m', 'py_info']
    script_output = subprocess.check_output(script_parts).decode('utf-8')
    module_output = subprocess.check_output(module_parts).decode('utf-8')
    assert script_output == module_output
