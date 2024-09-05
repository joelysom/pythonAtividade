preco = float(input("Digite o preço da mercadoria: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

valor_desconto = (percentual_desconto / 100) * preco
preco_final = preco - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço a pagar: R$ {preco_final:.2f}")
