document.write(`
<script>
function w3_open() {
  document.getElementById("sidebar").style.display = "block";
}

function w3_close() {
  document.getElementById("sidebar").style.display = "none";
}
</script>
     
<div class="w3-sidebar w3-bar-block w3-light-grey w3-card" style="display:none" id="sidebar">
  <button onclick="w3_close()" class="w3-bar-item w3-large">Close &times;</button>
	<a href="main.html" class="w3-bar-item w3-button">Home</a>

  <div class="w3-dropdown-hover">
		<button class="w3-button">Banner Spear <i class="fa fa-caret-down"></i></button>
		<div id="bsDrop" class="w3-dropdown-content w3-bar-block w3-card-4">
			<a href="bs-tank.html" class="w3-bar-item w3-button">Tank</a>
		</div>
  </div>

	<div class="w3-dropdown-hover">
		<button class="w3-button">Boneshaper <i class="fa fa-caret-down"></i></button>
		<div id="bsDrop" class="w3-dropdown-content w3-bar-block w3-card-4">
			<a href="bo-swarm.html" class="w3-bar-item w3-button">Skeleton Swarm</a>
		</div>
	</div>
</div>
`);
