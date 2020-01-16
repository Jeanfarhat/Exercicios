# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#Exercicio 1 - Faça um Programa que mostre a mensagem "Alô mundo" na tela.

    x = "Alô mundo"
    print(x)

#Exercicio 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

    def numero ():
        x = int(input("digite um numero "))
        print("o numero informado foi ")
        print(x) 
        
     numero ()

#Exercicio 3 - fazer um programa que imprima a soma de 2 numeros

    def exercicio3 ():
        x = int(input("digite o primeiro numero: "))
        y = int(input("digite o segundo numero: "))
        return x + y
    
    exercicio3 ()
        
#Exercicio 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
        
    def media_oficial ():
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        nota3 = float(input("digite a terceira nota: "))
        nota4 = float(input("digite a quarta nota: "))
        media = ((nota1 + nota2 + nota3 + nota4)/4)
        print(media)
        
      media_oficial ()
       
        
#Exercicio 5 - Faça um Programa que converta metros para centímetros.
      
      def converteMetro ():
          metro = float(input("digite o valor em metros"))
          formulacm = (metro/0.01)
          print(formulacm)
          
          converteMetro ()
    
#Exercício 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.       

    
    def area_circulo ():
        raio = float(input("digite o valor do raio "))
        formulaarea = (3.14 * raio**2)
        print(formulaarea)
        
        area_circulo ()
        
#Exercicio 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

    def areaQuadrado ():
        base = float(input("valor da base do quadrado"))
        altura = float(input("valor da altura do quadrado"))
        area = ((base * altura)/2)
        print(area*2)
        
        areaQuadrado ()
        
#Exercicio 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
        
        def salarioMes ():
            valorHora = float(input("Informe quanto R$ vc ganha por hora? "))
            horasMes = int(input("informe o total de horas trabalhados no referido mês "))
            salario = (valorHora * horasMes)
            print(salario)
            
            salarioMes ()
            
#Exercicio 9 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
            
            def converteCelcius ():
                F = float(input("Informe o valor em Farenheit "))
                conversao = (5 * (F-32) / 9)
                print(conversao)
                
                converteCelcius ()

#Exercicio 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.                
                
                def converteFar ():
                    C = float(input("informe o valor em celcius "))
                    conversao = (C * 9/5) + 32
                    print(conversao)
                    
                    converteFar ()
#Exercicio 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
                    
                    #A) o produto do dobro do primeiro com metade do segundo .
                    
                        num1 = int(input("digite o primeiro numero inteiro "))
                        num2 = int(input("digite o segundo numero inteiro "))
                     
                   
                    def letraA ():
                        respostaA = (num1*2) + (num2/2)
                        print(respostaA)
                        
                        letraA ()
                    
                    #B) a soma do triplo do primeiro com o terceiro.
                    
                    def letraB ():
                        num1 = int(input("digite o primeiro numero inteiro "))
                        num3 = float(input("digite um numero real "))
                        respostaB = (num1*3) + num3
                        print(respostaB)
                        
                        letraB ()
                    
                    #C) o terceiro elevado ao cubo.
                    
                    def letraC ():
                        num3 = float(input("digite um numero real "))
                        respostaC = num3**3
                        print(respostaC)
                        
                        letraC ()
        
#Exercicio 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
                    
                    def pesoideal ():
                        altura = float(input("digite sua altura "))
                        formula = (72.7*altura) - 58
                        print(formula)
                        
                        pesoideal ()
                        
#Exercicio 13 - praticamente identico ao 12
                        
#Exercicio 14 - Texto muito longo. Olhar no site: https://wiki.python.org.br/EstruturaSequencial
                        
                        def joaopescador ():
                          variavelPeso = int(input("Digite a quantidade de quilos da pesca "))
                          variavelMulta = 4
                          if (variavelPeso) > 20: 
                            variavelExcesso = variavelPeso - 20 
                            print("Sua multa é de") 
                            print(variavelExcesso * variavelMulta)
                          else:
                            print("Parabéns, Jony. Não haverá multa!")
                          
                                                   
                        joaopescador ()    

