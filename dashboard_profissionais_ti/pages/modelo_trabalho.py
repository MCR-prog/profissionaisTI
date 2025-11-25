import streamlit as st
import plotly.express as px

def app(df):
    st.title("Modelo de Trabalho")

    st.markdown("Distribuição do modelo de trabalho e flexibilidade.")

    # Gráfico 10: Modelo de trabalho
    fig1 = px.pie(df, names="modelo_trabalho", title="Modelo de Trabalho")
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico 11: Flexibilidade remoto
    fig2 = px.pie(df, names="flexibilidade_remoto", title="Flexibilidade Remota")
    st.plotly_chart(fig2, use_container_width=True)