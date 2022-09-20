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
          

          const movie_card = `<div class="movie-card-${location["name_irl"]}"> <div class="card" style="width: 18rem;">
            <img class="card-img-top" src= ${location["image"]} alt="Card image cap">
              </img><div class="card-body">
                <h5 class="card-title">${location["name_irl"]}</h5>
                <p class="card-text">${location["description"]}</p>
                <a href="#" class="btn btn-primary">Go somewhere</a></div>
                </div> </div>`;

          marker.addListener("click", () => {
            if (document.getElementById("info-card").firstChild!= null) {
                for (const node of document.getElementById("info-card").childNodes){
                  console.log(node)
                  node.remove()
                }
                document.getElementById("info-card").innerHTML += movie_card
                infowindow.open({
                  anchor:marker,
                  map,
                  shouldFocus:true
          })
          } else {
          document.getElementById("info-card").innerHTML += movie_card
                infowindow.open({
                  anchor:marker,
                  map,
                  shouldFocus:true
        })
      }
      })
    }
  })
}


filterMarkers = function (category) {
  console.log(category)
  for (const marker of map_markers) {
          // If is same category or category not picked
      if (marker.category == category || category.length === 0 || category == "all") {
          marker.setVisible(true);
      }
      // Categories don't match 
      else {
          marker.setVisible(false);
      }
  }
}

  
window.initMap = initMap;
