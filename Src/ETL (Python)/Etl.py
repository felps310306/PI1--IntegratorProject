import mysql.connector
from datetime import datetime

config = {
    'user': 'root',
    'password': 'felipedeus13',
    'host': 'localhost',
    'database': 'cashfy_db'
}

def pipeline_etl_final():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        print("--- INICIANDO CARGA MULTIDIMENSIONAL DO CASHFY ---")

        # Massa de dados baseada nas pesquisas UnB, UFU e Times Brasil
        transacoes_brutas = [
            # CAIO (ID 1): Base UnB - Custo Aluno
            {'user': 1, 'tipo': 'receita', 'info': 'Bolsa Estágio TI', 'valor': '1200.00', 'data': '05/05/2026'},
            {'user': 1, 'tipo': 'despesa', 'info': 'Mensalidade e Material (UnB)', 'valor': '850.50', 'data': '10/05/2026'},
            {'user': 1, 'tipo': 'meta', 'info': 'Fundo de Formatura', 'valor': '2000.00', 'data': '31/12/2026'},

            # PEDRO (ID 2): Base Serasa - Endividamento 66%
            {'user': 2, 'tipo': 'receita', 'info': 'Auxílio de Custo', 'valor': '500.00', 'data': '01/05/2026'},
            {'user': 2, 'tipo': 'despesa', 'info': 'Acordo Serasa (Atrasada)', 'valor': '400.00', 'data': '05/05/2026'},
            {'user': 2, 'tipo': 'meta', 'info': 'Quitar Dívidas', 'valor': '5000.00', 'data': '20/12/2026'},

            # RAFAEL (ID 3): Base Times Brasil - Desorganização 9%
            {'user': 3, 'tipo': 'receita', 'info': 'Salário Assistente', 'valor': '1800.00', 'data': '05/05/2026'},
            {'user': 3, 'tipo': 'despesa', 'info': 'JUROS E MULTA CARTAO', 'valor': '185.75', 'data': '07/05/2026'},
            {'user': 3, 'tipo': 'meta', 'info': 'Reserva de Emergência', 'valor': '1500.00', 'data': '15/11/2026'}
        ]

        for item in transacoes_brutas:
            # TRANSFORM: Normalização de dados
            desc = item['info'].upper()
            val = float(item['valor'])
            dt = datetime.strptime(item['data'], '%d/%m/%Y').strftime('%Y-%m-%d')
            uid = item['user']

            # LOAD: Inserção segura no banco
            if item['tipo'] == 'receita':
                sql = "INSERT INTO RECEITA (descricao, valor, data_recebimento, id_usuario) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (desc, val, dt, uid))
            
            elif item['tipo'] == 'despesa':
                id_cat = 1 # Essencial
                if "UNB" in desc: id_cat = 2 # Educação
                if "JUROS" in desc: id_cat = 4 # Dívida
                sql = "INSERT INTO DESPESA (descricao, valor, data_gasto, id_categoria, id_usuario) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (desc, val, dt, id_cat, uid))
            
            elif item['tipo'] == 'meta':
                # CORREÇÃO DA SINTAXE AQUI: Usando %s para todos os campos
                sql = "INSERT INTO META_FINANCEIRA (descricao, valor_meta, valor_atual, data_limite, id_usuario) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (desc, val, 0.0, dt, uid))

        conn.commit()
        print("--- SUCESSO: Dados de Caio, Pedro e Rafael carregados! ---")

    except Exception as e:
        print(f"Erro no pipeline: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    pipeline_etl_final()