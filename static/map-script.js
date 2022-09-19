//TO DO:
// - break this funciton up 
// - start thinking about testing

let map_markers = [];

function initMap() {

    const Japan = { lat: 36.2048, lng: 138.2529 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 5.5,
      center: Japan,
      mapId: "625155ec1bab001d", 
    });

    let location_data = {};
    fetch('/api/locations')
      .then((response) => response.json())
      .then((locations) => {
        
        for(const location of locations){

          //Creates all location markers
          const latlong = {lat: location["latitude"], lng: location["longitude"]}
          const marker = new google.maps.Marker({
            position: latlong,
            map,
            category: location["movie"],
            title: location["name_irl"]
            })
          map_markers.push(marker);    
      

          //Creates all info windows
          const infowindow = new google.maps.InfoWindow({
            content: location["description"]
          })

          const newel = document.createElement('p')
          newel.textContent = location["name_irl"] +": "+location["description"] 
          const newimg = document.createElement('img')
          newimg.src = "/static/sample_pic.jpg"
          console.log(newimg.src)


          marker.addListener("click", () => {
            document.getElementById("info-bar").appendChild(newel)
            document.getElementById("irl-picture").appendChild(newimg)
            infowindow.open({
              anchor:marker,
              map,
              shouldFocus:true
          })
      })
    }
  })
}

console.log(map_markers)
filterMarkers = function (category) {
  for (const marker of map_markers) {
          // If is same category or category not picke
      if (marker.category == category || category.length === 0) {
          marker.setVisible(true);
          console.log(marker)
      }
      // Categories don't match 
      else {
          marker.setVisible(false);
      }
  }
}

  
window.initMap = initMap;
