#!/bin/bash

pip3 install --user pipenv
pipenv --python $(which python3)
pipenv shell
pip install -e .
pip install -dev pytest
pipenv shell