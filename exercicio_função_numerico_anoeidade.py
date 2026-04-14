import os
from datetime import date
os.system("cls")

# Limpa o terminal.
# Funções com parâmetro.
# Com retorno.
def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    return ano_atual - ano_nascimento

# Exmeplo de uso de funções.

print("- Solicitando dados -")
ano_nascimento = int(input("Digite o ano em que nasceu: "))

# Chamando funções e enviando parâmetros.
idade = calcular_idade(ano_nascimento)

print(f"\n= Exibidno resultado =")
print(f"idade: {idade}")