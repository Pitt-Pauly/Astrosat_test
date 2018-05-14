
***AstroSat Django Test App***

_by Pierre Pauly_


**Pre-requisites**

Ubuntu 16.04 with python and pip installed

**App setup**

Simply run the setup script, located in the root directory of the app. make sure the script has execute permissions. If it has not run `chmod a+x ./setup.sh`
```
./setup.sh
```
_Note:_ The script will install `pipenv` on your system.

**Starting the App**

```
pipenv run python manage.py runserver
```

**Testing the App**

Included with the app files is a directory called `postman` which contains a Postman collection and environment. 
Both can be imported with the Postman tool and contain a series of requests ready to be sent and played around with.

Just make sure to first:
 - run the setup script  (if you haven't already)
 - start the app!
 - note the IP address and port runserver is using and make sure they match the postman environment variable `base_url`
 - send the requests!

The requests contain basic tests, so the collection can also be run all together, giving you an immediate overview 
of what is working and what is not

Additionally the management commands have basic unit tests written, which can be run as follows:
```
pipenv run python manage.py test
```






