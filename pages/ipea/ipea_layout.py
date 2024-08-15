from dash import dcc, html
import dash_bootstrap_components as dbc


class IpeaLayout(dbc.Container):
    INDICADORES = [
        {"value": "PAN4_PIBPMG4", "label": "PIB Real"},
        {"value": "PAN_PIBCAP", "label": "PIB per Capita"},
        {"value": "PAN4_PIBPMV4", "label": "PIB Nominal"},
        {"value": "PAN4_FBKFI90G4", "label": "Investimento Real"},
        {"value": "PAN4_FBKFPIBV4", "label": "Taxa de Investimento Nominal"},
        {"value": "PAN12_QIIGG12", "label": "Produção Industrial"},
        {"value": "PAN12_IVVRG12", "label": "Valor Real das Vendas no Varejo"},
        {"value": "PNADC12_PO12", "label": "Pessoas Ocupadas"},
        {"value": "PNADC12_TDESOC12", "label": "Taxa de Desocupação"},
        {"value": "PNADC12_RRPE12", "label": "Rendimento Médio"},
        {"value": "PAN12_IGPDIG12", "label": "IGP-DI"},
        {"value": "PAN12_IPCAG12", "label": "IPCA"},
        {"value": "PAN12_TJOVER12", "label": "Taxa de Juros SELIC"},
        {"value": "PAN12_ERV12", "label": "Taxa de Câmbio Nominal"},
        {"value": "PAN12_SBC12", "label": "Balança Comercial"},
        {"value": "PAN12_XTV12", "label": "Exportações"},
        {"value": "PAN12_MTV12", "label": "Importações"},
        {"value": "PAN12_STC12", "label": "Saldo em Transações Correntes"},
        {"value": "PAN_DEXT", "label": "Dívida Externa Total"},
        {"value": "PAN12_DTSPY12", "label": "Dívida Pública Total"},
    ]

    def __init__(self):
        super().__init__(
            fluid=True,
            children=dbc.Row(
                [
                    dbc.Col(
                        html.Div(dbc.Form(self.radio), className="coluna shadow"),
                        width=12,
                        md=3,
                    ),
                    dbc.Col(
                        html.Div(
                            dcc.Loading(dcc.Graph(id="main_graph")),
                            className="coluna shadow",
                        ),
                        width=12,
                        md=9,
                    ),
                ]
            ),
        )

    @property
    def radio(self) -> html.Div:
        return html.Div(
            [
                dbc.Label(
                    "Indicador",
                    className="mt-2 mb-1 bold_label",
                    html_for="kpi_radio",
                ),
                dbc.RadioItems(
                    options=self.INDICADORES,
                    value="PAN4_PIBPMG4",
                    id="kpi_radio",
                ),
            ]
        )
