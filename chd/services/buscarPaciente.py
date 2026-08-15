from chd.database.db_manager import carregar_pacientes

def buscarPaciente(cpf):
    pacientes = carregar_pacientes()
    for key, dados in pacientes.items():
        if key == cpf:
            print("=" * 70)
            print(f"{dados["nome"]:<40}{dados["nascimento"]:<10}{key:<15}")
            print("=" * 70)
        else:
            print("CPF não identificado")