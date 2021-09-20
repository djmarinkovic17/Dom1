import requests
import json

url = "https://getpantry.cloud/apiv1/pantry/3ab3757e-2586-4248-8cd5-843b30ae8ab8/basket/Student_podatci"

payload = json.dumps({
	"id": "119I17",
	"ime": "Djordje",
	"prezime": "Marinkovic",
	"smer": "RM",
	"predmeti": [
		"engleski",
		"fizicko",
		"srpski",
		"filozofija",
		"ors"
	],
	"prosek": 6.7,
	"kontakt": {
		"adresa": "Beogradska 20",
		"mesto": "Beograd",
		"telefon": "060 111 2233"
	}
})
headers = {
	'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)