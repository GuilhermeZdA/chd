import json
import caminhos
from pathlib import Path

def carregar_json(caminho_arquivo: Path, nome: str) -> dict:
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_carregados =json.load(arquivo)
        return dados_carregados
    
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Arquivo {nome}.json não existe!") from error
        
    except json.JSONDecodeError as error:
        raise ValueError(f"Arquivo {nome}.json está corrompido!") from error



def salvar_json(caminho_arquivo: Path, nome: str, chave: str, dados: dict) -> bool:
    dados_carregados = carregar_json(caminho_arquivo, nome)

    dados_carregados[chave] = dados

    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_carregados, arquivo, indent=4)
        return True

    except FileNotFoundError as error:
        raise FileNotFoundError(f"Arquivo {nome}.json não existe!") from error

    except json.JSONDecodeError as error:
        raise ValueError(f"Arquivo {nome}.json está corrompido!") from error
    
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Arquivo {nome}.json não existe!") from error
       
    except json.JSONDecodeError as error:
        raise ValueError(f"Arquivo {nome}.json está corrompido!") from error



def carregar_pacientes() -> dict:
    dados = carregar_json(caminhos.JSON_PACIENTES, "pacientes")
    return dados


def carregar_medicos() -> dict:
    dados = carregar_json(caminhos.JSON_MEDICOS, "medicos")
    return dados

def carregar_consultas() -> dict:
    dados = carregar_json(caminhos.JSON_CONSULTAS, "consultas")
    return dados

def carregar_bloqueios() -> dict:
    ...

def salvar_pacientes(dados: dict) -> bool:
    chave = dados["cpf"]
    dados_salvar = salvar_json(
        caminhos.JSON_PACIENTES,
        "pacientes",
        chave,
        dados
    )
    return dados_salvar

def salvar_medicos(dados: dict) -> bool:
    chave = dados["crm"]
    dados_salvar = salvar_json(
        caminhos.JSON_MEDICOS,
        "medicos",
        chave,
        dados
    )
    return dados_salvar

def salvar_consultas(dados: dict) -> bool:
    dados_salvar = salvar_json(caminhos.JSON_CONSULTAS, "consultas", dados)
    return dados_salvar













def inicializar_banco() -> None:
    ...

def gerar_backup(caminho_arquivo):
    ...

def restaurar_backup():
    ...



    