#Inteiros - números inteiros
idade = 25
ano = 2026

if idade >= 25:
    print('Voce ta perto dos 30')

else:
    print('Voce é jovem')

#float - números com casas decimais
altura = 1.86
meta = 1.000000

if altura >= 1.86 and idade >= 25 and meta >= 100000:
    print ('Voce precisa continuar')
else:
    print ('Voce ta perdido')

#str — texto (string)
nome = "Keven"
mensagem = "Bem-vindo ao Python"

print(f"Olá, {nome}")

#bool — verdadeiro ou falso

tem_carteira = True
esta_chovendo = False

tem_dinheiro = True

if tem_dinheiro:
    print("Pode comprar")
else:
    print("Não pode comprar")

#list — lista de coisas
numeros = [1, 2, 3, 4]
nomes = ["Ana", "João", "Maria"]

#dict — dicionário (chave e valor)
pessoa = {
    "nome": "Keven",
    "idade": 25
}

#Resenha
time = 'São Paulo'
bairro = 'Vergueiro'

if bairro == 'Vergueiro' and time != 'Corinthians':
    print ('GAY')
else:
    print ('ok')