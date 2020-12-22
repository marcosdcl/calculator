from flask import Flask

from calculator import (
    soma,
    subtracao,
    multiplicacao,
    divisao
)

app = Flask(__name__)

@app.route('/')
def index():

    title = '<h1> Calculadora Olist </h1>'
    operator = '''
                <ol>
                    <li> <a href='/sum'> Somar </a> </li>
                    <li> <a href='/sub'> Subtrair </a> </li>
                    <li> <a href='/mult'> Multiplicar </a> </li>
                    <li> <a href='/div'> Dividir </a> </li>
                </ol>
               '''
    return f'{title} {operator}'

@app.route('/sum')
def sum():

    n1 = 10.0
    n2 = 3.0
    result = soma(n1, n2)

    title = '<h1> Calculadora Olist </h1>'
    result_ = f'<h3> A soma de {n1} + {n2} é = {result} </h3>'
    back = '<a href="/"> Voltar </a>'

    return f'{title} {result_} {back}'

@app.route('/sub')
def sub():

    n1 = 10.0
    n2 = 3.0
    result = subtracao(n1, n2)

    title = '<h1> Calculadora Olist </h1>'
    result_ = f'<h3> A subtração de {n1} - {n2} é = {result} </h3>'
    back = '<a href="/"> Voltar </a>'

    return f'{title} {result_} {back}'

@app.route('/mult')
def mult():

    n1 = 10.0
    n2 = 3.0
    result = multiplicacao(n1, n2)

    title = '<h1> Calculadora Olist </h1>'
    result_ = f'<h3> A multiplicação de {n1} * {n2} é = {result} </h3>'
    back = '<a href="/"> Voltar </a>'

    return f'{title} {result_} {back}'

@app.route('/div')
def div():

    n1 = 10.0
    n2 = 3.0
    result = divisao(n1, n2)

    title = '<h1> Calculadora Olist </h1>'
    result_ = f'<h3> A divisão de {n1} / {n2} é = {result} </h3>'
    back = '<a href="/"> Voltar </a>'

    return f'{title} {result_} {back}'

app.run(debug=True)
