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
  <a href="events.html" class="w3-bar-item w3-button">Events</a>

  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('beDrop')">Berserker <i class="fa fa-caret-down"></i></button>
    <div id="beDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="be-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('brDrop')">Brute <i class="fa fa-caret-down"></i></button>
    <div id="brDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="br-main.html" class="w3-bar-item w3-button">Overview</a>
      <a href="br-striker.html" class="w3-bar-item w3-button">Striker</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('bsDrop')">Bladeswarm <i class="fa fa-caret-down"></i></button>
    <div id="bsDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="bs-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('btDrop')">Beast Tyrant <i class="fa fa-caret-down"></i></button>
    <div id="btDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="bt-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('chDrop')">Cragheart <i class="fa fa-caret-down"></i></button>
    <div id="chDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ch-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('deDrop')">Demolitionist <i class="fa fa-caret-down"></i></button>
    <div id="deDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="de-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('dsDrop')">Doomstalker <i class="fa fa-caret-down"></i></button>
    <div id="dsDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ds-main.html" class="w3-bar-item w3-button">Overview</a>
      <a href="ds-expose.html" class="w3-bar-item w3-button">Expose</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('elDrop')">Elementalist <i class="fa fa-caret-down"></i></button>
    <div id="elDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="el-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('haDrop')">Hatchet <i class="fa fa-caret-down"></i></button>
    <div id="haDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ha-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('mtDrop')">Mindthief <i class="fa fa-caret-down"></i></button>
    <div id="mtDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="mt-main.html" class="w3-bar-item w3-button">Overview</a>
      <a href="mt-campaign.html" class="w3-bar-item w3-button">Campaign</a>
      <a href="mt-guildmaster.html" class="w3-bar-item w3-button">Guildmaster</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('nsDrop')">Nightshroud <i class="fa fa-caret-down"></i></button>
    <div id="nsDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ns-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('phDrop')">Plagueherald <i class="fa fa-caret-down"></i></button>
    <div id="phDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ph-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('qmDrop')">Quartermaster <i class="fa fa-caret-down"></i></button>
    <div id="qmDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="qm-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('rgDrop')">Red Guard <i class="fa fa-caret-down"></i></button>
    <div id="rgDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="rg-main.html" class="w3-bar-item w3-button">Overview</a>
      <a href="rg-shield-spikes.html" class="w3-bar-item w3-button">Shield Spikes</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('sbDrop')">Sawbones <i class="fa fa-caret-down"></i></button>
    <div id="sbDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="sb-main.html" class="w3-bar-item w3-button">Overview</a>
      <a href="sb-damage.html" class="w3-bar-item w3-button">Damage</a>
      <a href="sb-tank-asist.html" class="w3-bar-item w3-button">Tank Assist</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('scDrop')">Scoundrel <i class="fa fa-caret-down"></i></button>
    <div id="scDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="sc-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('skDrop')">Sunkeeper <i class="fa fa-caret-down"></i></button>
    <div id="skDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="sk-main.html" class="w3-bar-item w3-button">Overview</a>
      <a href="sk-damage.html" class="w3-bar-item w3-button">Damage</a>
      <a href="sk-tank.html" class="w3-bar-item w3-button">Tank</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('ssDrop')">Soothsinger <i class="fa fa-caret-down"></i></button>
    <div id="ssDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ss-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('suDrop')">Summoner <i class="fa fa-caret-down"></i></button>
    <div id="suDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="su-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('swDrop')">Spellweaver <i class="fa fa-caret-down"></i></button>
    <div id="swDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="sw-main.html" class="w3-bar-item w3-button">Overview</a>
      <a href="sw-cold.html" class="w3-bar-item w3-button">Cold Fire</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('tiDrop')">Tinkerer <i class="fa fa-caret-down"></i></button>
    <div id="tiDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="ti-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('vwDrop')">Voidwarden <i class="fa fa-caret-down"></i></button>
    <div id="vwDrop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="vw-main.html" class="w3-bar-item w3-button">Overview</a>
    </div>
  </div>
</div>
`);
