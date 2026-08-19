import auth
import database

def cadastro_medico():

    print("\n=== CADASTRO DE MÉDICO ===")

    nome = input("Digite o nome do médico: ")
    crm = input("Digite o CRM do médico: ")

    # Continua perguntando até o e-mail ser válido
    while True:
        email = input("Digite o e-mail do médico: ")

        if auth.validar_email(email):
            break

        print("E-mail inválido. Digite novamente.")

    # Continua perguntando até a senha ser válida
    while True:
        senha = input("Digite a senha do médico: ")

        if auth.validar_senha(senha):
            break

        print("Senha inválida. Digite novamente.")

    while True:
        resultado = auth.cadastrar_medico(
          nome,
          crm,
          email,
          senha
        )   

        if resultado == "CRM já cadastrado":
            print(resultado)
            crm = input("Digite outro CRM: ")
            continue

        if resultado == "E-mail já cadastrado":
            print(resultado)
            email = input("Digite outro e-mail: ")
            continue

        print(resultado)
        break
