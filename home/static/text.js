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
        
    } else {
        console.log("Failed to retrieve weather data");
    }
    
    console.log("amit", typeof(result),result);

};

function failedToGet(){
    console.log("there was some issue")
};


function getLocation() {
    navigator.geolocation.getCurrentPosition(gotLocation, failedToGet)
}





