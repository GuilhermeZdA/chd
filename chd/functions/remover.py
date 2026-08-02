import json
from pathlib import Path

CAMINHO_PASTA = Path(__file__).parent / 'pasta_json'
CAMINHO_ARQUIVO = CAMINHO_PASTA / 'dados.json'

# Cria a pasta caso ela não exista
# O exist_ok=True faz com que não de erro caso a pasta ja exista.
CAMINHO_PASTA.mkdir(parents=True, exist_ok=True)

def remover_usuario(cpf: str) -> None:
    # Transforma o cpf em str
    cpf_str = str(cpf)

    if not cpf:
        return "Cpf não informado"
    
    try: 
        # Lê todos os dados do arquivo json. 
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
            dados_carregados = json.load(arquivo) # Passa os dados pra uma lista

    # Cria uma lista vazia caso o arquivo json esteja vazio
    except json.JSONDecodeError:
        dados_carregados = []

    except FileExistsError:
        return "Aquivo não existe!"
    
    dados_atualizados = []

    # Percorre a lista criada
    cpf_encontrado = False
    for dado in dados_carregados:
        if dado.get('cpf') == cpf_str:
            # Caso o cpf passado seja igual ao da lista ele não sera adicionado na lista atualizada
            cpf_encontrado = True
            continue
        else:
            dados_atualizados.append(dado)

    if not cpf_encontrado:
        return "CPF não econtrado!"
    
    # Reescreve o arquivo json sem o cpf passado na func
    with open(CAMINHO_ARQUIVO, "w", encoding='utf8') as arquivo:
        json.dump(dados_atualizados, arquivo, indent=4)

    return "Os dados do usuário foram apagados."   

# Ainda falta fazer algumas validações

# Futuramente também da pra colocar outras funções dentro dessa para ela so fazer o papel de deletar o usuário
# Exemplo: validador_cpf, carregar_dados, salvar_dados e uma de buscar usuario