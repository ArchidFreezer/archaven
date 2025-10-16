#!/home/archid/python/.archaven/bin/python

import argparse
import json
import jmespath

def html_header(build):
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

<!-- Body -->
<div class="w3-container" style="margin-top:60px;z-index:-1;">
	''')

def html_overview():
	hf.write('''
	<!-- Overview -->
	<button id="overview" onclick="accClick('acc-overview')" class="w3-btn w3-block w3-left-align"><h2>Overview</h2></button>
	<div id="acc-overview" class="w3-container w3-hide">
	''')

	paras=jmespath.search("overview.body[]", jbuild)
	for para in paras:
		hf.write(f'''	<p>{para}</p>''')
	
	paras=jmespath.search("overview.benefits[]", jbuild)
	if len(paras) > 0:
		hf.write(f'''
		<p>So why would you play a {build} Build?</p>
		<ul>''')

		for para in paras:
			hf.write(f'''
			<li>{para}</li>''')

		hf.write(f'''
		</ul>
		''')
		
	paras=jmespath.search("overview.preferences[]", jbuild)
	if len(paras) > 0:
		hf.write(f'''
		<p>The tank build loves the following:</p>
		<ul>''')
	
		for para in paras:
			hf.write(f'''
			<li>{para}</li>''')
	
		hf.write('''
		</ul>
		''')
	
	hf.write('''
	</div> <!-- overview -->
	''')

def html_build_decks():
	hf.write('''
	<!-- Build Decks -->
	<div class="w3-container">
		<h2 id="deck">Build Deck</h2>
	''')
	
	for level in range(1,10):
		hf.write(f'''
		<button id="level-{level}" onclick="accClick('acc-{level}')" class="w3-btn w3-block w3-left-align">Level {level}</button>
		<div id="acc-{level}" class="w3-container w3-hide">
		''')
		html_new_cards(level)
		html_choices(level)
		html_hand(level)
		html_openers(level)
		
		hf.write(f'''
		</div> <!-- level {level} -->
		''')
	
	hf.write('''
	</div> <!-- build deck -->
	''')

def html_openers(level):
	openers=jmespath.search(f"openers[?level==`{level}`]", jbuild)
	if len(openers) > 0:
		hf.write(f'''
			<button id="level-openers" onclick="accClick('acc-{level}-openers')" class="w3-btn w3-block w3-left-align">Openers</button>
			<div id="acc-{level}-openers" class="w3-container w3-hide">
				<div class="w3-flex" style="gap:8px;flex-wrap:wrap">
		''')
		
		for jopener in openers:
			hf.write(html_opener_card(jopener))

		hf.write('''
				</div>
			</div> <!-- openers -->''')

def html_opener_card(jopener):
	basic=jmespath.search("[label, overview]", jopener)
	card=(f'''
					<div class="w3-card-4">
						<div class="w3-container w3-cell">
							<header class="w3-light-grey"><p>{basic[0]}</p></header>
	''')
				
	rounds=jmespath.search("rounds", jopener)
	for jround in rounds:
		round=jmespath.search("[top,bottom,strategy]", jround)
		card+=(f'''
							<div class="w3-container w3-cell w3-center">
								<img class="card-small" src="{cardimages[round[0]]}"/>
								<p></p>
								<img class="card-small" src="{cardimages[round[1]]}"/>
								<div style="width: 250px">{round[2]}</div>
							</div>
		''')

	card+=(f'''
							<footer class="w3-light-grey"><p>{basic[1]}</p></footer>
						</div>
					</div>
	''')
	
	return card
	
def html_hand(level):
	jhand=jmespath.search(f"levels[?level==`{level}`].hand[]", jbuild)
	if len(jhand) > 0:
		jhandcomment=jmespath.search(f"levels[?level==`{level}`].handcomment", jbuild)
		if len(jhandcomment) == 0:
			comment="This is the default hand to use at this level, however it should be modified based on the quest."
		else:
			comment=jhandcomment[0]
		hf.write(f'''
			<button id="level-{level}-hand" onclick="accClick('acc-{level}-hand')" class="w3-btn w3-block w3-left-align">Level {level} Hand</button>
			<div id="acc-{level}-hand" class="w3-container w3-hide">
				<div class="w3-container">
					<h3 class="w3-light-grey">Standard Hand</h3>
					<p>{comment}</p>
					<div class="w3-flex" style="gap:8px;flex-wrap:wrap">
		''')
		for jcard in jhand:
			hf.write(html_hand_card(jcard))
			
		hf.write(f'''
					</div>
				</div> <!-- standard level {level} cards -->
		''')
	
		jsideboard=jmespath.search(f"levels[?level==`{level}`].sideboard[]", jbuild)
		if len(jsideboard) > 0:
			hf.write('''
				<div class="w3-container">
					<h3 class="w3-light-grey">Sideboard Cards</h3>
					<p>These are cards that may be swapped in based on quest requirements</p>
					<div class="w3-flex" style="gap:8px;flex-wrap:wrap">
			''')

			for jcard in jsideboard:
				hf.write(html_hand_replacement_card(jcard))

			hf.write(f'''
					</div>
				</div> <!-- sideboard cards -->''')
				
		hf.write(f'''
			</div> <!-- level {level} hand -->
			''')

def html_hand_replacement_card(jcard):
	data=jmespath.search("[card, top.text, top.style, bottom.text, bottom.style, replace, comment]", jcard)
	card=f'''
						<div class="w3-card-4">
							<div class="w3-container w3-cell">
								<header class="w3-light-grey"><p>Take</p></header>
								<img class="card-small" src="{cardimages[data[0]]}">
								<p class="{data[2]}">{data[1]}</p>
								<p class="{data[4]}">{data[3]}</p>
							</div>
							<div class="w3-container w3-cell w3-cell-middle">
								<header class="w3-light-grey"><p>Replace</p></header>
								<img class="card-small" src="{cardimages[data[5]]}">
								<p class="w3-light-grey">-</p>
								<p class="w3-light-grey">-</p>
							</div>
							<div class="w3-container w3-cell w3-cell-middle w3-light-grey">
								<p>{data[6]}</p>
							</div>
						</div>
	'''
	return card

def html_hand_card(jcard):
	data=jmespath.search("[card, top.text, top.style, bottom.text, bottom.style]", jcard)
	card=f'''
						<div class="w3-card-4">
							<div class="w3-container w3-cell">
								<img class="card-med" src="{cardimages[data[0]]}">
								<p class="{data[2]}">{data[1]}</p>
								<p class="{data[4]}">{data[3]}</p>
							</div>
						</div>
	'''
	return card

def html_new_cards(level):
	hf.write(f'''
			<button id="level-{level}-new" onclick="accClick('acc-{level}-new')" class="w3-btn w3-block w3-left-align">New Level {level} Cards</button>
			<div id="acc-{level}-new" class="w3-container w3-hide">
				<h3 class="w3-light-grey">New Cards</h3>
				<div class="w3-flex" style="gap:4px;flex-direction:column">
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

	hf.write(f'''
				</div> <!-- new cards -->''')

	jpicks=jmespath.search(f"levels[?level==`{level}`].picks[]", jbuild)
	if len(jpicks) > 0:
		hf.write('''
				<div class="w3-container">
					<h3 class="w3-light-grey">Picks</h3>
					<div class="w3-flex" style="gap:8px;flex-wrap:wrap">
		''')

		for jcard in jpicks:
			hf.write(html_hand_replacement_card(jcard))

		hf.write('''
					</div>
				</div> <!-- new picks -->''')
				
	hf.write(f'''
				<p></p>
			</div> <!-- new level {level} cards -->
	''')

