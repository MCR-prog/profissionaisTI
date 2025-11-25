import streamlit as st
import plotly.express as px

def app(df):
    st.title("Visão Geral dos Profissionais de TI")

    st.markdown("Distribuição de dados demográficos e educacionais.")

    # Gráfico 1: Distribuição de gênero
    fig1 = px.pie(df, names="genero", title="Distribuição de Gênero")
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico 2: Distribuição de raça
    fig2 = px.pie(df, names="raca", title="Distribuição de Raça")
    st.plotly_chart(fig2, use_container_width=True)

    # Gráfico 3: Nível de escolaridade
    fig3 = px.histogram(df, x="nivel_escolaridade", title="Nível de Escolaridade")
    st.plotly_chart(fig3, use_container_width=True)

    # Gráfico 4: Idade
    fig4 = px.histogram(df, x="idade", nbins=20, title="Distribuição de Idade")
    st.plotly_chart(fig4, use_container_width=True)