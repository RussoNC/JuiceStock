# JuiceStock
API for managing e-juice stock and steep

This is a very rudimentary version, but it works !

Technologies used :
* [Python](https://www.python.org/)
* [Pyenv](https://github.com/pyenv/pyenv)
* [Flask](http://flask.pocoo.org/)
* [SqlAlchemy](https://www.sqlalchemy.org/)

Once you clone the project 

* Execute it with `python ./server.py`

**And its done !**

## How to use it ? 

So far, you can :

* Check if the API's up and running

 ⋅⋅⋅`curl http://localhost:5002/health`

* Get a Json with all the juices (that sounds... weird) on your database

 ⋅⋅⋅`curl http://localhost:5002/juices`

* Get an specific Juice searching by ID (further I'll add a more powerfull search feature)

 ⋅⋅⋅`curl http://localhost:5002/juice/1`

* Post (add) a new juice !

 ⋅⋅⋅`curl http://localhost:5002/juice/add -d "id=3&date_fabricated=2018-06-11 10:21:00&desc='Did it with curl !'&quantity=30&nic_value=3&date_steeped=2018-06-11 10:21:00" -X POST -v
`
