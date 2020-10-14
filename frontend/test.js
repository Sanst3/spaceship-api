fetch("http://localhost:5000/test")
.then(output => {return output.json()})
.then(res => {console.log(res)});