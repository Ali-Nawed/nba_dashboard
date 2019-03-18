from player_data import *
from data_visuals import *
import requests
from flask import Flask, render_template, request, jsonify
from bokeh.embed import components


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():

    player_id = 202695
    player_data = Player(player_id)
    hist_params = create_hist_params(player_data.stats)
    
    player_info = get_player_info(player_data.info)

    return render_template('template.html', params=hist_params, player_info=player_info)


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
