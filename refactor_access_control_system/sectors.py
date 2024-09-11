from database import connect_db

def add_sector(sector):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO sectors (sector) VALUES (?)', (sector,))
    conexao.commit()
    conexao.close()

def list_sectors():
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM sectors')
    sectors = cursor.fetchall()

    conexao.close()
    return sectors


def remove_sector(id):
    conexao = connect_db()
    cursor = conexao.cursor()

    # Verifica se algum funcionário está associado a esse setor
    cursor.execute('SELECT COUNT(*) FROM employees WHERE id = ?', (id,))
    funcionarios_no_setor = cursor.fetchone()[0]

    if funcionarios_no_setor > 0:
        print(f"Erro: Não é possível remover o setor. Existem {funcionarios_no_setor} funcionários associados a ele.")
    else:
        # Remove o setor se não houver funcionários associados
        cursor.execute('DELETE FROM sectors WHERE id = ?', (id,))
        conexao.commit()
        print(f"Setor com id {id} removido com sucesso.")
    
    conexao.close()


def edit_sector(id, new_name):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('UPDATE sectors SET sector = ? WHERE id = ?', (new_name, id))
    conexao.commit()
    conexao.close()

    print(f"Setor com id {id} foi atualizado para {new_name}.")


def list_employees_by_sector(setor_id):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM employees WHERE setor_id = ?', (setor_id,))
    employees = cursor.fetchall()

    conexao.close()
    return employees



