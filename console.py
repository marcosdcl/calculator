from calculator import (
    soma,
    subtracao,
    multiplicacao,
    divisao
)


def menu()->int:

    print('''
        Escolha o operador 
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        0 - Sair
    ''')
    opcao = input("... ")
    return opcao

def operador_operando()->float:

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("Os valores digitados precisam ser números")
    

while True:
    opcao = menu()

    try:

        if opcao == '1':
            num1, num2 = operador_operando()
            resultado = soma(num1, num2)
        elif opcao == '2':
            num1, num2 = operador_operando()
            resultado = subtracao(num1, num2)
        elif opcao == '3':
            num1, num2 = operador_operando()
            resultado = multiplicacao(num1, num2)
        elif opcao == '4':
            num1, num2 = operador_operando()
            resultado = divisao(num1, num2)
        elif opcao == '0':
            break

    except ValueError:
        print("Opação inválida")

    print(f"{resultado:.2f}")
