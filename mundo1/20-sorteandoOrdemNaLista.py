#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
aluno1 = str(input('Nome do aluno: '))
aluno2 = str(input('Nome do aluno: '))
aluno3 = str(input('Nome do aluno: '))
aluno4 = str(input('Nome do aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação será : ')
print(lista)
