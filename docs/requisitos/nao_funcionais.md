# Requisitos Não Funcionais - Projeto CashFy

Este documento lista os requisitos não funcionais essenciais definidos para o Painel de Inteligência Macroeconômica **CashFy**, focados na qualidade, segurança, desempenho e arquitetura do sistema.

* **RNF01 - Desempenho de Carregamento:** O painel (*dashboard*) deve carregar e renderizar os gráficos iniciais em menos de 3 segundos em ligações de internet padrão (banda larga), garantindo uma experiência fluida ao utilizador.
* **RNF02 - Usabilidade e Responsividade:** A interface deve ser plenamente responsiva, adaptando-se sem quebras de *layout* a diferentes resoluções de ecrã (desktops, portáteis e tablets), e seguir um padrão de *design* executivo (cores institucionais e tipografia limpa).
* **RNF03 - Segurança e Privacidade (LGPD):** O sistema não deve recolher, armazenar ou transacionar qualquer tipo de Informação Pessoalmente Identificável (PII). Todo o tráfego e acesso ao painel deve ser encriptado via protocolo HTTPS.
* **RNF04 - Disponibilidade e Alojamento:** A aplicação deve garantir alta disponibilidade (próxima de 99,9% de *uptime*), operando de forma estável através do serviço de alojamento em nuvem (ex: GitHub Pages).
* **RNF05 - Compatibilidade de Navegadores:** O *dashboard* deve ser suportado e renderizado corretamente nas versões mais recentes dos principais navegadores do mercado (Google Chrome, Microsoft Edge, Mozilla Firefox e Apple Safari).
* **RNF06 - Manutenibilidade e Versionamento:** O código-fonte, especialmente os *scripts* de ETL em Python, deve ser estruturado de forma modular, devidamente comentado e versionado num repositório Git, permitindo que qualquer engenheiro da equipa possa realizar futuras manutenções.
* **RNF07 - Robustez de Integração (APIs):** O sistema de extração (ETL) deve possuir mecanismos de tratamento de exceções (ex: *timeouts* ou valores nulos) caso as APIs do Banco Central (SGS) ou do IBGE (SIDRA) apresentem instabilidade temporária.
