def limpar_dados(lista):

    #criando o filtro (lambda + filter)
    filtro = filter(lambda status: status.get("status_ativo") == True, lista)


#Normalize com loop Nomes em maiúsculas (.upper()) e e-mails em minúsculas (.lower()) 
   
def limpar_dados(lista):
    filtro = filter(lambda u: u.get("status_ativo"), lista)

    normalizados = []

    for usuario in filtro:
        usuario_padronizado = {
            "nome": usuario.get("nome", "").upper(),
            "email": usuario.get("email", "").lower(),
            "status_ativo": True
        }
        normalizados.append(usuario_padronizado)

    return normalizados

usuarios = [
    {"nome": "Gabriel", "email": "GABRIEL@EMAIL.COM", "status_ativo": True},
    {"nome": "Ana", "email": "ANA@email.com", "status_ativo": False},
    {"nome": "Carlos", "email": "Carlos@Email.Com", "status_ativo": True},
    {"nome": "Mariana", "email": "MARIANA@EMAIL.COM", "status_ativo": True},
    {"nome": "João", "email": "joao@email.com", "status_ativo": False},
    {"nome": "Fernanda", "email": "Fernanda@Email.Com", "status_ativo": True},
    {"nome": "Lucas", "email": "LUCAS@EMAIL.COM", "status_ativo": False},
    {"nome": "Beatriz", "email": "beatriz@email.com", "status_ativo": True}
]

resultado = limpar_dados(usuarios)


#função para imprimir um dicionario de resultado de cada vez
contagem = len(resultado)

for i in range(contagem):
    print(resultado[i]/n)


#entendendo o lambda
#lambda parametro:expressão

#exemplo:

#def somar(x,y):
    #return x + y

#print(somar(1,2))

#somar = lambda x,y : x + y
#print(somar(5,2))

