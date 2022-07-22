import json


with open('skaterstats.json') as player:#opens json file and reads it, stores it as  a variable
    playerdata = json.load(player)



#for i in playerdata:
    #print(i['stats']['name']+',', i['stats']['position'])
    #print('A:', i['stats']['assists'],'G:',i['stats']['goals'],
          #'P:', i['stats']['points'], 'PIM:',i['stats']['penaltyInMinutes'], 'Blocked Shots:',i['stats']['blockedShots'],
          #'TOI:',i['stats']['averageTimeOnIce'], 'Hits:',i['stats']['hits'])
goals = []
names = []
assists = []
points = []
hits = []

playerName_goals = []
playerName_assists = []
playerName_points = []
playerName_hits = []
for i in playerdata:#all players with more than 10 games played(all player)
    if int(i['stats']['gamesPlayed']) > 20:
        names.append(i['stats']['name'])
        goals.append(int(i['stats']['goals']))
        assists.append(int(i['stats']['assists']))
        points.append(int(i['stats']['points']))
        hits.append(int(i['stats']['hits']))

for i in playerdata:#all players with more than 10 games and more than 15 goals (top goal scorers)
    if int(i['stats']['goals']) > 25:
        playerName_goals.append(i['stats']['name'])
        goals.append(int(i['stats']['goals']))



for i in playerdata:#all players with more than 10 games and more than 20 assists(top assisters)
    if int(i['stats']['assists']) > 20:
        playerName_assists.append(i['stats']['name'])
        assists.append(int(i['stats']['assists']))


for i in playerdata:#all players with more than 10 games and more than 20 points(top point scorers)
    if int(i['stats']['points']) > 35:
        playerName_points.append(i['stats']['name'])
        points.append(int(i['stats']['points']))

for i in playerdata:#all players with more than 10 games and more than 85 hits
    #if int(i['stats']['hits']) > 20:
    playerName_hits.append(i['stats']['name'])
    hits.append(int(i['stats']['hits']))

goalScorers = dict(zip(playerName_goals,goals))
assisters = dict(zip(playerName_assists,assists))
pointScorers = dict(zip(playerName_points, points))
hitters = dict(zip(playerName_hits, hits))


best_goalScorers = {p: g for p,g in sorted(goalScorers.items(),key=lambda g: g[1], reverse=True)}
best_assisters = {p: a for p,a in sorted(assisters.items(), key=lambda a: a[1], reverse=True)}
best_pointScorers = {p: s for p,s in sorted(pointScorers.items(), key=lambda s: s[1], reverse=True)}
best_hitters = {p: h for p,h in sorted(hitters.items(), key=lambda h: h[1], reverse=True)}

for i,j in best_pointScorers.items():
    print(i,j)

def sort_players_descending(stat):
    for player, statistic in stat.items():
        print(player, statistic)
#sort_players_descending(best_goalScorers)
#sort_players_descending(best_assisters)
#sort_players_descending(best_pointScorers)
sort_players_descending(best_hitters)