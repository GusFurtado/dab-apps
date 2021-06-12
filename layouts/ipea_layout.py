import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc



INDICADORES = [
    {'label': 'PIB Real',           'value': 'PAN_PIBPMG'},
    {'label': 'Desocupação',        'value': 'PAN_TDESOC'},
    {'label': 'IPCA',               'value': 'PAN_IPCAG'},
    {'label': 'Over/Selic',         'value': 'PAN_TJOVER'},
    {'label': 'Dólar',              'value': 'PAN_ERV'},
    {'label': 'Balança Comercial',  'value': 'PAN_SBC'},
    {'label': 'Dívida externa',     'value': 'PAN_DEXT'}
]



radio = dbc.FormGroup([
    dbc.Label(
        html.B(
            'Indicador',
            className = 'mt-2 mb-1'
        ),
        html_for = 'kpi_radio'
    ),
    dbc.RadioItems(
        options = INDICADORES,
        value = 'PAN_PIBPMG',
        id = 'kpi_radio'
    )
])



LOGO = 'https://raw.githubusercontent.com/GusFurtado/DadosAbertosBrasil/master/assets/logo.png'



layout = dbc.Container(
    dbc.Row([
        dbc.Col(
            html.Div([
                html.A(
                    html.Img(
                        src = LOGO,
                        style = {'maxWidth': '100%'},
                        className = 'mt-1 mb-1'
                    ),
                    href = 'https://www.gustavofurtado.com/dab.html'
                ),
                dbc.Form(radio)
            ],
                className = 'coluna shadow'
            ),
            width = 12,
            md = 3
        ),
        dbc.Col(
            html.Div(
                dcc.Loading(
                    dcc.Graph(
                        id = 'main_graph'
                    )
                ),
                className = 'coluna shadow'
            ),
            width = 12,
            md = 9
        )
    ]),
    fluid = True
)