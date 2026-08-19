from datetime import datetime
import auth
import database
import services

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

def cadastrar_paciente(nome, cpf, email, data_nascimento):
    if not validar_nome(nome): # se na função retornar False, retorna "nome inválido."
        return "Nome inválido"

    if not validar_cpf(cpf): # se na função retornar False, retorna "CPF inválido."
        return "CPF inválido"

    if not validar_email(email): # se na função retornar False, retorna "email inválido."
        return "Email inválido"

    if not validar_data_nascimento(data_nascimento):
        return "Data de nascimento inválida"

    pacientes = database.carregar_pacientes()
    agendamento = services.gerador_de_agendamentos_validos()

    for paciente in pacientes["pacientes"]:
        if paciente.get("cpf") == cpf:
            return "CPF já cadastrado."

        if paciente.get("email") == email:
            return "E-mail já cadastrado."
    

    dados = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "data_nascimento": data_nascimento,
        "agendamento": agendamento

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

def validar_crm(crm: str):
    if not crm:
        return False

    crm = crm.strip().upper()
    crm_limpa = crm.replace("-", "").replace(" ", "")

    if len(crm_limpa) < 3 or len(crm_limpa) > 8:
        return False
    
    lista_ufs_validas = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
    'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 
    'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    ]

    digitos = "".join(digito for digito in crm_limpa if digito.isdigit())
    uf = "".join(letra for letra in crm_limpa if letra.isalpha())

    if len(uf) > 2:
        return False
    
    if uf not in lista_ufs_validas:
        return False

    if len(digitos) + len(uf) != len(crm_limpa):
        return False
    
    return True
    
