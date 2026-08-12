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