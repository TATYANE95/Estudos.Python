"""
Saindo de loops com break

Funciona da mesma forma como na linguagens c e Java

Utilizamos o break para sair do loop de maneira projetada.
"""
# Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break  # Break esta dentro do bloco for mas sim do bloco if
    else:  # Esta dentro do bloco if
        print(numero)  # Print esta dentro do bloco else
print('Sai do loop')  # Print esta fora do bloco interno do for

# Exemplo 2

while Truegit :
    comando = input("Digite 'sair' para sair")
    if comando == 'sair':
        break