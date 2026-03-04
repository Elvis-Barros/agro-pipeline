# 🌱 Agro Pipeline — Inteligência de Dados para o Produtor Rural

> Pipeline de dados end-to-end aplicado ao agronegócio brasileiro:  
> do dado bruto à decisão do produtor, em 3 projetos conectados.

---

## 🎯 O Problema

Um produtor de soja no Cerrado precisa responder uma pergunta todo dia:

> **"Vale a pena vender minha safra hoje?"**

Para isso, ele precisa cruzar **dois dados críticos ao mesmo tempo**:
- 📈 O **preço da soja** no mercado (CEPEA/ESALQ)
- 🌧️ O **clima da sua região** (chuva, temperatura, risco de perda)

Este repositório resolve exatamente isso — com um pipeline de dados construído do zero.

---

## 🗂️ Estrutura do Projeto

```
agro-pipeline/
│
├── projeto01_scraping/       # Coleta do preço da soja (Web Scraping)
├── projeto02_clima/          # Coleta do clima por API + banco SQLite
├── projeto03_dashboard/      # Dashboard Streamlit (preço × clima)
├── docs/                     # Imagens e documentação extra
│
├── requirements.txt          # Dependências do projeto
├── .gitignore                # Arquivos ignorados pelo Git
└── README.md                 # Este arquivo
```

---

## 🔗 Os 3 Projetos — Como se Conectam

```
[ CEPEA Website ]                    [ Open-Meteo API ]
       │                                     │
       ▼                                     ▼
 Projeto 01                           Projeto 02
 Web Scraping                         API + SQLite
 precos_soja.csv                      clima.db
       │                                     │
       └──────────────┬──────────────────────┘
                      ▼
                Projeto 03
            Dashboard Streamlit
         "Devo vender minha soja hoje?"
```

---

## 📦 Projetos

### Projeto 01 — Rastreador de Preços da Soja
**Técnicas:** Web Scraping · requests · BeautifulSoup · pandas  
Coleta o preço diário da soja direto do CEPEA (Centro de Estudos Avançados em Economia Aplicada da ESALQ/USP) — a mesma fonte usada por tradings e cooperativas no Brasil. Salva histórico em CSV e Excel.

### Projeto 02 — Monitor Climático da Região Produtora
**Técnicas:** Consumo de API REST · JSON · SQLite · SQL  
Consulta temperatura, chuva e umidade de Doverlândia-GO (-16.7660, -52.4465) via Open-Meteo API e persiste em banco relacional com histórico. Executa consultas analíticas SQL para identificar padrões.

### Projeto 03 — Dashboard de Decisão
**Técnicas:** Streamlit · Plotly · integração de dados  
Une os dados dos dois projetos anteriores num dashboard interativo. Mostra a correlação entre clima extremo e variação de preço — entregando ao produtor uma visão de contexto para a decisão de venda.

---

## 🚀 Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/agro-pipeline.git
cd agro-pipeline
```

**2. Crie um ambiente virtual e instale as dependências**
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

**3. Execute na ordem**
```bash
# Coleta preços
python projeto01_scraping/scraping_soja.py

# Coleta clima
python projeto02_clima/clima_api.py

# Sobe o dashboard
streamlit run projeto03_dashboard/dashboard.py
```

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.2-lightblue?logo=pandas)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.22-3F4F75?logo=plotly)

---

## 👤 Autor

Desenvolvido como projeto de portfólio para demonstrar habilidades em  
**Engenharia de Dados** aplicada ao agronegócio brasileiro.

---

*Dados de preço: CEPEA/ESALQ-USP · Dados climáticos: Open-Meteo API (open-source)*
