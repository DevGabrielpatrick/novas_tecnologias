# Estoque da loja (lista de dicionários)
estoque = [
    {"nome": "Notebook", "preco": 3500, "quantidade": 3},
    {"nome": "Mouse Gamer", "preco": 150, "quantidade": 10},
    {"nome": "Monitor", "preco": 900, "quantidade": 2},
    {"nome": "Teclado Mecânico", "preco": 450, "quantidade": 0},
    {"nome": "Headset", "preco": 300, "quantidade": 5}
]

valor_total = 0

print("Itens com valor total acima de R$500:\n")

# Percorrendo o estoque
for item in estoque:
    valor_item = item["preco"] * item["quantidade"]
    valor_total += valor_item

    if valor_item > 500:
        print(f"{item['nome']} - Valor em estoque: R${valor_item}")

print("\nValor total do estoque: R$", valor_total)

# Bônus: produtos em falta
produtos_em_falta = [item["nome"] for item in estoque if item["quantidade"] == 0]

print("\nProdutos em falta:")
print(produtos_em_falta)
