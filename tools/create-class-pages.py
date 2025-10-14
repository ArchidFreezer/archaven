#!/home/archid/python/.archaven/bin/python

import argparse
import json
import jmespath

def html_create(jclass):
	id=jmespath.search('id', jclass)
	name=jmespath.search('label', jclass)
	label=name.lower().replace(" ", "-")
	dlines=jmespath.search('description', jclass)
	
	jclasscards=jmespath.search(f"cards[?classid=='{id}']", jcards)
	
	# Open the output html file
	hf = open(f"../html/{id}-main.html", "w")
#	hf = open(f"{id}-main.html", "w")
	
	hf.write(f'''<!DOCTYPE html>
<html>
<head>
	<title>{name}</title>
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" href="archaven.css">
</head>
<body>

<script src="mainsidebar.js"></script>

<header class="w3-top w3-display-container w3-green" style="height:60px">
	<button class="w3-button w3-xlarge w3-display-left" onclick="mainsidebar_open()">☰</button>
	<h1 class="w3-display-middle">{name}</h1>
</header>

<div class="w3-container" style="margin-top:60px;z-index:-1;">

	<div class="w3-container">
		<table>
			<tr><td><img src="images/frosthaven/character-mats/fh-{label}.png"><td><img src="images/frosthaven/character-mats/fh-{label}-back.png">
		</table>
	</div>

	<div class="w3-container">''')
	
	for line in dlines:
		hf.write(f'''
		<p>{line}</p>''')
	
	hf.write(f'''
		<h3 class="w3-light-grey">Cards</h3>
		<div class="w3-flex" style="gap:4px;flex-wrap:wrap">
''')

	for level in range(1,10):
		if level == 1:
			query=f"[?level == '1' || level == 'x'].id"
		else:
			query=f"[?level == '{level}'].id"

		ids = jmespath.search(query, jclasscards)
		for id in ids:
			hf.write(f'''			<div class="w3-container w3-cell"><img class="card-med" src="{cardimages[id]}"></div>
''')

	hf.write(f'''		</div>
	</div>
</div>

</body>
	
<footer class="w3-container w3-teal">
	<div style="font-size:0.8rem">Built using assets from: <a href="https://github.com/any2cards/worldhaven">worldhaven github</a></div>
</footer>

</html>''')

with open('../data/class-data.json') as fd:
	jclasses = json.load(fd)

with open('../data/card-data.json') as fd:
	jcards = json.load(fd)

jclasses = jmespath.search(f"classes", jclasses)

cardimages = dict()
cards = jmespath.search("cards[*].[image, id]", jcards)
for data in cards:
	img=f"images/frosthaven/{data[0]}"
	cardimages.update({data[1]: img})

for jclass in jclasses:
	html_create(jclass)
