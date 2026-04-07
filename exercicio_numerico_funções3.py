import os

os.system("Cls")
# Limpa a terminal.
# Funções com parâmetros.
def valor(numero):
    if numero > 0:
        print(f"O valor e positivo.")
    elif numero < 0:
        print(f"O valor e negativo.")
    else:
        print(f"O valor e igual a 0.")

# Exemplo de uso de função.
numero = float(input("Digite seu numero: ")) 

# Chamando a função.
# Enviando parâmetros.
valor(numero)