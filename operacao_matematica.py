a = int(input('Insira um valor: '))
b = int(input('Insira outro valor: '))

soma = a + b
subtr = a - b
multi = a * b
div = a/b
resto = a % b
resultado = ('A soma é: {soma}. \nA subtração é: {subtr}.'
                '\nA Multiplicação é: {multi}.'
                '\nA divisão é: {div}. '
                '\nO resto é: {resto}'.format(soma=soma,
                                                subtr=subtr,
                                                multi=multi,
                                                div=div,
                                                resto=resto))
print(resultado)

