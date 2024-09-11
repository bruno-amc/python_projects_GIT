 def pesquisar_status(janela_alterar_status, matricula, resultado_status):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM employees WHERE matricula = ?',(matricula,))
    registred_found = cursor.fetchone()
    

  # searching the new status and using a variable to store it
    cursor.execute('SELECT status FROM employees WHERE matricula = ?', (matricula,))
    new_status = cursor.fetchone()[0]  # first item of the tuple
    conexao.close()

    status_text = "Ativo" if new_status == 1 else "Inativo"

    if registred_found:
        situacao = f"Register Nº {matricula} is {status_text}"
    else:
        situacao = "Status/User not found"
    resultado_status.config(text=f"{situacao}")

    return registred_found   