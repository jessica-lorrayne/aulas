
valor_pedido = int(input("insira o valor nescessario"))

while True:
    
    if(valor_pedido >= 100):
        cont100 = valor_pedido // 100
        valor_pedido -= cont100 * 100
    elif(valor_pedido == 50):
        cont50 = valor_pedido // 50
        valor_pedido -= cont100 * 50
    elif(valor_pedido == 20):
        cont20 = valor_pedido // 20
        valor_pedido -= cont100 * 20
    elif(valor_pedido == 10):
        cont10 = valor_pedido // 10
        valor_pedido -= cont100 * 10
    elif(valor_pedido == 5):
        cont5 = valor_pedido // 5
        valor_pedido -= cont100 * 5
    elif(valor_pedido):
        cont1 = valor_pedido
        
def ilusor():
    '''
    dedededede
    '''