import json
from database.db_manager import *
from auth.auth_services import *
import caminhos

def remover_paciente(cpf: str) -> str:
    if not validar_cpf(cpf):
        return "Cpf inválido"
    
    cpf = "".join(filter(str.isdigit, cpf))
    
    dados_carregados = carregar_pacientes()

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