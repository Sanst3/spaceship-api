payload = {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
    
}
fetch("http://localhost:5000/ships/1", payload)
.then(output => {return output})
.then(res => {console.log(res)});