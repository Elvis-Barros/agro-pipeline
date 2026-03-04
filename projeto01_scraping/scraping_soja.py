import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# ── CONFIGURAÇÕES ──────────────────────────
TICKER      = "ZS=F"                          # Código da soja no Yahoo Finance
ARQUIVO_CSV = "projeto01_scraping/precos_soja.csv"

# ── FUNÇÕES ────────────────────────────────
def buscar_preco():
    print("🌐 Consultando preço da soja — Yahoo Finance...")
    soja = yf.Ticker(TICKER)
    dados = soja.history(period="1d")
    preco = round(float(dados["Close"].iloc[-1]), 2)
    print(f"✅ Preço encontrado: US$ {preco} por bushel")
    return preco

def salvar_dados(preco):
    print("💾 Salvando dados...")
    novo_registro = {
        "ticker":      TICKER,
        "preco_usd":   preco,
        "data_coleta": datetime.now().strftime("%Y-%m-%d"),
        "hora_coleta": datetime.now().strftime("%H:%M:%S"),
    }
    df_novo = pd.DataFrame([novo_registro])
    if os.path.exists(ARQUIVO_CSV):
        df_novo.to_csv(ARQUIVO_CSV, mode="a", header=False, index=False)
    else:
        df_novo.to_csv(ARQUIVO_CSV, mode="w", header=True, index=False)
    print(f"✅ Dados salvos em: {ARQUIVO_CSV}")

# ── EXECUÇÃO ───────────────────────────────
if __name__ == "__main__":
    print("🌱 Iniciando coleta do preço da soja")
    preco = buscar_preco()
    salvar_dados(preco)
    print("🎉 Coleta finalizada com sucesso!")