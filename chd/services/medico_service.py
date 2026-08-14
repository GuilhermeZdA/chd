import email

from database.db_manager import carregar_medicos, salvar_medicos
from auth.auth_services import geradorHash, validar_email, validar_senha

def cadastrar_medico(nome, crm, especialidade, email, senha):
        medicos = carregar_medicos()

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

        senha_hash = geradorHash(senha)

        dados = {
            "nome": nome,
            "crm": crm,
            "especialidade": especialidade,
            "email": email,
            "senha": senha_hash
    }
        salvar_medicos(dados)

        return "Médico cadastrado com sucesso."

