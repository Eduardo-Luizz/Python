#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distance = float(input('Digite a distância em KM : '))

if distance <= 200 :
    custo = distance * 0.50
    print('A passagem custará R${:.2f} '.format(custo))
else:
    custo = distance * 0.45
    print('A passagem custará R${:.2f}'.format(custo))