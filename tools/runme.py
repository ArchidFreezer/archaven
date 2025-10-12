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
		<p>The Tank build is more of a sub-build of a Spear build than a completely independent build, given the Banner Spear doesn’t have that many dedicated tanking cards. But more than anything, choosing to play this build represents a slightly different focus, which is based on protecting the party as much as possible rather than maximizing your damage output.</p>
		
		<p>So why would you play a Tank Build? This will mostly come down to party composition:</p>
		<ul>
			<li>Your group is mostly fragile and cannot afford to take many hits. In that case, your party will typically have plenty of damage output, but survivability will be a concern. Accordingly, rather than focusing on your output, your focus will be keeping everyone alive.</li>
			<li>You lack melee allies who can consistently help you out in setting up formations. While you will still play some formation attacks, you’ll mostly stick to the easier ones, and you’ll still play less of them.</li>
		</ul>
		
		<p>The tank build loves the following:</p>
		<ul>
			<li>Boneshaper. A Boneshaper appreciates having a tank to keep her summons alive longer, allowing them to deal more damage. And while you care less about formations than a Spear build, you do still use some of them, which Skeletons help you to more easily set up.</li>
			<li>Damage-dealers and a bit of support. Obviously every tank would like a bit of support for healing, and as you’re going to be more focused on mitigating incoming damage to the party, you do need allies whose primary aim is killing enemies.</li>
			<li>An example of an ideal four-character party for a Tank build would be something like: Ranged+Healing Drifter, Skeleton Swarm Boneshaper, Ranged Deathwalker, and Banner Spear.</li>
		</ul>
	</div>
	''')

def html_builddeck():
	hf.write('''
	<div class="w3-container">
		<h2 id="deck">Build Deck</h2>
	''')
	
	for index in range(1,10):
		html_levelcardstable("banner spear", index)
	
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
		query=f"cards[?character=='{char}' && (level == '1' || level == 'x')].image"
	else:
		query=f"cards[?character=='{char}' && level == '{level}'].image"

	images = jmespath.search(query, jcards)
	for image in images:
		hf.write(f'''
				<tr>
					<td rowspan="2"><img class="ability-desc" src="images/frosthaven/{image}"/>
					<td class="w3-container" style="width:60%">The top action discussion.
					<td class="w3-container" rowspan="2">Overall card discussion.
				<tr>
					<td class="w3-container">The bottom action discussion.
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

# Read our json card data
with open('../data/card-data.json') as fd:
	jcards = json.load(fd)

# Open the output html file
hf = open("../html/test.html", "w")

html_top("Banner Spear Tank")
html_overview()
html_builddeck()
html_bottom()
