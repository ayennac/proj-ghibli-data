location_data = [
  {
      "image": "this is a url",
      "latitude": 35.7802,
      "longitude": 139.4219,
      "place_movie": "Totoro's Forest",
      "name_irl": "Totoro's Forest",
      "description": "This is the description for Totoro's Forest", 
      "movie": "My Neighbor Totoro"
  },
  {
      "image": "this is a url",
      "latitude": 35.7260,
      "longitude": 139.4053,
      "place_movie": "Sayama Lake",
      "name_irl": "Sayama Lake",
      "description": "This is the description for Sayama Lake",
      "movie": "My Neighbor Totoro"
  },
  {
      "image": "this is a url",
      "latitude": 33.85116326,
      "longitude": 132.7851635,
      "place_movie": "The Bathhouse",
      "name_irl": "Dōgo Onsen Honkan",
      "description": "This is the description for Dōgo Onsen Honkan",
      "movie": "Spirited Away"
  },
  {
      "image": "this is a url",
      "latitude": 30.38017,
      "longitude": 130.57421,
      "place_movie": "Princess Mononoke's Forest",
      "name_irl": "Shiratani Unsuikyō Gorge",
      "description": "This is the description for Princess Mononoke's Forest",
      "movie": "Princess Mononoke"
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
