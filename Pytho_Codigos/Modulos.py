#import math
#num = float(input('Digite um número:'))
#raiz= math.sqrt(num)
#print('A raiz quadrada de {} é {}'.format(num, raiz))

#num  =float(input('Digite um número:'))
#x=int(num)
#print('A parte inteira de {} é {}'.format(num, x))

#import math
#a=float(input('Digite o comprimento do lado do triângulo(cateto):'))
#b=float(input('Digite o comprimento do lado do triângulo(cateto):'))
#h=math.sqrt((a**2) + (b**2))
#print('A hipotenusa vale:',h)

#import math
#ang=float(input('Digite um ângulo para o calculo:'))
#seno=math.sin(ang)
#cos=math.cos(ang)
#tan=math.tan(ang)
#print(f'Seno de {ang}, é igual a: {seno}\nCosseno de {ang} é a: {cos}\nTangente de {ang} é igual a: {tan}')


import random           #{Algoritimo para sortear um elemento em um array}
alunos=[]               #{Lista onde sera alocados os elementos}
cont=0                  #{Contador para finalizar o programa}

while cont < 5:         #{Controlador de execução}
    aluno=str(input("Digite o nome do aluno"))      
    alunos.append(aluno)                            #{Inserção de elementos}
    cont +=1
escolido=random.choice(alunos)                
print(f'O aluno escolido foi:{escolido}')

import random
alunos=[]
conte=0

while conte < 5:
    aluno=str(input('Digite o nome do aluno: '))
    alunos.append(aluno)
    conte +=1
    
random.shuffle(alunos)
print(alunos)

