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

def html_builddecks():
	hf.write('''
	<div class="w3-container">
		<h2 id="deck">Build Deck</h2>
	''')
	
	for level in range(1,10):
		hf.write(f'''
			<button id="level-{level}" onclick="accClick('acc-lvl-{level}')" class="w3-btn w3-block w3-left-align">Level {level}</button>
			<div id="acc-lvl-{level}" class="w3-container w3-hide">
				<div class-"w3-flex" style="gap:4px;flex-direction:column">
		''')
		html_new_cards(level)
		html_choices(level)
		hf.write(f'''
				</div>
			</div>
		''')
	
	hf.write('''
	</div>
	''')

def html_buildhand(level):
	hf.write(f'''
		<button id="level-1-hand" onclick="accClick('build-1-hand')" class="w3-btn w3-block w3-left-align">Level 1 Hand</button>
		<div id="build-1-hand" class="w3-container w3-hide">
			<div class="w3-container">
				<h3 class="w3-light-grey">Standard Hand</h3>
				<p>This is the default hand to use at this level, however it should be modified based on the quest.
				<div class="w3-flex" style="gap:8px;flex-wrap:wrap">
	''')
	
	jhand=jmespath.search(f"levels[?level=='{level}'].hand[]", jbuild)
	for jcard in jhand:
		data=jmespath.search("[card, top.text, top.style, bottom.text, bottom.style]", jcard)
		
	hf.write('''
				</div> <!-- default deck -->
			</div>
		</div>
	''')
	
def html_new_cards(level):
	hf.write(f'''
			<button id="level-{level}-new" onclick="accClick('acc-{level}-new')" class="w3-btn w3-block w3-left-align">New Level {level} Cards</button>
			<div id="acc-{level}-new" class="w3-container w3-hide">
				<div class-"w3-flex" style="gap:4px;flex-direction:column">
	''')
	
	if level == 1:
		query=f"[?level == '1' || level == 'x'].id"
	else:
		query=f"[?level == '{level}'].id"

	ids = jmespath.search(query, jclasscards)
	for id in ids:
		builddata=jmespath.search(f"cards[?id=='{id}'].[top, bottom, overall][]", jbuild)
		if len(builddata) == 0:
			builddata.append("The top action discussion.")
			builddata.append("The bottom action discussion.")
			builddata.append("The overall card discussion.")

		hf.write(html_new_card(id, builddata))

	hf.write('''
				</div>
			</div>
	''')

def html_new_card(id, data):
	card=f'''
				<div class="w3-card-4">
					<div class="w3-container w3-cell">
						<img class="ability-desc" src="{cardimages[id]}"/>
					</div>
					<div class="w3-container w3-cell w3-cell-middle">
						<p>{data[0]}
						<hr>
						<p>{data[1]}
					</div>
					<div class="w3-container w3-cell w3-cell-middle w3-light-grey">
						<p>{data[2]}
					</div>
				</div>
	'''
	return card

def html_choices(level):
	hf.write(f'''
		<button id="level-{level}-choices" onclick="accClick('acc-{level}-choices')" class="w3-btn w3-block w3-left-align">Level {level} Choices</button>
		<div id="acc-{level}-choices" class="w3-container w3-hide">
	''')
	
	choices=jmespath.search(f"levels[?level == '{level}'].choices[].[label,overview]", jbuild)
	for choice in choices:
		hf.write(f'''
			<div class="w3-container">
				<h3 class="w3-light-grey">{choice[0]}</h3>
				<p>{choice[1]}
				<div class="w3-flex" style="gap:8px;flex-wrap:wrap">
		''')

		cards = jmespath.search(f"levels[?level == '{level}'] | [0].choices[?label=='{choice[0]}'].cards[].[id,comment]", jbuild)
		for card in cards:
			hf.write(f'''
					<div class="w3-card-4" style="width:250px">
						<img class="ability-desc" src="{cardimages[card[0]]}"/>
						<p class="w3-container">{card[1]}
					</div>
			''')
			
		hf.write('''
				</div>
			</div>
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
	classname = jmespath.search(f"classes[?id=='{id}'].label|[0]", jclasses)
	return classname + " " + build

def get_card_images():
	cards = jmespath.search("[*].[image, id]", jclasscards)
	for data in cards:
		img=f"images/frosthaven/{data[0]}"
		cardimages.update({data[1]: img})

buildid="bn-tank"

# Read our json card data
with open('../data/card-data.json') as fd:
	jcards = json.load(fd)

with open('../data/class-data.json') as fd:
	jclasses = json.load(fd)

with open(f'../data/build-data.json') as fd:
	jbuilds = json.load(fd)

# Open the output html file
hf = open(f"../html/{buildid}.html", "w")

# Get the specific build
jbuild=jmespath.search(f"builds[?id=='{buildid}']|[0]", jbuilds)

classid=jmespath.search("classid", jbuild)
build=jmespath.search("build", jbuild)
buildname=get_build_name(classid, build)

# Get the cards json for only our class
jclasscards=jmespath.search(f"cards[?classid=='{classid}']", jcards)

# We reuse card so create a cache of their image path
cardimages = dict()
get_card_images()

html_top(buildname)
html_overview()
html_builddecks()
html_bottom()
