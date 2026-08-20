import database
  
def atualizar_Dados(cpf, tipo, inf):

    pacientes = database.carregar_pacientes()

    for key, dados in pacientes.items():
        if key == cpf:
            novosDados = (tipo, inf)
            if novosDados[0] == "nome":
                dados["nome"] = novosDados[1]
            elif novosDados[0] == "nascimento":
                dados["data_nascimento"] = novosDados[1]
            elif novosDados[0] == "email":
                dados["email"] = novosDados[1]
            database.salvar_pacientes(pacientes)

            print("Dados atualizados com sucesso!")
            
            break

                