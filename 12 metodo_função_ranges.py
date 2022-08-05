"""
Rarnges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Rnges são utilicados para gerar sequências numericas, não de forma aleatórea, mas sim de maneira especificada.

Formas gerais:
"""

# Forma 1

# range(valor_de_parada)
# OBS:valor_de_parada não inclusive (início padrão 0. e passo de 1 em 1)

for num in range(11):  # (loop vai de 0 ... até 10)
    print(num)


# Forma 2

# range(valor_de_início, valor_de_parada)
# OBS:valor_de_parada não inclusive (início especificado pelo usuario, e o passo de 1 em 1)

for num in range(1, 11):  # (loop vai de 1 ... até 10)
    print(num)


# Forma 3

# range(valor_de_início, valor_de_parada, passo)
# OBS:valor_de_parada não inclusive (início especificado pelo usuario, e o passo especificado pelo usuário)

for num in range(1, 10, 2):  # (loop vai de 1 ... até 10 contando  de 2 em 2)
    print(num)  # (1 + 2 = 3 | 3 + 2 = 5 | 5 + 2 = 7 | 7 + 2 = 9)

for num in range(5, 50, 5):  # (loop vai de 5 ... até 50 contando  de 5 em 5 | # se quiser que o loop pare dem 50 tenho que representar o numero final do loop de 55)
    print(num)  # (5 | 5 + 5 = 10 | 10 + 5 = 15 | 15 + 5 = 20 |20 + 5 = 25 ...)

# Forma 4 (inversa)

# range(valor_de_final, valor_de_parada, passo)
# OBS:valor_de_parada não inclusive (valor_final especificado pelo usuario, passo especificado pelo usuario)

for num in range(10, -1, -1):  # (loop vai de 1 ... até 10)
    print(num)





#lista = list(range(10))  # imprime ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
