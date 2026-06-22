# Requisitos Funcionais - Projeto CashFy

Este documento lista os requisitos funcionais essenciais (MVP) definidos para o Painel de Inteligência Macroeconômica **CashFy**, focados na engenharia de dados e na camada de *Business Intelligence*.

* **RF01 - Extração Automatizada de Dados (ETL):** O sistema deve conectar-se e extrair automaticamente séries temporais de dados macroeconômicos (Taxa Selic, IPCA, Inadimplência, Saldo de Crédito) das APIs oficiais do Banco Central do Brasil (SGS) e do IBGE (SIDRA).
* **RF02 - Tratamento e Transformação de Dados:** O sistema deve processar os dados brutos via *script* (Python/Pandas), realizar a limpeza de valores nulos e estruturar os dados para análise.
* **RF03 - Armazenamento Estruturado (Modelagem):** O sistema deve armazenar e organizar os dados processados em um modelo dimensional (*Star Schema*, com tabelas Fato e Dimensão) para alimentar a camada de visualização.
* **RF04 - Conversão de Escala Financeira:** O sistema deve aplicar formatação visual inteligente aos grandes volumes de saldo de crédito, convertendo automaticamente os valores brutos para a escala legível de "Bilhões" (Bi).
* **RF05 - Visualização em Dashboard Interativo:** O sistema deve apresentar os indicadores através de um painel visual (*dashboard*) responsivo e acessível via navegador de internet.
* **RF06 - Filtragem Temporal Dinâmica:** O sistema deve dispor de segmentadores (filtros) que permitam ao usuário refinar os dados visualizados por períodos específicos (ex: "Ano" e "Mês"), atualizando todos os gráficos simultaneamente.
* **RF07 - Cruzamento Visual de Indicadores:** O sistema deve possuir gráficos comparativos (como linhas sobrepostas) para demonstrar a correlação direta entre indicadores, como a variação da Taxa Selic frente à curva de Inflação (IPCA).
* **RF08 - Detalhamento de Risco (Drill-down):** O sistema deve permitir detalhar métricas críticas, exibindo o percentual de inadimplência e a variação mensal atrelada à carteira de crédito.
* **RF09 - Conformidade e Privacidade (Zero PII):** O sistema deve garantir que o fluxo de processamento atue estritamente sobre dados macroeconômicos agregados, bloqueando qualquer coleta ou exposição de informações de identificação pessoal (PII) segundo a LGPD.
