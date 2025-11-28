#!/home/archid/python/.archaven/bin/python

import argparse
import json
import jmespath

def html_create(jclass):
  id=jmespath.search('id', jclass)
  name=jmespath.search('label', jclass)
  label=name.lower().replace(" ", "-")
  olines=jmespath.search('overview', jclass)
  jdescription=jmespath.search('description', jclass)
  
  jclasscards=jmespath.search(f"cards[?classid=='{id}']", jcards)
  
  # Open the output html file
  hf = open(f"../{gamepath}/html/{id}-main.html", "w")
# hf = open(f"{id}-main.html", "w")
  
  hf.write(f'''<!DOCTYPE html>
<html>
<head>
  <title>{name}</title>
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="../../archaven.css">
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
      <tr><td><img src="images/character-mats/{gameprefix}-{label}.png"><td><img src="images/character-mats/{gameprefix}-{label}-back.png">
    </table>
  </div>

  <div class="w3-container">''')
  
  if not olines is None and len(olines) > 0:
    for line in olines:
      hf.write(f'''
    <p>{line}</p>''')
  
  if not jdescription is None and len(jdescription) > 0:
    for heading in jdescription:
      hlevel=jmespath.search('headinglevel', heading)
      htext=jmespath.search('headingtext', heading)
      hf.write(f'''
    <h{hlevel} class="w3-light-grey">{htext}</h{hlevel}>''')
      hcontarr=jmespath.search('content', heading)
      if not hcontarr is None and len(hcontarr) > 0:
        for hcont in hcontarr:
          hf.write(f'''
      <div class="w3-container">{hcont}</div>''')

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
      hf.write(f'''     <div class="w3-container w3-cell"><img class="card-med" src="{cardimages[id]}"></div>
''')

  hf.write(f'''   </div>
  </div>
</div>

</body>
  
<footer class="w3-container w3-teal">
  <div style="font-size:0.8rem">Built using assets from: <a href="https://github.com/any2cards/worldhaven">worldhaven github</a></div>
</footer>

</html>''')

parser = argparse.ArgumentParser(
                    prog='class-pages-create',
                    description='Reads a json file containing an xhaven class data and produces a static html page from it.',
                    epilog='This needs to be used with the archaven github repository file structure.')
parser.add_argument('game', choices=['fh','gh','gha'], help='game whose data should be parsed')
args = parser.parse_args()

gameprefix=args.game
gamepath=''
match gameprefix:
  case 'fh':
    gamepath='frosthaven'
  case 'gh':
    gamepath='gloomhaven'
  case 'gha':
    gamepath='gloomhaven-archid'

with open(f'../{gamepath}/data/class-data.json') as fd:
  jclasses = json.load(fd)

with open(f'../{gamepath}/data/card-data.json') as fd:
  jcards = json.load(fd)

jclasses = jmespath.search(f"classes", jclasses)

cardimages = dict()
cards = jmespath.search("cards[*].[image, id]", jcards)
for data in cards:
  img=f"images/{data[0]}"
  cardimages.update({data[1]: img})

for jclass in jclasses:
  html_create(jclass)
