payload = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({username: "bababooi", password: "PASS"})
}
fetch("http://localhost:5000/test", payload)
.then(output => {return output.json()})
.then(res => {console.log(res)});