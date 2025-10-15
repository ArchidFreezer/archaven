#!/home/archid/python/.archaven/bin/python

# Open the output json file
hf = open(f"build-template.json", "w")

hf.write('''{
	"builds": [
		{
			"id": "",
			"classid": "",
			"build": "",
			"orig_author": "",
			"orig_url": "",
			"overview": { 
				"body": [
					"",
					""
				],
				"benefits": [
					"",
					""
				],
				"preferences": [
					"",
					""
				]
			},
			"openers": [
				{
					"label": "",
					"level": x,
					"overview": "",
					"rounds": [
						{
							"top": "cardid",
							"bottom": "cardid",
							"strategy": ""
						},
												{
							"top": "cardid",
							"bottom": "cardid",
							"strategy": ""
						}
					]
				}
			],
			"cards": [
				{
					"id": "cardid",
					"top": "",
					"bottom": "",
					"overall": ""
				},
				{
					"id": "cardid",
					"top": "",
					"bottom": "",
					"overall": ""
				}
			]
			"levels": [
				{
					"level": 1,
					"handcomment": "",
					"choices": [
						{
							"label": "Core",
							"overview": "",
							"cards": [
								{
									"id": "cardid",
									"comment": ""
								},
								{
									"id": "cardid",
									"comment": ""
								}
							]
						},
						{
							"label": "",
							"overview": "",
							"cards": [
								{
									"id": "cardid",
									"comment": ""
								},
								{
									"id": "cardid",
									"comment": ""
								}
							]
						}
					],
					"hand": [
						{
							"card": "cardid",
							"top": {
								"text":"",
								"style": "w3-pale-green"
							},
							"bottom": {
								"text": "",
								"style": "w3-pale-red"
							}
						},
						{
							"card": "cardid",
							"top": {
								"text":"",
								"style": "w3-pale-yellow"
							},
							"bottom": {
								"text": "",
								"style": "w3-pale-blue"
							}
						}
					],
					"sideboard": [
						{
							"card": "cardid",
							"top": {
								"text":"",
								"style": ""
							},
							"bottom": {
								"text": "",
								"style": ""
							},
							"replace": "cardid",
							"comment": "on this condition"
						}
					]
				}
				{
					"level": x,
					"handcomment": "",
					"picks": [
						{
							"card": "cardid",
							"top": {
								"text":"",
								"style": ""
							},
							"bottom": {
								"text": "",
								"style": ""
							},
							"replace": "cardid",
							"comment": ""
						},
						{
							"card": "cardid",
							"top": {
								"text":"",
								"style": ""
							},
							"bottom": {
								"text": "",
								"style": ""
							},
							"replace": "cardid",
							"comment": ""
						}
					],
					"hand": [
						{
							"card": "cardid",
							"top": {
								"text":"",
								"style": "w3-pale-green"
							},
							"bottom": {
								"text": "",
								"style": "w3-pale-red"
							}
						},
						{
							"card": "cardid",
							"top": {
								"text":"",
								"style": "w3-pale-yellow"
							},
							"bottom": {
								"text": "",
								"style": "w3-pale-blue"
							}
						}
					],
					"sideboard": [
						{
							"card": "cardid",
							"top": {
								"text":"",
								"style": ""
							},
							"bottom": {
								"text": "",
								"style": ""
							},
							"replace": "cardid",
							"comment": "on this condition"
						}
					]
				}
			],
			"enhancements": [
				{
					"card": "cardid",
					"position": "top/bottom",
					"enhancement": "",
					"comment": ""
				},
				{
					"card": "cardid",
					"position": "top/bottom",
					"enhancement": "",
					"comment": ""
				}
			],
			"perks": [
				{
					"comment": "",
					"picks": [
						{
							"order": 1,
							"name": "",
							"effect": ""
						},
						{
							"order": 2,
							"name": "",
							"effect": ""
						}
					]
				},
				{
					"comment": "",
					"picks": [
						{
							"order": 1,
							"name": "",
							"effect": ""
						},
						{
							"order": 2,
							"name": "",
							"effect": ""
						}
					]
				}
			],
			"items": {
				"comments": "",
				"levels": [
					{
						"level": "Starting",
						"comments": "",
						"picks": [
							{
								"id": "itemid",
								"comment": ""
							},
							{
								"id": "itemid",
								"comment": ""
							}
						]
					},
					{
						"level": "Craftsman 1",
						"comments": "",
						"picks": [
							{
								"id": "itemid",
								"comment": ""
							},
							{
								"id": "itemid",
								"comment": ""
							}
						]
					}
				]
			},
			"potions": {
				"comments": "",
				"levels": [
					{
						"numherbs": "2",
						"comments": "",
						"picks": [
							{
								"id": "itemid",
								"comment": ""
							},
							{
								"id": "itemid",
								"comment": ""
							}
						]
					},
					{
						"numherbs": "",
						"comments": "",
						"picks": [
							{
								"id": "itemid",
								"comment": ""
							},
							{
								"id": "itemid",
								"comment": ""
							}
						]
					}
				]
			}
		}
	]
}''')