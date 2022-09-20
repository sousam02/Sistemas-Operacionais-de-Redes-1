
from webbrowser import get


tabela = [
    {
        'produto' : 'Azeite de oliva - extra virgem LAT 500ml',
        'entradas' : 500,
        'saidas' : 40,
        'saldo_estoque' : 60,
        'preco' : 21.9,
        'subtotal' : 1314
    },
    {
        'produto' : 'Castanha do Pará - Granel(gr)',
        'entradas' : 100,
        'saidas' : 5,
        'saldo_estoque' : 95,
        'preco' : 6.0,
        'subtotal' : 300
    },
    {
        'produto' : 'Flocos de Aveia CXA 500g',
        'entradas' : 1000,
        'saidas' : 200,
        'saldo_estoque' : 800,
        'preco' : 10.9,
        'subtotal' : 872
    },
    {
        'produto' : 'Paçoca de Amendoim - CXA 30 Und',
        'entradas' : 100,
        'saidas' : 8,
        'saldo_estoque' : 92,
        'preco' : 1.5,
        'subtotal' : 30
    },
    {
        'produto' : 'Panetone Sem glúten - CXA 1 Und',
        'entradas' : 100,
        'saidas' : 60,
        'saldo_estoque' : 40,
        'preco' : 17.3,
        'subtotal' : 692
    },{
        'produto' : 'Polpa de Açaí Natural PCT 5L',
        'entradas' : 100,
        'saidas' : 1,
        'saldo_estoque' : 99,
        'preco' : 7.1,
        'subtotal' : 639
    },{
        'produto' : 'Queijo Vegano PCT 450g',
        'entradas' : 100,
        'saidas' : 30,
        'saldo_estoque' : 70,
        'preco' : 25,
        'subtotal' : 1750
    },{
        'produto' : 'Pãp Sírio Integral - Saco 500g',
        'entradas' : 100,
        'saidas' : 70,
        'saldo_estoque' : 30,
        'preco' : 5.9,
        'subtotal' : 177
    },
]

print('+------------------------------------------+--------------+----------+-------------+-----------------+---------+')
print("|{:^42}|{:^14}|{:^10}|{:^13}|{:^17}|{:^9}|".format('Produto', 'QTD Entradas', 'QTD Saídas', 'Saldo Estoque', 'Preço Unitário', 'Subtotal'))

for i in range(len(tabela)):
    print('+------------------------------------------+--------------+----------+-------------+-----------------+---------+')
    print("|{produto:<42}|{entradas:14}|{saidas:10}|{saldo_estoque:13}|{preco:17.2f}|{subtotal:9.2f}|".format(**tabela[i]))
print('+------------------------------------------+--------------+----------+-------------+-----------------+---------+')


