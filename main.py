#Importa o módulo

import os
from modulo import *

#Programa principal

if __name__ == '__main__':
    while True:
        print(f'{'*'*30} CALCULADORA DE ÁREA {'*'*30}\n')
        exibir_menu()
        print()
        opcao = input('Opção desejada: ')

        match opcao:
            case '1':
                b = int(input('Base do quadrilátero: '))
                h = int(input('Altura do quadrilátero: '))
                print(f'Área: {calcular_quadrilatero(b,h)}')
                continue
            case '2':
                r = int(input('Raio do círculo: '))
                print(f'Área: {calcular_circulo(r)}')
                continue
            case '3':
                b = int(input('Base do triângulo: '))
                h = int(input('Altura do triângulo: '))
                print(f'Área: {calcular_triangulo(b,h)}')
            case '4':
                base_menor = int(input('Base menor do trapézio: '))
                base_maior = int(input('Base maior do trapézio: '))
                h = int(input('Altura do trapézio: '))
                print(f'Área: {calcular_trapezio(b,h)}')
                continue
            case '5':
                break
            case _:
                print('Opção inválida.')