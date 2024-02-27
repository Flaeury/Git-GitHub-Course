import random


minusculo = "abcdefghijklmnopqrstuvxyz"
maiusculo = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
especiais = "!_-.;:[]()"
numeros = "0123456789"


tudo = minusculo + maiusculo + especiais + numeros
tamanho = 12  


senha = ""

for _ in range(tamanho):
    senha += random.choice(tudo)


print("=========================================")
print("\nTa aqui a senha seu preguiçoso:", senha)
print("=========================================")
