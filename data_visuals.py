from bokeh.plotting import figure
from bokeh.models import LinearAxis, Grid
from bokeh.models.glyphs import VBar
from bokeh.io import show
from player_data import *
import numpy as np





def make_hist(data, title):


    bin = np.arange(np.floor(data.min()), np.ceil(data.max())).shape[0]
    hist, bins = np.histogram(data, bins=bin)

    width = (bins[-1] -  bins[0])/bin

    plot = figure(plot_width=400, plot_height=250, title=title, tools='',
            toolbar_location=None,h_symmetry=False, v_symmetry=False)

    plot.vbar(x=bins[1:], 
            top=hist, 
            width=width, 
            bottom=0, 
            line_color='white',
            fill_color='navy',
            fill_alpha=0.6)
    return plot


def wedge_data(data):

        return data[['AST','TOV', 'FT_PCT', 'FG_PCT', 'FG3_PCT']].mean()


def ratio_plot(data, title):

        pass

def pct_plot(data):

        pass