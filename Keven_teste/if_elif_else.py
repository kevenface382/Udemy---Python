'''''
🧠 Pense assim:

if, elif e else servem para o computador tomar decisões.

É tipo perguntar:

“Se acontecer isso, faça isso.
Se não, veja outra condição.
Se nada disso acontecer, faça outra coisa.”
--------------------------------------------
📌 1️⃣ if → SE

Significa "se isso for verdadeiro"

idade = 18

if idade >= 18:
    print("Pode dirigir")
-------------------------------------------
📌 2️⃣ elif → SENÃO SE

Usamos quando queremos testar outra condição, caso o if seja falso.

idade = 16

if idade >= 18:
    print("Pode dirigir")
elif idade >= 16:
    print("Pode dirigir com autorização")
----------------------------------------------
📌 3️⃣ else → SENÃO

É o "resto".
Executa quando nenhuma condição anterior foi verdadeira.

idade = 14

if idade >= 18:
    print("Pode dirigir")
elif idade >= 16:
    print("Pode dirigir com autorização")
else:
    print("Não pode dirigir")
-------------------------------------------------

🎯 Estrutura básica:
if condição:
    faz isso
elif outra condição:
    faz outra coisa
else:
    faz isso aqui se nada funcionar
---------------------------------------------------
🧠 Exemplo bem simples:
numero = 5

if numero > 0:
    print("É positivo")
elif numero < 0:
    print("É negativo")
else:
    print("É zero")
----------------------------------------------------
🔥 Resumão:

if → primeira verificação

elif → outras verificações

else → se nenhuma for verdadeira

'''