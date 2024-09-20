import sys

def is_jolly(seq):
    '''
        Funcion que devuelve "Jolly" si la secuencia de numeros (variable "seq") 
        es considerada un Jolly Jumper y "Not Jolly" en caso contrario
    '''
    
    if len(seq) == 1:
        return True
    
    myset = set([abs(a-b) for a, b in zip(seq, seq[1:])]) #Creo un set por comprension. Cada posicion va a contener el valor abs del elemento i - i+1 de la lista de seq
    
    for I in range(1, len(seq)):
        if I not in myset:
            return False
        
    return True

for line in sys.stdin:
    seq = list(map(int, line.split()))
    
    if is_jolly(seq[1:]):
        sys.stdout.write("Jolly" + "\n")
    else:
        sys.stdout.write("Not jolly" + "\n")