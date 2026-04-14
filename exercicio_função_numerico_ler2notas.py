import os
os.system("cls")

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado

print("= Solicitando dados =")
while True:
    primeira_nota = float(input("Digite a primeira nota: "))
    if primeira_nota >= 0 and primeira_nota <= 10:
        break

while True:
    segunda_nota = float(input("\nDigite a segunda nota: "))
    if segunda_nota >=  0 and segunda_nota <= 10:
        break

media = calcular_media(primeira_nota, segunda_nota)
situacao = verificar_situacao(media)

print("\n= Exibindo dados =")
print(f"Média: {media}")
print(f"Resultado: {situacao}")


