import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        chute = input("Tente adivinhar o número entre 1 e 100 (ou digite 'sair' para encerrar): ")

        if chute.lower() == 'sair':
            print("Jogo encerrado. O número secreto era", numero_secreto)
            break

        try:
            chute = int(chute)
            tentativas += 1

            if chute < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            elif chute > numero_secreto:
                print("Muito alto! Tente um número menor.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, insira um número válido ou 'sair' para encerrar o jogo.")

jogo_adivinhacao()
