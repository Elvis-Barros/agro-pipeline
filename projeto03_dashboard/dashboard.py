import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
import requests
from datetime import datetime

# ── CONFIGURAÇÕES ──────────────────────────
TICKER      = "ZS=F"
LATITUDE    = -16.766045
LONGITUDE   = -52.44655
CIDADE      = "Doverlândia/GO"
ARQUIVO_CSV_SOJA  = "projeto01_scraping/precos_soja.csv"
ARQUIVO_CSV_CLIMA = "projeto02_clima/historico_clima.csv"

# ── FUNÇÕES DE COLETA ──────────────────────
@st.cache_data(ttl=300)
def buscar_preco_soja():
    soja = yf.Ticker(TICKER)
    dados = soja.history(period="1d")
    return round(float(dados["Close"].iloc[-1]), 2)

@st.cache_data(ttl=300)
def buscar_dolar():
    dolar = yf.Ticker("BRL=X")
    dados = dolar.history(period="1d")
    return round(float(dados["Close"].iloc[-1]), 4)

@st.cache_data(ttl=300)
def buscar_clima():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LATITUDE, "longitude": LONGITUDE,
        "hourly": "temperature_2m,rain,relativehumidity_2m",
        "timezone": "America/Sao_Paulo", "forecast_days": 1,
    }
    dados = requests.get(url, params=params).json()
    hora = datetime.now().hour
    return {
        "temperatura": dados["hourly"]["temperature_2m"][hora],
        "chuva":       dados["hourly"]["rain"][hora],
        "umidade":     dados["hourly"]["relativehumidity_2m"][hora],
    }

# ── CONVERSÃO ──────────────────────────────
def calcular_preco_saca(preco_usd_bushel, cotacao_dolar):
    preco_usd_kg   = preco_usd_bushel / 27.216
    preco_usd_saca = preco_usd_kg * 60
    preco_brl_saca = preco_usd_saca * cotacao_dolar
    return round(preco_brl_saca, 2)

# ── DASHBOARD ──────────────────────────────
st.set_page_config(
    page_title="Painel do Produtor",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Painel do Produtor Rural")
st.subheader(f"📍 {CIDADE} — {datetime.now().strftime('%d/%m/%Y às %H:%M')}")
st.divider()

# ── MÉTRICAS ───────────────────────────────
preco_soja  = buscar_preco_soja()
cotacao_dolar = buscar_dolar()
clima       = buscar_clima()
preco_saca  = calcular_preco_saca(preco_soja, cotacao_dolar)

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Soja (R$/saca)",  f"R$ {preco_saca:,.2f}")
col2.metric("💱 Dólar (R$)",      f"R$ {cotacao_dolar:,.2f}")
col3.metric("🌡️ Temperatura",     f"{clima['temperatura']}°C")
col4.metric("🌧️ Chuva",           f"{clima['chuva']} mm")

# ── GRÁFICOS ───────────────────────────────
st.divider()
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("📈 Histórico do Preço da Soja")
    try:
        df_soja = pd.read_csv(ARQUIVO_CSV_SOJA)
        fig = px.line(df_soja, x="data_coleta", y="preco_usd",
                      title="Preço da Soja (US$/bushel)",
                      markers=True)
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.info("📊 Rode o Projeto 01 para gerar os dados.")

with col_graf2:
    st.subheader("🌡️ Histórico de Temperatura")
    try:
        df_clima = pd.read_csv(ARQUIVO_CSV_CLIMA)
        fig2 = px.line(df_clima, x="data_coleta", y="temperatura",
                       title="Temperatura em Doverlândia (°C)",
                       markers=True)
        st.plotly_chart(fig2, use_container_width=True)
    except:
        st.info("📊 Rode o Projeto 02 para gerar os dados.")

# ── RODAPÉ ─────────────────────────────────
st.divider()
st.caption("📡 Dados: Yahoo Finance · Open-Meteo API | Desenvolvido por Elvis Barros & Claude")