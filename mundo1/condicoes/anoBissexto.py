# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

print('\n')
print('Programa identificador de anos bissextos ! ')
print('\n')

print('= ' * 20 )
print('Qual ano deseja identificar ? Digite 0 caso queira verificar o ano atual : ')
print('= ' * 20 )
print('\n')

ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
