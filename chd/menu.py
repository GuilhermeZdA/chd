import auth


def acesso_paciente():
    while True:
        cpf = input("\033[34mDigite o seu CPF: ")
        

def acesso_medico(tipo_usuario):
    while True:
        print("\033[32m=" * 33)
        print(f"\033[34mAcesso: {tipo_usuario}\033[0m")
        print("\033[32m=" * 33)

        print("\033[1m1. Login")
        print("2. Criar Conta")
        print("0. Voltar\033[0m")
        print("-" * 33)

        opcao = input("\033[34mEscolha uma opção (0-2): \033[0m")

        if opcao == '1':
            print(f"\n[Iniciando Login de {tipo_usuario}...]\n")
            # func login
            break
        elif opcao == '2':
            print(f"\n[Iniciando Criação de Conta para {tipo_usuario}...]\n")
            if tipo_usuario == "Paciente":
                auth.cadastrar_paciente()
            break
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
            acesso("Médico")
        elif opcao == '2':
            acesso("Paciente")
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
        print("4. Sair do Sistema\033[0m")
        print("-" * 40)
        
        opcao = input("\033[34mEscolha uma opção (1-4):\033[0m")
        if opcao == '1':
            print("[Carregando o Sistema de Cadastro de Pacientes...")
            #cadastro()
        elif opcao == '2':
            print("[Carregando a Exibição de Dados dos Pacientes...]")
            #exibirDados()
        elif opcao == '3':
            print("[Carregando o Sistema de Remoção de Pacientes ")
            #removerPaciente()
        elif opcao == '4':
            print("Encerrando o Sistema!")
            break
        else:
            print("\n\033[31mOpção Inválida! Por favor,digite um número entre 1 e 4.\n\033[0m")

def menu_paciente():
    while True:
        print("\033[32m=" * 33)
        print("\033[34mÁrea do Paciente\033[0m")
        print("\033[32m=" * 33 + "\033[0m")

        print("\033[0m1. Consultar meus dados")
        print("2. Consultar meus agendamentos")
        print("3. Sair\033[0m")
        print("-" * 33)

        opcao = input("\033[34mEscolha uma opção (1-3): \033[0m")

        if opcao == '1':
            print("\n[Carregando seus dados...]\n")
        elif opcao == '2':
            print("\n[Carregando seus agendamentos...]\n")
        elif opcao == '3':
            print("\n\033[32mSaindo da Área do Paciente!\033[0m")
            break
        else:
            print("\n\033[31mOpção Inválida! Por favor, digite um número entre 1 e 3.\033[0m\n")
menu_inicial()