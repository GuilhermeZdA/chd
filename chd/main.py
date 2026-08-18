import caminhos
import json
import auth
import services
import database
#import backups

def main():

    print("\n=== SISTEMA CHD ===")
    print("1 - Paciente")
    print("2 - Médico")

    while True:
        escolha = input("Escolha o tipo de cadastro que você deseja: ")

        if escolha == "1":
            services.cadastro_paciente()
            break

        elif escolha == "2":
            services.cadastro_medico()
            break

        else:
            print("Opção inválida. Digite 1 ou 2.")
            
main()
