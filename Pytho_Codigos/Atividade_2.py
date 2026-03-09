#Exercícios while
#1.Imprimir números de 0 até 1000

i=0
while i<1000:
    print(i)
    i+=1

#2.Leia um número (n) e imprima os números entre n e 100

n=float(input('Digite um número:'))
ct=0
while ct<=100:
    print(n)
    n+=1
    ct=n

#3.Faça um programa que imprime os números 10 a 0 (ordem decrescente): 10,9,8,7,6,5,4,3,2,1,0

i=10
while i>=0:
    print(i)
    i-=1

i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i)
print('=========')

#Exercício continue
#Faça um programa em Python que imprime os números pares entre 0 a 20 use while e continue

ct=0
while ct<20:
    ct+=1
    if ct%2==1:
        continue
    print(ct)

#Tentativas limitadas para acertar uma senha

senhaCorreta='AvanteVingadores'
tent=3
while tent>0:
    senha=input('Digite a senha:')
    if senha==senhaCorreta:
        print('Acesso liberado.')
        break
    tent-=1
    print('Senha incorreta. Você tem {} tentativas.'.format(tent))
else:
    print('Tentativas esgotadas. Acesso bloqueado.')
