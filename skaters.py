import requests

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

with open("skaterstats.json", 'w+') as skaters:
    skaters.write(response.text)
    skaters.close()