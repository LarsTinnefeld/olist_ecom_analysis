import pandas as pd
from pywaffle import Waffle
import matplotlib.pyplot as plt


class Olist_analysis():

    def __init__(self):

        print('Olist analysis class initialized')

    def convert_to_dt(dat, cols):
        '''
        Function takes in a dataframe name and date
        columns for conversion into datetime format

        Input:
        - Dataframe

        Output:
        - None (Converts the format of the column into datetime)

        '''
        for col in cols:
            dat[col] = pd.to_datetime(dat[col]).dt.date

    def plot_waffle_chart(dat, metric, agg, title_txt, group='sub_segment'):
        '''
        Funtion to create a waffle chart. The visualization shows how the
        customer sub-segments are distributed according defined metrics.

        Input:
        - dat - dataframe
        - metric - feature/ kpi metric to visualize
        - agg - method to aggregate
        - title_txt - text to display as chart title

        Outout:
        - waffle chart

        '''
        data_revenue = dict(round(
            dat.groupby(group).agg({metric: agg}))[metric])

        plt.figure(
            FigureClass=Waffle,
            rows=5,
            columns=10,
            values=data_revenue,
            labels=[f"{k, v}" for k, v in data_revenue.items()],
            legend={'loc': 'lower left', 'bbox_to_anchor': (1, 0)},
            figsize=(8, 5)
            )

        plt.title(title_txt)
