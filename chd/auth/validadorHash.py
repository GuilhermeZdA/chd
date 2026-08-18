from .geradorHash import gerarHash

def validarHash(senha):
    hash = "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"
    novoHash = gerarHash(senha)
    if hash == novoHash:
        return True
    else:
        return False
