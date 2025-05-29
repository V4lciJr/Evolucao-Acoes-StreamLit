# ?? Análise de Performance de Ações com Python e Streamlit

Este projeto é uma aplicação interativa desenvolvida com **Python** e **Streamlit**, que permite visualizar a performance histórica de ações da bolsa brasileira (IBOVESPA) de **janeiro de 2015 a abril de 2025**.

> ?? Projeto criado durante o **Curso de Python** da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/), com o objetivo de consolidar conhecimentos em análise de dados, visualização e construção de dashboards com Streamlit.

---

## ?? Funcionalidades

- ?? **Seleção de ações** do IBOV para análise personalizada.
- ?? **Filtro de período** com controle deslizante de datas.
- ?? **Visualização interativa** da evolução dos preços das ações.
- ?? **Cálculo automático da performance individual** de cada ativo.
- ?? **Cálculo da performance da carteira** considerando pesos iguais.

---

## ?? Demonstração

![Demonstração do Projeto](https://via.placeholder.com/800x400.png?text=Insira+um+print+do+dashboard+aqui)

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
??? app.py # Código principal do Streamlit
??? IBOV.csv # Base com os códigos das ações do IBOV
??? requirements.txt # Dependências do projeto


## ?? Como Executar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/projeto-performance-acoes.git
   cd projeto-performance-acoes

2. **Crie um ambiente virtual e ative:**

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. **Instale as dependências:**

pip install -r requirements.txt

4. **Execute a aplicação:**

streamlit run app.py


## ?? Aprendizados

- Leitura e manipulação de dados com Pandas.

- Uso da biblioteca yFinance para importar dados financeiros históricos.

- Criação de dashboards com Streamlit.

- Aplicação de lógica de negócio para análise de performance de ativos.

- Conceitos de carteira de investimentos com pesos iguais.

## ?? Observações

- Os dados das ações são carregados diretamente do Yahoo Finance via yfinance, e os códigos são lidos de um arquivo IBOV.csv.

- As análises são de caráter educativo e não configuram recomendação de investimento.


?? Contato
?? Projeto desenvolvido por Valci Júnior
?? Email: valcijunior19@hotmail.com
?? LinkedIn: [Valco Júnior](https://www.linkedin.com/in/valci-junior/)

? Dê uma estrela
Se você gostou do projeto, não se esqueça de deixar uma ? no repositório para apoiar!
