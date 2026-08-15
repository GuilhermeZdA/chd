def menu():
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
            cadastro()
        elif opcao == '2':
            print("[Carregando a Exibição de Dados dos Pacientes...]")
            exibirDados()
        elif opcao == '3':
            print("[Carregando o Sistema de Remoção de Pacientes ")
            removerPaciente()
        elif opcao == '4':
            print("Encerrando o Sistema!")
            break
        else:
            print("\n\033[31mOpção Inválida! Por favor,digite um número entre 1 e 4.\n\033[0m")
    
menu()