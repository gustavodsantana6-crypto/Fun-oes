import os

# Limpa o terminal.
# Função sem retorno e sem parâmetro.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
sobrenomes = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    sobrenome = input("Digite seu sobrenome (ou 'sair' para encerrar): ")
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair' or sobrenome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    sobrenomes.append(sobrenome)

# Adiciondo função de IMC.
def calcular_imc(peso,altura):
    """Calcula o IMC e retorna o valor."""
    return peso / altura ** 2

def obter_classificação(imc):
    """Recebe o IMC e retorna uma tupla com (classificação, recomendação)."""
    if imc <= 18.5:
        return "Abaixo do peso."
    elif 18.5 < imc < 25:
        return "Peso normal."
    elif 25 <= imc < 30:
        return "Sobrepeso."
    elif 30 <= imc < 35:
        return "Obesidade grau I."
    elif 35 <= imc < 40:
        return "Obesidade grau II."
    if imc >= 40:
        return "Obesidade grau III(Mórbido(a).)"

def main():
    """Função principal que executa o fluxo do programa."""
    print("--- Calculadora de IMC ---")
    
    # Exibindo os dados armazenados
    logoSenai()
    print("\nDados dos usuários:")
    for i in range(len(nomes)):
        try:
            # Processamento
            valor_imc = calcular_imc(pesos[i], alturas[i])
            classificacao = obter_classificação(valor_imc)
            
            print(f"Usuário {i+1}:")
            print("Nome:", nomes[i])
            print("Sobrenome:", sobrenomes[i])
            print(f"Seu IMC: {valor_imc:.2f}")
            print(f"Classificação: {classificacao}")
            print()
        except ValueError:
            print("Erro: Por favor, insira apenas números usando ponto para decimais.")

# Inicia o programa
if __name__ == "__main__":
    main()