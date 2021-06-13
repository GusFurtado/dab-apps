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
        'Indicador',
        className = 'mt-2 mb-1 bold_label',
        html_for = 'kpi_radio'
    ),
    dbc.RadioItems(
        options = INDICADORES,
        value = 'PAN_PIBPMG',
        id = 'kpi_radio'
    )
])



layout = dbc.Container(
    dbc.Row([
        dbc.Col(
            html.Div(
                dbc.Form(radio),
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