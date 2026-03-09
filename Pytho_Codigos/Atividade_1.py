#1.Peça um número e verifique se ele está entre 1 e 100 (inclusive).

num=int(input('Digite um número:'))
if (num>=1) and (num<=100):
    print('o número digitado está entre 1 e 100.')
else:
    print('o número digitado não está entre 1 e 100.')


#2.Peça a idade de uma pessoa. Se ela tiver 18 anos ou mais, exiba: 
# “Você é maior de idade.” Caso contrário, diga quantos anos faltam para ela atingir a maioridade.

idade=int(input('Digite sua idade:'))
if idade>=18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade. Faltam:', 18-idade,'anos para atingir a maior idade.')


#3.Peça uma nota de 0 a 10 e, com base na nota, 
#exiba "Aprovado" se a nota for maior ou igual a 7, ou "Reprovado" se a nota for menor que 7.

nota=float(input('Digite uma nota entre 0 e 10:'))
if nota>=7:
    print('Aprovado!')
else:
    print('Reprovado!')


#4.Solicite um número ao usuário e, com base no valor, 
#classifique-o como "Positivo", "Negativo" ou "Zero".

num=int(input('Digite um número:'))
if num>0:
    print('POSITIVO!')
elif num<0:
    print('NEGATIVO!')
else:
    print('ZERO!')


#5.Peça um número ao usuário e diga se ele é múltiplo de 2, de 3 ou de ambos.

num=int(input('Digite um número:'))
if (num%2==0) and (num%3==0):
    print('Multiplo de 2 e 3.')
elif num%2==0:
    print('Multiplo de 2.')
elif num%3==0:
    print('Multiplo de 3.')
else:
    print('Não é multiplo de 2 e 3')


#6.Peça o valor da compra e o cupom: 
#se o usuário digitar o cupom “DESCONTO10”, aplique 10% de desconto no total.

comp=float(input('Digite o valor da compra:'))
cup=input('Adicione o cupom de desconto:')
if cup=='DESCONTO10':
    valor=comp-(comp*(10/100))
    print('A sua compra ficou no valor de:R$',valor)
else:
    print('A sua compra ficou no valor de:R$',comp)


#7.Solicite a idade e classifique como: Criança (0-12); Adolescente (13-17); Adulto (18-59); Idoso (60+)

idade=int(input('Digite a idade:'))
if idade<=12:
    print('Criança!')
elif (idade>=13) and (idade<=17):
    print('Adolescente!')
elif (idade>=18) and (idade<60):
    print('Adulto!')
else:
    print('Idoso!')


#8.Calculadora de IMC: Peça o peso (kg) e altura (m), calcule o IMC e informe a faixa:
# Abaixo do peso (<18.5); Peso normal (18.5–24.9); Sobrepeso (25–29.9); Obesidade (30+)

peso=float(input('Digite o seu peso Kg:'))
altura=float(input('Digite a sua altura:'))
IMC= peso/(altura**2)
if IMC<18.5:
    print('Abaixo do peso!')
elif (IMC>=18.5) and (IMC<25):
    print("Peso ideal!")
elif (IMC>=25) and (IMC<30):
    print('Sobrepeso!')
else:
    print('Obesidade!')