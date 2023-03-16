'''Código criado por Felipe Alberto'''

from datetime import datetime


def linha():
    print('=' * 40)


def obter_limite():
    print('Bem-vindo a loja do Felipe, a mais supimpa da cidade!')
    print('Caro usuário, para uma análise aprofundada de crédito, digite os dados a seguir\n')
    nome_cliente = str(input('Qual o seu nome? ')).strip()
    cargo = str(input('Informe seu cargo: ')).strip()
    salario = float(input('Informe seu salário: R$'))
    ano_nascimento = int(input('Informe seu ano de nascimento: '))
    linha()
    ano = datetime.now().year
    idade_aprox = ano - ano_nascimento
    limite_gastos = salario * (idade_aprox / 1000) + 100
    print('Nome: ', nome_cliente)
    print('Idade aproximada: ', idade_aprox)
    print('Cargo: ', cargo)
    print(f'Salário: {salario:.2f}')
    linha()
    print(f'\033[32mLimite total de gastos na loja: R${limite_gastos:.2f}\033[m')
    linha()
    return limite_gastos, idade_aprox


def verificar_produto(limite):
    meu_nome_completo = str('Felipe Alberto de Lima da Silva')
    meu_primeiro_nome = str('Felipe')
    tamanho_nome_completo = len(meu_nome_completo)
    tamanho_primeiro_nome = len(meu_primeiro_nome)
    produto = str(input('Qual produto você procura? ')).strip()
    preco = float(input('Informe o preço do produto: R$'))
    print('')
    bloqueado = 0
    if preco < (0.6 * limite):
        print('\033[32mLiberado!\033[m')
    elif preco < (0.9 * limite):
        print('\033[32mParcela em até 2x!\033[m')
    elif preco < limite:
        print('\033[32mParcela em ate 3x ou mais!\033[m')
    else:
        print('\033[31mBloqueado\033[m')
        bloqueado = 1
    print('')
    if not bloqueado:
        if tamanho_nome_completo < preco < idade:
            desconto = tamanho_primeiro_nome
            print(f'Desconto: R${float(desconto):.2f}')
            preco = preco - desconto
            print(f'Valor com desconto: R${preco:.2f}')
        else:
            print('\033[31mNão possui desconto.\033[m')
        limite -= preco

    linha()
    return limite


limite, idade = obter_limite()
qtdade_produtos = int(input('Quantos produtos deseja comprar? '))
produtos = 0
while produtos < qtdade_produtos:
    limite = verificar_produto(limite)
    print(f'\033[4mLimite atual: R${limite:.2f}\033[m\n')
    produtos += 1
