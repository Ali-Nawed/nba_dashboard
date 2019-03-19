from player_data import *
from bokeh.io import show
from data_visuals import *
player = Player(201939)
wdata = wedge_data(player.stats)
plot = pct_plot(wdata, 'FT_PCT')
show(plot)