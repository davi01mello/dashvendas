# 🚀 Dashboard de Vendas (Python + Streamlit)

Dashboard interativo criado para analisar dados de vendas de uma empresa fictícia. O objetivo era transformar uma planilha estática (CSV) em insights visuais rápidos para a tomada de decisão.

## 🖼️ O que tem aqui?
Um painel web onde você consegue ver:
- **KPIs:** Faturamento Total, Quantidade de Pedidos e Ticket Médio.
- **Gráficos:** Evolução das vendas no tempo, categorias mais vendidas e performance por país.
- **Filtros:** Dá pra filtrar tudo por Ano e Status do pedido (ex: ver só o que já foi enviado).

---

## 🧠 Por que escolhi Python e Streamlit?
No desafio eu tinha a opção de usar Power BI, mas escolhi fazer **Via Código (Python)** por alguns motivos:

1.  **Liberdade Total:** Com Python (Pandas), eu limpo e transformo os dados exatamente como eu quero, sem depender das limitações visuais de ferramentas "arrasta e solta".
2.  **Agilidade:** O Streamlit é incrível. Consegui transformar meu script de análise em um site funcional em poucos minutos.
3.  **Portfólio:** Queria mostrar que sei manipular dados e construir aplicações reais, não apenas apertar botões. É uma solução que escala melhor se precisarmos integrar com Machine Learning no futuro.

---

## 💡 O que aprendi fazendo isso
Não foi só "copiar código". Tive alguns desafios reais:
* **Encoding de Arquivos:** Descobri na prática que nem todo CSV é UTF-8. Tive que tratar o encoding (`ISO-8859-1`) para o arquivo abrir.
* **Performance:** Aprendi a usar o `@st.cache_data` do Streamlit. Sem ele, o dashboard recarregava os dados do zero a cada clique. Agora ficou instantâneo.
* **Visualização:** O Plotly é muito poderoso para gráficos interativos (passar o mouse e ver os números) comparado ao Matplotlib estático.

---

## ⚙️ Como rodar na sua máquina
Quer testar? É só clonar e rodar:

1.  Instale as bibliotecas:
    ```bash
    pip install -r requirements.txt
    ```
2.  Rode o app:
    ```bash
    streamlit run app.py
    ```
