import json, os
import database

def exibirDados():
    pacientes = database.carregar_pacientes()
      # Identifica o caminho absoluto do arquivo

    #with open(caminhos.JSON_PACIENTES, "r", encoding="utf-8") as arq: 
    #    pacientes = json.load(arq)  # Carrega os dados do arquivo em uma váriavel

    print("\033[32m=\033[0m"* 135)

    print(f'\033[1m{"NOME":^40}{"DATA DE NASCIMENTO":^20}{"EMAIL":^35}{"CPF":^18}{"DATA DA CONSULTA":^25}\033[0m')

    print("\033[32m=\033[0m"* 135)

    for cpf, dados in pacientes.items():

        data_nasc = dados["data_nascimento"][:2] + "/" + dados["data_nascimento"][2:4] + "/" + dados["data_nascimento"][4:8]

        print(f'{dados["nome"]:<40}{data_nasc:^20}{dados["email"]:^35}{cpf:^18}{dados["agendamento"]:^25}')

        print("\033[32m-\033[0m"* 135)    

    
