const button = document.getElementById("get-location-button");


async function getData(lat, long){
    const promise = await fetch(`http://api.weatherapi.com/v1/current.json?key=d4e6137622a94ef8a4660035242310&q=${lat},${long}&aqi=yes`
    );
    return await promise.json();
}

async function gotLocation(position){
    const result = await getData(position.coords.latitude, position.coords.longitude);

    if (result && result.location && result.location.name) {
        const cityName = result.location.name;
        console.log("City Name:", cityName);
        window.location.href = "/home?city="+cityName
        // Send the city name to Django
        // sendCityNameToDjango(cityName);
    } else {
        console.log("Failed to retrieve weather data");
    }
    
    console.log("amit", typeof(result),result);

};

function failedToGet(){
    console.log("there was some issue")
};

// Function to send city name to Django via POST request
async function sendCityNameToDjango(cityName) {
    try {
        
        const response = await fetch('http://127.0.0.1:8000/index/receive-city/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',  // This format works well with Django
                'X-CSRFToken': getCSRFToken(),  // Pass CSRF token if necessary
            },
            body: new URLSearchParams({
                'city': cityName
            })
        });

        const result = await response.json();
        console.log("Response from Django:", result);
    } catch (error) {
        console.error('Error sending city to Django:', error);
    }
}

// Helper function to get CSRF token from the cookie
function getCSRFToken() {
    let cookieValue = null;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            cookieValue = cookie.substring('csrftoken='.length, cookie.length);
            break;
        }
    }
    return cookieValue;
}

function getLocation() {
    navigator.geolocation.getCurrentPosition(gotLocation, failedToGet)
}





