function getApiUrl() {
    return window.location.href;
}

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
            throw response.statusText;
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
            throw response.statusText;
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
            throw response.statusText;
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

    if (Array.isArray(result)) {
        for (resultRow of result) {
            wrapper.append(newObject(resultRow));
        }
    } else {
        wrapper.append(newObject(result));
    }
    
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

    const url = "http://localhost:5000/locations/parked/" + loc["id"];

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

function insertError(message) {
    let wrapper = $("#result")
    let row = $(document.createElement("p"));
    row.text(message);
    wrapper.append(row);
}

function refresh() {
    $("#result").empty();
    $("#state").empty();
    insertState();
}
function addFormListener(formId, url, method, variableId) {
    let formSelector = "#" + formId;
    $(formSelector).submit((event) => {
        event.preventDefault();
        let array = $(formSelector).serializeArray();
        let args = convertArray(array);

        let newUrl = variableId ? url + args["id"] : url;
        let fetchFunc;

        switch(method) {
            case "POST":
                fetchFunc = fetchPost(newUrl, args);
                break;
            case "GET":
                fetchFunc = fetchGet(newUrl);
                break;
            case "DELETE":
                fetchFunc = fetchDelete(newUrl);
                break;

        }
        fetchFunc
        .then(response => { 
            refresh();
            insertResult(response);
        })
        .catch(error => {
            console.log(error);
            refresh();
            insertError(error); }
        );
        return false;
    });
}

$(document).ready(function() {
    refresh();
    addFormListener("locationsInsertForm", getApiUrl() + "locations", "POST", false);
    addFormListener("shipsInsertForm", getApiUrl() + "ships", "POST", false);
    addFormListener("shipsGetForm", getApiUrl() + "ships/", "GET", true);
    addFormListener("shipsDeleteForm", getApiUrl() + "ships/", "DELETE", true);
    addFormListener("locationsGetForm", getApiUrl() + "locations/", "GET", true);
    addFormListener("locationsDeleteForm", getApiUrl() + "locations/", "DELETE", true);
    addFormListener("locationsGetAllForm", getApiUrl() + "locations", "GET", false);
    addFormListener("locationsParkedGetForm", getApiUrl() + "locations/parked/", "GET", true);
    addFormListener("shipsStatusSetForm", getApiUrl() + "ships/status/", "POST", true);
    addFormListener("shipsParkingSetForm", getApiUrl() + "ships/parking/", "POST", true);
});
