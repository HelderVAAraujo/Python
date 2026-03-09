#Exercício Python 5: Faça um programa que leia um número Inteiro 
# e mostre na tela o seu sucessor e seu antecessor.

#num=int(input('Digite um número:'))
#ant=num-1
#suc=num+1
#print('O antecessor de {} é {}, o sucessor é {}.'.format(num, ant, suc))


#Exercício Python 6: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#n=float(input("Digite um número:"))
#D=n*2
#T=n*3
#R=n**(1/2)
#print('O dobro de {} é {}, o triplo é {}, a raiz quadrada é {}.'.format(n, D, T, R))


#Exercício Python 7: Desenvolva um programa que leia as duas notas 
#de um aluno, calcule e mostre a sua média

#nota1=float(input('Digite a primeira nota:'))
#nota2=float(input('Digite a segunda nota:'))
#print('A media das notas é:',(nota1+nota2)/2)


#Exercício Python 8: Escreva um programa que leia um valor em metros 
#e o exiba convertido em centímetros e milímetros.

#metro=float(input('Digite o valor em metros:'))
#cent=metro*100
#mili=metro*1000
#print('{} metros convertido para centímetros é {}, para milímetros é {}'.format(metro, cent, mili))

#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer
# e mostre na tela a sua tabuada.

#n=int(input('Digite um número:'))
#print('--------TABUADA-------')
#print('{}X{}={}'.format(n, 1, n*1))
#print('{}X{}={}'.format(n, 2, n*2))
#print('{}X{}={}'.format(n, 3, n*3))
#print('{}X{}={}'.format(n, 4, n*4))
#print('{}X{}={}'.format(n, 5, n*5))
#print('{}X{}={}'.format(n, 6, n*6))
#print('{}X{}={}'.format(n, 7, n*7))
#print('{}X{}={}'.format(n, 8, n*8))
#print('{}X{}={}'.format(n, 9, n*9))
#print('{}X{}={}'.format(n, 10, n*10))


#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar.

#cart=float(input('Quantos reais tem em sua carteira? R$'))
#dolar= (cart/5.72)
#print('Você pode comprar $USD {}.'.format(dolar))


#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg=float(input('Digite a largura da parede:'))
alt=float(input('Digite a altura da parede:'))
area=larg*alt
Ltinta=area/2
print('A quantidade de litros de tinta necessaria para pintar a parede é de:', Ltinta)