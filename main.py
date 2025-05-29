import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import timedelta


# função de carregamento de dados
# carrega as informações de ações de janeiro de 2015 à abril de 2025
@st.cache_data
def carregar_dados(empresas):
    texto_acoes = " ".join(empresas)
    dados_acao = yf.Tickers(texto_acoes)
    cotacoes_acao = dados_acao.history(period='1d', start="2015-01-01", end="2025-04-01")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao


# carrega a base contendo os códigos das ações
@st.cache_data
def carregar_tickers_acoes():
    base_tickers = pd.read_csv('IBOV.csv', sep=';')
    tickers = list(base_tickers['Código'])
    tickers = [item + ".SA" for item in tickers]

    return tickers


acoes = carregar_tickers_acoes()
dados = carregar_dados(acoes)

st.write("""
    # Performance de Ações e Carteira
    O gráfico abaixo representa a evolução do preço das ações ao longo dos anos.
""")

# prepara as visualizações
st.sidebar.header("Filtros")

# filtro de ações
lista_acoes = st.sidebar.multiselect("Selecione as acões que deseja visualizar", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})

# filtro de datas
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()

intervalo_data = st.sidebar.slider("Selecione o período desejado",
                                   min_value=data_inicial,
                                   max_value=data_final,
                                   value=(data_inicial, data_final),
                                   step=timedelta(days=30))

dados = dados.loc[intervalo_data[0]: intervalo_data[1]]

# grafico de area
st.line_chart(dados)

# calculo de performance
texto_performance_ativo = ''
texto_performance_carteira = ''

if len(lista_acoes) == 0:
    lista_acoes = list(dados.columns)
elif len(lista_acoes) == 1:
    dados = dados.rename(columns={"Close": acao_unica})

carteira = [1000 for acao in lista_acoes]
total_inicial_carteira = sum(carteira)

# itera sobre a lista e ações e calcula a perfomance do ativo e da carteira
for i, acao in enumerate(lista_acoes):
    performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
    performance_ativo = float(performance_ativo)

    carteira[i] = carteira[i] * (1 + performance_ativo)

    if performance_ativo > 0:
        texto_performance_ativo += f'  \n{acao}: :green[{performance_ativo:.1%}]'
    elif performance_ativo < 0:
        texto_performance_ativo += f'  \n{acao}: :red[{performance_ativo:.1%}]'

total_final_carteira = sum(carteira)
performance_carteira = total_final_carteira / total_inicial_carteira - 1

if performance_carteira > 0:
    texto_performance_carteira += f'Performance da carteira com todos os ativos: :green[{performance_carteira:.1%}]'
elif performance_carteira < 0:
    texto_performance_carteira += f'Performance da carteira com todos os ativos: :red[{performance_carteira:.1%}]'

st.write(f"""
### Performance dos Ativos
Abaixo temos a performance de ativo selecionado

{texto_performance_ativo}

{texto_performance_carteira}

Para o cálculo da perfomance da carteira, partimos do princípio que ela possui o mesmo peso para cada ativo.
""")
