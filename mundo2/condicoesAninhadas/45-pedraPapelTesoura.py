#Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time

print('Olá bora jogar pedra,papel,tesoura ? ')
print('''
    Suas opções:
    [1] Pedra
    [2] Papel
    [3] Tesoura ''')
print('Qual a sua escolha ?')
itens = ['pedra', 'papel', 'tesoura']
player = int(input('Digite : '))
computador = random.randint(1,3)

time.sleep(1)
print('JO')
time.sleep(2)
print('KEN')
time.sleep(2)
print('PO')

if computador == 1 : # computador jogou pedra
    if player == 1 :
        print('Empate')
    elif player == 2 :
        print('Jogador vence')
    elif player == 3 :
        print('Computador vence')
    else :
        print('Jogado inválida')
elif computador == 2 : # computador jogou papel
    if player == 1 :
        print('Computador vence')
    elif player == 2 :
        print('Empate')
    elif player == 3 :
        print('Jogador vence')
    else :
        print('Jogado inválida')
elif computador == 3 : # computador jogou tesoura
    if player == 1 :
        print('Jogador vence')
    elif player == 2 :
        print('Computador vence')
    elif player == 3 :
        print('Empate')
    else :
        print('Jogado inválida')

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[player]))