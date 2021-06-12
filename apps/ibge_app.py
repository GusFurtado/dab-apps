from DadosAbertosBrasil import favoritos

import os

import dash
from dash_extensions.enrich import DashProxy
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL
import plotly.express as px

import pandas as pd

import layouts.ibge_layout as layout
import utils.ibge_utils as utils



TOKEN = os.environ.get('TOKEN')
if TOKEN is None:
    from data import mapbox_token
    TOKEN = mapbox_token.TOKEN



app = DashProxy(
    name = __name__,
    external_stylesheets = [dbc.themes.SANDSTONE]
)

app.layout = layout.layout
server = app.server



@app.callback(
    [Output('button_uf', 'label'),
    Output('button_kpi', 'label'),
    Output('button_color', 'label'),
    Output('chart_info', 'data')],
    [Input({'uf': ALL}, 'n_clicks'),
    Input({'kpi': ALL}, 'n_clicks'),
    Input({'colorscale': ALL}, 'n_clicks')],
    [State('chart_info', 'data')],
    prevent_initial_call = True)
def update_data(uf, kpi, color, data):
    cc = dash.callback_context.triggered[0]['prop_id'].split('"')
    data[cc[1]] = cc[3]
    return (
        data['uf'],
        data['kpi'],
        data['colorscale'],
        data
    )



@app.callback(
    Output('map', 'figure'),
    [Input('chart_info', 'data')])
def update_map(data):

    geojson = favoritos.geojson(data['uf'])
    df = pd.read_parquet(
        'data/ibge_data.parquet',
        columns = ['Código', 'Município', data['kpi']]
    )

    fig = px.choropleth_mapbox(
        data_frame = df,
        geojson = geojson,
        featureidkey = 'properties.id',
        locations= 'Código',
        color = data['kpi'],
        mapbox_style = 'open-street-map',
        color_continuous_scale = data['colorscale'],
        opacity = 0.5,
        hover_name = 'Município',
        hover_data = {'Código': False, data['kpi']: True}
    )

    fig.update_layout({
        'mapbox': {
            'accesstoken': TOKEN,
            'bearing': 0,
            'pitch': 0,
            'zoom': 5.5,
            'center': {
                'lat': utils.UFS[data['uf']]['Latitude'],
                'lon': utils.UFS[data['uf']]['Longitude']
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



if __name__ == '__main__':
    app.run_server(
        host = '0.0.0.0',
        port = '1010',
        debug = False
    )