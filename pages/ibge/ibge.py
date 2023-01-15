import DadosAbertosBrasil as dab

import os

from dash import Input, Output, callback, register_page
import pandas as pd
import plotly.express as px

from .ibge_layout import IbgeLayout
from utils import lists


register_page(
    __name__,
    path="/ibge",
    title="Indicadores Municipais",
)


layout = IbgeLayout()
TOKEN = os.environ.get("TOKEN")
if TOKEN is None:
    t1 = "pk.eyJ1IjoiZ3VzdGF2b2Z1cnRhZG8iLC"
    t2 = "JhIjoiY2s2NmlsYjkwMDFsaTNtbzhjdmZ"
    t3 = "seG0ybCJ9.eMOZ1ywNoc7ui4uqcsJk8A"
    TOKEN = t1 + t2 + t3


@callback(
    Output("map", "figure"),
    Input("dd_uf", "value"),
    Input("dd_kpi", "value"),
    Input("dd_cor", "value"),
)
def update_map(uf, kpi, color):

    geojson = dab.geojson(uf)
    df = pd.read_parquet("data/ibge_data.parquet", columns=["Código", "Município", kpi])

    fig = px.choropleth_mapbox(
        data_frame=df,
        geojson=geojson,
        featureidkey="properties.id",
        locations="Código",
        color=kpi,
        mapbox_style="open-street-map",
        color_continuous_scale=color,
        opacity=0.5,
        hover_name="Município",
        hover_data={"Código": False, kpi: True},
    )

    fig.update_layout(
        {
            "coloraxis": {"colorbar": {"title": {"text": "Escala"}}},
            "mapbox": {
                "accesstoken": TOKEN,
                "bearing": 0,
                "pitch": 0,
                "zoom": 5.5,
                "center": {
                    "lat": lists.UFS[uf]["Latitude"],
                    "lon": lists.UFS[uf]["Longitude"],
                },
            },
            "hovermode": "closest",
            "margin": {"r": 0, "t": 0, "l": 0, "b": 0},
        }
    )

    return fig
