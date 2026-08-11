import json, os

def exibirDados(arquivo):

    caminho = os.path.join(os.path.dirname(__file__), arquivo)  # Identifica o caminho absoluto do arquivo

    with open(caminho, "r", encoding="utf-8") as arq: 
        pacientes = json.load(arq)  # Carrega os dados do arquivo em uma váriavel

        print("=" * 70)
        print(f"{"NOME":^40}{"IDADE":<10}{"CPF":^11}")
        for cpf, v in pacientes.items():
            print(f"{v["nome"]:<40}{v["nascimento"]:<10}{cpf:<15}")
        print("=" * 70)

exibirDados("teste.json")