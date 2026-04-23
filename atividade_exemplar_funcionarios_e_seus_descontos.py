import os
os.system("cls")

print("--- ACESSO DO FUNCIONÁRIO ---")
matricula = input("Matrícula: ")
senha = input("Senha: ")

salario = float(input("Salário Base: R$ "))
quer_vt = input("Quer Vale Transporte? (s/n): ")
valor_vr = float(input("Valor do Vale Refeição: R$ "))
dependentes = int(input("Número de dependentes: "))

# Calculando o INSS (por faixas simples)
if salario <= 1518:
    inss = salario * 0.075
elif salario <= 2793.88:
    inss = salario * 0.09
elif salario <= 4190.83:
    inss = salario * 0.12
elif salario <= 8157.41:
    inss = salario * 0.14
else:
    inss = 951.62

# Calculando o IRRF
if salario <= 2428.80:
    irrf = 0
elif salario <= 2826.65:
    irrf = salario * 0.075
elif salario <= 3751.05:
    irrf = salario * 0.15
elif salario <= 4664.68:
    irrf = salario * 0.225
else:
    irrf = salario * 0.275

# Calculando os Benefícios
desc_vt = 0
if quer_vt == "s":
    desc_vt = salario * 0.06

desc_vr = valor_vr * 0.20
desc_saude = dependentes * 150

# Resultado Final
total_descontos = inss + irrf + desc_vt + desc_vr + desc_saude
salario_liquido = salario - total_descontos

print("\n--- RESULTADO ---")
print("Desconto INSS: R$", inss)
print("Desconto IRRF: R$", irrf)
print("Desconto VT: R$", desc_vt)
print("Desconto VR: R$", desc_vr)
print("Desconto Saúde: R$", desc_saude)
print("SALÁRIO LÍQUIDO: R$", salario_liquido)