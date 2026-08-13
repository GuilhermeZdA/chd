import json
import caminhos
from pathlib import Path

def carregar_json(caminho_arquivo: Path) -> dict:
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_carregados =json.load(arquivo)
        return dados_carregados
    
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Arquivo {caminho_arquivo.name}.json não existe!") from error
        
    except json.JSONDecodeError as error:
        raise ValueError(f"Arquivo {caminho_arquivo.name}.json está corrompido!") from error



def salvar_json(caminho_arquivo: Path, str, dados: dict) -> bool:
    try: 
        dados_carregados = carregar_json(caminho_arquivo)
        dados_carregados.update(dados)


        with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            json.dump(dados_carregados, arquivo, ensure_ascii=False, indent=4)
        return True
    
    except (FileNotFoundError, ValueError) as error:
        raise error


def carregar_pacientes() -> dict:
    dados = carregar_json(caminhos.JSON_PACIENTES)
    return dados

def carregar_medicos() -> dict:
    dados = carregar_json(caminhos.JSON_MEDICOS)
    return dados

def carregar_consultas() -> dict:
    dados = carregar_json(caminhos.JSON_CONSULTAS)
    return dados

def carregar_bloqueios() -> dict:
    ...

def salvar_pacientes(dados: dict) -> bool:
    dados_salvar = salvar_json(caminhos.JSON_PACIENTES, dados)
    return dados_salvar

def salvar_medicos(dados: dict) -> bool:
    dados_salvar = salvar_json(caminhos.JSON_MEDICOS, dados)
    return dados_salvar

def salvar_consultas(dados: dict) -> bool:
    dados_salvar = salvar_json(caminhos.JSON_CONSULTAS, dados)
    return dados_salvar



def inicializar_banco() -> bool:
    ...

def gerar_backup(nome_arquivo) -> bool:
    pacientes = carregar_pacientes()
    caminho_salvar = caminhos.CAMINHO_BACKUP / nome_arquivo

    with open(caminho_salvar, "w", encoding='utf-8') as arquivo:
        json.dump(pacientes, arquivo, indent=4)
    
    return True

def restaurar_backup():
    ...
    


    