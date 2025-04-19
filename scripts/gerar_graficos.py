import matplotlib.pyplot as plt

# Criando as funções para os gráficos.
def top10_populacao(df):
    top10 = df.sort_values(by='populacao', ascending=False).head(10)

    plt.figure(figsize=(12,6))
    barras = plt.bar(top10['municipio'], top10['populacao'], color='royalblue')
    plt.title('Top 10 Cidades Mais Populosas do Paraná')
    plt.xlabel('Município')
    plt.ylabel('População')
    plt.xticks(rotation=45, ha='right')
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{int(altura):,}'.replace(',', '.'),
                 ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig('relatorios/top10_populacao.png')
    plt.close()

def top10_menor_populacao(df):
    top10_menor = df.sort_values(by='populacao', ascending=True).head(10)

    plt.figure(figsize=(12,6))
    barras = plt.bar(top10_menor['municipio'], top10_menor['populacao'], color='royalblue')
    plt.title('Top 10 Cidades com as Menores Populações do Paraná')
    plt.xlabel('Município')
    plt.ylabel('População')
    plt.xticks(rotation=45, ha='right')
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{int(altura):,}'.replace(',', '.'),
                 ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig('relatorios/top10_menor_populacao.png')
    plt.close()

def top10_renda(df):
    pib_top10 = df.sort_values(by='renda_per_capita', ascending=False).head(10)

    plt.figure(figsize=(12,6))
    barras = plt.bar(pib_top10['municipio'], pib_top10['renda_per_capita'], color='royalblue')
    plt.title('Top 10 cidades com as melhores rendas do Paraná')
    plt.xlabel('Município')
    plt.ylabel('Renda Per Capita - Anual')
    plt.xticks(rotation=45, ha='right')
    for barra in barras:
        valor = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, valor,
                 f'R$ {valor:,.2}'.replace(',', 'X').replace('.', ',').replace('X', '.'),
                 ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig('relatorios/top10_renda_per_capita')
    plt.close()
    
def bottom_10_renda(df):
    pib_bottom10 = df.sort_values(by='renda_per_capita', ascending=True).head(10)

    plt.figure(figsize=(12,6))
    barras = plt.bar(pib_bottom10['municipio'], pib_bottom10['renda_per_capita'], color='royalblue')
    plt.title('Top 10 cidades com as Piores rendas do Paraná')
    plt.xlabel('Município')
    plt.ylabel('Renda Per Capita - Anual')
    plt.xticks(rotation=45, ha='right')
    for barra in barras:
        valor = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, valor,
                 f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'),
                 ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig('relatorios/top10_menor_renda_percapita')
    plt.close()

                
                