def html_new_card(id, data):
	card=f'''
					<div class="w3-card-4">
						<div class="w3-container w3-cell">
							<img class="card-med" src="{cardimages[id]}">
						</div>
						<div class="w3-container w3-cell w3-cell-middle">
							<p>{data[0]}</p>
							<hr>
							<p>{data[1]}</p>
						</div>
						<div class="w3-container w3-cell w3-cell-middle w3-light-grey">
							<p>{data[2]}</p>
						</div>
					</div>
	'''
	return card

def html_choices(level):
	choices=jmespath.search(f"levels[?level == `{level}`].choices[].[label,overview]", jbuild)
	if len(choices) > 0:
		hf.write(f'''
			<button id="level-{level}-choices" onclick="accClick('acc-{level}-choices')" class="w3-btn w3-block w3-left-align">Level {level} Choices</button>
			<div id="acc-{level}-choices" class="w3-container w3-hide">
		''')
	
		for choice in choices:
			hf.write(f'''
				<div class="w3-container">
					<h3 class="w3-light-grey">{choice[0]}</h3>
					<p>{choice[1]}</p>
					<div class="w3-flex" style="gap:8px;flex-wrap:wrap">
			''')

			cards = jmespath.search(f"levels[?level == `{level}`] | [0].choices[?label=='{choice[0]}'].cards[].[id,comment]", jbuild)
			for card in cards:
				hf.write(f'''
						<div class="w3-card-4" style="width:250px">
							<img class="card-med" src="{cardimages[card[0]]}">
							<p class="w3-container">{card[1]}</p>
						</div>
				''')
				
			hf.write('''
					</div>
				</div>''')
		hf.write('''
			</div> <!-- choices -->
		''')

