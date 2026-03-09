#x=int(input('Digite um número'))
#if x>0:
#    print('POSITIVO')

#x=int(input('Digite um número'))
#if (x%2==0):
#    print('PAR')
#elif (x%2==1):
#    print('ÍMPAR')

#num1= int(input('Digite um número:'))
#num2= int(input('Digite um número:'))
#if num1>num2:
#    print("{} é o maior!".format(num1))
#elif num2>num1:
#    print('{} é o maior!'.format(num2))
#else:
#    print('São iguais!')

#x=int(input("Digite um número:"))
#if (x%3==0) and (x%5==0):
#    print("É divisivel por 3 e 5.")
#else:
#    print('Não é divisivel por 3 e por 5.')

#i=1
#while i<6:
#    print(i)
#    i+=1
#print('________')

#i=0
#while i<=1000:
#    print(i)
#    i+=1

#n=int(input('Digite um número:'))
#while n<=100:
#    print(n)
#    n+=1

#i=10
#while i>=0:
#    print(i)
#    i-=1

#i=1
#while i<6:
#    print(i)
#    if i==3:
#        break
#    i+=1

#num_secrt=7
#while True:
#    palp=int(input('Digite um número entre 0 e 10'))
#    if palp == num_secrt:
#        print('Parabéns, você acertou.')
#        break
#    else:
#        print('Tente outra vez!')

nota=float(input('Digite a nota do aluno:'))
if (nota>=9):
    print('Aprovado, conceito A!')
elif (nota>=7) and (nota < 9):
    print('Aprovado, conceito B!')
elif (nota>=5) and (nota<7):
    print('Reprovado, conceito C')
else:
    print('Reprovado, conceito D!')

#nome=input('Digite o seu nome')
#print(nome.capitalize())

usuario=input('Digite o seu usuário para verificação:')
use='hvaa'
#useC=usuario.casefold()
print(usuario.casefold())
while True:
    if use == usuario.casefold():
        print('Usuário invalido. Altere para prosseguir.')
        usuario=input('Digite o seu usuário para verificação:')
    else:
        print('Usuário aceito.')
        break

#1
nome=input('Digite o seu nome:')
print(nome.capitalize())

#2
usuario=input('Informe usuário para verificação:')
while True:
    use='hvaa'
    if use==usuario.casefold():
        print('Usuário invalido!')
        #print(usuario.casefold())
        usuario=input('Informe usuário para verificação:')
    else:
        print('Usuario valido.')
        break

#3
titulo=input('Digite o titulo:')
print('===================================================')
print(titulo.center(50))
print('===================================================')


#4
TXT=input('Digite uma comentario:')
print(TXT.count('ótimo'))

#5
#arq=input('Digite o nome do arquivo')
#if arq.endswith('.pdf'):
#    print('arquivo aceito.')
#else:
#    print('Formatodo arquivo não aceito!')


#6
#email=input('Digite o seu o e-mail:')
#a=email.find('@')
#print(a)
#print('Usuario:',email[:a])


#7
#nome=input('Digite o seu nome:')
#pedido=input('Informe o seu pedido:')
#print('Olá {}, seu pedido {} está pronto para retirada.'.format(nome,pedido))

#8

#9
#use=input('Informe o usuário:')
#verfic=use.isalnum()
#if verfic == True:
#    print('Usuário correto.')
#else:
#    print('Usuário incorreto.')

#10
#nome=input('Digite o seu nome:')
#while True:
#    vdd=nome.isalpha()
#    if vdd == True:
#        print('Correto')
#        break
#    else:
#        print('Incorreto! Preencha o campo apenas com letras.')
#        nome=input('Digite o seu nome:')

#11
#numCart=(input('Digite o número do cartão:'))
#while True:
#    vdd=numCart.isdigit()
#    if vdd == True:
#        print('Correto')
#        break
#    else:
#        print('Incorreto! Preencha o campo apenas com números.')
#        numCart=input('Digite o número do cartão:')

#12
#senha=input('Digite a senha:')
#while True:
#    s=senha.islower()
#    if s == True:
#        print('Para uma senha mais segura adicione letras maiusculas!')
#        senha=input('Digite a senha:')
#    else:
#        print('Senha aceita.')
#        break

#13
#txt=input('Comentario:') 
#xt=txt.isupper()
#if xt==True:
#    print('Sem gritos no chat!!!')

#14
#EMAILS=[]
#while True:
#    email=input('Digite o seu o e-mail:')
#    if email=='FIM':
#        break
#    else:
#        txt=email.lower()
#        EMAILS.append(txt)
#print(EMAILS)

#15
nomes=input('Digite os nomes:')
txt=nomes.split(',')
print(txt)

#def saldacao():
#    print('Bem vindo!')

#saldacao()


#def soma(a,b):
#    return a+b

#resultado=soma(10,5)
#print('Resultado:',resultado)


#def boa_vindas(pessoa='Usuario'):
#    print(f'Olá {pessoa}, bem vindo!')

#boa_vindas('Kakashi')
#boa_vindas()


#def compra(valor,pagamento):
#    if pagamento == 0:
#        r=valor
#        return r #'Total da compra R$', r
#    elif pagamento == 1:
#        r=valor+(valor*(5/100))
#        return r #'Total da compra R$', r

#print('Menu de compra:\n0 - para compra avista.\n1 - para compra a prazo.')
#op=int(input('Digite a opção:'))
#val=float(input('Digite o valor da compra:R$'))

#compra(val,op)


#def operacoes_matematica(a,b):
#    soma=a+b
#    sub=a-b
#    mult=a*b
#    if b!=0:
#        div=a/b
#    else:
#        div=None
#    return soma, sub, mult, div

#n1=float(input('Digite um número para as operações:'))
#n2=float(input('Digite um número para as operações:'))

#x,y,z,w=operacoes_matematica(n1,n2)
#print(f'Soma {x}\n Subtração {y}\n Multiplicação {z}')
#if w is not None:
#    print(f'Divisão {w}')
#else:
#    print('Não foi possivel realizar a divisão!')


#def maior(a,b):
#    return max(a,b)

#def menor(a,b):
#    return min(a,b)

#def media(a,b):
#    R=(a+b)/2
#    return R

#while True:
#    print('1-para maior número\n2-para menor número\n3-para media\n0-SAIR')
#    opcao=int(input('Digite a apção:'))
#    if opcao==1:
#        n1=float(input('digite um número:'))
#        n2=float(input('digite um número:'))
#        print('O maior número é:',maior(n1,n2))
#    elif opcao==2:
#        n1=float(input('digite um número:'))
#        n2=float(input('digite um número:'))
#        print('O menor número é:',menor(n1,n2))
#    elif opcao==3:
#        n1=float(input('digite um número:'))
#        n2=float(input('digite um número:'))
#        print('A media é:',media(n1,n2))
#    elif opcao==0:
#        break

#def analizador_de_numeros(x,y):
#    maior=max(x,y)
#    menor=min(x,y)
#    media=(x+y)/2
#    return maior, menor, media

#n1=float(input('digite um número:'))
#n2=float(input('digite um número:'))

#m, n, s=analizador_de_numeros(n1,n2)
#print(f'O maior número{m}\nO menor número {n}\nA media{s}')


#def exibir_nomes(nomes):
#    for nome in nomes:
#        print(nome)

#lista=['Kakashi','Naruto','Sakura','Sasuke']
#exibir_nomes(lista)

def soma_numeros(*numeros):
    return sum(numeros)

print(soma_numeros(1, 5, 8, 99, 12, 5, 9))

