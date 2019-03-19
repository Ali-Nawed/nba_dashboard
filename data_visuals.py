from bokeh.plotting import figure
from bokeh.models import LinearAxis, Grid
from bokeh.models.glyphs import VBar
from bokeh.io import show
from player_data import *
import numpy as np
import pandas as pd


DATA_STAT_TITLE = {

        'FT_PCT': 'Freethrow Percentage ',
        'FG_PCT': 'Field Goal Percentage',
        'FG3_PCT': '3-Point Percentage'
}

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
    plot.outline_line_color = None
    plot.xgrid.visible = False    
    return plot


def wedge_data(data):

        return data[['FT_PCT', 'FG_PCT', 'FG3_PCT']].mean()


def pct_plot(data, stat_name):


        data_stat = {

                stat_name: data[stat_name],
                stat_name+'_not': 1 - data[stat_name]
        }

        angle = [data_stat[stat_name]*2*np.pi, 2*np.pi]

        colors = ['navy', 'red']

        plot = figure(plot_height=250, plot_width=250,
        title = DATA_STAT_TITLE[stat_name],
        toolbar_location=None,
        tools='')

        plot.annular_wedge(x=1, y=1, inner_radius=0.4, outer_radius=0.8,
                           start_angle=np.pi/2, end_angle=angle[0] + np.pi/2,
                           line_color="white", fill_color=colors[0],
                           fill_alpha=0.8)

        plot.annular_wedge(x=1, y=1, inner_radius=0.4, outer_radius=.8,
                           start_angle=angle[0] + np.pi/2, end_angle=angle[1] + np.pi/2,
                           line_color="white", fill_color=colors[1],
                           fill_alpha=0.8)

        plot.text(x=1, y=1, text=['{:.2f}'.format(data_stat[stat_name])],
                  text_font_size='30pt',
                  x_offset=-40,
                  y_offset=25)

        plot.axis.axis_label=None
        plot.axis.visible=False
        plot.grid.grid_line_color = None
        plot.outline_line_color = None

        return plot
        

        