import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Profissionais de TI", layout="wide")

# Carregar dados
@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/MCR-prog/profissionaisTI/refs/heads/main/dashboard_profissionais_ti/data/profissionais_ti.csv")
    return df

df = load_data()

# Sidebar: filtros globais
st.sidebar.header("Filtros Globais")
estados = st.sidebar.multiselect("Selecione Estados:", df["estado_mora"].unique(), default=df["estado_mora"].unique())
senioridade = st.sidebar.multiselect("Selecione Senioridade:", df["senioridade"].unique(), default=df["senioridade"].unique())
cargo = st.sidebar.multiselect("Selecione Cargo:", df["cargo"].unique(), default=df["cargo"].unique())

# Filtrar dados
df_filtered = df[
    (df["estado_mora"].isin(estados)) &
    (df["senioridade"].isin(senioridade)) &
    (df["cargo"].isin(cargo))
]

# Navegação entre páginas
st.sidebar.header("Navegação")
pagina = st.sidebar.radio("Ir para:", ["Visão Geral", "Salário e Experiência", "Cargos e Tecnologias", "Modelo de Trabalho"])

if pagina == "Visão Geral":
    import pages.overview as overview
    overview.app(df_filtered)
elif pagina == "Salário e Experiência":
    import pages.salario_experiencia as salario
    salario.app(df_filtered)
elif pagina == "Cargos e Tecnologias":
    import pages.cargos_tecnologias as cargos
    cargos.app(df_filtered)
elif pagina == "Modelo de Trabalho":
    import pages.modelo_trabalho as modelo

    modelo.app(df_filtered)
