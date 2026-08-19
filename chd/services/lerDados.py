import json, os
import caminhos
def exibirDados():

      # Identifica o caminho absoluto do arquivo

    with open(caminhos.JSON_PACIENTES, "r", encoding="utf-8") as arq: 
        pacientes = json.load(arq)  # Carrega os dados do arquivo em uma váriavel

        print("=" * 70)
        print(f'{"NOME":^40}{"IDADE":<10}{"CPF":^11}')
        for cpf, v in pacientes.items():
            print(f'{v["nome"]:<40}{v["nascimento"]:<10}{cpf:<15}')
        print("=" * 70)
