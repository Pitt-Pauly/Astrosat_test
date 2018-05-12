#!/usr/bin/env bash

# Steps:
# 1. create venv
# 2. create DB
# 3. gather JSON data - try to get data from web API, if fails then use local file
# 4. load fixture (JSON data)
# 5. start server


# 1. create venv
# python and pip should be installed along with Ubuntu 16.04
python --version
pip --version

# installing pipenv to manage venv and package requirements
pip install --user pipenv
local_base=python -m site --user-base + '/bin'
export PATH=local_base:$PATH

pipenv install --ignore-pipfile

# 2. create DB
# running with sqlite for now

# 3. gather JSON data
# try to get fresh data from endpoint
coreapi get https://data.nasa.gov/resource/9g7e-7hzz.json > facilities/fixtures/new.json

base_path="$( pwd )"
file_to_load="$base_path/facilities/fixtures.json"
if [ -s "$base_path/facilities/fixtures/new.json" ] ; then
    file_to_load="$base_path/facilities/fixtures/new.json"
fi

python manage.py loaddata --app facilities "$file_to_load"