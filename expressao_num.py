import math

def calcular_expressao(expressao):
    try:
        resultado = eval(expressao, {"__builtins__": None}, {"sqrt": math.sqrt})
        print('O resultado é ', resultado)
    except Exception as e:
        return f"Erro: {e}"