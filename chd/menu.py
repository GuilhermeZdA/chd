import auth
import services
import database
import subprocess
from os import name
from time import sleep


def limpar_tela():
    subprocess.run(
        "cls" if name == "nt" else "clear",
        shell = True
    )

def acesso_paciente():
    while True:
        limpar_tela()
        print("\033[32m=\033[0m" * 33)
        print("\033[34mÁrea do Paciente\033[0m")
        print("\033[32m=\033[0m" * 33)
        print("\033[1m1. Login")
        print("0. Voltar\033[0m")
        print("\033[32m=\033[0m" * 33)

        opcao = input("\033[34mEscolha uma opção (0-1): \033[0m")

        if opcao == '1':
            cpf = input("\033[34mDigite o seu CPF: \033[0m")
            print("\n\033[33m[Buscando dados...]\033[0m\n")
            sleep(2)
            limpar_tela()
            services.buscarPaciente(cpf)
            input("\033[34m[Pressione Enter para continuar]\033[0m")
        elif opcao == '0':
            print("\n\033[33m[Voltando para o menu inicial...]\033[0m\n")
            sleep(2)
            return menu_inicial()
        else:
            print("\n\033[31m[Opção Inválida! Por favor, digite 0 ou 1.]\033[0m\n")
            sleep(3)

def acesso_medico():
    while True:
        limpar_tela()
        print("\033[32m=\033[0m" * 33)
        print("\033[34mÁrea do Médico\033[0m")
        print("\033[32m=\033[0m" * 33)
        print("\033[1m1. Login")
        print("2. Criar Conta") 
        print("0. Voltar\033[0m")
        print("\033[32m-\033[0m" * 33)

        opcao = input("\033[34mEscolha uma opção (0-2): \033[0m")

        if opcao == '1':
            print(f"\n\033[33m[Iniciando Login...]\033[0m\n")
            sleep(2)
            return login_medico()
        elif opcao == '2':
            print(f"\n\033[33m[Iniciando Criação de Conta...]\033[0m\n")
            sleep(2)
            limpar_tela()
            return services.cadastro_medico()    
        elif opcao == '0':
            print("\n\033[33m[Voltando ao menu principal...]\033[0m\n")
            sleep(2)
            return menu_inicial()
        else:
            print("\n\033[31mOpção Inválida! Por favor, digite 0, 1 ou 2.\033[0m\n")
            sleep(3)

def menu_inicial():
    while True:
        limpar_tela()
        print("\033[32m=\033[0m" * 33)
        print("\033[34mÁrea do Usuário CHD\033[0m")
        print("\033[32m=\033[0m" * 33)

        print("\033[34mIdentificação:\033[0m")
        print("1. Médico")
        print("2. Paciente")
        print("3. Sair")
        print("\033[32m-\033[0m" * 33)

        opcao = input("\033[34mEscolha uma opção (1-3): \033[0m")

        if opcao == '1':
            print("\n\033[33m[Acessando área do médico...]\033[0m\n")
            sleep(2)
            return acesso_medico()
        elif opcao == '2':
            print("\n\033[33m[Acessando área do paciente...]\033[0m\n")
            sleep(2)
            return acesso_paciente()
        elif opcao == '3':
            print("\n\033[31m[Encerrando o Sistema!]\033[0m")
            sleep(1)
            break
        else:
            print("\n\033[31m[Opção Inválida! Digite um número entre 1 e 3!]\033[0m\n")
            sleep(2)

