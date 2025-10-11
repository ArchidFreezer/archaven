document.write(`
<script>
function w3_open() {
  document.getElementById("sidebar").style.display = "block";
}

function w3_close() {
  document.getElementById("sidebar").style.display = "none";
}

function sidebarDropClick(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
    x.previousElementSibling.className += " w3-green";
  } else { 
    x.className = x.className.replace(" w3-show", "");
    x.previousElementSibling.className = x.previousElementSibling.className.replace(" w3-green", "");
  }
}
</script>
     
<div class="w3-sidebar w3-bar-block w3-light-grey w3-card" style="display:none" id="sidebar">
  <button onclick="w3_close()" class="w3-bar-item w3-large">Close &times;</button>
	<a href="index.html" class="w3-bar-item w3-button">Home</a>

  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarDropClick('bsDrop')">Banner Spear <i class="fa fa-caret-down"></i></button>
    <div id="bsDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="bs-tank.html" class="w3-bar-item w3-button">Tank</a>
    </div>
  </div>

  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarDropClick('boDrop')">Boneshaper <i class="fa fa-caret-down"></i></button>
    <div id="boDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="bo-swarm.html" class="w3-bar-item w3-button">Skeleton Swarm</a>
    </div>
  </div>

</div>
`);
