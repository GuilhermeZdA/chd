import database

def buscarPaciente(cpf):
    pacientes = database.carregar_pacientes() # Armazena os dados dos pacientes
    for key, dados in pacientes.items(): 
        if key == cpf: # Compara se o CPF informado condiz com o CPF no banco de dados
            print("=" * 70)
            print(f"{dados["nome"]:<40}{dados["nascimento"]:<10}{key:<15}")
            print("=" * 70)
        else:
            print("CPF não identificado")

def buscarFuncionario(cpf):
    funcionarios = database.carregar_medicos()
    for key, dados in funcionarios.items():
        if key == cpf:
            return dados
        else:
            print("Usuário não identificado")
