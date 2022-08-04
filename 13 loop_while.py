"""
Loop while

Forma geral

While expressão_booleana:
    //execução do loop

O bloco while será repetido enquanto a expressãp booleana for verdadeira TRUE.

 Ex:
 num = 5
 num < 10
 (True)

 num = 5
 num > 10
 False

"""
# 1 Exemplo

numero = 1

while numero < 10:  # (numero vai de 1 até 9)
    print(numero)
    numero = numero + 1

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.
"""  while numero < 10:
         print(numero)
      // numero = numero + 1 // Não deixar de incrementar o loop
"""

# 2 Exemplo

resposta = ''

while resposta != 'sim':  # ( != diferente ou igual a 'sim')
    resposta = input('Já acabou Jéssica?') # A resposta do usuario tem que ser TRUE.
"""
TERMINAL 
Já acabou Jéssica?não
Já acabou Jéssica?não
Já acabou Jéssica?sim
 
 fim
"""



