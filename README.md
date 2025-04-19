# Análise de Dados Públicos - Paraná
Este projeto é um pipeline simples de análise de dados públicos do IBGE com Python. O objetivo é ler, processar, e gerar relatórios gráficos sobre a população e indicadores socieconômicos dos municípios do Paraná.

## Estrutura

<pre> $tree. 
├── README.md
├── dados
│   └── municipios_pr.xlsx
├── main.py
├── relatorios
│   ├── top10_menor_populacao.png
│   ├── top10_menor_renda_percapita.png
│   ├── top10_populacao.png
│   └── top10_renda_per_capita.png
├── requirements.txt
└── scripts
    ├── carregar.py
    └── gerar_graficos.py

``` </pre>

## Funcionalidades

- Leiura de planilha Excel (.xlsx) com dados municipais
- Processamento e filtragem dos dados relevantes
- Geração de gráficos com o TOP 10 cidades
- Salvamento automático dos gráficos em '.png'


## Requisitos

- Python 3.8+
- Pandas
- Matplotlib
- openpyxl
 Instale com:
 """ pip install -r requeriments.txt """

 ## Observações
 - Os dados utilizados foram obtidos de fontes públicas (IBGE).
 - Este projeto é educativo e voltado para a prática de **engenharia e análise de dados** com Python

 ## Autor
 Pedro Cruz - estudante de Engenharia de software
 Linkedin: [linkedin](https://www.linkedin.com/in/pedro-luiz-cruz-01aa1b1b2/)