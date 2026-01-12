# 📊 Dashboard de Vendas - Análise de Performance

## 🎯 Objetivo
Desenvolvimento de um painel interativo para análise de performance comercial, permitindo visão clara de faturamento, evolução temporal e mix de produtos.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Framework:** Streamlit (pela agilidade de desenvolvimento e interatividade)
* **Visualização:** Plotly Express (para gráficos dinâmicos)
* **Dados:** Pandas (ETL e manipulação in-memory)

## 💡 Decisão Técnica: Por que Python/Streamlit?
Optei pelo desenvolvimento em Python (Code-First) em vez de ferramentas Low-Code (Power BI) pelos seguintes motivos:
1.  **Customização e Escala:** O Streamlit permite total controle sobre a lógica de tratamento de dados (ETL) antes da visualização, algo ideal para lidar com regras de negócio complexas.
2.  **Performance na Web:** A aplicação renderiza grandes volumes de dados de forma leve no navegador, facilitando o acesso remoto sem necessidade de licenças de software proprietário (como Power BI Pro).
3.  **Versionamento:** Por ser código puro, todo o projeto é versionado via Git, garantindo histórico de alterações e trabalho em equipe seguro.

## 🚀 Como executar
1. Clone o repositório.
2. Instale as dependências: `pip install pandas plotly streamlit`.
3. Execute: `streamlit run app.py`.
