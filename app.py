from flask import Flask, render_template
from skaterstats import tuple_scorer, tuple_points, tuple_powerplay, tuple_assists, tuple_blocks, tuple_hitters, tuple_shorthanded, \
    tuple_faceoff, tuple_pen_mins, tuple_plus_minus, tuple_game_win_goals
from goaliestats import tuple_GAA, tuple_wins, tuple_saves, tuple_shutouts, tuple_save_percent
from teamregions import tuple_teams_atl, tuple_teams_metro, tuple_teams_central, tuple_teams_pacific


app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def stats_nhlers():  # put application's code here


    return render_template("players.html", tuple_faceoff=tuple_faceoff, tuple_powerplay=tuple_powerplay, tuple_blocks=tuple_blocks, tuple_shorthanded=tuple_shorthanded,
                           tuple_hitters=tuple_hitters, tuple_assists=tuple_assists, tuple_points=tuple_points, tuple_scorer=tuple_scorer, tuple_pen_mins=tuple_pen_mins
                           ,tuple_plus_minus=tuple_plus_minus, tuple_game_win_goals=tuple_game_win_goals, tuple_saves=tuple_saves, tuple_GAA=tuple_GAA,
                           tuple_wins=tuple_wins, tuple_shutouts=tuple_shutouts, tuple_save_percent=tuple_save_percent, tuple_teams_atl=tuple_teams_atl,
                            tuple_teams_metro=tuple_teams_metro,tuple_teams_central=tuple_teams_central, tuple_teams_pacific=tuple_teams_pacific)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
