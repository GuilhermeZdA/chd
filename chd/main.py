from services.paciente_service import cadastrar_paciente
from services.medico_service import cadastrar_medico
from auth.auth_services import validar_cpf, validar_email, validar_senha


def cadastro_paciente():

    print("\n=== CADASTRO DE PACIENTE ===")

    nome = input("Digite o nome do paciente: ")

    # Continua perguntando até o CPF ser válido
    while True:
        cpf = input("Digite o CPF do paciente: ")

        if validar_cpf(cpf):
            break

        print("CPF inválido. Digite novamente.")

    # Continua perguntando até o e-mail ser válido
    while True:
        email = input("Digite o email do paciente: ")

        if validar_email(email):
            break

        print("E-mail inválido. Digite novamente.")

    # Continua perguntando até a senha ser válida
    while True:
        senha = input("Digite a senha do paciente: ")

        if validar_senha(senha):
            break

        print("Senha inválida. Digite novamente.")

    data_nascimento = input(
        "Digite a data de nascimento do paciente: "
    )

    while True:
        resultado = cadastrar_paciente(
            nome,
            cpf,
            email,
            senha,
            data_nascimento
        )

        if resultado == "CPF já cadastrado":
            print(resultado)

            while True:
                cpf = input("Digite outro CPF: ")

                if validar_cpf(cpf):
                    break

                print("CPF inválido. Digite novamente.")

            continue

        if resultado == "E-mail já cadastrado":
            print(resultado)

            while True:
                email = input("Digite outro e-mail: ")

                if validar_email(email):
                    break

                print("E-mail inválido. Digite novamente.")

            continue

        print(resultado)
        break


def cadastro_medico():

    print("\n=== CADASTRO DE MÉDICO ===")

    nome = input("Digite o nome do médico: ")
    crm = input("Digite o CRM do médico: ")
    especialidade = input("Digite a especialidade do médico: ")

    # Continua perguntando até o e-mail ser válido
    while True:
        email = input("Digite o e-mail do médico: ")

        if validar_email(email):
            break

        print("E-mail inválido. Digite novamente.")

    # Continua perguntando até a senha ser válida
    while True:
        senha = input("Digite a senha do médico: ")

        if validar_senha(senha):
            break

        print("Senha inválida. Digite novamente.")

    while True:
        resultado = cadastrar_medico(
          nome,
          crm,
          especialidade,
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


def main():

    print("\n=== SISTEMA CHD ===")
    print("1 - Paciente")
    print("2 - Médico")

    while True:
        escolha = input("Escolha o tipo de cadastro que você deseja: ")

        if escolha == "1":
            cadastro_paciente()
            break

        elif escolha == "2":
            cadastro_medico()
            break

        else:
            print("Opção inválida. Digite 1 ou 2.")


main()