# Solicitar ao usuário o valor do quanto ele ganha por hora e o numero de horas trabalhadas
recebe_hora = float(input("Quantos reais você ganha por hora? R$"))
horas_trabalhadas = float(input("Quantas horas trabalhadas você tem atualmente? "))

# Calcula quanto o salário total referente ao mês
salario_total = recebe_hora * horas_trabalhadas

# Mostra na tela o salário total
print(f"O seu salário/horas trabalhadas é: {salario_total:.2f}")
