# spaceship-api

## Installation

### Dependencies
You will need:
- Python 3.X: https://www.python.org/downloads/

### Server Setup
1. Create a virtual environment in the project directory (this step only needs to be done once and can be skipped on subsequent builds):

	a) Linux/MacOS: `python3 -m venv venv`
	
	b) Windows Powershell: `py -3 -m venv venv`

2. Activate the virtual environment:

	a) Linux/MacOS: `. venv/bin/activate`
	
	b) Windows Powershell: `venv\Scripts\activate`
	
	If working on Windows, you might have to execute `Set-ExecutionPolicy RemoteSigned` in order to be able to activate the virtual environment (Make sure Powershell is running as administrator for this).

3. Install flask and flask-cors (this step only needs to be done once and can be skipped on subsequent builds): 
   `pip install Flask`
   
   `pip install flask-cors`

4. Run the following commands in the base project directory:

	a) Linux/MacOS: 
	
	`export FLASK_APP=server`
	
	`export FLASK_ENV=development`
	
	`flask run`
	
	b) Windows Powershell:
	
	`$env:FLASK_APP="server"`
	
	`$env:FLASK_ENV="development"`
	
	`flask run`

The web server should now be running and the website should be visitable at the address shown by the output after running flask (e.g. http://127.0.0.1:5000/). 

`ctrl+c` to terminate the server.

Run `deactivate` to end the virtual environment.

# API Demonstration

Once the server is launched, a web page demonstrating each API call and its result can be accessed at the root address of the server (e.g. http://127.0.0.1:5000/).

The page itself contains instructions on how to use it.

# Documentation

## The Location Object

### Attributes

**id** *int*

A unique identifier for the location

---

**city_name** *string*

The name of the ship

---

**planet_name** *string*

The model of the ship

---

**capacity** *int*

The maximum number of ships the location can house

---

### Example

```javascript
{
    "id": 1,
    "city_name": "Sydney",
    "planet_name": "Earth",
    "capacity": 321
}
```

## Create a location

### POST /locations

### Parameters

---

**city_name** *string* ***Required***

The name of the city in the location

---

**planet_name** *string* ***Required***

The name of the planet in the location

---

**capacity** *int* ***Required***

The maximum number of ships that can be parked in this location

---


### Returns

Returns an object containing the ID of the new location created. This call will return a status code of 400 Bad Request if somethings goes wrong. A common source of this error is invalid parameter inputs such as a non-integer capacity

### Example

```javascript
{
    "city_name": "Sydney",
    "planet_name": "Earth",
    "capacity": 321
}
```

### Response

```javascript
{
    "id": 1
}
```

## Retrieve a location

### GET /locations/:id

Retrives the details of a location that has been created. Give the location ship id in `:id`, and the location information wil be returned.

### Parameters

None

### Returns

Returns a location if a valid ID was provided, returns a status code of 400 Bad request otherwise.

### Response

```javascript
{
    "id": 1,
    "city_name": "Sydney",
    "planet_name": "Earth",
    "capacity": 321
}
```

## Delete a location

### DELETE /locations/:id

Deletes a location that has been created. Give the unique ship id in `:id`, and the deletion success will be returned.

### Parameters 

None

### Returns

Returns a boolean of the deletion success if successful. Returns a status code of 400 Bad request if the id is invalid.

### Response

```javascript
{
    "deleted": true
}
```

## The Ship Object

### Attributes

**id** *int*

A unique identifier for the ship

---

**name** *string*

The name of the ship

---

**model** *string*

The model of the ship

---

**status** *int*

The status of the ship is represented by an integer status code and can only be the following:

0: Decommissioned

1: Maintenance

2: Operational

---

**parking_id** *int*

The ID of the location the ship is parked in

---

### Example

```javascript
{
    "id": 1,
    "name": "Camry",
    "model": "Toyota",
    "status": 2,
    "location_id": 1
}
```

## Create a ship

### POST /ships

### Parameters

---

**name** *string* ***Required***

The name of the ship

---

**model** *string* ***Required***

The model of the ship

---

**status** *int* ***Required***

The status of the ship is represented by an integer status code and can only be the following:

0: Decommissioned

1: Maintenance

2: Operational

---

**parking_id** *int* ***Required***

The ID of the location the ship is parked in

---

### Returns

Returns an object containing the ID of the new ship created. This call will return a status code of 400 Bad Request if somethings goes wrong. A common source of this error is an invalid status code, an invalid location_id or the fact that the location the ship is to be created at is at full capacity already.

### Example

```javascript
{
    "name": "Camry",
    "model": "Toyota",
    "status": 2,
    "location_id": 1
}
```

### Response

```javascript
{
    "id": 1
}
```


## Retrieve a ship

### GET /ships/:id

Retrives the details of a ship that has been created. Give the unique ship id in `:id`, and the ship information wil be returned.

### Parameters

None

### Returns

Returns a ship if a valid ID was provided, returns a status code of 400 Bad request otherwise.

### Response

```javascript
{
    "id": 1,
    "name": "Camry",
    "model": "Toyota",
    "status": 2,
    "location_id": 1
}
```

## Update a ship's status

### POST /ships/status/:id

Updates the status of a ship that has been created. Give the unique ship id in `:id`, and the new status will be returned.

### Parameters

**status** *int* ***Required***

The new status code of the ship.

---

### Returns

Returns the new status if successful. Returns a status of 400 Bad Request if status code is invalid or ship id is invalid.

### Example
```javascript
{
    "status": 0
}
```

### Response:

```javascript
{
    "status": 0
}
```

## Update a ship's location

### POST /ships/parking/:id

Updates the location of a ship that has been created. Give the unique ship id in `:id`, and the new location will be returned.

### Parameters

**location_id** *int* ***Required***

The unique identifier of the location the ship is to move to.

---

### Returns

Returns the unique identifier of the new location the ship has moved to. Returns a status code of 400 Bad Request an error occurs. Common reasons for this are invalid id and location_id, and if the location that has the location_id is already at maximum capacity.

### Example

```javascript
{
    "location_id": 3
}
```

### Response

```javascript
{
    "location_id": 3
}
```

## Delete a ship

### DELETE /ships/:id

Deletes a ship that has been created. Give the unique ship id in `:id`, and the deletion success will be returned.

### Parameters 

None

### Returns

Returns a boolean of the deletion success if successful. Returns a status code of 400 Bad request if the id is invalid.

### Response

```javascript
{
    "deleted": true
}
```

## Utility API Calls

Note: These calls were made so that the frontend demonstration of the backend API could work.

## Get all locations

### GET /locations

Gets all locations in database.

### Parameters 

None

### Returns 

Returns a list of all locations.

### Response

```javascript
[
    {
        "id": 1,
        "city_name": "Sydney",
        "planet_name": "Earth",
        "capacity": 321
    },
    {
        "id": 2,
        "city_name": "Melbourne",
        "planet_name": "Earth",
        "capacity": 123
    },
    {
        "id": 3,
        "city_name": "Perth",
        "planet_name": "Earth",
        "capacity": 1234
    }
]
```

## Get all ships in a location

### GET /locations/parked/:id

Returns a list of ships that are in a location, given its location ID. Give the unique location id in `:id`.

### Parameters

None

### Returns

Returns a list of all ships contained by the location given its location ID.

### Response

```javascript
[
    {
        "id": 1,
        "name": "Camry",
        "model": "Toyota",
        "status": 2,
        "location_id": 1
    },
    {
        "id": 2,
        "name": "Corolla",
        "model": "Toyota",
        "status": 0,
        "location_id": 1
    },
    {
        "id": 3,
        "name": "Sedan",
        "model": "Toyota",
        "status": 1,
        "location_id": 1
    }
]
```