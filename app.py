import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análise de anúncios de veículos')
st.write('Explore a distribuição da rodagem e sua relação com o preço.')

hist_checkbox = st.checkbox('Criar histograma')
scatter_checkbox = st.checkbox('Criar gráfico de dispersão')

if hist_checkbox:
    st.write('Distribuição da rodagem dos veículos anunciados.')

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribuição da rodagem dos veículos',
        labels={'odometer': 'Rodagem'},
        color_discrete_sequence=['#D96BA0']
    )

    fig.update_layout(yaxis_title='Quantidade de anúncios')
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:
    st.write('Relação entre rodagem e preço dos veículos anunciados.')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Relação entre rodagem e preço',
        labels={'odometer': 'Rodagem', 'price': 'Preço'},
        opacity=0.5,
        color_discrete_sequence=['#A678C4']
    )

    st.plotly_chart(fig, use_container_width=True)
