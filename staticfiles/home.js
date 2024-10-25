// Function to get user's location
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

// Function to handle successful retrieval of position
function showPosition(position) {
    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;

    // Call function to convert lat/lng to city name
    getCityName(latitude, longitude);
}

// Function to handle errors in getting location
function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}

// Function to get city name from latitude and longitude
function getCityName(latitude, longitude) {
    //let apiKey = "20dfa298c3884808b4055526242310" // Replace with your API key
    //let url = `https://maps.googleapis.com/maps/api/geocode/json?latlng=${latitude},${longitude}&key=${apiKey}`;
    let url = `http://api.weatherapi.com/v1/current.json?key=&q=${latitude},${longitude}&aqi=d4e6137622a94ef8a4660035242310`
    fetch(url)
    .then(response => response.json())
    .then(data => {
        if (data.status === "OK") {
            let results = data.results;
            let city = results[0].address_components.find(component =>
                component.types.includes("locality")
            ).long_name;

            // Set the city name in the input field
            document.getElementById("cityInput").value = city;
        } else {
            console.log("Geocode was not successful for the following reason: " + data.status);
        }
    })
    .catch(error => console.log("Error fetching city data: " + error));
}

// Automatically fetch the location when the page loads
window.onload = getLocation;
