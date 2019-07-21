PYTHON := python
SETUP := setup.py
SETUPOPTS := -q

.PHONY: help install

help:
	@ echo "Usage:"
	@ echo "\tmake install   install the package using setuptools."

install:
	$(PYTHON) $(SETUP) $(SETUPOPTS) install
