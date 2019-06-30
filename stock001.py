import requests
url='https://open.lixinger.com/api/a/stock/fundamental'
para={
	"token": "92b790f7-88a9-4444-98d8-574352028ad4",
	"date": "2019-06-28",
	"stockCodes": [
		"000028",
		"600519"
	],
	"metrics": [
		"pe_ttm",
		"mc",
        "sp"
	]
}


r = requests.post(url,para)

#print(r.text)