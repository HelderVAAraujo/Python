#EXERCICIO-01
#def notas(a,b,c,d,e):
#    return (a+b+c+d+e)/5

#n1=float(input('Digite a primeira nota:'))
#n2=float(input('Digite a segunda nota:'))
#n3=float(input('Digite a terceira nota:'))
#n4=float(input('Digite a quarta nota:'))
#n5=float(input('Digite a quinta nota:'))

#m=notas(n1,n2,n3,n4,n5)
#print(f'A media das notas é igual a {m}')  

#EX-03
#def num(*numeros):
#    m=max(numeros)
#    mn=min(numeros)
#    return m, mn

#print(num(15, 23, 88, 151, 49, 2, 1 ,16, 25, 29,30))

#EX-04
#def notas(*nota):
#    s=0
#    for x in nota:
#        s=x+s
#    media=s/len(nota)
#    return media

#print(notas(12, 4, 12, 5, 16, 25, 20, 10, 15))

#Solicite ao usuário que digite 5 números e armazene-os em um array. 
#Em seguida, imprima a soma desses números.

numeros=[]
for i in range(5):
    num=int(input('Digite um número:'))
    numeros.append(num)
soma=0
for i in numeros:
    soma+=i
print('A soma dos números é:',soma)

