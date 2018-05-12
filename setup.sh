#!/usr/bin/env bash

# Steps:
# 1. create venv
# 2. create DB
# 3. gather JSON data - try to get data from web API, if fails then use local file
# 4. load fixture (JSON data)


# 1. create venv
# python and pip should be installed along with Ubuntu 16.04
python --version
pip --version

# installing pipenv to manage venv and dependencies
pip install --user pipenv
local_base="$( python -m site --user-base )/bin"
export PATH=local_base:$PATH

# install dependencies in Pipfile.lock
pipenv install --ignore-pipfile

## activate the venv
#pipenv shell

# 2. create DB
# running with sqlite for now

# 3. gather JSON data

# default dataset
base_path="$( pwd )"
file_to_load="$base_path/facilities/fixtures/9g7e-7hzz.json"

# try to get fresh data from endpoint, else use the default dataset
echo "Attempting to gather fresh data from NASA API..."
pipenv run coreapi get https://data.nasa.gov/resource/9g7e-7hzz.json > facilities/fixtures/new.json 2> /dev/null

if [ $? -eq 0 ]; then
    echo "Success!"
    if [ -s "$base_path/facilities/fixtures/new.json" ] ; then
        file_to_load="$base_path/facilities/fixtures/new.json"
    fi
else
    echo "Failed to retrieve new dataset, using local data"
fi

# 4. load fixture (this will overwrite any data that's already in the database
pipenv run python manage.py loaddata --app facilities "$file_to_load"