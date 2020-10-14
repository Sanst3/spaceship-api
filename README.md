# spaceship-api

## Description
In the distant future, humans have colonised all 8 planets in our solar system. You work for Stomble, a shipping company trying to expand their operations to the whole solar system. You have been asked to develop a system to manage the logistics of Stomble’s fleet of spaceships.

## Requirements
You will develop a REST API which will store information about the location of the spaceships, as well as the locations in which they are stationed.


In order to accomplish this, your API must fulfill the following use cases:

* Add spaceships: a spaceship must have an id, name, model, location (made up of a city and a planet) and its status (decommissioned, maintenance or operational).

* Update the spaceship status: to one of the 3 possible states.

* Add a location: a location must have an id, city name and a planet name; as well as the spaceport capacity (how many spaceships can be stationed at this location simultaneously).

* Remove spaceships: given a spaceship’s id.

* Remove location: given a location’s id.

* Travel functionality: Travel involves changing the location of the spaceship and adjusting the capacity of the source and destination spaceports. Before carrying out the travel transaction, check these two factors:

    * The spaceport capacity of the destination (if not, return an appropriate error).

    * The status of the spaceship (only operational spaceships can travel).

## Notes
* Feel free to use the programming language you're most comfortable with.

* You don't have to worry about coding a frontend. However, you do need a way to show that your API functions correctly.

* Code must be placed in a public git repository (e.g. GitHub, GitLab), don’t forget to use meaningful commit messages.

* Spaceship fuel levels don’t have to be accounted for, and one can assume that they can travel to any location in a single trip.

* To simplify the task, and to avoid concurrency issues, travel from planet to planet is so fast that the time taken can be ignored (i.e. travel happens instantaneously).

* All spaceships must be stationed in a hangar somewhere, regardless of their status.

* Consider documenting and testing your API.

* If time permits, use a database.

