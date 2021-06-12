import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pandas import concat



UFS = {
    'AC': 'Acre',
    'AM': 'Amazonas',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espirito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MG': 'Minas Gerais',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'PR': 'Paraná',
    'RJ': 'Rio de Janeiro',
    'RO': 'Rondônia',
    'RN': 'Rio Grande do Norte',        
    'RR': 'Roraima',
    'RS': 'Rio Grande do Sul',
    'SC': 'Santa Catarina',
    'SE': 'Sergipe',
    'SP': 'São Paulo',
    'TO': 'Tocantins'
}



MESES = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}



class Charts:
    '''
    Objeto para importação de dados com métodos para geração de gráficos.

    Parameters
    ----------
    deputado : DadosAbertosBrasil.camara.Deputado
        Classe Deputado.
    ano : int
        Ano da análise.

    Attributes
    ----------
    ano : int
        Ano da análise.
    despesas : pandas.core.frame.DataFrame
        Tabela de despesas do deputado.
    total : str
        Valor total das despesas no formato 'R$ #.##0,00'.

    --------------------------------------------------------------------------
    '''

    def __init__(self, deputado, ano:int):

        self.ano = ano
        i = 0
        dfs = []
        b = True

        while b:
            i += 1
            df = deputado.despesas(itens=100, pagina=i, ano=ano)
            dfs.append(df)
            b = not df.empty

        try:
            self.despesas = concat(dfs, ignore_index=True)
            self.total = f'{self.despesas.valorDocumento.sum():,.2f}'

        except:
            raise Exception('NoData')


    def donut(self) -> go.Pie:
        '''
        Gera um gráfico de donut dos tipos de despesas.

        Returns
        -------
        plotly.graph_objects.Pie
            Gráfico de donut, onde cada fatia é um tipo de despesas e o valor
            no centro do gráfico é a soma total das despesas.

        ----------------------------------------------------------------------
        '''

        categorias = self.despesas[['tipoDespesa', 'valorDocumento']] \
            .groupby('tipoDespesa').sum()

        return go.Pie(
            labels = categorias.index,
            values = categorias.valorDocumento,
            hole = 0.7,
            marker = {
                'line': {
                    'color': 'white',
                    'width': 2
                }
            }
        )


    def timeline(self) -> go.Bar:
        '''
        Gera uma linha do tempo de despesas.

        Returns
        -------
        plotly.graph_objects.Bar
            Gráfico de barras, onde cada categoria do gráfico é um mês e os
            valores são as despesas dos meses respectivos.

        ----------------------------------------------------------------------
        '''

        meses = self.despesas[['mes', 'valorDocumento']] \
            .groupby('mes').sum()

        mes = meses.index.map(MESES)
        value_num = meses.valorDocumento
        value_text = value_num.apply(lambda x: f'{x:,.2f}')
        hover = [f'<b>Mês:</b> {i}<br><b>Valor:</b> {v}<extra></extra>' \
            for i, v in zip(mes, value_text)]

        return go.Bar(
            x = mes,
            y = value_num,
            cliponaxis = False,
            hovertemplate = hover,
            text = value_text,
            textposition = 'inside',
            marker_color = 'purple'
        )


    def fornecedores(self):
        forn = self.despesas[['nomeFornecedor', 'valorDocumento']] \
            .groupby('nomeFornecedor').sum() \
            .sort_values(by='valorDocumento', ascending=False)[:5]

        forns = forn.index[::-1]
        value_num = forn.valorDocumento[::-1]
        value_text = value_num.apply(lambda x: f'{x:,.2f}')
        hover = [f'<b>Fornecedor:</b> {i}<br><b>Valor:</b> {v}<extra></extra>' \
            for i, v in zip(forns, value_text)]

        return go.Bar(
            x = value_num,
            y = forns.str[:25],
            orientation = 'h',
            hovertemplate = hover,
            text = value_text,
            textposition = 'inside',
            marker_color = 'purple'
        )


    def plots(self) -> go.Figure:
        '''
        Figure contendo os gráficos de despesas.

        Returns
        -------
        plotly.graph_objs._figure.Figure
            Subplots com gráficos de despesas.

        ----------------------------------------------------------------------
        '''

        fig = make_subplots(
            rows = 2,
            cols = 2,
            horizontal_spacing = 0.3,
            vertical_spacing = 0.05,
            column_widths = [0.4, 0.6],
            row_heights = [0.6, 0.4],
            specs = [
                [{'type': 'domain'}, {}],
                [{'colspan': 2}, None]
            ]
        )

        fig.add_trace(
            self.donut(),
            row = 1,
            col = 1
        )

        fig.add_trace(
            self.timeline(),
            row = 2,
            col = 1
        )

        fig.add_trace(
            self.fornecedores(),
            row = 1,
            col = 2
        )

        fig.update_layout({
            'showlegend': False,
            'font': {'family': 'Montserrat'},
            'margin': {
                't': 10,
                'b': 0,
                'l': 10,
                'r': 10
            },
            'annotations': [{
                'text': f'<b>{self.total}</b>',
                'font': {
                    'size': 18,
                    'color': 'purple',
                },
                'xref': 'paper',
                'yref': 'paper',
                'x': 0.06,
                'y': 0.75,
                'showarrow': False
            }]
        })

        fig.update_yaxes(
            ticksuffix = '   ',
            row = 1,
            col = 2
        )

        return fig
