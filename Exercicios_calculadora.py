#!/usr/bin/env python
# coding: utf-8

# In[16]:



print('Exercicio Calculadora')
print('selecione o numero da operacao desejada')
print('1 - soma')
print('2 - subtracao')
print('3 - multiplicacao')
print('4 - divisão')
opcao = int(input())

# Selecionando os numeros da operação

print('Digite o primeiro numero')
x = int(input())
print('Digite o segundo numero')
y = int(input())

#Função da calculadora

def calc(x,y):
    if opcao == 1:
        resultado = (x+y)
        print('A soma entre %s + %r eh %s' %(x,y,resultado))
    elif opcao == 2:
        resultado = (x-y)
        print('A subtracao entre %s e %r eh %s'%(x,y,resultado))
    elif opcao == 3:
        resultado = (x*y)
        print('A multiplicacao entre %s e %r eh %s'%(x,y,resultado))
    elif opcao == 4:
        resultado = (x/y)
        print('A divisao entre %s e %r eh %s'%(x,y,resultado))
    else:
        print('opcao invalida')
    print('fim')

calc(x,y)

