function fetch_post(url, body) {
    return fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    })
}

function fetch_get(url) {
    return fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        }
    })
}


fetch_post("http://localhost:5000/locations", {
    city: "sydney",
    planet: "earth",
    capacity: "3"
})
.then(output => {return output.json()})
.then(res => {console.log(res)})
.then(res => {return fetch_post("http://localhost:5000/ships", {
    name: "bob",
    model: "pal",
    status: "2",
    location_id: "1"
})})
.then(output => {return output.json()})
.then(res => {console.log(res)})
.then(res => {return fetch_get("http://localhost:5000/ships/1")})
.then(output => {return output.json()})
.then(res => {console.log(res)})
.catch(error => {
    console.error("ERROR: ", error)
})