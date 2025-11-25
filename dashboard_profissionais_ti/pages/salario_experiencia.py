import streamlit as st
import plotly.express as px

def app(df):
    st.title("Salário e Experiência")

    st.markdown("Análise de faixa salarial e tempo de experiência.")

    # Gráfico 5: Faixa salarial por senioridade
    fig1 = px.box(df, x="senioridade", y="faixa_salarial", color="senioridade", title="Faixa Salarial por Senioridade")
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico 6: Tempo de experiência em dados
    fig2 = px.histogram(df, x="tempo_experiencia_dados", color="senioridade", title="Tempo de Experiência em Dados")
    st.plotly_chart(fig2, use_container_width=True)

    # Gráfico 7: Tempo de experiência em TI
    fig3 = px.histogram(df, x="tempo_experiencia_ti", color="senioridade", title="Tempo de Experiência em TI")
    st.plotly_chart(fig3, use_container_width=True)