from hashlib import sha256

def geradorHash(senha):
    """Função que gera um hash com base em uma string
    encode('utf-8') - transforma uma string em bytes
    sha256 cria um objeto hash
    hexdigest() transforma o objeto em uma string hexadecimal"""

    hash = sha256(senha.encode('utf-8')).hexdigest()
    return hash
