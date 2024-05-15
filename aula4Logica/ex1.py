

# x = 3

# while x <=12:
#     print(f"{x}")
#     x += 1

# for i in range (3,13,1):
#     print(f"{i}")

# x = 0

# while x <=9:
#     print(f"{x}")
#     x += 2

# for i in range (0,9,2):
#     print(f"{i}")


print("coxinha  - R$ 5,00 digite = 1")
print("pastel  - R$ 7,00 digite = 2")
print("café  - R$ 4,00 digite = 3")
print("suco  - R$ 6,00 digite = 4")
print("sair digite = 5")

total = 0

while True:
    op = int(input("digite o que deseja comprar ou sair:\n"))
    qtnd = int(input("qual a quantidade de itens você deseja comprar?:\n"))

    if (op == 5):
        print(f"\no valor é de {total}")
        break
    elif (op == 1):
        qtnd = int(input("qual a quantidade de itens você deseja comprar?:\n"))
        total += qtnd * 5
        print(f"\no valor é de {total} até o momento")
        
    elif (op == 2):
        qtnd = int(input("qual a quantidade de itens você deseja comprar?:\n"))
        total += qtnd * 7
        print(f"\no valor é de {total} até o momento")
        
    elif (op == 3):
        qtnd = int(input("qual a quantidade de itens você deseja comprar?:\n"))
        total += qtnd * 4
        print(f"\no valor é de {total} até o momento")
        
    elif (op == 4):
        qtnd = int(input("qual a quantidade de itens você deseja comprar?:\n"))
        total += qtnd * 6
        print(f"\no valor é de {total} até o momento")
        
    else:
        print("opção inválida")
