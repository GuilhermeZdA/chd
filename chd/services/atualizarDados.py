from chd.database.db_manager import carregar_pacientes
from datetime import datetime

def menuAtualizar():
    while True:
        print("=" * 70)
        print("Qual dado será atualizado?")
        print("""1 - NOME
2 - DATA DE NASCIMENTO
3 - CPF
0 - VOLTAR""")
        opc = int(input("Digite sua opção: "))

        if opc == 0:
            break
        elif opc == 1:
            dado = str(input("Digite o novo nome: "))
            return "nome", dado
        elif opc == 2:
            dado = int(input("Digite a nova data de nascimento: "))
            idade = datetime.today().year - dado
            return "nascimento", dado
        

def atualizarDados(cpf):
    pacientes = carregar_pacientes()
    for key, dados in pacientes.items():
        if key == cpf:
            novosDados = menuAtualizar()
            if novosDados[0] == "nome":
                dados["nome"] == novosDados[1]
            elif novosDados[1] == "nascimento":
                dados["nascimento"] == novosDados[1]
            print("Dados atualizados com sucesso!")
            break

                