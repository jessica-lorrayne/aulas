op = input("insira qual operação matematica vc deseja fazer")
a = int(input("insira o primeiro valor"))
b = int(input("insira o segundo valor"))
if(op == "+"):
    res = a + b 
    print(f"o resultado de {a} + {b} é {res}")
elif(op == "-"):
    res = a - b 
    print(f"o resultado de {a} - {b} é {res}")
elif(op == "/"):
    res = a / b 
    print(f"o resultado de {a} / {b} é {res}")
elif(op == "*"):
    res = a * b 
    print(f"o resultado de {a} * {b} é {res}")
else:
    print("operação inválida, encerrando o programa")