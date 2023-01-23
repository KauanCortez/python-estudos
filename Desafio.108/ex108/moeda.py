def metade(valor=0):
    return valor / 2
    
    
def dobro(valor=0):
    return valor * 2
    
        
def aumentar(valor=0, perc=0):
    res = valor * perc / 100
    return valor + res
    
                    
def diminuir(valor=0, perc=0):
    res = valor * perc / 100
    return valor + res
 
  
def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor :.2f}'        
    