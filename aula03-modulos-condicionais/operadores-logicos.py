# logica e (and)

verifica_email = True
verifica_senha = True

verifica_login = verifica_email and verifica_senha
print(verifica_login)

#logica ou (or)
logica_ou = False or False or True
print(logica_ou)

#not
negacao = not True
print(negacao)
if not verifica_login:
    print("loga certo ai...")
else:
    print("entra no programa")