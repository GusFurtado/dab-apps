import DadosAbertosBrasil as dab

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import utils.ibge_utils as utils



dd_uf = dbc.DropdownMenu([
    dbc.DropdownMenuItem([
        html.Span(
            html.Img(src=dab.bandeira(uf, 20)),
            className = 'mr-2'
        ),
        html.Span(utils.UFS[uf]['Nome'])
    ],
        id = {'uf': uf}
    ) for uf in utils.UFS
],
    direction = 'left',
    nav = True,
    in_navbar = True,
    label = 'UF',
    id = 'button_uf'
)



dd_kpi = dbc.DropdownMenu([
    dbc.DropdownMenuItem(
        kpi,
        id = {'kpi': kpi}
    ) for kpi in utils.KPIS
],
    direction = 'left',
    nav = True,
    in_navbar = True,
    label = 'Indicador',
    id = 'button_kpi'
)



dd_cor = dbc.DropdownMenu([
    dbc.DropdownMenuItem(
        color,
        id = {'colorscale': color}
    ) for color in utils.COLORS
],
    direction = 'left',
    nav = True,
    in_navbar = True,
    label = 'Paleta de Cores',
    id = 'button_color'
)



navbar = dbc.NavbarSimple([
        dd_uf,
        dd_kpi,
        dd_cor,
    ],
    brand = 'Dados Abertos Brasil',
    brand_style = {
        'font-weight': 'bold',
        'color': '#FEDF00'
    },
    brand_href = "https://www.gustavofurtado.com/dab.html",
    color = "primary",
    dark = True,
)



layout = html.Div([
    dcc.Store(
        id = 'chart_info',
        data = {
            'uf': 'AC',
            'colorscale': 'plasma',
            'kpi': 'Taxa de Alfabetização'
        }
    ),
    navbar,
    dcc.Loading(
        dcc.Graph(id='map')
    )
],
    id = 'background'
)
