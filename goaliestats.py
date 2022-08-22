import json
import operator



with open('goaliestats.json') as goalie: #opens the goalie file
    goaltenderstats = json.load(goalie)

save_percentage = []
wins = []
saves = []
shutouts = []
avg_goals_against = []


for goaltender in goaltenderstats:
    if int(goaltender['stats']['gamesPlayed']) > 20:


        city = goaltender['stats']['competitor-seo-identifier']  # the team (or city) that a skater plays for

        if city == 'new-york-rangers':
            city = 'NYR'
        elif goaltender['stats']['competitor-seo-identifier'] == 'new-york-islanders':
            city = 'NYI'
        elif goaltender['stats']['competitor-seo-identifier'] == 'calgary-flames':
            city = 'CGY'
        elif goaltender['stats']['competitor-seo-identifier'] == 'tampa-bay-lightning':
            city = 'TBL'
        elif goaltender['stats']['competitor-seo-identifier'] == 'vegas-golden-knights':
            city = 'VGK'
        elif goaltender['stats']['competitor-seo-identifier'] == 'los-angeles-kings':
            city = 'LAK'
        elif goaltender['stats']['competitor-seo-identifier'] == 'st-louis-blues':
            city = 'STL'
        elif goaltender['stats']['competitor-seo-identifier'] == 'new-jersey-devils':
            city = 'NJ'
        elif goaltender['stats']['competitor-seo-identifier'] == 'san-jose-sharks':
            city = 'SJS'
        elif goaltender['stats']['competitor-seo-identifier'] == 'florida-panthers':
            city = 'FLA'
        elif goaltender['stats']['competitor-seo-identifier'] == 'columbus-blue-jackets':
            city = 'CBJ'
        elif goaltender['stats']['competitor-seo-identifier'] == 'nashville-predators':
            city = 'NSH'
        else:
            city = goaltender['stats']['competitor-seo-identifier']



        most_shutouts = [goaltender['stats']['name'], int(goaltender['stats']['shutouts']), city[0:3].upper()]
        shutouts.append(most_shutouts)

        num_wins = [goaltender['stats']['name'], int(goaltender['stats']['wins']), city[0:3].upper()]
        wins.append(num_wins)

        num_saves = [goaltender['stats']['name'], int(goaltender['stats']['saves']), city[0:3].upper()]
        saves.append(num_saves)

        lowest_goals_against = [goaltender['stats']['name'], float(goaltender['stats']['goalsAgainstAverage']), city[0:3].upper()]
        avg_goals_against.append(lowest_goals_against)


        highest_save_percent = [goaltender['stats']['name'], float(goaltender['stats']['savePercentage']), city[0:3].upper()]
        save_percentage.append(highest_save_percent)



sorted_shutouts = sorted(shutouts, key=operator.itemgetter(1), reverse=True)
tuple_shutouts = tuple(tuple(goaltender) for goaltender in sorted_shutouts[0:5])

sorted_wins = sorted(wins, key=operator.itemgetter(1), reverse=True)
tuple_wins = tuple(tuple(goaltender) for goaltender in sorted_wins[0:5])

sorted_saves = sorted(saves, key=operator.itemgetter(1), reverse=True)
tuple_saves = tuple(tuple(goaltender) for goaltender in sorted_saves[0:5])

sorted_save_percentage = sorted(save_percentage, key=operator.itemgetter(1), reverse=True)
tuple_save_percent = tuple(tuple(goaltender) for goaltender in sorted_save_percentage[0:5])

sorted_avg_goals_against = sorted(avg_goals_against, key=operator.itemgetter(1), reverse=False)
tuple_GAA = tuple(tuple(goaltender) for goaltender in sorted_avg_goals_against[0:5])
