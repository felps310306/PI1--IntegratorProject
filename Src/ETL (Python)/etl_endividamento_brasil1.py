import pandas as pd
from bcb import sgs
import logging
import time  # <-- NOVO: Biblioteca nativa para controlar o tempo de espera

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_bcb_data(series_dict, start_date, max_retries=3):
    """
    Tenta extrair os dados do BCB. Se o servidor der Timeout, 
    espera 5 segundos e tenta novamente (até 3 vezes).
    """
    logging.info(f"Iniciando extração desde {start_date}...")
    
    for attempt in range(1, max_retries + 1):
        try:
            # Tenta fazer o download
            df = sgs.get(series_dict, start=start_date)
            logging.info(f"Extração concluída com sucesso (Tentativa {attempt}).")
            return df
            
        except Exception as e:
            logging.warning(f"Falha na tentativa {attempt}/{max_retries} - Erro: {e}")
            
            if attempt == max_retries:
                # Se já tentou 3 vezes e falhou, aí sim ele para o código
                logging.error("Máximo de tentativas atingido. A API do Banco Central está instável.")
                raise
                
            logging.info("Aguardando 5 segundos para tentar novamente...")
            time.sleep(5) # Pausa a execução por 5 segundos antes do próximo loop

def transform_data(df_mensal, df_diario, series_metadata):
    logging.info("Transformando e unindo dados...")
    
    # 1. Tratar os dados diários (Meta da Selic)
    # Pega o último valor válido de cada mês para alinhar com as outras séries
    df_diario_mensalizado = df_diario.resample('MS').last()
    
    # 2. Unir as duas tabelas pela data (Index)
    df_full = df_mensal.join(df_diario_mensalizado, how='outer')
    
    # 3. Formatar para o Star Schema (Unpivot)
    df_full = df_full.reset_index()
    df_full = df_full.rename(columns={'Date': 'data_referencia'})
    
    df_long = pd.melt(
        df_full, 
        id_vars=['data_referencia'], 
        var_name='id_indicador', 
        value_name='valor'
    )
    
    # Limpeza e metadados
    df_long = df_long.dropna(subset=['valor'])
    df_long['nome_indicador'] = df_long['id_indicador'].map(lambda x: series_metadata.get(x, x))
    df_long['data_extracao'] = pd.Timestamp.now().normalize()
    
    return df_long

def run_etl():
    # 1. Séries Mensais
    SERIES_MENSAIS = {
        29037: 'Endividamento das Famílias (%)',
        29038: 'Comprometimento de Renda (%)',
        21082: 'Inadimplência PF (%)',
        20542: 'Saldo Carteira Crédito PF (R$ Mi)',
        4390: 'Taxa Selic Mensal (% a.a.)',
        433: 'IPCA - Inflação Mensal (% a.m.)',
        24369: 'Taxa de Desocupação - Desemprego (%)',
        20716: 'Taxa Média de Juros PF (% a.a.)',
        20744: 'Concessões - Cartão de Crédito (R$ Mi)',
        20749: 'Concessões - Aquisição de Veículos (R$ Mi)'
    }
    
    # 2. Série Diária (Meta da Selic)
    SERIE_DIARIA = {
        432: 'Meta da Selic (% a.a.)'
    }
    
    Dicionario_Completo = {**SERIES_MENSAIS, **SERIE_DIARIA}
    
    # 3. Execução separada para evitar o bloqueio de 10 anos na diária
    raw_mensal = extract_bcb_data({k: k for k in SERIES_MENSAIS.keys()}, '2016-01-01')
    raw_diario = extract_bcb_data({k: k for k in SERIE_DIARIA.keys()}, '2017-01-01')
    
    clean_data = transform_data(raw_mensal, raw_diario, Dicionario_Completo)
    
    output_file = 'fEndividamento_Brasil.parquet'
    clean_data.to_parquet(output_file, index=False)
    logging.info(f"Arquivo salvo com sucesso: {output_file}")

if __name__ == "__main__":
    run_etl()