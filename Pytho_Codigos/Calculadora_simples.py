#Exercício
#Calculadora simples (usando match):
#Crie um programa em Python que funcione como uma calculadora básica. 
#O usuário deve informar dois números e uma operação (+ - * /). 
#O programa deve usar match para identificar a operação e exibir o resultado.

x=float(input('Digite o primeiro número:'))
y=float(input('Digite o segundo número:'))
op=input('Escolha a operação: ( + - * / )')
match op:
    case '+':
        R=x+y
    case '-':
        R=x-y
    case '*':
        R=x*y
    case '/':
        R=x/y
    case _:
        print('Operação invalida!!!')
print('O resultado é igual a:',R)