#Exercicio 15 - Texto muito longo. Olhar no site: https://wiki.python.org.br/EstruturaSequencial

                IR = 11
                INSS = 8
                sindicato = 5

                #A) salário bruto
                def salarioBruto ():
                  valorHora = float(input("Informe quanto R$ vc ganha por hora? "))
                  horasMes = int(input("informe o total de horas trabalhados no referido mês "))
                  Bruto = (valorHora * horasMes)
                  print("Seu salario bruto é: ")
                  print(Bruto)
                  
                  salarioBruto ()
                

                #B) quanto pagou ao INSS   
                
                def descontoINSS ():
                  valorHora = int(input("Informe quanto R$ vc ganha por hora? "))
                  horasMes = int(input("informe o total de horas trabalhados no referido mês "))
                  Bruto = (valorHora * horasMes)
                  INSS = 8
                  desconto = (INSS * Bruto) /100
                  print("seu desconto do INSS é:")
                  print(desconto)
                  
                  descontoINSS ()
                  
                  

                #C) quanto pagou ao sindicato
                
                def descontoSindicato ():
                  valorHora = float(input("Informe quanto R$ vc ganha por hora? "))
                  horasMes = int(input("informe o total de horas trabalhados no referido mês "))
                  Bruto = (valorHora * horasMes)
                  sindicato = 5
                  descontoSindicato = (sindicato * Bruto) / 100
                  print("seu desconto do sindiato é:")
                  print(descontoSindicato)
                  
                  descontoSindicato ()
                  

                #D) o salário líquido. Salário Bruto - Descontos = Salário Líquido.
                
                def salarioLiquido ():
                  valorHora = float(input("Informe quanto R$ vc ganha por hora? "))
                  horasMes = int(input("informe o total de horas trabalhados no referido mês "))
                  Bruto = (valorHora * horasMes)
                  INSS = 8
                  descontoINSS = (INSS * Bruto) /100
                  sindicato = 5
                  descontoSindicato = (sindicato * Bruto) / 100
                  liquido = (Bruto - descontoINSS - descontoSindicato)
                  print("Seu slário líquido é: ")
                  print(liquido)
                                   
                  salarioLiquido ()
                  

                #E) calcule os descontos e o salário líquido, conforme a tabela abaixo: 
                
                def salarioLiquido ():
                  valorHora = float(input("Informe quanto R$ vc ganha por hora? "))
                  horasMes = int(input("informe o total de horas trabalhados no referido mês "))
                  Bruto = (valorHora * horasMes)
                  INSS = 8
                  descontoINSS = (INSS * Bruto) /100
                  sindicato = 5
                  descontoSindicato = (sindicato * Bruto) / 100
                  IR = 11
                  descontoIR = (IR * Bruto) / 100
                  liquido = (Bruto - descontoINSS - descontoSindicato - descontoIR)
                  print("Seu slário líquido é: ")
                  print(liquido)
                                   
                  salarioLiquido ()

#Exercicio 16 - Texto muito longo. Olhar no site: https://wiki.python.org.br/EstruturaSequencial   
                  
                  def calculalitros():
                    areaAp = float(input("Informe quantos m2 tem seu ap "))
                    formulaLitros = (areaAp / 3)
                    print("A quantidade de litrso que vc vai precisar é: ")
                    print(formulaLitros)
                    calcularPreco = (formulaLitros / 18) * 80
                    print("vc vai gastar: ")
                    print(calcularPreco)
                    
                    calculalitros()
                 
                
#Exercicio 17 - Texto muito longo. Olhar no site: https://wiki.python.org.br/EstruturaSequencial
                  
                  #A) Litros e gastos: comprar apenas latas de 18 litros;
                  
                  def calculalitros():
                    areaAp = float(input("Informe quantos m2 tem seu ap "))
                    formulaLitros = (areaAp / 6)
                    print("A quantidade de litros que vc vai precisar é: ")
                    print(formulaLitros)
                    calcularLatas = (formulaLitros / 18)
                    print("A quantidade de latas que vc vai precisar é: ")
                    print(calcularLatas)
                    print("vc vai gastar: ")
                    calcularPreco = (calcularLatas * 80)
                    print(calcularPreco)
                
                    calculalitros ()
                  
                  #B) Litros e gastos: comprar apenas galões de 3,6 litros;
                
                def calculalitros():
                    areaAp = float(input("Informe quantos m2 tem seu ap "))
                    formulaLitros = (areaAp / 6)
                    print("A quantidade de litros que vc vai precisar é: ")
                    print(formulaLitros)
                    calcularGaloes = (formulaLitros / 3.6)
                    print("A quantidade de galoes que vc vai precisar é: ")
                    print(calcularGaloes)
                    print("vc vai gastar: ")
                    calcularPreco = (calcularGaloes * 25)
                    print(calcularPreco)
                    
                    calculalitros()
                    
                 
                  
                  