print("="*10)
print("JÓ-KEN-PÔ")
print("="*10)

from random import randint
from time import sleep
#Definindo jogadores
elementos = ('Pedra', 'Papel', 'Tesoura',)
comp = randint(0, 2)
jogadas = 0
nome = str(input("Nome do Jogador: "))

# Opções de Jogada
print("Escolha a sua opção de jogada:\n"
      "[0]. Pedra\n"
      "[1]. Papel\n"
      "[2]. Tesoura\n"
      "")
escolha = int(input(f"{nome}, escolha a sua jogada: "))

#Definição de escolha dos Jogadores
print("-"*40)
print(f"O computador escolheu: {elementos[comp]}")
print(f"O jogador {nome} escolheu: {elementos[escolha]}")
print("-"*40)

print("JÓ")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print("+"*14)
#Condições do jogo
cont = 0
placarj = 0
placarc = 0
while True:
    # Comp jogou PEDRA
    if comp == 0:
        if escolha == 0:
            print(f"{nome} PEDRA x PEDRA Computador")
            print("EMPATE!")
        elif escolha == 1:
            print(f"{nome} PAPEL x PEDRA Computador")
            print(f"{nome}, Você Venceu!")
            placarj += 1
        elif escolha == 2:
            print(f"{nome}, TESOURA x PEDRA Computador")
            print(f"{nome},Você Perdeu!")
            placarc += 1
        else:
            print("Opção Inválida")
    # Comp jogou PAPEL
    elif comp == 1:
        if escolha == 0:
            print(f"{nome} PEDRA x PAPEL Computador")
            print(f"{nome}, Você Perdeu!")
            placarc += 1
        elif escolha == 1:
            print(f"{nome} PAPEL x PAPEL Computador")
            print(f"EMPATE!")
        elif escolha == 2:
            print(f"{nome} TESOURA x PAPEL Computador")
            print(f"{nome}, Você Venceu!")
            placarj += 1
        else:
            print("Opção Invalida!")
    # Comp jogou TESOURA
    elif comp == 2:
        if escolha == 0:
            print(f"{nome} PEDRA x TESOURA Computador")
            print(f"{nome}, Você Venceu!")
            placarj += 1
        elif escolha == 1:
            print(f"{nome} PAPEL x TESOURA Computador")
            print(f"{nome}, Você Perdeu!")
            placarc += 1
        elif escolha == 2:
            print(f"{nome} TESOURA x TESOURA Computador")
            print(f"EMPATE!")
        else:
            print("Opção Inválida!")
jogadas += 1

print(f"Placar Final: {nome} {placarj} X {placarc} Computador")
if placarj > placarc:
    print(f"{nome}, Você Venceu!")
elif placarj < placarc:
    print(f"{nome}, Você Perdeu!")
#else:
    #placarc = 0
    #placarj = 0
    #print("Jogo empatado!")

    if jogadas == 5:
        reposta = str(input("Deseja continuar jogando: [S/N}? ")).upper()
        if continuar == "Nn":
            print("Jogo Encerrado...Obrigado pela partida!")
        elif continuar == "Ss":
            jogadas == 0
        print("Acabou...........")
