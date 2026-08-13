import caminhos
import json
from database.db_manager import salvar_pacientes
from services.paciente_service import *
from auth.auth_services import cadastrar_paciente


def main():
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o CPF do paciente: ")
    email = input("Digite o email do paciente: ")
    senha = input("Digite a senha do paciente: ")
    data_nascimento = input("Digite a data de nascimento do paciente: ")

    resultado = cadastrar_paciente(
        nome,
        cpf,
        email,
        senha,
        data_nascimento
    )
    print(resultado)
    
main()