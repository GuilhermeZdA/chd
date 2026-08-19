import database

def buscarPaciente(cpf):
    pacientes = database.carregar_pacientes() # Armazena os dados dos pacientes
    encontrado = False
    for key, dados in pacientes.items(): 
        if key == cpf: # Compara se o CPF informado condiz com o CPF no banco de dados
            encontrado = True
            data_nasc = dados["nascimento"][:2] + "/" + dados["nascimento"][2:4] + "/" + dados["nascimento"][4:8]

            print("\033[32m=\033[0m"* 135)

            print(f'\033[1m{"NOME":^40}{"DATA DE NASCIMENTO":^20}{"EMAIL":^35}{"CPF":^18}{"DATA DA CONSULTA":^25}\033[0m')

            print("\033[32m-\033[0m"* 135)

            print(f'{dados["nome"]:<40}{data_nasc:^20}{dados["email"]:^35}{key:^18}{dados["agendamento"]:^25}')

            print("\033[32m-\033[0m"* 135)
            break
    if not encontrado:
        print("CPF não encontrado!")

def buscarFuncionario(crm):
    funcionarios = database.carregar_medicos()
    for key, dados in funcionarios.items():
        if key == crm:
            return dados

