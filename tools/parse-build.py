#!/home/archid/python/.archaven/bin/python

import json
import jmespath

def html_top(build):
	hf.write(f'''<!DOCTYPE html>
<html>
<head>
	<title>{build}</title>
	<!-- This uses the css from the W3.CSS open source project https://www.w3schools.com/w3css/default.asp -->
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" href="archaven.css">
</head>
<body>

<script src="mainsidebar.js"></script>
<script src="buildsidebar.js"></script>
<script src="archaven.js"></script>

<header class="w3-top w3-display-container w3-green" style="height:60px">
	<button class="w3-button w3-xlarge w3-display-left" onclick="mainsidebar_open()">☰</button>
	<h1 class="w3-display-middle">{build}</h1>		
	<button class="w3-button w3-xlarge w3-display-right" onclick="buildsidebar_open()">☰</button>
</header>

<div class="w3-container" style="margin-top:60px;z-index:-1;">
	''')

def html_overview():
	hf.write('''
	<div class="w3-container">
		<h2 id="overview">Overview</h2>
	''')

	paras=jmespath.search("overview.body[]", jbuild)
	for para in paras:
		hf.write("<p>" + para)
	
	hf.write(f'''
		<p>So why would you play a {build} Build?
		<ul>
	''')

	paras=jmespath.search("overview.benefits[]", jbuild)
	for para in paras:
		hf.write("<li>" + para)

	hf.write(f'''
		</ul>
		
		<p>The tank build loves the following:</p>
		<ul>
	''')
	
	paras=jmespath.search("overview.preferences[]", jbuild)
	for para in paras:
		hf.write("<li>" + para)
	
	hf.write('''
		</ul>
	</div>
	''')

def html_builddeck(char):
	hf.write('''
	<div class="w3-container">
		<h2 id="deck">Build Deck</h2>
	''')
	
	for index in range(1,10):
		html_levelcardstable(char, index)
	
	hf.write('''
	</div>
	''')

def html_levelcardstable(char, level):
	hf.write(f'''
		<button id="level-{level}-cards" onclick="accClick('build-cards-{level}')" class="w3-btn w3-block w3-left-align">Level {level} Cards</button>
		<div id="build-cards-{level}" class="w3-container w3-hide">
			<table>
	''')
	
	if level == 1:
		query=f"cards[?character=='{char}' && (level == '1' || level == 'x')].[image, id]"
	else:
		query=f"cards[?character=='{char}' && level == '{level}'].[image, id]"

	carddata = jmespath.search(query, jcards)
	for data in carddata:
		builddata=jmespath.search(f"cards[?id=='{data[1]}'].[top, bottom, overall][]", jbuild)
		if len(builddata) == 0:
			builddata.append("The top action discussion.")
			builddata.append("The bottom action discussion.")
			builddata.append("The overall card discussion.")

		hf.write(f'''
				<tr>
					<td rowspan="2"><img class="ability-desc" src="images/frosthaven/{data[0]}"/>
					<td class="w3-container" style="width:60%">{builddata[0]}
					<td class="w3-container" rowspan="2">{builddata[2]}
				<tr>
					<td class="w3-container">{builddata[1]}
		''')
	hf.write('''
			</table>
		</div>
	''')

def html_bottom():
	hf.write('''
</div>

<footer class="w3-container w3-teal">
	Tank build by Gripeaway
</footer>

</body>
</html>
	''')

def get_build_name(id, build):
	charname = jmespath.search(f"characters[?id=='{id}'].label|[0]", jchars)
	return  charname + " " + build
	
buildid="bn-tank"

# Read our json card data
with open('../data/card-data.json') as fd:
	jcards = json.load(fd)

with open('../data/character-data.json') as fd:
	jchars = json.load(fd)

with open(f'../data/build-data.json') as fd:
	jbuilds = json.load(fd)

# Open the output html file
hf = open(f"../html/{buildid}.html", "w")

# Get the specific build
jbuild=jmespath.search(f"builds[?id=='{buildid}']|[0]", jbuilds)

charid=jmespath.search("character", jbuild)
build=jmespath.search("build", jbuild)
buildname=get_build_name(charid, build)

html_top(buildname)
html_overview()
html_builddeck(charid)
html_bottom()
