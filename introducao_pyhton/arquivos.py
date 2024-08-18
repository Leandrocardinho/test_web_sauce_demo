# 1 - importação de pacotes
import json

# 2 - Classes

# 3 - Definições (Funções e metodos)

dados = {} # usa chaves por ser um json

dados['cliente'] = [] #indica a criação de uma matriz, lista, vetor
dados['cliente'].append({
    'nome':'Juca',
    'telefone':'11972993636',
    'email':'juca@inter.com.br'
})
dados['cliente'].append({                          #outro cliente formato json
    'nome':'Fernanda',
    'telefone':'21666663636',
    'email':'Fernanda@inter.com.br'
})

def criar_json():
    with open('clientes.json', 'w') as outfile:  #primeiro o que eu quero cliar, segundo usa w para ler
        json.dump(dados,outfile,indent=4) # vai juntar o dados com o arquivo

def ler_json():
    with open('clientes2.json') as outfile:
        dados = json.load(outfile) #load para pegar os dados
        for registro in dados['cliente']:
            print(f'nome: {registro['nome']}')
            print(f'telefone: {registro['telefone']}')
            print(f'email: {registro['email']}')   #esse bloca vai imprimir os dados
            print('')

def ler_e_adiconar_no_json():
    with open('clientes2.json') as outfile:
        dados2 = json.load(outfile) #load para ler os dados
        #exibir no console

        temp = []
        for registro in dados2['cliente']:
            #Exibir no console
            print(f'nome: {registro['nome']}')
            print(f'telefone: {registro['telefone']}')
            print(f'email: {registro['email']}')   #esse bloca vai imprimir os dados
            print('')

            #Salvar na lista
                    # 'nome': 'Claudio'
            temp.append({
                'nome': registro['nome'],
                'telefone': registro['telefone'],
                'email': registro['email']
            })

        dados['cliente'].extend(temp)

        # Ordenar a lista de clientes pela chave 'nome' em ordem alfabética
        dados['cliente'].sort(key=lambda x: x['nome'])

        with open('clientes3.json', 'w') as outfile:  # primeiro o que eu quero cliar, segundo usa w para ler
            json.dump(dados, outfile,indent=4)



def testar_criar_json():
    criar_json()
    print(dados['cliente'])

def testar_ler_json():
    print('Leitura do JSON por linha / campo')
    ler_json()
    print(dados['cliente'])

def testar_ler_acionar_json():
    ler_e_adiconar_no_json()
    print('Lista atualizada')
    print(dados['cliente'])




