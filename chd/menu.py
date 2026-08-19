import auth
import services
import database

def acesso_paciente():
    while True:
        print("\033[1m1. Login")
        print("0. Voltar\033[0m")
        print("-" * 33)

        opcao = input("\033[34mEscolha uma opção (0-1): \033[0m")

        if opcao == '1':
            cpf = input("\033[34mDigite o seu CPF: \033[0m")
            services.buscarPaciente(cpf)
            input("\033[34mPressione Enter para continuar\033[0m")
        elif opcao == '0':
            menu_inicial()
        else:
            print("\n\033[31mOpção Inválida! Por favor, digite 0, 1 ou 2.\033[0m\n")

def acesso_medico():
    while True:
        print("\033[1m1. Login")
        print("2. Criar Conta") 
        print("0. Voltar\033[0m")
        print("-" * 33)

        opcao = input("\033[34mEscolha uma opção (0-2): \033[0m")

        if opcao == '1':
            print(f"\n[Iniciando Login...]\n")
            login_medico()
            break
        elif opcao == '2':
            print(f"\n[Iniciando Criação de Conta para...]\n")
           
            services.cadastro_medico()
            
        elif opcao == '0':
            print("\nVoltando ao menu principal...\n")
            break
        else:
            print("\n\033[31mOpção Inválida! Por favor, digite 0, 1 ou 2.\033[0m\n")

def menu_inicial():
    while True:
        print("\033[32m=" * 33)
        print("\033[34mÁrea do Usuário CHD\033[0m")
        print("\033[32m=" * 33)

        print("\033[34m Identificação:")
        print("1. Médico")
        print("2. Paciente")
        print("3. Sair\033[0m")
        print("-" * 33)

        opcao = input("\033[34mEscolha uma opção (1-3): \033[0m")

        if opcao == '1':
            acesso_medico()
        elif opcao == '2':
            acesso_paciente()
        elif opcao == '3':
            print("\n\033[32mEncerrando o Sistema!\033[0m")
            break
        else:
            print("\n\033[31mOpção Inválida!Digite um número entre 1 e 3.\033[0m\n")

def menu_medicos():
    while True: 
        print("\033[32m="*33)
        print("\033[34mSistema de Cadastro de Pacientes")
        print("\033[32m=\033[0m"*33)
        
        print("\033[1m1. Cadastrar Paciente")
        print("2. Exibir Dados dos Pacientes")
        print("3. Remover Paciente")
        print("4. Voltar\033[0m")
        print("-" * 40)
        
        opcao = input("\033[34mEscolha uma opção (1-4):\033[0m")
        if opcao == '1':
            print("[Carregando o Sistema de Cadastro de Pacientes...")
            services.cadastro_paciente()
        elif opcao == '2':
            print("[Carregando a Exibição de Dados dos Pacientes...]")
            services.exibirDados()
        elif opcao == '3':
            print("[Carregando o Sistema de Remoção de Pacientes ")
            cpf = input("\033[34mDIgite o CPF do paciente: ")
            print(services.remover_paciente(cpf))


        elif opcao == '4':
            print("Voltando!")
            break
        else:
            print("\n\033[31mOpção Inválida! Por favor,digite um número entre 1 e 4.\n\033[0m")

def login_medico():
    print("\033[32m=" * 33)
    print("\033[34mÁrea de Login\033[0m")
    print("\033[32m=" * 33 + "\033[0m")

    crm_digitada = input("\033[34mCRM:  \033[0m")
    senha = input("\033[34mSenha: \033[0m")
    encontrado = auth.validarHash(senha, crm_digitada)
    if encontrado:
        menu_medicos()
    else:
        print("\033[31mUsuário ou senha incorreta\033[0m")

    login_medico()

        
menu_medicos()