deposito_inicial = float(input("Digite o valor do depósito inicial: R$ "))
deposito_mensal = float(input("Digite o valor depositado mensalmente: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (%): ")) / 100
meses = int(input("Digite o número de meses: "))


valor_total = deposito_inicial

for mes in range(1, meses + 1):
    valor_total += deposito_mensal
    valor_total += valor_total * taxa_juros

print(f"Valor total ao final de {meses} meses: R$ {valor_total:.2f}")
