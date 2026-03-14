# Constantes
NUMERO_SECRETO = 42
MAX_TENTATIVAS = 5

tentativa = 1

print("Adivinhe o número \n Ele está entre 0 e 100;")

while tentativa <= MAX_TENTATIVAS:
    chute = int(input(f"Tentativa {tentativa}/{MAX_TENTATIVAS}: "))

    if chute == NUMERO_SECRETO:
        print("Correto! Você acertou o número!")
        break
    elif chute < NUMERO_SECRETO:
        print("Muito baixo! Tente maior.")
    else:
        print("Muito alto! Tente menor.")

    tentativa += 1

if tentativa > MAX_TENTATIVAS:
    print("Você perdeu! O número secreto era 42.")
