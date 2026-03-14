def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc_oficial(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III (mórbida)"

# Exibindo a tabela oficial de classificação do IMC (OMS)
print("\nTabela oficial de classificação do IMC (OMS):")
print("-----------------------------------------------------")
print("| Faixa de IMC          | Classificação               |")
print("-----------------------------------------------------")
print("| Menos de 18.5         | Abaixo do peso              |")
print("| Entre 18.5 e 24.9     | Peso normal                 |")
print("| Entre 25.0 e 29.9     | Sobrepeso                   |")
print("| Entre 30.0 e 34.9     | Obesidade grau I            |")
print("| Entre 35.0 e 39.9     | Obesidade grau II           |")
print("| Acima de 40.0         | Obesidade grau III (mórbida)|")
print("-----------------------------------------------------\n")

# Entrada de dados
nome = input("Digite seu nome: ")
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
genero = input("Digite o seu gênero (masculino/feminino): ").lower()

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Classificação do IMC
classificacao_oficial = classificar_imc_oficial(imc)

# Resultado
print(f"\nOlá, {nome}!")
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação oficial (OMS): {classificacao_oficial}")
