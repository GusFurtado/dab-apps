from DadosAbertosBrasil import camara

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import pandas as pd

pio.templates.default = "plotly_white"



def bandeira(uf:str, tamanho:int=100) -> str:
    '''
    Gera a URL da WikiMedia para a bandeira de um estado de um tamanho
    escolhido.

    Parâmetros
    ----------
    uf: str
        Sigla da Unidade Federativa.
    tamanho: int (default=100)
        Tamanho em pixels da bandeira.

    Retorna
    -------
    str
        URL da bandeira do estado no formato PNG.

    --------------------------------------------------------------------------
    '''
    
    URL = r'https://upload.wikimedia.org/wikipedia/commons/thumb/'
    
    bandeira = {
        'AC': f'4/4c/Bandeira_do_Acre.svg/{tamanho}px-Bandeira_do_Acre.svg.png',
        'AM': f'6/6b/Bandeira_do_Amazonas.svg/{tamanho}px-Bandeira_do_Amazonas.svg.png',
        'AL': f'8/88/Bandeira_de_Alagoas.svg/{tamanho}px-Bandeira_de_Alagoas.svg.png',
        'AP': f'0/0c/Bandeira_do_Amap%C3%A1.svg/{tamanho}px-Bandeira_do_Amap%C3%A1.svg.png',
        'BA': f'2/28/Bandeira_da_Bahia.svg/{tamanho}px-Bandeira_da_Bahia.svg.png',
        'CE': f'2/2e/Bandeira_do_Cear%C3%A1.svg/{tamanho}px-Bandeira_do_Cear%C3%A1.svg.png',
        'DF': f'3/3c/Bandeira_do_Distrito_Federal_%28Brasil%29.svg/{tamanho}px-Bandeira_do_Distrito_Federal_%28Brasil%29.svg.png',
        'ES': f'4/43/Bandeira_do_Esp%C3%ADrito_Santo.svg/{tamanho}px-Bandeira_do_Esp%C3%ADrito_Santo.svg.png',
        'GO': f'b/be/Flag_of_Goi%C3%A1s.svg/{tamanho}px-Flag_of_Goi%C3%A1s.svg.png',
        'MA': f'4/45/Bandeira_do_Maranh%C3%A3o.svg/{tamanho}px-Bandeira_do_Maranh%C3%A3o.svg.png',
        'MG': f'f/f4/Bandeira_de_Minas_Gerais.svg/{tamanho}px-Bandeira_de_Minas_Gerais.svg.png',
        'MT': f'0/0b/Bandeira_de_Mato_Grosso.svg/{tamanho}px-Bandeira_de_Mato_Grosso.svg.png',
        'MS': f'6/64/Bandeira_de_Mato_Grosso_do_Sul.svg/{tamanho}px-Bandeira_de_Mato_Grosso_do_Sul.svg.png',
        'PA': f'0/02/Bandeira_do_Par%C3%A1.svg/{tamanho}px-Bandeira_do_Par%C3%A1.svg.png',
        'PB': f'b/bb/Bandeira_da_Para%C3%ADba.svg/{tamanho}px-Bandeira_da_Para%C3%ADba.svg.png',
        'PE': f'5/59/Bandeira_de_Pernambuco.svg/{tamanho}px-Bandeira_de_Pernambuco.svg.png',
        'PI': f'3/33/Bandeira_do_Piau%C3%AD.svg/{tamanho}px-Bandeira_do_Piau%C3%AD.svg.png',
        'PR': f'9/93/Bandeira_do_Paran%C3%A1.svg/{tamanho}px-Bandeira_do_Paran%C3%A1.svg.png',
        'RJ': f'7/73/Bandeira_do_estado_do_Rio_de_Janeiro.svg/{tamanho}px-Bandeira_do_estado_do_Rio_de_Janeiro.svg.png',
        'RO': f'f/fa/Bandeira_de_Rond%C3%B4nia.svg/{tamanho}px-Bandeira_de_Rond%C3%B4nia.svg.png',
        'RN': f'3/30/Bandeira_do_Rio_Grande_do_Norte.svg/{tamanho}px-Bandeira_do_Rio_Grande_do_Norte.svg.png',        
        'RR': f'9/98/Bandeira_de_Roraima.svg/{tamanho}px-Bandeira_de_Roraima.svg.png',
        'RS': f'6/63/Bandeira_do_Rio_Grande_do_Sul.svg/{tamanho}px-Bandeira_do_Rio_Grande_do_Sul.svg.png',
        'SC': f'1/1a/Bandeira_de_Santa_Catarina.svg/{tamanho}px-Bandeira_de_Santa_Catarina.svg.png',
        'SE': f'b/be/Bandeira_de_Sergipe.svg/{tamanho}px-Bandeira_de_Sergipe.svg.png',
        'SP': f'2/2b/Bandeira_do_estado_de_S%C3%A3o_Paulo.svg/{tamanho}px-Bandeira_do_estado_de_S%C3%A3o_Paulo.svg.png',
        'TO': f'f/ff/Bandeira_do_Tocantins.svg/{tamanho}px-Bandeira_do_Tocantins.svg.png',        
    }
    
    return URL + bandeira[uf]



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

    def __init__(self, deputado:camara.Deputado, ano:int):

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
            self.despesas = pd.concat(dfs, ignore_index=True)
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



def get_partidos_json():
    '''
    Captura partidos e a URL para as logos e exporta em um arquivo JSON que
    será consumido pela aplicação.

    --------------------------------------------------------------------------
    '''

    def get_logo(cod:int) -> str:
        p = camara.Partido(cod)
        return p.logo

    partidos = camara.lista_partidos(legislatura=56, itens=50)
    partidos['logo'] = partidos.id.apply(get_logo)
    partidos.drop(columns='uri', inplace=True)
    partidos.to_json('data/camara_data.json')

    return