import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from utils import lists



dd_uf = dbc.FormGroup([
    dbc.Label(
        'Unidade da Federação',
        html_for = 'dd_uf',
        className = 'bold_label'
    ),
    dcc.Dropdown(
        id = 'dd_uf',
        value = 'AC',
        clearable = False,
        options = [
            {'label': lists.UFS[uf]['Nome'], 'value': uf} for uf in lists.UFS
        ]
    )
])

dd_cor = dbc.FormGroup([
    dbc.Label(
        'Escala de Cores',
        html_for = 'dd_cor',
        className = 'bold_label'
    ),
        dcc.Dropdown(
        id = 'dd_cor',
        value = 'plasma',
        clearable = False,
        options = [
            {'label': color, 'value': color} for color in lists.COLORS
        ]
    )
])

dd_kpi = dbc.FormGroup([
    dbc.Label(
        'Indicador',
        html_for = 'dd_kpi',
        className = 'bold_label'
    ),
        dcc.Dropdown(
        id = 'dd_kpi',
        value = 'Taxa de Alfabetização',
        clearable = False,
        options = [
            {'label': kpi, 'value': kpi} for kpi in lists.KPIS
        ]
    )
])



column1 = html.Div([
    dd_uf,
    html.Hr(),
    dd_kpi,
    html.Hr(),
    dd_cor
],
    className = 'coluna shadow'
)

column2 = html.Div(
    dcc.Loading(
        dcc.Graph(id='map')
    ),
    className = 'coluna shadow'
)



layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            column1,
            width = 4
        ),
        dbc.Col(
            column2,
            width = 8
        )
    ])
],
    fluid = True
)
