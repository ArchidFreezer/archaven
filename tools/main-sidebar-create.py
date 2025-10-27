#!/home/archid/python/.archaven/bin/python

import json
import jmespath
import glob
import os

def get_build_name(id):
	name=jmespath.search(f"builds[?id=='{id}'].build|[0]", jbuilds)
	return name
	
def html_class(cls):
	id=cls[0]
	name=cls[1]
	menu=f'''  <div class="w3-dropdown-click">
    <button class="w3-button" onclick="sidebarMainDropClick('{id}Drop')">{name} <i class="fa fa-caret-down"></i></button>
    <div id="{id}Drop" class="w3-dropdown-content w3-bar-block w3-white w3-card">
      <a href="{id}-main.html" class="w3-bar-item w3-button">Overview</a>
'''
	
	# find all the build files
	files = glob.glob('../html/' + id + '-*.html')
	for file in files:
		file=os.path.basename(file)
		if file != id + "-main.html":
			name=get_build_name(os.path.splitext(file)[0])
			menu+=f'''			<a href="{file}" class="w3-bar-item w3-button">{name}</a>
'''
	
	menu+='''    </div>
  </div>
'''
	return menu


with open('../data/class-data.json') as fd:
	jclasses = json.load(fd)
classes=jmespath.search(f"classes[].[id,label]", jclasses)

with open('../data/build-data.json') as fd:
	jbuilds = json.load(fd)

# Open the output html file
hf = open(f"../html/mainsidebar.js", "w")

hf.write('''document.write(`
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

''')

for cls in classes:
	hf.write(html_class(cls))

hf.write('''</div>
`);
''')