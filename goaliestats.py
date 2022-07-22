import json




with open('goaliestats.json') as goalie: #opens the goalie file
    goaliestats = json.load(goalie)
#for i in goaliestats:
    #print(i['stats']['name'])
    #print('GAA:',i['stats']['goalsAgainstAverage'], 'GA:',i['stats']['goalsAgainst'],
          #'SV%:',i['stats']['savePercentage'], 'Saves:',i['stats']['saves'], 'SA:',i['stats']['shotsAgainst'],
          #'Shutouts:',i['stats']['shutouts'], 'W:',i['stats']['wins'])

"""
arrays for holding the stats of each goaltender
"""
goalsAgainstAverage = []
goalsAgainst = []
savePercentage = []
save = []
shutouts = []
shotsAgainst = []
wins = []

"""
stores the leaders(names of goaltenders) in each area in array (list)
"""
namesGAA = []
namesGA = []
namesSV = []
namesSaves = []
namesSA = []
names_shutouts = []
namesWins = []

"""
this function parses through the goalistats api data and returns the goaltenders
in descending order (best to worst)
"""
for i in goaliestats:
    if float(i['stats']['goalsAgainstAverage']) < 2.79:
        namesGAA.append(i['stats']['name'])
        goalsAgainstAverage.append(float(i['stats']['goalsAgainstAverage']))

for i in goaliestats:
    if int(i['stats']['goalsAgainst']) < 40:
        namesGA.append(i['stats']['name'])
        goalsAgainst.append(int(i['stats']['goalsAgainst']))

for i in goaliestats:
    if float(i['stats']['savePercentage']) > .922:
        namesSV.append(i['stats']['name'])
        savePercentage.append(float(i['stats']['savePercentage']))

for i in goaliestats:
    if int(i['stats']['shotsAgainst']) > 700:
        namesSA.append(i['stats']['name'])
        shotsAgainst.append(int(i['stats']['shotsAgainst']))

for i in goaliestats:
    if int(i['stats']['saves']) > 640:
        namesSaves.append(i['stats']['name'])
        save.append(int(i['stats']['saves']))


for i in goaliestats:
    if int(i['stats']['shutouts']) >= 3:
        names_shutouts.append(i['stats']['name'])
        shutouts.append(int(i['stats']['shutouts']))

for i in goaliestats:
    if int(i['stats']['wins']) > 14:
        namesWins.append(i['stats']['name'])
        wins.append(int(i['stats']['wins']))


"""
connects the names of goaltenders and ties it with a specific stat, and zips it into a dictionary (name:kay, stat is the value)
"""


GAA = dict(zip(namesGAA,goalsAgainstAverage))
GA = dict(zip(namesGA,goalsAgainst))
SV = dict(zip(namesSV,savePercentage))
saves = dict(zip(namesSaves,save))
SA = dict(zip(namesSA, shotsAgainst))
shutouts = dict(zip(names_shutouts,shutouts))
wins = dict(zip(namesWins, wins))

"""
dictionaries that sorts the goaltender stats in ascending order
"""
lowest_GAA = {g: gaa for g,gaa in sorted(GAA.items(), key= lambda gaa: gaa[1])}




lowest_GA = {g: ga for g,ga in sorted(GA.items(), key= lambda ga:ga[1])}
highest_SV = {g: sv for g,sv in sorted(SV.items(), key=lambda sv: sv[1], reverse=True)}
most_saves = {g: s for g,s in sorted(saves.items(), key= lambda s: s[1], reverse=True)}
most_SA = {g: sa for g,sa in sorted(SA.items(), key=lambda sa: sa[1], reverse=True)}
most_shutouts = {g: so for g,so in sorted(shutouts.items(), key=lambda so: so[1], reverse=True)}
most_wins = {g: w for g,w in sorted(wins.items(), key= lambda w: w[1], reverse=True)}

def sort_goalies_descending(stat):
    for goalie,statistic in stat.items():
        print(goalie,statistic)

sort_goalies_descending(most_wins)