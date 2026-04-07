import os

os.system("Cls")
# Limpa o terminal.
# Função com parâmetro.
def numeros(numero):
    if numero % 2 == 0:
        print(f"O valor e par.")
    else:
        print(f"O numero e impar.")

# Exemplo de uso de função.
numero = int(input("Digite seu numero: "))

# Chamando a função.
# Enviando parâmetros.
numeros(numero)