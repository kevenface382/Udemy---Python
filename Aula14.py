a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

"""""
Resto da divisão
Se numero % 2 == 0 → é par
Se numero % 2 != 0 → é ímpar
"""