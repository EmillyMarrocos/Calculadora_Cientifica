def Calcular_Raiz_Quadrada(numero):
    return numero ** 0.5    

def Calcular_Raiz_Cubica(numero):
    return numero ** (1/3)

aux = True
    
def Selecionar_Raiz():
    while True:
        print("Selecione a operação desejada:")
        print("1. Raiz Quadrada")
        print("2. Raiz Cúbica")
        
        escolha = input("Digite o número da operação desejada (ou 's' para sair): ")

        if escolha  == 's':
             break
             
        elif escolha == '1':
            numero = float(input("Digite o número para calcular a raiz quadrada: "))
            print("A raiz quadrada  é:", Calcular_Raiz_Quadrada(numero))

        elif escolha == '2':
            numero = float(input("Digite o número para calcular a raiz cúbica: "))
            print("A raiz cúbica é: ", Calcular_Raiz_Cubica(numero))

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


