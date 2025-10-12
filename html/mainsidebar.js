document.write(`
<script>
function mainsidebar_open() {
  document.getElementById("main-sidebar").style.display = "block";
}

function mainsidebar_close() {
  document.getElementById("main-sidebar").style.display = "none";
}

function sidebarMainDropClick(id) {
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
     
<div class="w3-sidebar w3-bar-block w3-light-grey w3-card w3-animate-left" style="display:none" id="main-sidebar">
  <button onclick="mainsidebar_close()" class="w3-bar-item w3-large">Close &times;</button>
	<a href="index.html" class="w3-bar-item w3-button">Home</a>

  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('bnDrop')">Banner Spear <i class="fa fa-caret-down"></i></button>
    <div id="bnDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="bn-main.html" class="w3-bar-item w3-button">Overview</a>
      <a href="bn-tank.html" class="w3-bar-item w3-button">Tank</a>
    </div>
  </div>

  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('boDrop')">Boneshaper <i class="fa fa-caret-down"></i></button>
    <div id="boDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="bo-main.html" class="w3-bar-item w3-button">Overview</a>
      <a href="bo-swarm.html" class="w3-bar-item w3-button">Skeleton Swarm</a>
    </div>
  </div>

</div>
`);
