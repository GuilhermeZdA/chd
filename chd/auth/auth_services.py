from database.db_manager import carregar_pacientes, salvar_pacientes
from auth.hash.geradorHash import geradorHash
from datetime import datetime

def validar_cpf(cpf: str) -> bool:

    cpf = "".join(filter(str.isdigit, cpf))

    if not cpf or len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    decimo_digito = sum(int(x) * y for x, y  in zip(cpf[:9], range(10, 1, -1)))
    decimo_digito = 0 if (decimo_digito % 11) < 2 else 11 - (decimo_digito % 11)
    
    undecimo_digito = sum(int(x) * y for x, y  in zip(cpf[:10], range(11, 1, -1)))
    undecimo_digito = 0 if (undecimo_digito % 11) < 2 else 11 - (undecimo_digito % 11)

    if str(decimo_digito) == cpf[9] and str(undecimo_digito) == cpf[10]:
        return True
    return False

def validar_nome(nome: str) -> bool: # receber um nome para devolver uma valor booleano.
    nome = nome.strip() # retira espaços antes e depois do nome.

    if not nome: # Se estive espaço vazio, devolve False.
        return False

    if "  " in nome: # impede dois ou mais espaços consecutivos.
        return False

    if not all(caractere.isalpha() or caractere.isspace() for caractere in nome): # verifica se o nome é composto apenas por letras.
        return False

    return True

def validar_email(email: str) -> bool:
    email = email.strip() # remove espaços antes e depois do email

    if not email: # se o email estiver vazio, retorna False
        return False

    
    if email.count("@") != 1: # O email deve ter exatamente um "@"
        return False

    parte_antes, parte_depois = email.split("@")

    
    if not parte_antes: # Deve existir algo antes do "@"
        return False

    
    if not parte_depois: # Deve existir algo depois do "@"
        return False

    
    if "." not in parte_depois: # O domínio deve possuir um "."
        return False

    
    if parte_depois.startswith(".") or parte_depois.endswith("."): # O "." não pode ser o primeiro ou o último caractere do domínio
        return False

    
    parte_dominio, extensao = parte_depois.split(".", 1) # Deve existir algo entre o "@" e o "."

    if not parte_dominio:
        return False

    
    if len(extensao) < 2: # A extensão deve ter pelo menos 2 caracteres
        return False

    return True

def validar_senha(senha: str) -> bool:
    if len(senha) < 6: # Retorna False se a senha for menor que 6 dígitos.
        return False

    if not any(caractere.isupper() for caractere in senha): # Retorna False se a senha não tiver no mínimo 1 caractere em maiúsculo.
        return False

    if not any(caractere.isdigit() for caractere in senha): # Retorna False se a senha não tiver no mínimo 1 número.
        return False

    return True

def validar_data_nascimento(data_nascimento: str) -> bool:
    try:
        data = datetime.strptime(data_nascimento, "%d%m%Y")

        hoje = datetime.now()

        # Não permite data de nascimento no futuro.
        if data > hoje:
            return False

        # Não permite pessoas com mais de 120 anos(idade máxima).
        if data.year < hoje.year - 120:
            return False

        return True

    except ValueError:
        return False

def cadastrar_paciente(nome, cpf, email, senha, data_nascimento):
    if not validar_nome(nome): # se na função retornar False, retorna "nome inválido."
        return "Nome inválido"

    if not validar_cpf(cpf): # se na função retornar False, retorna "CPF inválido."
        return "CPF inválido"

    if not validar_email(email): # se na função retornar False, retorna "email inválido."
        return "Email inválido"

    if not validar_senha(senha): # se na função retornar False, retorna a mensagem.
        return "A senha deve ter no mínimo 6 caracteres, 1 letra maiúscula e 1 número."

    if not validar_data_nascimento(data_nascimento):
        return "Data de nascimento inválida"

    pacientes = carregar_pacientes()

    if cpf in pacientes:
        return "CPF já cadastrado"

    for paciente in pacientes.values():
     if paciente.get("email") == email:
        return "E-mail já cadastrado"


    senha_hash = geradorHash(senha)

    dados = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha_hash,
        "data_nascimento": data_nascimento
    }

    salvar_pacientes(dados)

    return "Paciente cadastrado com sucesso"