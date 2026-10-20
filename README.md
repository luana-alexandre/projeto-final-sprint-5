# Análise de anúncios de veículos

Aplicativo web desenvolvido como projeto final do Sprint 5 da TripleTen. Permite explorar dados de anúncios de veículos nos Estados Unidos por meio de gráficos interativos.

## Funcionalidades

- Histograma da distribuição da rodagem dos veículos.
- Gráfico de dispersão da relação entre rodagem e preço.
- Caixas de seleção para exibir os gráficos individualmente ou ao mesmo tempo.

## Tecnologias utilizadas

Python, pandas, Plotly Express e Streamlit.

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o aplicativo na pasta raiz do projeto:

```bash
streamlit run app.py
```

## Arquivos do projeto

- `app.py`: código do aplicativo web.
- `vehicles_us.csv`: conjunto de dados.
- `notebooks/EDA.ipynb`: análise exploratória dos dados.
- `requirements.txt`: bibliotecas necessárias e suas versões.