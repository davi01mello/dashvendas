import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Dashboard de Vendas",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------------------
# 2. CARREGAMENTO E TRATAMENTO DE DADOS
# ---------------------------------------------------------------------
@st.cache_data
def load_data():
    # O dataset do Kaggle geralmente requer encoding ISO-8859-1
    df = pd.read_csv("sales_data_sample.csv", encoding="ISO-8859-1")
    
    # Converter data
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
    
    # Criar colunas auxiliares de tempo
    df['Year'] = df['ORDERDATE'].dt.year
    df['Month_Year'] = df['ORDERDATE'].dt.to_period('M').astype(str)
    
    return df

try:
    df_raw = load_data()
except FileNotFoundError:
    st.error("Arquivo 'sales_data_sample.csv' não encontrado. Verifique a pasta.")
    st.stop()

# ---------------------------------------------------------------------
# 3. SIDEBAR (FILTROS)
# ---------------------------------------------------------------------
st.sidebar.header("Filtros")

# Filtro de Ano
anos_disponiveis = sorted(df_raw['Year'].unique())
ano_selecionado = st.sidebar.multiselect(
    "Selecione o Ano",
    options=anos_disponiveis,
    default=anos_disponiveis # Vem tudo selecionado por padrão
)

# Filtro de Status do Pedido
status_disponiveis = sorted(df_raw['STATUS'].unique())
status_selecionado = st.sidebar.multiselect(
    "Status do Pedido",
    options=status_disponiveis,
    default=["Shipped", "Resolved"] # Focamos em vendas concretizadas
)

# Aplicando os filtros
df_filtrado = df_raw[
    (df_raw['Year'].isin(ano_selecionado)) &
    (df_raw['STATUS'].isin(status_selecionado))
]

# ---------------------------------------------------------------------
# 4. DASHBOARD PRINCIPAL
# ---------------------------------------------------------------------
st.title("📊 Dashboard de Performance de Vendas")
st.markdown("---")

# --- BLOCO DE KPIs (Indicadores) ---
total_vendas = df_filtrado['SALES'].sum()
qtd_pedidos = df_filtrado['ORDERNUMBER'].nunique()
ticket_medio = total_vendas / qtd_pedidos if qtd_pedidos > 0 else 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Faturamento Total", f"US$ {total_vendas:,.2f}")
with col2:
    st.metric("Total de Pedidos", qtd_pedidos)
with col3:
    st.metric("Ticket Médio", f"US$ {ticket_medio:,.2f}")

st.markdown("---")

# --- GRÁFICOS ---

col_graf1, col_graf2 = st.columns([2, 1])

# Gráfico 1: Evolução Temporal (Linha)
with col_graf1:
    vendas_tempo = df_filtrado.groupby('Month_Year')['SALES'].sum().reset_index()
    fig_line = px.line(
        vendas_tempo, 
        x='Month_Year', 
        y='SALES', 
        title='Evolução do Faturamento Mensal',
        markers=True
    )
    st.plotly_chart(fig_line, use_container_width=True)

# Gráfico 2: Vendas por Linha de Produto (Barras)
with col_graf2:
    vendas_produto = df_filtrado.groupby('PRODUCTLINE')['SALES'].sum().reset_index().sort_values('SALES', ascending=True)
    fig_bar = px.bar(
        vendas_produto, 
        x='SALES', 
        y='PRODUCTLINE', 
        title='Faturamento por Categoria',
        orientation='h'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico 3: Top Países (Mapa ou Barras)
st.subheader("Performance por País")
vendas_pais = df_filtrado.groupby('COUNTRY')['SALES'].sum().reset_index().sort_values('SALES', ascending=False)
fig_country = px.bar(
    vendas_pais, 
    x='COUNTRY', 
    y='SALES', 
    color='SALES',
    title='Ranking de Vendas por País'
)
st.plotly_chart(fig_country, use_container_width=True)

# ---------------------------------------------------------------------
# 5. TABELA DE DADOS (Opcional, para detalhamento)
# ---------------------------------------------------------------------
with st.expander("Ver Base de Dados Filtrada"):
    st.dataframe(df_filtrado)