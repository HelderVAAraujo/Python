#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome=input('Digite o seu nome completo: ')

print(nome.upper())
print(nome.lower)

print(len(nome) - nome.count(' '))

print(nome.find(' '))
#OU
separar = nome.split()
print(len(separar[0]))

#Faça um programa que leia um número entre 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero=input('Digite um número entre 0 e 9999: ')
