# 1 - imports / bibliotecas

# 2 - Classe

# 3 - Métodos e Funções ( funções tem retorno, metodo não)
#def = definition = definição
def print_hi(name):
    print(f'Oi, {name}') #modelo novo
    print('Oi, ' + name) #modelo tradicional

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura, comprimneto):
    return (largura * comprimneto) / 2

def contagem_progressiva(fim):
    for numero in range(fim):     #For é um loop, irá repedir o blobo até o fim, por padrão o numero vai comecar em 0
        print(numero, end=' ') #end vai colocar um numero do lado do outro

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        contador = numero ++1
        if numero < 9:
            print(f'0{numero +1} - {nome}', end=' ')
        else:
            print(numero +1, '-',nome,  end=' ')

def apoiar_candidato_dois(nome, vezes):
    for numero in range(vezes):
        if numero <9:                               #se o numero < 9 vai colocar 00 na frente
            print(f'00{numero+1} - {nome}')
        elif numero <99:                            #senao o numero <99 vai ter 00 na frente
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero +1 , '-' + nome)

def brincar_de_plim(fim):
    for numero in range(1,fim +1):
        if numero % 4 == 0: # % resto da divisao
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero)) #'{:0>9}'.format definição de formato




#Estrutura de indentificação/ execução do script

if __name__ == '__main__':

    resposta = 'C'

    while resposta.upper() != 'Z':             #while =enquanto

        print('#######################################')
        print('#                                     #')
        print('#      M E N U  D E  O P Ç Õ E S      #')
        print('#                                     #')
        print('#######################################')
        print('#        1 - Olá Mundo                #')
        print('#        2 - Área do retangulo        #')
        print('#        3 - Área do quadrado         #')
        print('#        4 - Área do triângulo        #')
        print('#        5 - Contagem progressiva     #')
        print('#        6 - Apoiar candidato         #')
        print('#        7 - Apoiar candidato Trump   #')
        print('#        8 - Brincar de Plim          #')
        print('#                                     #')
        print('#        Z - Sair                     #')
        print('#                                     #')
        print('#######################################')


        resposta = input('Escolha sua opção: ')
        print(f'A sua escolha foi : {resposta}')

        if resposta.upper() != 'Z':
            if resposta == '1':
               print_hi('Leandro')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(8,7)
                print(f'A área do retângulo é de {resultado} m')
            elif resposta == '3':
                resultado =calcular_area_do_quadrado(2)
                print(print(f'A área do quadrado é de {resultado} m'))
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(6,2)
                print(f'A área do triângulo é de {resultado} m')
            elif resposta == '5':
                resultado = contagem_progressiva(10)

            elif resposta == '6':
                apoiar_candidato('Trump', 10)

            elif resposta == '7':
                apoiar_candidato_dois('Doido', 10)

            elif resposta == '8':
                brincar_de_plim(100)

            else:
                print('Opção invalida, ezscolha uma opção de 1 a 8')
        else:
            print('Você escolheu1'
                  ' sair, Volte Sempre')


