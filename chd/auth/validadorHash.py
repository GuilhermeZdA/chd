import auth
import services

def validarHash(senha, crm):
    dados = services.buscarFuncionario(crm)
    if dados == None:
        return False
    hash = dados["senha"]
    novoHash = auth.gerarHash(senha)

    if hash == novoHash:
        return True
    else:
        return False
