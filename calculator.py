def soma(num1:float, num2:float)->float:
    if valida_numero(num1) and valida_numero(num2):
        soma = num1 + num2
        return soma

def subtracao(num1:float, num2:float)->float:
    if valida_numero(num1) and valida_numero(num2):
        subtracao = num1 - num2
        return subtracao

def multiplicacao(num1:float, num2:float)->float:
    if valida_numero(num1) and valida_numero(num2):
        multiplicacao = num1 * num2
        return multiplicacao

def divisao(num1:float, num2:float)->float:
    if valida_numero(num1) and valida_numero(num2):
        divisao = num1 / num2
        return divisao

def valida_numero(numero:float)->bool:
    if isinstance(numero, float):
        return True
    raise ValueError(f"{numero} precisa ser um número.")
