import json
from pathlib import Path

CAMINHO_PASTA = Path(__file__).parent / 'pasta_json'
CAMINHO_ARQUIVO = CAMINHO_PASTA / 'dados.json'


CAMINHO_PASTA.mkdir(parents=True, exist_ok=True)

def remover_usuario(cpf: str) -> None:

    cpf_str = str(cpf)

    try: 
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
            dados_carregados = json.load(arquivo)

    except json.JSONDecodeError:
        dados_carregados = []
    
    dados_atualizados = []

    for dado in dados_carregados:
        if dado.get['cpf'] == cpf_str:
            continue
        else:
            dados_atualizados.append(dado)

    with open(CAMINHO_ARQUIVO, "w", encoding='utf8') as arquivo:
        json.dump(dados_atualizados, arquivo, indent=4)

    print(
         "Os dados do usuário foram apagados."
    )
