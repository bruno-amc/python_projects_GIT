from database import connect_db
import sqlite3

# funções para adicionar,  e listar funcionários / functions for add and list employees


def add_employees(matricula, nome, setor, idade, status):
    conexao = connect_db()
    cursor = conexao.cursor()

    try:
        cursor.execute('''INSERT INTO employees (matricula, nome, setor_id, idade, status)
                          VALUES (?, ?, ?, ?, ?)''', (matricula, nome, setor, idade, status))
        conexao.commit()
        print(f"Funcionário {nome} adicionado com sucesso.")
    except sqlite3.IntegrityError:
        print(f"Erro: A matrícula {matricula} já está registrada.")

    conexao.commit()
    conexao.close()


def inactivate_employee(matricula):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('''UPDATE employees SET status = 0 WHERE matricula =?''',(matricula,))
    print(f"Funcionário com matrícula {matricula} foi desativado.")

    conexao.commit()
    conexao.close()


def activate_employee(matricula):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('''UPDATE employees SET status = 1 WHERE matricula =?''',(matricula,))
    print(f"Funcionário com matrícula {matricula} foi ativado.")

    conexao.commit()
    conexao.close()


def list_employees():
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM employees')
    funcionarios = cursor.fetchall()

    conexao.close()
    return funcionarios