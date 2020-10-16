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
.catch(error => {
    console.error("ERROR: ", error)
})

fetch_get("http://localhost:5000/locations/1")
.then(output => {return output.json()})
.then(res => {console.log(res)})
.catch(error => {
    console.error("ERROR: ", error)
})