#Exercício break
#Solicite do usuário uma senha e só finalize o programa quando a senha correta for digitada:

#senha_correta='python123'
#while True:
#    senha=input('Digite a senha:')
#    if senha_correta==senha:
#        print('Acesso liberado.')
#        break
#    else:
#        print('Senha incorreta, acesso negado.')


#5.Uma empresa que possui 100 funcionários decide dar um aumento de salário de 30% aos funcionários.
#Escreva um programa que possa ser utilizado para efetuar o aumento de salário.

#ct=0
#while ct<=5:
#    nome=input('Digite o nome do funcionário: ')
#    salario=float(input('Digite o salário do funcionário:R$'))
#    Nsal=salario+(salario*0.3)
#    print('O salário de {} com o reajuste é de R${}'.format(nome, Nsal))
#    ct+=1


#4.Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000, 
#imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).

num=int(input('Digite um número:'))
ct=0
while ct<=100000:
    num+=1000
    if num==100001:
        break
    print(num)
    ct=num+1000