def menu_medicos():
    while True:
        limpar_tela()
        print("\033[32m=\033[0m"*33)
        print("\033[34mSistema de Cadastro de Pacientes")
        print("\033[32m=\033[0m"*33)
        
        print("\033[1m1. Cadastrar Paciente")
        print("2. Exibir Dados dos Pacientes")
        print("3. Remover Paciente")
        print("4. Atualizar Dados dos Pacientes")
        print("5. Voltar\033[0m")
        print("\033[32m-\033[0m" * 33)
        
        opcao = input("\033[34mEscolha uma opção (1-5): \033[0m")
        if opcao == '1':
            print("\n\033[33m[Carregando o Sistema de Cadastro de Pacientes...]\033[0m\n")
            sleep(2)
            limpar_tela()
            services.cadastro_paciente()
            input("\n\033[34m[Pressione Enter para continuar]\033[0m")
        elif opcao == '2':
            print("\n\033[33m[Carregando a Exibição de Dados dos Pacientes...]\033[0m\n")
            sleep(2)
            limpar_tela()
            services.exibirDados()
            input("\n\033[34m[Pressione Enter para continuar]\033[0m")
        elif opcao == '3':
            print("\n\033[33m[Carregando o Sistema de Remoção de Pacientes...]\033[0m\n")
            sleep(2)
            cpf = input("\033[34mDigite o CPF do paciente: \033[0m")
            print(services.remover_paciente(cpf))
            input("\n\033[34m[Pressione Enter para continuar]\033[0m")
        elif opcao == '4':
            print("\n\033[33m[Carregando o Sistema de Atualização de Dados dos Pacientes...]\033[0m\n")
            sleep(2)
            return menuAtualizar()
        elif opcao == '5':
            print("\n\033[33m[Voltando para a área do médico...]\033[0m\n")
            sleep(2)
            return acesso_medico()
        else:
            print("\n\033[31m[Opção Inválida! Por favor, digite um número entre 1 e 5.]\n\033[0m")
            sleep(3)

def login_medico():
    limpar_tela()
    print("\033[32m=\033[0m" * 33)
    print("\033[34mÁrea de Login\033[0m")
    print("\033[32m=\033[0m" * 33)

    crm_digitada = input("\033[34mCRM:  \033[0m")
    senha = input("\033[34mSenha: \033[0m")
    encontrado = auth.validarHash(senha, crm_digitada)
    if encontrado:
        print("\n\033[32m[Acesso liberado! Carregando...]\033[0m\n")
        sleep(2)
        return menu_medicos()
    else:
        print("\033[31m[Usuário ou senha incorreta!]\033[0m")
        sleep(3)
    return login_medico()

def menuAtualizar():
    while True:
        limpar_tela()

        print("\033[32m=\033[0m" * 33)
        print("\033[34mAtualizar dados\033[0m")
        print("\033[32m=\033[0m" * 33)
        print("\033[1m1. Nome")
        print("2. Data de nascimento")
        print("3. Email")
        print("4. Voltar\033[0m")
        print("\033[32m-\033[0m" * 33)   
  
        opc = input("\033[34mEscolha uma opção (1-4): \033[0m")

        if opc == '4':
            print("\n\033[33m[Voltando para o sistema de cadastro...]\033[0m\n")
            sleep(2)
            return menu_medicos()
        if opc in ['1', '2', '3']:
            while True:
                cpf = input("\033[34mDigite o CPF do paciente: \033[0m")

                if auth.validar_cpf(cpf):
                    break
            
            if opc == '1':
                while True:
                    dado = str(input("Digite o novo nome: "))

                    if auth.validar_nome(dado):
                        break
                services.atualizar_Dados(cpf, "nome", dado)
                sleep(2)
            elif opc == '2':
                while True:
                    dado = str(input("Digite a nova data de nascimento: "))

                    if auth.validar_data_nascimento(dado):
                        break
                services.atualizar_Dados(cpf, "nascimento", dado)
                sleep(2)
            elif opc == '3':
                while True:
                    dado = str(input("Digite o novo email: "))

                    if auth.validar_email(dado):
                        break
                services.atualizar_Dados(cpf, "email", dado)
                sleep(2)
        else:
            print("\n\033[31m[Opção Inválida! Por favor, digite um número entre 0 e 2.]\n\033[0m")
            sleep(3)
        
menu_medicos()