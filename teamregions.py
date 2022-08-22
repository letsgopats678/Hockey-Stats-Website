import json

with open('divisionteams.json') as teams:
    franchises = json.load(teams)

hockey_teams = []

def divisions():#function brings in divisions in order
    for i in franchises:    #sorts the teams in each division in order
        #print(i)
        #print(f"\n{i['division']['label']}")
        #hockey_teams.append(i['division']['label'])
        for j in i['competitorStats']:

            division_team_stats = [j['competitor']['place'], j['competitor']['shortName'],j['competitor']['recordOverall'], j['competitor']['points'],
                  j['stats']['goalsFor'], j['stats']['goalsAgainst'],j['competitor']['streak'], j['stats']['lastTen']]
            hockey_teams.append(division_team_stats)

divisions()
tuple_teams_atl = tuple(tuple(team) for team in hockey_teams[0:8])
tuple_teams_metro = tuple(tuple(team) for team in hockey_teams[8:16])
tuple_teams_central = tuple(tuple(team) for team in hockey_teams[16:24])
tuple_teams_pacific = tuple(tuple(team) for team in hockey_teams[24:])

#html css from w3schools from w3chools
#javascript functionality from w3 schools
