import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from utils import utils, lists



inputs1 = dbc.Row([
    dbc.Col(
        dcc.Dropdown(
            id = 'uf_dropdown',
            placeholder = 'Selecione uma UF...',
            options = [{
                'label': lists.UFS[uf]['Nome'],
                'value': uf
            } for uf in lists.UFS]
        ),
        width = 8,
        style = {'padding': 2}
    ),
    dbc.Col(
        dbc.Input(
            id = 'ano_input',
            type = 'number',
            value = 2021,
            max = 2022,
            min = 2019,
            size = 'sm'
        ),
        width = 4,
        style = {'padding': 2}
    )
],
    no_gutters = True
)



inputs2 = dcc.Dropdown(
    id = 'dep_dropdown',
    placeholder = 'Selecione um deputado...',
    clearable = False,
    style = {'padding': 2}
)



main_info = dbc.Row([
    dbc.Col(
        html.Img(
            id = 'dep_foto',
            className = 'shadow'
        ),
        width = 'auto'
    ),
    dbc.Col([
        html.Div(
            id = 'dep_nome',
            className = 'title'
        ),

        # Email
        html.Div([
            html.Div('Email', className='dep_atributo_title'),
            html.Div(id='dep_email')
        ],
            className = 'dep_atributo'
        ),

        # Telefone
        html.Div([
            html.Div('Telefone', className='dep_atributo_title'),
            html.Div(id='dep_telefone'),
        ],
            className = 'dep_atributo'
        ),

        # Nascimento
        html.Div([
            html.Div('Nascimento', className='dep_atributo_title'),
            html.Div(id='dep_nascimento')
        ],
            className = 'dep_atributo'
        )

    ],
        width = 'auto'
    )
])



estado = dbc.Row([
    dbc.Col(
        html.Img(
            id = 'uf_bandeira',
            className = 'shadow',
            style = {'height': 50}
        ),
        width = 'auto'
    ),
    dbc.Col(
        html.Div([
            html.Div('Unidade Federativa', className='dep_atributo_title'),
            html.Div(id='dep_uf'),
        ],
            className = 'dep_atributo'
        )
    )
],
    style = {'padding': 10}
)



partido = dbc.Row([
    dbc.Col(
        html.Img(
            id = 'partido_logo',
            style = {'height': 50}
        ),
        width = 'auto'
    ),
    dbc.Col(
        html.Div([
            html.Div('Partido', className='dep_atributo_title'),
            html.Div(id='dep_partido'),
        ],
            className = 'dep_atributo'
        )
    )
],
    style = {'padding': 10}
)



column1 = dbc.Col(
    html.Div([
        inputs1,
        inputs2,
        html.Hr(),
        dcc.Loading(main_info),
        html.Hr(),
        estado,
        partido
    ],
        className = 'coluna shadow'
    ),
    width = 12,
    lg = 5
)



column2 = dbc.Col(
    html.Div(
        dcc.Loading([
            html.Div(
                'Despesas',
                className = 'title',
                style = {'text-align': 'center'}
            ),
            html.Div(
                dcc.Graph(
                    id = 'plots',
                    config = {'displayModeBar': False}
                )
            )
        ]),
        className = 'coluna shadow'
    ),
    width = 12,
    lg = 7
)



layout = dbc.Container([
    dbc.Row([
        column1,
        column2
    ])
],
    fluid = True
)