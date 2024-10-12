import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa variáveis
tentativas = 0
adivinhar = True

print("Bem-vindo ao jogo de adivinhação!")
print("Eu escolhi um número entre 1 e 100.")
print("Tente adivinhar qual é o número.")

# Loop principal do jogo
while adivinhar:
    # Pede ao usuário para adivinhar o número
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    # Estruturas condicionais para verificar o palpite
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativas} tentativas.")
        adivinhar = False

# Mensagem de fim de jogo
print("Fim do jogo. Obrigado por jogar!")
