import sqlite3

#conexão com o banco de dados / connection with data bank
def connect_db():
    connection = sqlite3.connect('AccessControl.db')
    return connection


# criar as tabelas se elas não existirem / create table if they don't exist
def creat_tables():
    db_connection = connect_db()
    cursor = db_connection.cursor()

    # tabela dados cadastrais dos funcionarios / employees table
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula TEXT UNIQUE,                 
            nome TEXT NOT NULL,
            setor_id TEXT NOT NULL,
            idade INTEGER,
            status INTEGER,
            FOREIGN KEY(setor_id) REFERENCES setores(id)                   
                   )
                   ''')
    
    # Tabela de setores
  
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sectors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sector TEXT NOT NULL
    )
        ''')
    
    # tabela de acessos / access control table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS access (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula TEXT,
            data TEXT,
            hora TEXT,
            refeicao TEXT,
            FOREIGN KEY(matricula) REFERENCES employees(matricula)
        )
    ''')

    db_connection.commit()
    db_connection.close()






