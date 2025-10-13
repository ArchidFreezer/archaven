document.write(`
<script>
function buildsidebar_open() {
  document.getElementById("build-sidebar").style.display = "block";
}

function buildsidebar_close() {
  document.getElementById("build-sidebar").style.display = "none";
}

function sidebarBuildDropClick(id) {
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
     
<div class="w3-sidebar w3-bar-block w3-light-grey w3-card w3-animate-right" style="display:none;right:0;" id="build-sidebar">
  <button onclick="buildsidebar_close()" class="w3-bar-item w3-large">Close &times;</button>
	<a href="#overview" class="w3-bar-item w3-button">Overview</a>

  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarBuildDropClick('deckDrop')">Deck <i class="fa fa-caret-down"></i></button>
    <div id="deckDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="#level-1" class="w3-bar-item w3-button">Level 1</a>
      <a href="#level-2" class="w3-bar-item w3-button">Level 2</a>
      <a href="#level-3" class="w3-bar-item w3-button">Level 3</a>
      <a href="#level-4" class="w3-bar-item w3-button">Level 4</a>
      <a href="#level-5" class="w3-bar-item w3-button">Level 5</a>
      <a href="#level-6" class="w3-bar-item w3-button">Level 6</a>
      <a href="#level-7" class="w3-bar-item w3-button">Level 7</a>
      <a href="#level-8" class="w3-bar-item w3-button">Level 8</a>
      <a href="#level-9" class="w3-bar-item w3-button">Level 9</a>
    </div>
  </div>

</div>
`);
