function init() {
  var tiles_toner = 'http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png',
      tiles_waterColor = 'http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.jpg',
      tiles_osm = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      tiles_osm_blackandwhite ='http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png',
      tiles_esri_worldmap = 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
      tiles_open_topomap = 'http://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
      tiles_mtbmap = 'http://tile.mtbmap.cz/mtbmap_tiles/{z}/{x}/{y}.png',
      tiles_osmfrance = 'http://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png';



  var map = new L.Map('map', {
    center: [44.1903677,350.227259],
    zoom: 3,
    minZoom: 3,
    layers: [
      L.tileLayer('http://otile{s}.mqcdn.com/tiles/1.0.0/{type}/{z}/{x}/{y}.{ext}', {
  type: 'sat',
  ext: 'jpg',
  attribution: 'Tiles Courtesy of <a href="http://www.mapquest.com/">MapQuest</a> &mdash; Portions Courtesy NASA/JPL-Caltech and U.S. Depart. of Agriculture, Farm Service Agency',
  subdomains: '1234'
})
    ]
  });

        //Around Cursor
    L.magnifyingGlass({
    zoomOffset: 0,
    radius: 60,
    layers: [
      L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012'
})
    ],
    fixedPosition: false,
    latLng: [ 41.9028908,12.4962851]
  }).addTo(map);

 
}


window.onload = init;