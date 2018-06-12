# JuiceStock
API for managing e-juice stock and steep

This is a very rudimentary version, but it works !

Technologies used :
*[Python](https://www.python.org/)
*[Pyenv](https://github.com/pyenv/pyenv)
*[Flask](http://flask.pocoo.org/)
*[SqlAlchemy](https://www.sqlalchemy.org/)

Once you clone the project 

1. just execute it with python ./server.py

**And its done !

## How to use it ? 

So far, you can :

* Check if the API's up and running
ex. `curl http://localhost:5002/health`

* Get a Json with all the juices (that sounds... weird) on your database
ex. `curl http://localhost:5002/juices`

* Get an specific Juice searching by ID (further I'll add a more powerfull search feature)
 ex. `curl http://localhost:5002/juice/1`

* Post (add) a new juice !
ex . `curl http://localhost:5002/juice/add/--TODO`
