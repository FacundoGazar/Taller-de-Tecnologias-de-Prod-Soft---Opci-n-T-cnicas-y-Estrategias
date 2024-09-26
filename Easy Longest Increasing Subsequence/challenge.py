import sys

def lengthOfLIS(seq):
    '''
        Devuelve la longitud de la subsecuencia incremental mas larga 
    '''
    LIS = [1] * len(seq) # Hago una lista de unos con el mismo tamaño que la secuencia leida
    
    for i in range(len(seq) -1, -1, -1): # Itero la lista al reves, empezando por el ultimo indice
        for j in range(i + 1, len(seq)): # En la primer iteracion no entra porque no hay elementos despues del ultimo indice asi que ese queda en 1
            if seq[i] < seq[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j]) # Me aseguro de  quedarme con la subsecuencia mas larga para el indice i
    
    return max(LIS)

list_length = sys.stdin.readline()

seq = list(map(int, sys.stdin.readline().split()))

sys.stdout.write(str(lengthOfLIS(seq)))
