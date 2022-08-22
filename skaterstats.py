import json
import operator

with open('skaterstats.json') as player:#opens json file and reads it, stores it as  a variable
    playerdata = json.load(player)

#lists set for each type of statistic in the nhl storage (data structure)
goal_scorers = []
point_scorers = []
assist_scorers = []
biggest_hitters = []
shorthanded_scorers = []
shot_blockers = []
pp_goal_scorers = []
faceoff_winners = []
plus_minus_list = []
penalty_minutes = []
game_winning_goals = []

def adding_players():
    for i in playerdata:#all players with more than 10 games played(all player)

        position_player = i['stats']['position'] #returns the position of a specific player
        city = i['stats']['competitor-seo-identifier'] #the team (or city) that a skater plays for

        if city == 'new-york-rangers':
            city = 'NYR'
        elif i['stats']['competitor-seo-identifier'] == 'new-york-islanders:':
            city = 'NYI'
        elif i['stats']['competitor-seo-identifier'] == 'calgary-flames':
            city = 'CGY'
        elif i['stats']['competitor-seo-identifier'] == 'tampa-bay-lightning':
            city = 'TBL'
        elif i['stats']['competitor-seo-identifier'] == 'vegas-golden-knights':
            city = 'VGK'
        elif i['stats']['competitor-seo-identifier'] == 'los-angeles-kings':
            city = 'LAK'
        elif i['stats']['competitor-seo-identifier'] == 'st-louis-blues':
            city = 'STL'
        elif i['stats']['competitor-seo-identifier'] == 'new-jersey-devils':
            city = 'NJ'
        elif i['stats']['competitor-seo-identifier'] == 'san-jose-sharks':
            city = 'SJS'
        elif i['stats']['competitor-seo-identifier'] == 'florida-panthers':
            city = 'FLA'
        elif i['stats']['competitor-seo-identifier'] == 'columbus-blue-jackets':
            city = 'CBJ'
        elif i['stats']['competitor-seo-identifier'] == 'nashville-predators':
            city = 'NSH'
        else:
            city = i['stats']['competitor-seo-identifier']


        best_scorers = [i['stats']['name'], int(i['stats']['goals']), position_player, city[0:3].upper()]
        goal_scorers.append(best_scorers)

        highest_pointscorers = [i['stats']['name'], int(i['stats']['points']), position_player, city[0:3].upper()]
        point_scorers.append(highest_pointscorers)

        highest_assisters = [i['stats']['name'], int(i['stats']['assists']), position_player, city[0:3].upper()]
        assist_scorers.append(highest_assisters)

        hardest_hitters = [i['stats']['name'], int(i['stats']['hits']), position_player, city[0:3].upper()]
        biggest_hitters.append(hardest_hitters)

        most_shorthandedgoals = [i['stats']['name'], int(i['stats']['shortHandedGoals']), position_player, city[0:3].upper()]
        shorthanded_scorers.append(most_shorthandedgoals)

        most_shots_blocked = [i['stats']['name'], int(i['stats']['blockedShots']), position_player, city[0:3].upper()]
        shot_blockers.append(most_shots_blocked)

        pp_goals = [i['stats']['name'], int(i['stats']['ppGoals']), position_player, city[0:3].upper()]
        pp_goal_scorers.append(pp_goals)

        faceoff_wins = [i['stats']['name'], int(i['stats']['faceoffsWon']), position_player, city[0:3].upper()]
        faceoff_winners.append(faceoff_wins)

        plus_minus = [i['stats']['name'], int(i['stats']['plusMinus']), position_player, city[0:3].upper()]
        plus_minus_list.append(plus_minus)

        pen_mins = [i['stats']['name'], int(i['stats']['penaltyInMinutes']), position_player, city[0:3].upper()]
        penalty_minutes.append(pen_mins)

        game_win_goals = [i['stats']['name'], int(i['stats']['gameWinningGoals']), position_player, city[0:3].upper()]
        game_winning_goals.append(game_win_goals)


adding_players()

sorted_goalscorelist = sorted(goal_scorers, key=operator.itemgetter(1), reverse=True)
tuple_scorer = tuple(tuple(skater) for skater in sorted_goalscorelist[0:5])

sorted_pointscorelist = sorted(point_scorers, key=operator.itemgetter(1), reverse=True)
tuple_points = tuple(tuple(skater) for skater in sorted_pointscorelist[0:5])

sorted_assisterlist = sorted(assist_scorers, key=operator.itemgetter(1), reverse=True)
tuple_assists = tuple(tuple(skater) for skater in sorted_assisterlist[0:5])


sorted_hitters = sorted(biggest_hitters, key=operator.itemgetter(1), reverse=True)
tuple_hitters = tuple(tuple(skater) for skater in sorted_hitters[0:5])

sorted_SHG = sorted(shorthanded_scorers, key=operator.itemgetter(1), reverse=True)
tuple_shorthanded = tuple(tuple(skater) for skater in sorted_SHG[0:5])

sorted_shotblockers = sorted(shot_blockers, key=operator.itemgetter(1), reverse=True)
tuple_blocks = tuple(tuple(skater) for skater in sorted_shotblockers[0:5])

sorted_pp_goals = sorted(pp_goal_scorers, key=operator.itemgetter(1), reverse=True)
tuple_powerplay = tuple(tuple(skater) for skater in sorted_pp_goals[0:5])


sorted_faceoff_wins = sorted(faceoff_winners, key=operator.itemgetter(1), reverse=True)
tuple_faceoff = tuple(tuple(skater) for skater in sorted_faceoff_wins[0:5])

sorted_plus_minus = sorted(plus_minus_list, key=operator.itemgetter(1), reverse=True)
tuple_plus_minus = tuple(tuple(skater) for skater in sorted_plus_minus[0:5])

sorted_pen_mins = sorted(penalty_minutes, key=operator.itemgetter(1), reverse=True)
tuple_pen_mins = tuple(tuple(skater) for skater in sorted_pen_mins[0:5])

sorted_game_win_goals = sorted(game_winning_goals, key=operator.itemgetter(1), reverse=True)
tuple_game_win_goals = tuple(tuple(skater) for skater in sorted_game_win_goals[0:5])
