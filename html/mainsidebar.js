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
    <button class="w3-button" onclick="sidebarMainDropClick('bbDrop')">Blinkblade <i class="fa fa-caret-down"></i></button>
    <div id="bbDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="bb-main.html" class="w3-bar-item w3-button">Overview</a>
			<a href="bb-slowblade.html" class="w3-bar-item w3-button">SlowBlade</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('bnDrop')">Banner Spear <i class="fa fa-caret-down"></i></button>
    <div id="bnDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="bn-main.html" class="w3-bar-item w3-button">Overview</a>
			<a href="bn-banner.html" class="w3-bar-item w3-button">Banner</a>
			<a href="bn-spear.html" class="w3-bar-item w3-button">Spear</a>
			<a href="bn-tank.html" class="w3-bar-item w3-button">Tank</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('boDrop')">Boneshaper <i class="fa fa-caret-down"></i></button>
    <div id="boDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="bo-main.html" class="w3-bar-item w3-button">Overview</a>
			<a href="bo-bone.html" class="w3-bar-item w3-button">Bone Wall</a>
			<a href="bo-single.html" class="w3-bar-item w3-button">Single-Summon</a>
			<a href="bo-skel.html" class="w3-bar-item w3-button">Skeleton Swarm</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('crDrop')">Crashing Tide <i class="fa fa-caret-down"></i></button>
    <div id="crDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="cr-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('dfDrop')">Drifter <i class="fa fa-caret-down"></i></button>
    <div id="dfDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="df-main.html" class="w3-bar-item w3-button">Overview</a>
			<a href="df-bruiser.html" class="w3-bar-item w3-button">Bruiser</a>
			<a href="df-ranger-heal.html" class="w3-bar-item w3-button">Ranged/Healer</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('dtDrop')">Deepwraith <i class="fa fa-caret-down"></i></button>
    <div id="dtDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="dt-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('dwDrop')">Deathwalker <i class="fa fa-caret-down"></i></button>
    <div id="dwDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="dw-main.html" class="w3-bar-item w3-button">Overview</a>
			<a href="dw-puppet.html" class="w3-bar-item w3-button">Puppetmaster</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('ffDrop')">Frozen Fist <i class="fa fa-caret-down"></i></button>
    <div id="ffDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ff-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('geDrop')">Geminate <i class="fa fa-caret-down"></i></button>
    <div id="geDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ge-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('hvDrop')">Hive <i class="fa fa-caret-down"></i></button>
    <div id="hvDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="hv-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('ifDrop')">Infuser <i class="fa fa-caret-down"></i></button>
    <div id="ifDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="if-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('meDrop')">Metal Mosaic <i class="fa fa-caret-down"></i></button>
    <div id="meDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="me-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('pcDrop')">Pain Conduit <i class="fa fa-caret-down"></i></button>
    <div id="pcDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="pc-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('pyDrop')">Pyroclast <i class="fa fa-caret-down"></i></button>
    <div id="pyDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="py-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('sdDrop')">Snowdancer <i class="fa fa-caret-down"></i></button>
    <div id="sdDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="sd-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('shDrop')">Shattersong <i class="fa fa-caret-down"></i></button>
    <div id="shDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="sh-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('taDrop')">Trapper <i class="fa fa-caret-down"></i></button>
    <div id="taDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ta-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
</div>
`);
