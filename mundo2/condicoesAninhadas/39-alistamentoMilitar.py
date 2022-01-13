#Faça um programa que leia o ano de nascimento de um jovem 
# e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar 
# ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNasc = int(input('Qual o seu ano de nascimento ? '))

# descobrir idade
idade = date.today().year - anoNasc 
#ano atual 
anoAtual = date.today().year

if idade < 18 :
    #anos que faltam 
    anos = 18 - idade
    #ano que vai ser o alistamento
    ano = anoAtual + anos
    print('Você ainda não pode se alistar, tem {} anos.'.format(idade))
    print('Poderá se alistar com {} anos.'.format(anos + idade))
    print('E seu alistamento será no ano de {} '.format(ano + idade))

elif idade > 18 :
    #anos que passaram
    anos = idade - 18
    #ano que era o alistamento
    ano = anoAtual - anos
    print('Você já passou da idade para se alistar, ORGANIZE SUA SITUAÇÃO MILITAR!')
    print('Já passou a hora de se alistar em {} anos.'.format(anos))
    print('O alistamento era no ano de {} '.format(ano))

elif idade == 18 :
    print('Está na hora de contribuir com o seu país, ALISTE-SE!')
