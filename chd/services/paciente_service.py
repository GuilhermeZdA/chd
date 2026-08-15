import database
import caminhos
import json
import auth

def remover_paciente(cpf: str) -> str:
    if not auth.validar_cpf(cpf):
        return "Cpf inválido"
    
    cpf = "".join(filter(str.isdigit, cpf))
    
    dados_carregados = database.carregar_pacientes()

    cpf_encontrado = False

    if cpf in dados_carregados:
        del dados_carregados[cpf]
        cpf_encontrado = True

    if not cpf_encontrado:
        return "CPF não econtrado!"
    
    with open(caminhos.JSON_PACIENTES, "w", encoding='utf8') as arquivo:
        json.dump(dados_carregados, arquivo, indent=4)

    return "Os dados do usuário foram apagados."   

# Ainda falta fazer algumas validações

# Futuramente também da pra colocar outras funções dentro dessa para ela so fazer o papel de deletar o usuário
# Exemplo: validador_cpf, carregar_dados, salvar_dados e uma de buscar usuario

def cadastro_paciente():

    print("\n=== CADASTRO DE PACIENTE ===")

    nome = input("Digite o nome do paciente: ")

    # Continua perguntando até o CPF ser válido
    while True:
        cpf = input("Digite o CPF do paciente: ")

        if auth.validar_cpf(cpf):
            break

        print("CPF inválido. Digite novamente.")

    # Continua perguntando até o e-mail ser válido
    while True:
        email = input("Digite o email do paciente: ")

        if auth.validar_email(email):
            break

        print("E-mail inválido. Digite novamente.")

    # Continua perguntando até a senha ser válida
    while True:
        senha = input("Digite a senha do paciente: ")

        if auth.validar_senha(senha):
            break

        print("Senha inválida. Digite novamente.")

    data_nascimento = input(
        "Digite a data de nascimento do paciente: "
    )

    while True:
        resultado = auth.cadastrar_paciente(
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

                if auth.validar_email(email):
                    break

                print("E-mail inválido. Digite novamente.")

            continue

        print(resultado)
        break
