import streamlit as st
import pandas as pd
import yfinance as yf


# função de carregamento de dados
@st.cache_data
def carregar_dados(empresas):
    lista_acoes = " ".join(empresas)
    dados_acao = yf.Tickers(lista_acoes)
    cotacoes_acao = dados_acao.history(period='1d', start="2015-01-01", end="2025-04-01")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao


acoes = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA", "VALE3.SA", "ABEV3.SA", "GGBR4.SA"]
dados = carregar_dados(acoes)

st.write("""
    # App Preço de Ações
    O gráfico abaixo representa a evolução do preço das ações ao longo dos anos.
""")

# prepara as visualizações
lista_acoes = st.multiselect("Selecione as acões que deseja visualizar", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})



# grafico de area
st.line_chart(dados)