def html_enhancements():
	enhancements=jmespath.search(f"enhancements[].[card,position,enhancement,comment]", jbuild)
	if not enhancements is None:
		hf.write('''
	<!-- Enhancements -->
	<button id="enhancements" onclick="accClick('acc-enhancements')" class="w3-btn w3-block w3-left-align"><h2>Enhancements</h2></button>
	<div id="acc-enhancements" class="w3-container w3-hide">
		<table class="w3-table w3-striped w3-border">''')

		for enhancement in enhancements:
			hf.write(f'''
			<tr><td><img class="card-small" src="{cardimages[enhancement[0]]}"></td><td>{enhancement[1]}</td><td>{enhancement[2]}</td><td>{enhancement[3]}</td></tr>''')
	
		hf.write('''
		</table>
	</div> <!-- enhancements -->
	''')
	
def html_perks():
	jperks=jmespath.search(f"perks[]", jbuild)
	if len(jperks) > 0:
		hf.write('''
	<!-- Perks -->
	<button id="perks" onclick="accClick('acc-perks')" class="w3-btn w3-block w3-left-align"><h2>Perks</h2></button>
	<div id="acc-perks" class="w3-container w3-hide">
''')	
	
		for jperk in jperks:
			hf.write(f'''
		<div class="w3-light-grey">{jmespath.search("comment", jperk)}</div>
		<table class="w3-table w3-border">''')
			
			picks=jmespath.search(f"sort_by(picks, &order)[*][name,effect]", jperk)
			for pick in picks:
				hf.write(f'''
			<tr><td width="250px">{pick[0]}</td><td>{pick[1]}</td></tr>''')
		
			hf.write('''
		</table><br>
''')

		hf.write('''
	</div> <!-- perks -->
''')

def html_items():
	jitems=jmespath.search("items", jbuild)
	if not jitems is None:
		hf.write(f'''
	<!-- Items -->
	<button id="items" onclick="accClick('acc-items')" class="w3-btn w3-block w3-left-align"><h2>Items</h2></button>
	<div id="acc-items" class="w3-container w3-hide">
		<div class="w3-container w3-light-grey">{jmespath.search("comments", jitems)}</div>
	''')
		
		levels=jmespath.search("levels", jitems)
		for jlevel in levels:
			level=jmespath.search("level", jlevel)
			levelid=level.lower().replace(" ","")
			hf.write(f'''
		<button id="items-{levelid}" onclick="accClick('acc-items-{levelid}')" class="w3-btn w3-block w3-left-align"><h4>{level}</h4></button>
		<div id="acc-items-{levelid}" class="w3-container w3-hide">
			<div class="w3-container w3-light-grey"><p>{jmespath.search("comments", jlevel)}</p></div>
			<div class="w3-flex" style="gap:8px;flex-wrap:wrap">
			''')
			picks=jmespath.search("picks", jlevel)
			for jpick in picks:
				data=jmespath.search("[id,comment]", jpick)
				hf.write(f'''
				<div class="w3-card-4" style="width:250px">
					<img class="card-med" src="{itemimages[data[0]]}">
					<p class="w3-container">{data[1]}</p>
				</div>
				''')
				
			hf.write('''
			</div>
		</div>''')
	
		hf.write('''
	</div> <!-- items -->
		''')

