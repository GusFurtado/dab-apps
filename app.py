import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_extensions.enrich import DashProxy
from dash_extensions.multipage import PageCollection, app_to_page, CONTENT_ID, URL_ID
import plotly.io as pio

from apps import ibge_app
from apps import ipea_app
from apps import camara_app

import config



pio.templates.default = "plotly_white"



pc = PageCollection(pages=[
    app_to_page(ibge_app.app, "ibge", "Mapa de Indicadores"),
    app_to_page(ipea_app.app, "ipea", "Indicadores Econômicos"),
    app_to_page(camara_app.app, "camara", "Painel de Deputados")
],
    default_page_id = 'ibge'
)



navbar = dbc.Row([
    dbc.Col(
        html.A(
            html.Img(
                src = config.LOGO,
                height = 48
            ),
            href='http://gustavofurtado.com/dab.html'
        ),
        width = 'auto'
    ),
    dbc.Col(
        dbc.Row([
            dbc.Col(
                html.A(
                    children = page.label,
                    href = f'/{page.id}',
                    style = {'color': 'white'}
                ),
                width = 'auto'
            ) for page in pc.pages
        ]),
        width = 'auto',
        align = 'center'
    )
],
    justify = 'between',
    style = {
        'background-color': '#002776',
        'margin': 0,
        'padding': 5
    }
)



app = DashProxy(
    name = __name__,
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        config.MONTSERRAT
    ],
    suppress_callback_exceptions = True
)

stuff = [html.Div(id=CONTENT_ID), dcc.Location(id=URL_ID)]
app.layout = html.Div([navbar] + stuff)
app.title = config.TITLE



pc.navigation(app)
pc.callbacks(app)



if __name__ == '__main__':
    app.run_server(
        host = '0.0.0.0',
        port = config.PORT
    )