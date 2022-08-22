import requests

"""
url = "https://datacrunch.9c9media.ca/statsapi/sports/hockey/leagues/nhl/leaders"

querystring = {"brand":"tsn","type":"json"}

payload = ""
headers = {"cookie": "TS01b5e851=01881d1d7e652bab697978b77de19a76b67d3210fe4036a6c914beb170ab5c7ff92a460c7029a25fa8cd16dc1eb1f7ad8efb15ca4e; TS01cb24f5=01881d1d7eff90b9415b794260970178eb0d4604163888307da6b26a5c26ad2557deace2ec4b263a3efc13eea857c360a85e34e297"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)


url = "https://datacrunch.9c9media.ca/statsapi/sports/hockey/leagues/nhl/sortablePlayerSeasonStats/skater"

querystring = {"brand":"tsn","type":"json","seasonType":"regularSeason","season":"2021"}

payload = ""
headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.tsn.ca",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "datacrunch.9c9media.ca",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Accept-Language": "en-us",
    "Referer": "https://www.tsn.ca/",
    "Connection": "keep-alive"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
"""





url = "https://datacrunch.9c9media.ca/statsapi/sports/hockey/leagues/nhl/sortablePlayerSeasonStats/skater"

querystring = {"brand":"tsn","type":"json","seasonType":"regularSeason","season":"2021"}

payload = ""
headers = {"cookie": "TS01b5e851=01881d1d7e652bab697978b77de19a76b67d3210fe4036a6c914beb170ab5c7ff92a460c7029a25fa8cd16dc1eb1f7ad8efb15ca4e; TS01cb24f5=01881d1d7e96fdb9b0cf2c1765faa91429e37604136329f04be9ea68c79b29574bb5753abb47ce827340764aa4f2d399ac30f5f5aa"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)

with open("skaterstats.json", 'w+') as skaters:
    skaters.write(response.text)
    skaters.close()