from database.db_manager import carregar_medicos, salvar_medicos
from auth.auth_services import validar_email, validar_nome

def cadastrar_medico(nome, crm, email):
        if not validar_nome(nome):
         return "Nome inválido"
        
        medicos = carregar_medicos()

        if crm in medicos:
            return "CRM já cadastrado"

        for medico in medicos.values():
            if medico.get("email") == email:
                return "E-mail já cadastrado"
            
        if not validar_email(email):
            return "E-mail inválido"

       

        dados = {
            "nome": nome,
            "crm": crm,
            "email": email,
    }
        salvar_medicos(dados)

        return "Médico cadastrado com sucesso."

