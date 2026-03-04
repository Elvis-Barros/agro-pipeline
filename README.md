# 🌱 Agro Pipeline — Inteligência de Dados para o Produtor Rural

> Pipeline de dados end-to-end aplicado ao agronegócio brasileiro:
> do dado bruto à decisão do produtor, em 3 projetos conectados.

---

## 🎯 O Problema

Um produtor de soja no Cerrado precisa responder uma pergunta todo dia:

> **"Vale a pena vender minha safra hoje?"**

Para isso, ele precisa cruzar **dois dados críticos ao mesmo tempo**:
- 📈 O **preço da soja** no mercado (Yahoo Finance / CBOT)
- 🌧️ O **clima da sua região** (chuva, temperatura, risco de perda)

Este repositório resolve exatamente isso — com um pipeline de dados construído do zero.

---

## 🗂️ Estrutura do Projeto
```
agro-pipeline/
│
├── projeto01_scraping/       # Coleta do preço da soja (yfinance)
│   └── scraping_soja.py
├── projeto02_clima/          # Coleta do clima por API + banco SQLite
│   └── clima_api.py
├── projeto03_dashboard/      # Dashboard Streamlit (preço × clima)
│   └── dashboard.py
├── docs/                     # Documentação extra
│   └── GUIA_GIT.md
│
├── requirements.txt          # Dependências do projeto
├── .gitignore                # Arquivos ignorados pelo Git
└── README.md                 # Este arquivo
```

---

## 🔗 Como os 3 Projetos se Conectam
```
[ Yahoo Finance ]                    [ Open-Meteo API ]
       │                                     │
       ▼                                     ▼
 Projeto 01                           Projeto 02
 scraping_soja.py                     clima_api.py
 precos_soja.csv                      clima.db
                                      historico_clima.csv
       │                                     │
       └──────────────┬──────────────────────┘
                      ▼
                Projeto 03
            dashboard.py
     "Devo vender minha soja hoje?"
```

---

## 📦 Os 3 Projetos

### Projeto 01 — Rastreador de Preços da Soja
**Técnicas:** yfinance · pandas · CSV  
Coleta o preço diário da soja em tempo real via Yahoo Finance (mercado CBOT).
Salva histórico em CSV com data e hora da coleta.

### Projeto 02 — Monitor Climático de Doverlândia/GO
**Técnicas:** API REST · JSON · SQLite · SQL  
Consulta temperatura, chuva e umidade via Open-Meteo API e persiste
em banco relacional SQLite com histórico. Exporta CSV para o dashboard.

### Projeto 03 — Painel do Produtor Rural
**Técnicas:** Streamlit · Plotly · integração de dados · conversão de moeda  
Une os dados dos dois projetos num dashboard interativo. Converte o preço
de US$/bushel para R$/saca automaticamente. Mostra gráficos de histórico
de preço e temperatura lado a lado.

---

## 🚀 Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/Elvis-Barros/agro-pipeline.git
cd agro-pipeline
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute na ordem**
```bash
# Coleta preços da soja
python projeto01_scraping/scraping_soja.py

# Coleta clima de Doverlândia
python projeto02_clima/clima_api.py

# Sobe o dashboard
python -m streamlit run projeto03_dashboard/dashboard.py
```

**4. Acesse no navegador**
```
http://localhost:8501
```

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.2-lightblue?logo=pandas)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.22-3F4F75?logo=plotly)
![yfinance](https://img.shields.io/badge/yfinance-0.2-green)

---

## 👤 Autor

**Elvis Barros**  
Desenvolvido como projeto de portfólio para demonstrar habilidades em
**Engenharia de Dados** aplicada ao agronegócio brasileiro.

[![GitHub](https://img.shields.io/badge/GitHub-Elvis--Barros-181717?logo=github)](https://github.com/Elvis-Barros)

---

*Dados de preço: Yahoo Finance (CBOT) · Dados climáticos: Open-Meteo API (open-source)*