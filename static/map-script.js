

function initMap() {

    const aussie = { lat: -25.344, lng: 131.031 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 3,
      center: aussie,
    });
    //to create a map you must initialize with zoom and center

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
// window.eqfeed_callback = eqfeed_callback;