import pandas as pd
from pywaffle import Waffle
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.offline import iplot


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

    def plot_map(
                df,
                title,
                lower_bound,
                upper_bound,
                metric,
                maker_size=3,
                sub_segment_y_n=False
                ):
        '''
        Funtion for geographic data visualization of demographic metrics.

        Input:
        - df - dataframe with target feature
            (metric; color-code field needed if sub_segment to visualize
        - title - text to display as chart title
        - lower_bound - lower threshold for color scale
        - upper_bound - upper threshold for color scale
        - metric - feature/ kpi metric to visualize
        - sub_sement_y_n - boolean,
            if "True": sub-segment will be visualized with color-code,
            if no, color acording value
        - marker_size - size of the marker

        Outout:
        - geographic data visualization

        '''

        if sub_segment_y_n is True:
            dict_marker = dict(
                size=maker_size,
                color=df.color,
                )
        else:
            dict_marker = dict(
                size=maker_size,
                color=df[metric],
                showscale=True,
                colorscale=[[0, 'blue'],
                            [1, 'red']],
                cmin=lower_bound,
                cmax=upper_bound
                )

        data_geo = [go.Scattermapbox(
            lon=df['geolocation_lng'],
            lat=df['geolocation_lat'],
            marker=dict_marker
            )]

        layout = dict(
                title=title,
                showlegend=False,
                mapbox=dict(
                    accesstoken='pk.eyJ1IjoiaG9vbmtlbmc5MyIsImEiOiJjam43cGhpNng2ZmpxM3JxY3Z4ODl2NWo3In0.SGRvJlToMtgRxw9ZWzPFrA',
                    center=dict(lat=-23.5, lon=-46.6),
                    bearing=10,
                    pitch=0,
                    zoom=2,
                )
            )
        fig = dict(data=data_geo, layout=layout)
        iplot(fig, validate=False)
