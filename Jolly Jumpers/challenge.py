import sys

def load_seq():
    '''
        Funcion que lee el input para el desafio
    '''
    seq_str = sys.stdin.readline() #Linea completa del input
    if seq_str == '\n' or seq_str=='':
        return None

    return list(map(int, seq_str.split())) #Divido el input en strings independientes y los transformo a integers.

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

while True:
    seq = load_seq()
    
    if seq is None:
        break
    
    if is_jolly(seq[1:]):
        sys.stdout.write("Jolly" + "\n")
    else:
        sys.stdout.write("Not jolly" + "\n")