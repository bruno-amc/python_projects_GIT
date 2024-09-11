from datetime import datetime
from search_registered_employee import search_on_database_for_employee_register
from database import connect_db

def process_register_number(matricula, resultado, input_collaborator):
    register = search_on_database_for_employee_register(matricula)
   
    if register: #verifica se o registro existe (true), se não existir é um None.
        if register[5] == 1: #posição 5 = status. Exemplo da tupla: (1, '111111', 'aaaa', 'setorTeste1', 55, 1)
            resultado.config(text=f"Matrícula: {matricula}. Registrado!\n Boa refeição {register[2]}")
            tipo_refeicao = 'Almoço' if 11 <= datetime.now().hour <= 16 else 'Jantar'
            hora_registro = datetime.now().strftime("%H:%M:%S")
            data_registro = datetime.now().strftime("%d-%m-%Y")
            insert_register_into_table_access(matricula, data_registro, hora_registro, tipo_refeicao)

        else: 
            resultado.config(text=f"Matrícula {matricula} está inativa!")
    else: 
        resultado.config(text=f"Matrícula {matricula} não está cadastrada!")
    
    # Limpar o campo de entrada
    input_collaborator.delete(0, 'end')


def insert_register_into_table_access(matricula, data, hora, refeicao):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO access (matricula, data, hora, refeicao) VALUES (?, ?, ?, ?)',(matricula, data, hora, refeicao))
    print("inserido no banco a refeicao!")

    conexao.commit()
    conexao.close()


