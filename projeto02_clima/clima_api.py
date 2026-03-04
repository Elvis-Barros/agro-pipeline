import requests
import sqlite3
import pandas as pd
from datetime import datetime

# ── CONFIGURAÇÕES ──────────────────────────
CIDADE    = "Doverlândia"
LATITUDE  = -16.766045
LONGITUDE = -52.44655
ARQUIVO_DB  = "projeto02_clima/clima.db"
ARQUIVO_CSV = "projeto02_clima/historico_clima.csv"

# ── BANCO DE DADOS ─────────────────────────
def criar_banco(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS clima (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade      TEXT,
            temperatura REAL,
            chuva       REAL,
            umidade     INTEGER,
            descricao   TEXT,
            data_coleta TEXT,
            hora_coleta TEXT
        )
    """)
    conn.commit()
    print("✅ Banco de dados pronto!")

# ── API DE CLIMA ───────────────────────────
def buscar_clima():
    print(f"🌐 Consultando clima de {CIDADE}...")
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":       LATITUDE,
        "longitude":      LONGITUDE,
        "hourly":         "temperature_2m,rain,relativehumidity_2m,weathercode",
        "timezone":       "America/Sao_Paulo",
        "forecast_days":  1,
    }
    resposta = requests.get(url, params=params, timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()
    hora_atual = datetime.now().hour
    hourly = dados["hourly"]
    temperatura = hourly["temperature_2m"][hora_atual]
    chuva       = hourly["rain"][hora_atual]
    umidade     = hourly["relativehumidity_2m"][hora_atual]
    weathercode = hourly["weathercode"][hora_atual]
    descricao   = "Chuva" if chuva > 0 else "Sem chuva"
    print(f"✅ Temperatura: {temperatura}°C | Chuva: {chuva}mm | Umidade: {umidade}%")
    return temperatura, chuva, umidade, descricao

# ── SALVAR NO BANCO ────────────────────────
def salvar_dados(conn, temperatura, chuva, umidade, descricao):
    print("💾 Salvando no banco de dados...")
    conn.execute("""
        INSERT INTO clima
            (cidade, temperatura, chuva, umidade, descricao, data_coleta, hora_coleta)
        VALUES
            (?, ?, ?, ?, ?, ?, ?)
    """, (
        CIDADE,
        temperatura,
        chuva,
        umidade,
        descricao,
        datetime.now().strftime("%Y-%m-%d"),
        datetime.now().strftime("%H:%M:%S"),
    ))
    conn.commit()
    print("✅ Dados salvos no banco!")

# ── EXPORTAR CSV ───────────────────────────
def exportar_csv(conn):
    print("📊 Exportando histórico para CSV...")
    df = pd.read_sql("SELECT * FROM clima ORDER BY id DESC", conn)
    df.to_csv(ARQUIVO_CSV, index=False, encoding="utf-8-sig")
    print(f"✅ Histórico exportado: {ARQUIVO_CSV} ({len(df)} registros)")

# ── EXECUÇÃO ───────────────────────────────
if __name__ == "__main__":
    print("🌦️  Iniciando monitor climático — Doverlândia/GO")
    conn = sqlite3.connect(ARQUIVO_DB)
    criar_banco(conn)
    temperatura, chuva, umidade, descricao = buscar_clima()
    salvar_dados(conn, temperatura, chuva, umidade, descricao)
    exportar_csv(conn)
    conn.close()
    print("🎉 Monitor climático finalizado com sucesso!")

