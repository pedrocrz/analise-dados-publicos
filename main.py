from scripts.carregar import carregar_dados
from scripts.gerar_graficos import top10_populacao
from scripts.gerar_graficos import top10_menor_populacao
from scripts.gerar_graficos import top10_renda
from scripts.gerar_graficos import bottom_10_renda

caminho_arquivo = 'dados/municipios_pr.xlsx'

def main():
    print('Carregando dados...')
    df = carregar_dados(caminho_arquivo)
    print('Dados carregados com sucesso!\n')

    print('Visualizando as primeiras linhas:')
    print(df.head(5))

    top10_populacao(df)
    top10_menor_populacao(df)
    top10_renda(df)
    bottom_10_renda(df)
    print('Gráfico gerado em: relatorios')
    


if __name__ == '__main__':
    main()
