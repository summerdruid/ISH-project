var map;
function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
                 zoom: 2,
                 center: new google.maps.LatLng(2.8,-187.3),
                 mapTypeId: 'terrain'
        });

}

// Loop through the results array and place a marker for each
// set of coordinates.
window.eqfeed_callback = function(results) {
        points = [];
        bounds = new google.maps.LatLngBounds();
	results.find("trkpt").each(function() {
                var lat = $(this).attr("lat");
                var lon = $(this).attr("lon");
                var p = new google.maps.LatLng(lat, lon);
                points.push(p);
                bounds.extend(p);
                })

        var poly = new google.maps.Polyline({
            path: points,
            strokeColor: "green",
            strokeOpacity: 1,
            strokeWeight: 4
            });
        poly.setMap(map);
        map.fitBounds(bounds);
};


function loadMapAPI() {
	var script = document.createElement('script')
	script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyCxMQjhTqS3PnWEQpPOt8Wyx4Q-pnUptqs&callback=initMap';
	document.getElementsByTagName('head')[0].appendChild(script);
}
loadMapAPI();
