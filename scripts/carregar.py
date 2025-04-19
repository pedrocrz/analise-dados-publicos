import pandas as pd

def carregar_dados(caminho_arquivo):

    # Carrega o arquivo .xls com os dados dos municípios do Paraná.
    # Retorna: DataFrame do pandas com as colunas principais tratadas    
            
    try:
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        print('Arquivo carregar com sucesso')
        print('Colunas disponíveis no arquivo excel:')
        print(df.columns.tolist())
        df.columns = df.columns.str.strip().str.lower()

    except Exception as e2:
        print(f'Erro com openpyxl também:{e2}')
        raise RuntimeError('Não foi possível abrir o arquivo excel.')
        


    # Renomeando as colunas para facilitar seu uso
    df = df.rename(columns={
        'município [-]': 'municipio',
        'população no último censo - pessoas [2022]': 'populacao',
        'idhm <span>índice de desenvolvimento humano municipal</span> [2010]': 'idhm',
        'pib per capita - r$ [2021]': 'renda_per_capita'
    })



    # Convertendo colunas para numérico e tratando erros
    df['populacao'] = pd.to_numeric(df['populacao'], errors='coerce')
    df['idhm'] = pd.to_numeric(df['idhm'], errors='coerce')
    df['renda_per_capita'] = pd.to_numeric(df['renda_per_capita'], errors='coerce')
    

    # Selecionando as colunas que irei utilizar
    df = df[['municipio', 'populacao', 'idhm', 'renda_per_capita']]

    # Remove linhas com valores ausentes
    df = df.dropna()

    # Ordena os municipios por ordem alfabética
    df = df.sort_values(by='municipio')

    return df