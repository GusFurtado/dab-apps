from dash import dcc, html
import dash_bootstrap_components as dbc



class IpeaLayout(dbc.Container):

    INDICADORES = [
        {'value': 'PAN_PIBPMG' , 'label': 'PIB Real'},
        {'value': 'PAN_TDESOC' , 'label': 'Desocupação'},
        {'value': 'PAN_IPCAG'  , 'label': 'IPCA'},
        {'value': 'PAN_TJOVER' , 'label': 'Over/Selic'},
        {'value': 'PAN_ERV'    , 'label': 'Dólar'},
        {'value': 'PAN_SBC'    , 'label': 'Balança Comercial'},
        {'value': 'PAN_DEXT'   , 'label': 'Dívida externa'}
    ]
    
    def __init__(self):
        super().__init__(
            fluid = True,
            children = dbc.Row([
                dbc.Col(
                    html.Div(
                        dbc.Form(self.radio),
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
            ])
        )

    @property
    def radio(self) -> html.Div:
        return html.Div([
            dbc.Label(
                'Indicador',
                className = 'mt-2 mb-1 bold_label',
                html_for = 'kpi_radio'
            ),
            dbc.RadioItems(
                options = self.INDICADORES,
                value = 'PAN_PIBPMG',
                id = 'kpi_radio'
            )
        ])
