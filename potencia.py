def Potencia():

    b01 = float(input("Digite o valor da base: "))
    e01 = float(input("Digite o valor do expoente: "))

    if e01 == 0:
        print ("O resultado é 1")

    elif e01 == 1:
        print ("O resultado é: ", b01)

    else:
        r = b01 ** e01
        print ("O resultado é: ", r)