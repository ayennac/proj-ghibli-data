
function initMap() {

    const uluru = { lat: -25.344, lng: 131.031 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 3,
      center: uluru,
    });
    //to create a map you must initialize with zoom and center

  }
  
window.initMap = initMap;