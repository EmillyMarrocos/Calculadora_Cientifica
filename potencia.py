def potencia(b, e):

    b01 = float(input("Digite o valor da base: "))
    e01 = float(input("Digite o valor do expoente: "))

    if e01 == 0:
        print ("O resultado é 1")

    elif e01 == 1:
        print ("O resultado é: ", b01)

    else:
        r = b ** e
        print ("O resultado é: ", r)

potencia(3, 2)