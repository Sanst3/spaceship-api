payload = {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
    
}
fetch("http://localhost:5000/ships/565", payload)
.then(output => {return output.json()})
.then(res => {console.log(res)})
.catch(error => {
    console.error("ERROR: ", error)
});