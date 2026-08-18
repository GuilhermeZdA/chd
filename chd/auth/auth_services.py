from datetime import datetime
import auth
import database

def validar_cpf(cpf: str) -> bool:

    cpf = "".join(filter(str.isdigit, cpf))

    if not cpf or len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    decimo_digito = sum(int(x) * y for x, y in zip(cpf[:9], range(10, 1, -1)))
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
    
    if not all(caractere.isalpha() or caractere.isspace() for caractere in nome): # verifica se o nome é composto apenas por letras.
        return False

    return True

def validar_email(email: str) -> bool:
    email = email.strip() # remove espaços antes e depois do email

    if not email: #se email estiver vazio, devolve False
        return False

    if "@" not in email: # Retorna False se não tiver @ no email.
        return False

    if "." not in email.split("@")[-1]: # Retorna False se não tiver "." após o "@"
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

def validar_data_nascimento(data_nascimento: str) -> bool: # função para certificar se a data é possível.
    try:
        datetime.strptime(data_nascimento, "%d%m%Y")
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

    pacientes = database.carregar_pacientes()

    for paciente in pacientes["pacientes"]:
        if paciente.get("cpf") == cpf:
            return "CPF já cadastrado."

        if paciente.get("email") == email:
            return "E-mail já cadastrado."

    senha_hash = auth.gerarHash(senha)

    dados = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha_hash,
        "data_nascimento": data_nascimento
    }

    database.salvar_pacientes(dados)

    return "Paciente cadastrado com sucesso"


def cadastrar_medico(nome, crm, especialidade, email, senha):
        medicos = database.carregar_medicos()

        for medico in medicos["medicos"]:
            if medico.get("crm") == crm:
             return "CRM já cadastrado"

        for medico in medicos["medicos"]:
            if medico.get("email") == email:
                return "E-mail já cadastrado"
            
        if not validar_email(email):
            return "E-mail inválido"

        if not validar_senha(senha):
            return "Senha inválida"

        senha_hash = auth.gerarHash(senha)

        dados = {
            "nome": nome,
            "crm": crm,
            "especialidade": especialidade,
            "email": email,
            "senha": senha_hash
    }
        database.salvar_medicos(dados)

        return "Médico cadastrado com sucesso."
