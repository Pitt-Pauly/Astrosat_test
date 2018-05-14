#!/usr/bin/env bash

# Steps:
# 1. create venv
# 2. create DB
# 3. gather JSON data - try to get data from web API, if fails then use local file
# 4. load data ( NASA Facilitites JSON data)


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

# add symbolic link to site-packages to install this app (ie. adding to the PYTHONPATH)
ln -s "$(pwd)" "$(pipenv --venv)/lib/python3.6/site-packages/astro_test"


# 2. create DB
# running with sqlite for now
pipenv run python manage.py migrate
pipenv run python manage.py createdummyadmin --username admin --email admin@mysite.com --password supersafe111


# 3. gather JSON data
# default dataset
base_path="$( pwd )"
file_to_load="$base_path/facilities/data/9g7e-7hzz.json"

# try to get fresh data from endpoint, else use the default dataset
echo "Attempting to gather fresh data from NASA API..."
pipenv run coreapi get https://data.nasa.gov/resource/9g7e-7hzz.json > facilities/data/new.json 2> /dev/null

if [ $? -eq 0 ]; then
    echo "Success!"
    if [ -s "$base_path/facilities/data/new.json" ] ; then
        file_to_load="$base_path/facilities/data/new.json"
    fi
else
    echo "Failed to retrieve new dataset, using local data"
fi


# 4. load fixture (this will overwrite any data that's already in the database
pipenv run python manage.py initdb "$file_to_load"