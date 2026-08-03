import json, os

def exibirDados(arquivo):

    caminho = os.path.join(os.path.dirname(__file__), arquivo)

    with open(caminho, "r", encoding="utf-8") as arq:
        pacientes = json.load(arq)
        return pacientes

print(exibirDados("teste.json"))
