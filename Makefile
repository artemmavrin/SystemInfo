PYTHON := python
SETUP := setup.py
SETUPOPTS := -q
IMAGE := py_info
CONTAINER := py_info_test

.PHONY: help install dev image run

help:
	@ echo "Usage:"
	@ echo "\tmake install   install the script using setuptools."
	@ echo "\tmake dev       install the package for development."
	@ echo "\tmake image     build a Docker image to test the script."
	@ echo "\tmake run       run the script in a Docker container."

install:
	$(PYTHON) $(SETUP) $(SETUPOPTS) install

dev:
	$(PYTHON) -m pip install --upgrade --editable .

image:
	docker build -t $(IMAGE) .

run:
	docker run -i --rm --name $(CONTAINER) $(IMAGE)
