import requests



url = "https://datacrunch.9c9media.ca/statsapi/sports/hockey/leagues/nhl/sortablePlayerSeasonStats/goaltender"

querystring = {"brand":"tsn","type":"json","seasonType":"regularSeason","season":"2021"}

payload = ""
headers = {"cookie": "TS01b5e851=01881d1d7e652bab697978b77de19a76b67d3210fe4036a6c914beb170ab5c7ff92a460c7029a25fa8cd16dc1eb1f7ad8efb15ca4e"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)

with open("goaliestats.json", 'w+') as goalies:
    goalies.write(response.text)
    goalies.close()
