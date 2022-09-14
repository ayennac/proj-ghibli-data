

//TO DO:
//Figure out how to import this location data
location_data = [
  {
      "image": "this is a url",
      "latitude": 35.7802,
      "longitude": 139.4219,
      "place_movie": "Totoro's Forest",
      "name_irl": "Totoro's Forest",
      "description": "This is the description for Totoro's Forest"
  },
  {
      "image": "this is a url",
      "latitude": 35.7260,
      "longitude": 139.4053,
      "place_movie": "Sayama Lake",
      "name_irl": "Sayama Lake",
      "description": "This is the description for Sayama Lake"
  }
]


//TO DO:
// - break this funciton up 
// - start thinking about testing 
function initMap() {

    const Japan = { lat: 36.2048, lng: 138.2529 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 5.5,
      center: Japan,
    });

    for(let i = 0; i < location_data.length; i++){
      const latlong = {lat: location_data[i]["latitude"], lng: location_data[i]["longitude"]};
      
      const infowindow = new google.maps.InfoWindow({
        content: location_data[i]["description"]
      })
      
      const marker = new google.maps.Marker({
        position: latlong,
        map,
        title: location_data[i]["name_irl"]
      })
      
      const newel = document.createElement('p')
      newel.textContent = location_data[i]["name_irl"] +": "+location_data[i]["description"] 
  
      marker.addListener("click", () => {
        document.getElementById("info-bar").appendChild(newel)
        infowindow.open({
          anchor:marker,
          map,
          shouldFocus:true
        })
      })
    //to create a map you must initialize with zoom and center

  }
}

  
// Loop through the results array and place a marker for each
// set of coordinates.
// const eqfeed_callback = function (results) {
//     for (let i = 0; i < results.features.length; i++) {
//       const coords = results.features[i].geometry.coordinates;
//       const latLng = new google.maps.LatLng(coords[1], coords[0]);
  
//       new google.maps.Marker({
//         position: latLng,
//         map: map,
//       });
//     }
//   };
  
window.initMap = initMap;
