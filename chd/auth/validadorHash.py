import auth
import services

def validarHash(senha):
    cpf = str(input("Digite seu CPF: "))
    dados = services.buscarFuncionario(cpf)
    hash = dados["senha"]
    
    novoHash = auth.gerarHash(senha)

    if hash == novoHash:
        return True
    else:
        return False
