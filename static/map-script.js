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
  
  }
}

  
window.initMap = initMap;
