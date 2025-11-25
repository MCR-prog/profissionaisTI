import streamlit as st
import plotly.express as px

def app(df):
    st.title("Cargos e Tecnologias")

    st.markdown("Análise de cargos e skills dos profissionais.")

    # Gráfico 8: Distribuição de cargos
    fig1 = px.histogram(df, x="cargo", color="senioridade", title="Distribuição de Cargos")
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico 9: Tecnologias mais usadas
    from collections import Counter
    import pandas as pd

    tecnologias = df["tecnologias"].dropna().tolist()
    lista_tecnologias = [t.strip() for sub in tecnologias for t in sub.split(",")]
    contagem = Counter(lista_tecnologias)
    df_tec = pd.DataFrame(contagem.items(), columns=["Tecnologia", "Contagem"]).sort_values(by="Contagem", ascending=False)

    fig2 = px.bar(df_tec, x="Tecnologia", y="Contagem", title="Tecnologias mais usadas")
    st.plotly_chart(fig2, use_container_width=True)