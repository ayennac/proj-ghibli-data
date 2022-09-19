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
          const latlong = {lat: location["latitude"], lng: location["longitude"]}
          const marker = new google.maps.Marker({
            position: latlong,
            map,
            title: location["name_irl"]
            })
          const infowindow = new google.maps.InfoWindow({
            content: location["description"]
          })
          }
      });
   

    
  //   // for(let i = 0; i < location_data.length; i++){
  //   //   const latlong = {lat: location_data[i]["latitude"], lng: location_data[i]["longitude"]};
      

      
  //   //   
      
  //   //   const newel = document.createElement('p')
  //   //   newel.textContent = location_data[i]["name_irl"] +": "+location_data[i]["description"] 
  
  //   //   marker.addListener("click", () => {
  //   //     document.getElementById("info-bar").appendChild(newel)
  //   //     infowindow.open({
  //   //       anchor:marker,
  //   //       map,
  //   //       shouldFocus:true
  //   //     })
  //   //   })
  
  // }
}

  
window.initMap = initMap;
