km_percorrido = float(input("insira os km percorrridos:"))
dias_alugados = float(input("insira a qunatidade de dias em que o carro foi alugado:"))

valor_por_dias = dias_alugados * 60
valor_por_km = km_percorrido *.15
valor_final = valor_por_dias + valor_por_km
print(f"a quantidade de km percorrido foi {km_percorrido}. a quantidade de dias alugado foi {dias_alugados}")
print(f"o valor por dia foi igual a: {valor_por_dias} e o valor por km foi igual a: {valor_por_km}")
print(f"o valor final a ser pago é de {valor_final}")