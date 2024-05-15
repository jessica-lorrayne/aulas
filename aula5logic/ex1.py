
def validacao(pergunta,min,max):
    
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x
def fatorial(num):
    
    '''
    num = parametro
    fat = variavel de acumulação
    for = faz o calc
    
    '''
        
    fat = 1
    
    if(num == 0):
        return fat

    for i in range(1,num + 1):
        fat *= i 
    return fat


x = validacao("digite o numero que deseja calcular a fatorial", 0, 9999)

print(f"a fatorial de {x} é igual a {x}! = {fatorial(x)} ")