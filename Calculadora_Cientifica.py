import math
import operacoesbasicas
import cosseno
import exponencial
import mode
import potencia
import raiz_quadrada
import seno
import tangente
import expressao_num
        
def menu():
        print(" ")
        print("Bem vindo à Calculadora Científica!")
        print("Esta calculadora contêm operações básicas e avançadas!")
        print(" ")
        print("Opções: ")
        print("1- Soma")
        print("2- Subtração")
        print("3- Multiplicação")
        print("4- Divisão")
        print("5- y^x: Elevado à Potência de x")
        print("6- Raiz Quadrada")
        print("7- ex: Exponenciação")
        print("8- sin: Seno")
        print("9- cos: Cosseno")
        print("10- tan: Tangente")
        print("11- Mode: Converter Graus para Radianos")
        print("12- Mode: Converter Radianos para Graus")
        print('13- Realizar expressão algébrica')
        print(' ')


pi = 3.14
        
        
while True:
    menu()

    escolha = input('Digite o número da operação desejada: ')
    print(' ')

    if escolha == '1':
        n1 = float(input('Digite o primeiro número:'))
        n2 = float(input('Digite o segundo número:'))
        c = operacoesbasicas.Soma(n1,n2)
        print(c)

    elif escolha == '2':
        n1 = float(input('Digite o primeiro número:'))
        n2 = float(input('Digite o segundo número:'))
        c = operacoesbasicas.Subtracao(n1,n2)
        print(c)

    elif escolha == '3':
        n1 = float(input('Digite o primeiro número:'))
        n2 = float(input('Digite o segundo número:'))
        c = operacoesbasicas.Multiplicacao(n1,n2)
        print(c)

    elif escolha == '4':
        n1 = float(input('Digite o primeiro número:'))
        n2 = float(input('Digite o segundo número:'))
        c = operacoesbasicas.Divisao(n1,n2)
        print(c)

    elif escolha == '5':
        potencia.Potencia()

    elif escolha == '6':
        raiz_quadrada.Selecionar_Raiz()

    elif escolha == '7':
        exponencial.Exponecial()

    elif escolha == '8':
        seno.Seno()

    elif escolha == '9':
        cosseno.Cosseno()

    elif escolha == '10':
        tangente.Tangente()

    elif escolha == "11":
        mode.Graus_para_Radianos()

    elif escolha == "12":       
        mode.Radianos_para_Graus()
    
    elif escolha == '13':
        ex = str(input('Digite a expressão: '))
        expressao_num.calcular_expressao(ex)

    else:
        continuar = input("Deseja continuar? (S/N)")
        if continuar.lower() != 'S':
            break
        else:
            print("Escolha inválida. Tente novamente!")