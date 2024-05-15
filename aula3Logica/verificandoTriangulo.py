lado_a = int(input("insira o lado A\n"))
lado_b = int(input("insira o lado B\n"))
lado_c = int(input("insira o lado C\n"))

if((lado_a > 0 and lado_b > 0 and lado_c> 0) and (lado_a + lado_b > lado_c and lado_c + lado_b > lado_a and lado_c + lado_a > lado_b)):
    if(lado_a == lado_b and lado_a == lado_c):
        print(f"este é um triangulo Equilatero pois, {lado_a}, {lado_b} e {lado_c} são iguais")
    elif(lado_a == lado_b or lado_a == lado_c or lado_b == lado_c ):
        print(f"este é um triangulo isósceles, pois apenas dois lados são iguais, {lado_a}, {lado_b} e {lado_c}")
    else:
        print(f"este é um triangulo escaleno, pois todos os lados são diferentes, {lado_a}, {lado_b} e {lado_c}")
else:
    print("um dos valores informados não é valido")