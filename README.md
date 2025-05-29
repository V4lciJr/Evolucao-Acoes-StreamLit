# ?? An�lise de Performance de A��es com Python e Streamlit

Este projeto � uma aplica��o interativa desenvolvida com **Python** e **Streamlit**, que permite visualizar a performance hist�rica de a��es da bolsa brasileira (IBOVESPA) de **janeiro de 2015 a abril de 2025**.

> ?? Projeto criado durante o **Curso de Python** da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/), com o objetivo de consolidar conhecimentos em an�lise de dados, visualiza��o e constru��o de dashboards com Streamlit.

---

## ?? Funcionalidades

- ?? **Sele��o de a��es** do IBOV para an�lise personalizada.
- ?? **Filtro de per�odo** com controle deslizante de datas.
- ?? **Visualiza��o interativa** da evolu��o dos pre�os das a��es.
- ?? **C�lculo autom�tico da performance individual** de cada ativo.
- ?? **C�lculo da performance da carteira** considerando pesos iguais.

---

## ?? Demonstra��o

![Demonstra��o do Projeto](https://via.placeholder.com/800x400.png?text=Insira+um+print+do+dashboard+aqui)

---

## ??? Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [yFinance](https://pypi.org/project/yfinance/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib / Plotly] (via Streamlit)
- Dados do IBOV via arquivo CSV (`IBOV.csv`)

---

## ?? Estrutura do Projeto

?? projeto-performance-acoes
??? app.py # C�digo principal do Streamlit
??? IBOV.csv # Base com os c�digos das a��es do IBOV
??? requirements.txt # Depend�ncias do projeto


## ?? Como Executar

1. **Clone o reposit�rio:**

   ```bash
   git clone https://github.com/seu-usuario/projeto-performance-acoes.git
   cd projeto-performance-acoes

2. **Crie um ambiente virtual e ative:**

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. **Instale as depend�ncias:**

pip install -r requirements.txt

4. **Execute a aplica��o:**

streamlit run app.py


## ?? Aprendizados

- Leitura e manipula��o de dados com Pandas.

- Uso da biblioteca yFinance para importar dados financeiros hist�ricos.

- Cria��o de dashboards com Streamlit.

- Aplica��o de l�gica de neg�cio para an�lise de performance de ativos.

- Conceitos de carteira de investimentos com pesos iguais.

## ?? Observa��es

- Os dados das a��es s�o carregados diretamente do Yahoo Finance via yfinance, e os c�digos s�o lidos de um arquivo IBOV.csv.

- As an�lises s�o de car�ter educativo e n�o configuram recomenda��o de investimento.


?? Contato
?? Projeto desenvolvido por Valci J�nior
?? Email: valcijunior19@hotmail.com
?? LinkedIn: [Valco J�nior](https://www.linkedin.com/in/valci-junior/)

? D� uma estrela
Se voc� gostou do projeto, n�o se esque�a de deixar uma ? no reposit�rio para apoiar!
