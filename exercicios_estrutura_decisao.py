# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:28:44 2019

@author: 93352774
"""

#Exercicio 1 - Faça um Programa que peça dois números e imprima o maior deles.

      def maiorNum ():
        lista = []
        qtd = input("Digite a quantidade de números ")
        for i in range(0,int(qtd)): 
          lista.append(int(input('Digite o número: ')))
        print ('Maior número da lista: ', max(lista)) 
        
        maiorNum ()
  
#Exercicio 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
        
        def condicao ():
          numero = int(input("escreva um numero "))
          if (numero) >= 0: 
             print("positivo") 
          else:
            print("negativo")
                          
        condicao()
        
#Exercicio 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
        
        def condicao2 ():
          letra = input("escreva uma letra ")
          if (letra) == "F": 
             print("Feminio") 
          elif (letra) == "M":
            print("Masculino")
          else:
            print("indefinido")
                          
        condicao2()
        
#Exercicio 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
        
      def vogal ():
        lista = (["a" , "e" , "i" , "o" , "u"])
        ehVogal = input("Digite uma letra ")
        if (ehVogal) in lista: 
            print("é vogal")
        else:
            print("é consoante")
        
        vogal ()
        
#Exercicio 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
        #A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        #A mensagem "Reprovado", se a média for menor do que sete
        #A mensagem "Aprovado com Distinção", se a média for igual a dez.
        
        def passaAno ():
          nota1 = float(input("Digite a primeira nota "))
          nota2 = float(input("Digite a segunda nota "))
          media = (nota1 + nota2) /2
          if (media) == 10:
            print("Aprovado com Distinção")
          elif (media) < 7:
            print("Reprovado")
          elif (media) >= 7:
            print("Aprovado")
         
            
          passaAno ()
          
#Exercicio 6 - Faça um Programa que leia três números e mostre o maior deles.
          
          def maiorNum ():
            lista = []
            qtd = input("Digite a quantidade de números ")
            for i in range(0,int(qtd)): 
              lista.append(int(input('Digite o número: ')))
              print ('Maior número da lista: ', max(lista)) 
        
        maiorNum ()
        
#Exercicio 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
        
            def maiorMenorNum ():
              lista = []
              qtd = input("Digite a quantidade de números ")
              for i in range(0,int(qtd)): 
                lista.append(int(input('Digite o número: ')))
                print ('Maior número da lista: ', max(lista))
                print ('Menor número da lista: ', min(lista)) 
        
        maiorMenorNum ()
              
        
#teste flamengo x botafogo

      def classico ():
        fla = int(input("Digite o numero de gols do Flamengo "))
        Bota = int(input("Digite o numero de gols do Botafogo "))
        if (fla > Bota):
          print("Flamengo campeão")
        elif (Bota > fla):
          print("Botafogo campeão")
        else:
          print("Empate")
          
        var = input("Teve intervenção do VAR? ")
        if (var == "sim"):
          print("Flamengo campeão")
        else:
          print("Botafogo campeão")
          
        classico ()
        
            
  
#Exercicio 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

        def produto ():
          produto1 = float(input("Digite o preço do produto 1 "))
          produto2 = float(input("Digite o preço do produto 2 "))
          produto3 = float(input("Digite o preço do produto 3 "))
          
          menor = produto1
          
          if (produto2 < menor):
            menor = produto2
          if (produto3 < menor):
            menor = produto3
            
          print("O menor preço é:", menor)
          
          produto()
          
#Exercicio 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
          
        def crescenteLista ():
          numeroLista = ([2 , 5 , 3 , 9 , 20 , 10])
          crescente = sorted(numeroLista)
          print(crescente)
          
          crescenteLista ()
          
        def descescente ():
          numeroLista = ([2 , 5 , 3 , 9 , 20 , 10])
          decrescente = sorted(numeroLista, reverse=True)
          print(decrescente)
          
         descescente ()
         
#Exercicio 10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
         
         def turnoEstudo ():
           turno = input("Em qual turno vc estuda? ")
           if (turno == "M"):
             print("bom dia")
           elif(turno == "T"):
             print("boa tarde")
           elif(turno == "N"):
             print("boa noite")
           else:
             print("valor inválido")
            
          turnoEstudo ()
          
 #Exercicio 11 - Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:         
 
     #a) salários até R$ 280,00 (incluindo) : aumento de 20%
     
       def salario_a ():
         salario = float(input("Digite o seu salário "))
         reajuste = (salario * 20/100)
         if (salario <= 280):
           print("O seu aumento é de", reajuste)
         else:
           print("você não terá reajuste")
        
        salario_a ()
        
        
     #b) salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
     
     def salario_b ():
         salario = float(input("Digite o seu salário "))
         reajuste = (salario * 15/100)
         if (salario <= 700 or salario <= 280):
           print("O seu aumento é de", reajuste, "R$")
         else:
           print("você não terá reajuste")
        
        salario_b ()
        
     
     #c) salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
     
     def salario_c ():
         salario = float(input("Digite o seu salário "))
         reajuste = (salario * 10/100)
         if (salario <= 1500 or salario <= 700 ):
           print("O seu aumento é de", reajuste, "R$")
         else:
           print("você não terá reajuste")
        
        salario_c ()
     
     #d) salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
     
     def salario_d ():
         salario = float(input("Digite o seu salário "))
         reajuste = (salario * 5/100)
         if (salario >= 1500):
           print("O seu aumento é de", reajuste, "R$")
         else:
           print("você não terá reajuste")
                  
        salario_d ()
     
     
     #e) o salário antes do reajuste;
     
      def salario_e ():
         salario = float(input("Digite o seu salário "))
         reajuste = (salario * 5/100)
         print("o seu reajuste é", reajuste, "R$")
         sem_reajuste = (salario - reajuste)
         print("o seu salário sem reajuste é", sem_reajuste, "R$")
         
         salario_e ()
     
     #f) o percentual de aumento aplicado;
     def salario_f ():
         salario = float(input("Digite o seu salário "))
         reajuste = (salario * 5/100)
         reajuste2 = (5/100*100)
         print("o seu reajuste é de", reajuste2, "%")
                 
         salario_f ()
     
     
  