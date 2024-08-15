from dash import dcc, html
import dash_bootstrap_components as dbc

from utils import lists


class CamaraLayout(dbc.Container):
    def __init__(self):
        super().__init__(fluid=True, children=dbc.Row([self.column1, self.column2]))

    @property
    def inputs1(self) -> dbc.Row:
        return dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="uf_dropdown",
                        placeholder="Selecione uma UF...",
                        options=[
                            {"label": lists.UFS[uf]["Nome"], "value": uf}
                            for uf in lists.UFS
                        ],
                    ),
                    width=8,
                    style={"padding": 2},
                ),
                dbc.Col(
                    dbc.Input(
                        id="ano_input",
                        type="number",
                        value=2024,
                        max=2024,
                        min=2023,
                        size="sm",
                    ),
                    width=4,
                    style={"padding": 2},
                ),
            ],
            class_name="g-0",
        )

    @property
    def inputs2(self) -> dcc.Dropdown:
        return dcc.Dropdown(
            id="dep_dropdown",
            placeholder="Selecione um deputado...",
            clearable=False,
            style={"padding": 2},
        )

    @property
    def main_info(self) -> dbc.Row:
        return dbc.Row(
            [
                dbc.Col(html.Img(id="dep_foto", className="shadow"), width="auto"),
                dbc.Col(
                    [
                        html.Div(id="dep_nome", className="title"),
                        # Email
                        html.Div(
                            [
                                html.Div("Email", className="dep_atributo_title"),
                                html.Div(id="dep_email"),
                            ],
                            className="dep_atributo",
                        ),
                        # Telefone
                        html.Div(
                            [
                                html.Div("Telefone", className="dep_atributo_title"),
                                html.Div(id="dep_telefone"),
                            ],
                            className="dep_atributo",
                        ),
                        # Nascimento
                        html.Div(
                            [
                                html.Div("Nascimento", className="dep_atributo_title"),
                                html.Div(id="dep_nascimento"),
                            ],
                            className="dep_atributo",
                        ),
                    ],
                    width="auto",
                ),
            ]
        )

    @property
    def estado(self) -> dbc.Row:
        return dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        id="uf_bandeira", className="shadow", style={"height": 50}
                    ),
                    width="auto",
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.Div(
                                "Unidade Federativa", className="dep_atributo_title"
                            ),
                            html.Div(id="dep_uf"),
                        ],
                        className="dep_atributo",
                    )
                ),
            ],
            style={"padding": 10},
        )

    @property
    def partido(self) -> dbc.Row:
        return dbc.Row(
            [
                dbc.Col(
                    html.Img(id="partido_logo", style={"height": 50}), width="auto"
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.Div("Partido", className="dep_atributo_title"),
                            html.Div(id="dep_partido"),
                        ],
                        className="dep_atributo",
                    )
                ),
            ],
            style={"padding": 10},
        )

    @property
    def column1(self) -> dbc.Col:
        return dbc.Col(
            html.Div(
                [
                    self.inputs1,
                    self.inputs2,
                    html.Hr(),
                    dcc.Loading(self.main_info),
                    html.Hr(),
                    self.estado,
                    self.partido,
                ],
                className="coluna shadow",
            ),
            width=12,
            lg=5,
        )

    @property
    def column2(self) -> dbc.Col:
        return dbc.Col(
            html.Div(
                dcc.Loading(
                    [
                        html.Div(
                            "Despesas",
                            className="title",
                            style={"text-align": "center"},
                        ),
                        html.Div(
                            dcc.Graph(id="plots", config={"displayModeBar": False})
                        ),
                    ]
                ),
                className="coluna shadow",
            ),
            width=12,
            lg=7,
        )
