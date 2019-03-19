import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

HEADERS = {
    "User-Agent": "M",
}


params = {

    'PlayerId': '201939',
    'LeagueID': '00',
    'Season': '2018-19',
    'SeasonType': 'Regular Season',
    'IsOnlyCurrentSeason': '1',
    'PerMode': 'PerGame'

}

ROOT = 'http://stats.nba.com/stats/'


def url_to_dataframe(url, params):

    '''
    @param str url: stats nba api endpoint
    @param dict params: dict contating parameters to call api
    '''

    json_data = requests.get(url,
                             headers=HEADERS,
                             params=params).json()['resultSets'][0]

    data = pd.DataFrame(json_data['rowSet'], columns=json_data['headers'])

    return data


class Season():

    def __init__(self, year):

        self._ENDPOINT = 'leaguedashplayerbiostats?'
        self._URL = ROOT + self._ENDPOINT
        self.year = year
        self._season_params = params
        self._season_params['Season'] = year
        self.players = url_to_dataframe(self._URL, self._season_params)


class Player():

    def __init__(self, id):

        self.id = id

        self._COMMON_PLAYER_INFO = 'commonplayerinfo?'
        self._PLAYER_GAME_LOG = 'playergamelog?'
        self._PLAYER_STATS_URL = ROOT + self._PLAYER_GAME_LOG
        self._PLAYER_INFO_URL = ROOT + self._COMMON_PLAYER_INFO

        self._player_params = params
        self._player_params['PlayerId'] = self.id

        self.stats = url_to_dataframe(self._PLAYER_STATS_URL,
                                      self._player_params)
        self.info = url_to_dataframe(self._PLAYER_INFO_URL,
                                     self._player_params)

    def __str__(self):

        return '{}, {}'.format(self.info['DISPLAY_FIRST_LAST'], self.id)
