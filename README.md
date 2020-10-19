# spaceship-api

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