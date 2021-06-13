import DadosAbertosBrasil as dab

import os

from dash_extensions.enrich import DashProxy
from dash.dependencies import Input, Output, ALL
import plotly.express as px

import pandas as pd

import layouts.ibge_layout as layout
from utils import lists



TOKEN = os.environ.get('TOKEN')
if TOKEN is None:
    import mapbox_token
    TOKEN = mapbox_token.TOKEN



app = DashProxy(name=__name__)
app.layout = layout.layout



@app.callback(
    Output('map', 'figure'),
    Input('dd_uf', 'value'),
    Input('dd_kpi', 'value'),
    Input('dd_cor', 'value'))
def update_map(uf, kpi, color):

    geojson = dab.geojson(uf)
    df = pd.read_parquet(
        'data/ibge_data.parquet',
        columns = ['Código', 'Município', kpi]
    )

    fig = px.choropleth_mapbox(
        data_frame = df,
        geojson = geojson,
        featureidkey = 'properties.id',
        locations= 'Código',
        color = kpi,
        mapbox_style = 'open-street-map',
        color_continuous_scale = color,
        opacity = 0.5,
        hover_name = 'Município',
        hover_data = {'Código': False, kpi: True}
    )

    fig.update_layout({
        'coloraxis': {
            'colorbar': {
                'title': {
                    'text': 'Escala'
                }
            }
        },
        'mapbox': {
            'accesstoken': TOKEN,
            'bearing': 0,
            'pitch': 0,
            'zoom': 5.5,
            'center': {
                'lat': lists.UFS[uf]['Latitude'],
                'lon': lists.UFS[uf]['Longitude']
            }
        },
        'hovermode': 'closest',
        'margin': {
            'r': 0,
            't': 0,
            'l': 0,
            'b': 0
        }
    })

    return fig