while True:
    senha = input("Digite uma senha: ")

    # Verificações de validade
    tem_numero = any(c.isdigit() for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)

    if len(senha) < 8:
        print("❌ A senha precisa ter pelo menos 8 caracteres.\n")
    elif not tem_numero:
        print("❌ A senha precisa ter pelo menos um número.\n")
    elif not tem_maiuscula:
        print("❌ A senha precisa ter pelo menos uma letra maiúscula.\n")
    else:
        print("✅ Senha válida!\n")
        break

# Relatório de segurança
tamanho = len(senha)
letras = sum(c.isalpha() for c in senha)
numeros = sum(c.isdigit() for c in senha)
especiais = sum(not c.isalnum() for c in senha)

# Nível da senha
if 8 <= tamanho <= 9:
    nivel = "Fraca"
elif 10 <= tamanho <= 12:
    nivel = "Média"
else:
    nivel = "Forte"

print("Relatório de Segurança da Senha")
print("-------------------------------")
print(f"Tamanho da senha: {tamanho}")
print(f"Letras: {letras}")
print(f"Números: {numeros}")
print(f"Caracteres especiais: {especiais}")
print(f"Nível da senha: {nivel}")
