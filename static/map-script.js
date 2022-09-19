//TO DO:
// - break this funciton up 
// - start thinking about testing 
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
            title: location["name_irl"]
            })
          const infowindow = new google.maps.InfoWindow({
            content: location["description"]
          })

          const newel = document.createElement('p')
          newel.textContent = location["name_irl"] +": "+location["description"] 


          marker.addListener("click", () => {
            document.getElementById("info-bar").appendChild(newel)
            infowindow.open({
              anchor:marker,
              map,
              shouldFocus:true
          })
      })
    }
  })
}

  
window.initMap = initMap;
