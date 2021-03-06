from player_data import *
from data_visuals import *
import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for
from bokeh.embed import components


app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    season_id = request.args.get("SeasonId")
    player_id = request.args.get("PlayerId")
    print(request.args)
    print(season_id)
    print(player_id)

    if not player_id or not season_id:
        player_id = '201939'
        season_id = '2018-19'

    else:
        print(player_id.split('\t'))
        player_id = player_id.split('\t')[1]

    print(player_id)


    season = Season(season_id)
    player_data = Player(int(player_id))
    hist_params = create_hist_params(player_data.stats)
    percent_data = wedge_data(player_data.stats)
    wedge_params = create_wedge_params(percent_data)
    player_info = get_player_info(player_data.info)

    player_name = list(season.players['PLAYER_NAME'])
    player_id = list(season.players['PLAYER_ID'])
    player_list = {'players':['{}\t{}'.format(player_name[i],player_id[i]) for i in range(len(player_id))]}
    return render_template('template.html', 
                           params=hist_params, 
                           player_info=player_info,
                           wedge_params=wedge_params,
                           player_list=player_list)


def create_hist_params(data):

    params = {}
    header_list = [('PTS', 'Points PerGame'),
                   ('REB', 'Rebounds PerGame'),
                   ('AST', 'Assists PerGame'),
                   ('STL', 'Steals PerGame'),
                   ('BLK', 'Blocks PerGame')]

    def _make_components(header_tuple):

        data_value = header_tuple[0]
        plot = make_hist(data[data_value], header_tuple[1])

        script_param = '{}_script'.format(data_value)
        div_param = '{}_div'.format(data_value)

        return components(plot), script_param, div_param

    for i in header_list:
        ([script_component,
         div_component],
         script_param,
         div_param) = _make_components(i)

        params[script_param] = script_component
        params[div_param] = div_component

    return params

def create_wedge_params(percent_data):
    params = {}

    for stat in percent_data.index:
        plot = pct_plot(percent_data, stat)

        script, div = components(plot)

        params['{}_script'.format(stat)] = script
        params['{}_div'.format(stat)] = div

    return params



def get_player_info(info):

    info_dict = {}

    data_columns = ['DISPLAY_FIRST_LAST',
                    'COUNTRY',
                    'JERSEY',
                    'HEIGHT',
                    'WEIGHT',
                    'TEAM_NAME',
                    'TEAM_ID',
                    'DRAFT_ROUND',
                    'DRAFT_YEAR',
                    'DRAFT_NUMBER',
                    'BIRTHDATE',
                    'SCHOOL',
                    'POSITION']
    info_dict = {i:str(info[i][0]) for i in data_columns}

    return info_dict
if __name__ == '__main__':

    app.run()
