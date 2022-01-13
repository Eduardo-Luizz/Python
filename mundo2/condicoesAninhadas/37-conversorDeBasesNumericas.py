#Escreva um programa em Python que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

number = int(input('Digite um número qualquer : '))

print(''' 
          Seja bem vindo ! 
          Sou seu conversor de bases
          Escolha uma das opções para que eu possa converter :
          1 Binário
          2 Octal
          3 Hexadecimal \n ''')

option = int(input('Digite um número : '))

if option == 1 :
    print('O número digitado foi {} convertido para binário fica {} '.format(number, bin(number)[2:]))
elif option == 2 :
    print('O número digitado foi {} convertido para octal fica {} '.format(number, oct(number)[2:]))
elif option == 3:
    print('O número digitado foi {} convertido para hexadecimal fica {} '.format(number, hex(number)[2:]))