def html_potions():
	jpotions=jmespath.search("potions", jbuild)
	if not jpotions is None:
		hf.write(f'''
	<!-- Potions -->
	<button id="potions" onclick="accClick('acc-potions')" class="w3-btn w3-block w3-left-align"><h2>Potions</h2></button>
	<div id="acc-potions" class="w3-container w3-hide">
		<div class="w3-container w3-light-grey">{jmespath.search("comments", jpotions)}</div>
	''')
		
		levels=jmespath.search("levels", jpotions)
		for jlevel in levels:
			numherbs=jmespath.search("numherbs", jlevel)
			hf.write(f'''
		<button id="items-{numherbs}" onclick="accClick('acc-items-{numherbs}')" class="w3-btn w3-block w3-left-align"><h4>{numherbs} Herb</h4></button>
		<div id="acc-items-{numherbs}" class="w3-container w3-hide">
			<div class="w3-container w3-light-grey"><p>{jmespath.search("comments", jlevel)}</p></div>
			<div class="w3-flex" style="gap:8px;flex-wrap:wrap">
			''')
			picks=jmespath.search("picks", jlevel)
			for jpick in picks:
				data=jmespath.search("[id,comment]", jpick)
				hf.write(f'''
				<div class="w3-card-4" style="width:250px">
					<img class="card-med" src="{itemimages[data[0]]}">
					<p class="w3-container">{data[1]}</p>
				</div>
				''')
				
			hf.write('''
			</div>
		</div>''')
	
		hf.write('''
	</div> <!-- potions -->
		''')
	
def html_footer():
	txt=jmespath.search("build", jbuild)
	author=jmespath.search("orig_author", jbuild)
	if len(author) > 0:
		txt+=f" based on {author} build"
	url=jmespath.search("orig_url", jbuild)
	if len(url) > 0:
		txt+=f''' (<a href="{url}">{url}</a>)'''
		
	hf.write(f'''
</div> <!-- body -->

<footer class="w3-container w3-teal">
	<div style="font-size:0.8rem">{txt}</div>
</footer>

</body>
</html>
	''')

def get_build_name(id, build):
	classname = jmespath.search(f"classes[?id=='{id}'].label|[0]", jclasses)
	return classname + " " + build

def cache_card_images():
	cards = jmespath.search("[*].[image, id]", jclasscards)
	for data in cards:
		img=f"images/frosthaven/{data[0]}"
		cardimages.update({data[1]: img})

def cache_item_images():
	items = jmespath.search("items[*].[image, id]", jitems)
	for data in items:
		img=f"images/frosthaven/{data[0]}"
		itemimages.update({data[1]: img})

parser = argparse.ArgumentParser(
                    prog='parse-build',
                    description='Reads a json file containing Frosthaven character build data and produces a static html page from it.',
                    epilog='This needs to be used with the archaven github repository file structure.')
parser.add_argument('-b', help='build id to parse')
parser.add_argument('-d', help='json file containing the build details')
args = parser.parse_args()

if (args.d):
	buildfile=args.d
else:
	buildfile='../data/build-data.json'


# Read our json data files
with open('../data/card-data.json') as fd:
	jcards = json.load(fd)

with open(f'../data/item-data.json') as fd:
	jitems = json.load(fd)

with open('../data/class-data.json') as fd:
	jclasses = json.load(fd)

with open(buildfile) as fd:
	jbuilds = json.load(fd)

if (args.b):
	buildids=[args.b]
else:
	buildids=jmespath.search("builds[*].id", jbuilds)

itemimages = dict()
cache_item_images()

for buildid in buildids:
	# Open the output html file
	hf = open(f"../html/{buildid}.html", "w")
	
	# Get the specific build
	jbuild=jmespath.search(f"builds[?id=='{buildid}']|[0]", jbuilds)

	classid=jmespath.search("classid", jbuild)
	build=jmespath.search("build", jbuild)
	buildname=get_build_name(classid, build)
	print("Processing: " + buildname)

	# Get the cards json for only our class
	jclasscards=jmespath.search(f"cards[?classid=='{classid}']", jcards)
	cardimages = dict()
	cache_card_images()
	
	html_header(buildname)
	html_overview()
	html_build_decks()
	html_enhancements()
	html_perks()
	html_items()
	html_potions()
	html_footer()
