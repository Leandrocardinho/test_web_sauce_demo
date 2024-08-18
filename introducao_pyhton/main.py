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

def exibir_dia_da_semana_if(numero):
    print('Execução com IF')
    if numero == 1:
        print('Segunda-feira')
    elif numero == 2:
        print('Terca-feira')
    elif numero == 3:
        print('Quarta-feira')
    elif numero == 4:
        print('Quinta-feira')
    elif numero == 5:
        print('Sexta-feira')
    elif numero == 6:
        print('Sabado')
    elif numero == 7:
        print('Domingo')
    else:
        print('Número invalido / Digite um número de 1 a 7')

def  exibir_dia_da_semana_match_case(numero):

    print('Execução com Math case')

    match numero:
        case 1:
            print('Segunda-feira')
            exit()
        case 2:
            print('Terca-feira')
            exit()
        case 3:
            print('Quarta-feira')
            exit()
        case 4:
            print('Quinta-feira')
            exit()
        case 5:
            print('Sexta-feira')
            exit()
        case 6:
            print('Sabado')
            exit()
        case 7:
            print('Domingo')
            exit()
        case _: #esse case vai tratar as outras opcoes como print abaixo
            print('Número invalido / Digite um número de 1 a 7')


def brincar_de_para_ou_continua():
    resposta = 'C' # c aqui significa continua

    while resposta.upper() == 'C':
            resposta = input('Digite P para parar ou C para continuar')

    print('Você decidiu para com a brincadeira')



# Estrutura de indentificação/ execução do script

if __name__ == '__main__':
    print_hi('Leandro')

    #chamar a função de calculo da area do retangulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A área do retângulo é de {resultado} m²')

    #chamar a função de calculo da area do retangulo
    resultado = calcular_area_do_quadrado(5)
    print((f'A área do quadrado é de {resultado}  m²'))

    #chamar a função calculo area do tringulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f'A área do triângulo é de {resultado} m²')

    # excutar uma contagem progressiva
    print(contagem_progressiva(11))

    #executar a função apoiar canditado, exiber nome e mostar vezes
    apoiar_candidato("Faker",10)
    print()

    #executar a função apoiar canditado dois
    apoiar_candidato_dois("Trump", 100)
    print()

    #executar a função brincar de plim
    brincar_de_plim(100)

    # exemplo com while - para ou continua
    brincar_de_para_ou_continua()

    # exemplo de dia da semana com if(se) -elif(senao se) - else (senao)
    exibir_dia_da_semana_if(5)

    # exemplo de dia da semana com o match case
    exibir_dia_da_semana_match_case(1)









