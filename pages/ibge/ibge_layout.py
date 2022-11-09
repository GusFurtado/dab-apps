from dash import dcc, html
import dash_bootstrap_components as dbc

from utils import lists



class IbgeLayout(dbc.Container):

    def __init__(self):
        super().__init__(
            fluid = True,
            children = dbc.Row([
                dbc.Col(
                    self.column1,
                    width = 12,
                    lg = 4
                ),
                dbc.Col(
                    self.column2,
                    width = 12,
                    lg = 8
                )
            ])
        )

    @property
    def dd_uf(self):
        return html.Div([
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

    @property
    def dd_cor(self):
        return html.Div([
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

    @property
    def dd_kpi(self):
        return html.Div([
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

    @property
    def column1(self):
        return html.Div([
            self.dd_uf,
            html.Hr(),
            self.dd_kpi,
            html.Hr(),
            self.dd_cor
        ],
            className = 'coluna shadow'
        )

    @property
    def column2(self):
        return html.Div(
            dcc.Loading(
                dcc.Graph(id='map')
            ),
            className = 'coluna shadow'
        )
