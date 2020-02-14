PYTHON := python
PIP := $(PYTHON) -m pip
SETUP := setup.py
SETUPOPTS := -q
IMAGE := py_info
CONTAINER := py_info_test

.PHONY: help install dev image run test

help:
	@ echo "Usage:"
	@ echo "\tmake install   install the script using setuptools."
	@ echo "\tmake dev       install the package for development."
	@ echo "\tmake image     build a Docker image to test the script."
	@ echo "\tmake run       run the script in a Docker container."

install:
	$(PIP) install .

dev:
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade --editable .[dev]

test:
	coverage run -m pytest
	coverage report --show-missing

image:
	docker build -t $(IMAGE) .

run:
	docker run -i --rm --name $(CONTAINER) $(IMAGE)
