preco_produto = float(input("informe o preço de um produto:"))
percentual_app = float(input("informe o percentual de desconto a ser aplicado:"))

desconto = preco_produto * (percentual_app / 100)

preco_final = preco_produto - desconto

print(f"o valor do produto é {preco_produto}. o valor do desconto é {percentual_app}%")
print(f"o valor final é {preco_final} e o desconto aplicado foi de {desconto}")

