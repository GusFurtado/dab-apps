from DadosAbertosBrasil import ibge
import pandas as pd



KPIS = {
        
    'Taxa de Alfabetização': {
        'agregado': 1383,
        'periodo': 2010,
        'variaveis': 1646,
        'classificacoes': {2: 6794}
    },

    'População Economicamente Ativa': {
        'agregado': 616,
        'periodo': 2010,
        'variaveis': 1000140,
        'classificacoes': {90: 3287}
    },
    
    'População sem Religião': {
        'agregado': 137,
        'periodo': 2010,
        'variaveis': 1000093,
        'classificacoes': {133: 2836}
    },

    'População Indígena': {
        'agregado': 136,
        'periodo': 2010,
        'variaveis': 1000093,
        'classificacoes': {86: 2780}
    },
    
    'Rede Geral de Abastecimento de Água': {
        'agregado': 3218,
        'periodo': 2010,
        'variaveis': 1000096,
        'classificacoes': {61: 92853}
    },
    
    'Sem Banheiro ou Sanitário': {
        'agregado': 3218,
        'periodo': 2010,
        'variaveis': 1000096,
        'classificacoes': {299: 10006}
    },
    
    'Lixo Coletado': {
        'agregado': 3218,
        'periodo': 2010,
        'variaveis': 1000096,
        'classificacoes': {67: 2520}
    },
    
    'Energia Elétrica': {
        'agregado': 3218,
        'periodo': 2010,
        'variaveis': 1000096,
        'classificacoes': {309: 3011}
    }
    
}



series = []
for kpi in KPIS:
    print(f'Capturando dados de {kpi}')
    df = ibge.sidra(
        tabela = KPIS[kpi]['agregado'],
        periodos = KPIS[kpi]['periodo'],
        variaveis = KPIS[kpi]['variaveis'],
        classificacoes = KPIS[kpi]['classificacoes'],
        localidades = {6: 'all'}
    )
    df = df.loc[:,['Município (Código)', 'Município', 'Valor']]
    df.Valor = df.Valor.replace('-', 0)
    df.Valor = df.Valor.astype(float)
    df.columns = ['Código', 'Município', kpi]
    df.set_index(['Código', 'Município'], inplace=True)
    series.append(df)



df_concat = pd.concat(series, axis=1)
df_concat.reset_index(inplace=True)
df_concat.to_parquet('data/Indicadores.parquet')