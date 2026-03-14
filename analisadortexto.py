# Receber frase do usuário
frase = input("Digite uma frase: ").lower()

# Separar palavras
palavras = frase.split()

# Dicionário para contar frequência
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

# Total de palavras
total_palavras = len(palavras)

# Total de palavras únicas
palavras_unicas = len(contagem)

# Palavras repetidas
repetidas = [palavra for palavra, qtd in contagem.items() if qtd > 1]

# Palavra mais frequente
palavra_mais_frequente = max(contagem, key=contagem.get)

# Relatório final
print("\nRelatório da frase")
print("----------------------")
print(f"Total de palavras: {total_palavras}")
print(f"Total de palavras únicas: {palavras_unicas}")
print(f"Palavra mais frequente: '{palavra_mais_frequente}' ({contagem[palavra_mais_frequente]} vezes)")

print("\nPalavras que se repetem:")
if repetidas:
    for palavra in repetidas:
        print(f"{palavra} ({contagem[palavra]} vezes)")
else:
    print("Nenhuma palavra repetida.")
