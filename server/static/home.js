function fetchPost(url, requestBody) {
    return fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
    })
    .then(response => { 
        if (response.status == 200) {
            return response.json();
        } else {
            throw "Error";
        }
    })
}

function fetchGet(url) {
    return fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        }
    })
    .then(response => { 
        if (response.status == 200) {
            return response.json();
        } else {
            throw "Error";
        }
    })
}

function fetchDelete(url) {
    return fetch(url, {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
        }
    })
    .then(response => { 
        if (response.status == 200) {
            return response.json();
        } else {
            throw "Error";
        }
    })
}

function convertArray(array) {
    let payload = {};
    for (input of array) {
        payload[input["name"]] = input["value"]
    }

    return payload;
}

function insertResult(result) {
    let wrapper = $("#result")
    let successText = "Success!";
    let sucessRow = $(document.createElement("p"));
    sucessRow.text(successText);
    wrapper.append(sucessRow);

    wrapper.append(newObject(result));
}

function newObject(obj) {
    let wrapper = $(document.createElement("div"));
    wrapper.addClass("col-sm-3 border");

    for (let key in obj) {
        let rowText = key + ": " + obj[key];
        let row = $(document.createElement("p"));
        row.text(rowText);
        wrapper.append(row);
    }

    return wrapper;
}

function insertLocation(loc) {
    let wrapper = $(document.createElement("div"));
    wrapper.addClass("container border mt-3");
    $("#state").append(wrapper);

    let locationWrapper = $(document.createElement("div"));
    locationWrapper.addClass("row");
    wrapper.append(locationWrapper);

    locationWrapper.append(newObject(loc));

    let shipWrapper = $(document.createElement("div"));
    shipWrapper.addClass("row");
    wrapper.append(shipWrapper);

    const url = "http://localhost:5000/locations/" + loc["id"] + "/parked";

    fetchGet(url)
    .then (results => {
        for (let result of results) {
            shipWrapper.append(newObject(result));
        }
    })
    .catch(error => { console.log(error); });
}

function insertState() {
    fetchGet("http://localhost:5000/locations")
    .then(results => { 
        for (let result of results) {
            insertLocation(result);
        }
    })
    .catch(error => { console.log(error); })
}

function insertError() {
    let wrapper = $("#result")
    let row = $(document.createElement("p"));
    row.text("Error");
    wrapper.append(row);
}

function refresh() {
    $("#result").empty();
    $("#state").empty();
    insertState();
}
// Adds a submit handler for API calls that expect a JSON response
function addPostFormListener(formId, url) {
    let formSelector = "#" + formId;
    $(formSelector).submit((event) => {
        event.preventDefault();
        let array = $(formSelector).serializeArray();
        let args = convertArray(array);

        fetch_post(url, args)
        .then(response => { 
            refresh();
            insertResult(response);
        })
        .catch(error => insertError());

        return false;
    });
}

function addFormListener(formId, url, method, variableId) {
    let formSelector = "#" + formId;
    $(formSelector).submit((event) => {
        event.preventDefault();
        let array = $(formSelector).serializeArray();
        let args = convertArray(array);

        if (variableId) { url = url + args["id"]; }

        let fetchFunc;

        switch(method) {
            case "POST":
                fetchFunc = fetchPost(url, args);
                break;
            case "GET":
                fetchFunc = fetchGet(url);
                break;
            case "DELETE":
                fetchFunc = fetchDelete(url);
                break;

        }
        fetchFunc
        .then(response => { 
            refresh();
            insertResult(response);
        })
        .catch(error => {
            refresh();
            insertError(); }
        );
        return false;
    });
}

$(document).ready(function() {
    refresh();
    addFormListener("locationsInsertForm", "http://localhost:5000/locations", "POST", false);
    addFormListener("shipsInsertForm", "http://localhost:5000/ships", "POST", false);
    addFormListener("shipsGetForm", "http://localhost:5000/ships/", "GET", true);
    addFormListener("shipsDeleteForm", "http://localhost:5000/ships/", "DELETE", true);
    addFormListener("locationsGetForm", "http://localhost:5000/locations/", "GET", true);
    addFormListener("locationsDeleteForm", "http://localhost:5000/locations/", "DELETE", true);
});
