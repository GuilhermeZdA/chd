import auth
import database

def cadastro_medico():
    print("\033[32m=\033[0m" * 33)
    print("\033[34mCadastro do Médico\033[0m")
    print("\033[32m=\033[0m" * 33)
    while True: 
        nome = input("\033[34mDigite o nome do médico:\033[0m ")

        if auth.validar_nome(nome):
            break

    while True:
        crm = input("\033[34mDigite o CRM do médico:\033[0m ")
        encontrado = False
        if auth.validar_crm(crm):
            medicos = database.carregar_medicos()
            for key in medicos.keys():
                if key == crm:
                    encontrado = True
                    break
        if not encontrado:
            break

    # Continua perguntando até o e-mail ser válido
    while True:
        email = input("\033[34mDigite o e-mail do médico:\033[0m ")
        encontrado = False
        if auth.validar_email(email):
            medicos = database.carregar_medicos()
            for item in medicos.values():
                if item["email"] == email:
                    encontrado = True
                    break
            if not encontrado:
                break

        print("E-mail inválido. Digite novamente!")

    # Continua perguntando até a senha ser válida
    while True:
        senha = input("\033[34mDigite a senha do médico:\033[0m ")

        if auth.validar_senha(senha):
            break

        print("Senha inválida. Digite novamente!")

    while True:
        resultado = auth.cadastrar_medico(
          nome,
          crm,
          email,
          senha
        )   


        if resultado == "E-mail já cadastrado":
            print(resultado)
            email = input("\033[34mDigite outro e-mail:\033[0m ")
            continue

        print(resultado)
        break