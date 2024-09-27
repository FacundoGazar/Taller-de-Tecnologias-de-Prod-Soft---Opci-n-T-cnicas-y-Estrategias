import sys

def lengthOfLIS(seq):
    '''
        Devuelve una lista de los indices de los que forman la subsecuencia incremental mas larga 
    '''
    LIS = [1] * len(seq) # Hago una lista de unos con el mismo tamaño que la secuencia leida
    prev = [-1] * len(seq) # Para despues restaurar el array guardo los previos
    
    for i in range(len(seq) -1, -1, -1): # Itero la lista al reves, empezando por el ultimo indice
        for j in range(i + 1, len(seq)): # En la primer iteracion no entra porque no hay elementos despues del ultimo indice asi que ese queda en 1
            if seq[i][0] < seq[j][0] and seq[i][1] > seq[j][1]: # Me fijo tambien por iq (posicion 1) de la secuencia
                if LIS[i] < 1 + LIS[j]:
                    LIS[i] = 1 + LIS[j]
                    prev[i] = j
                
    pos = LIS.index(max(LIS))   # Obtengo la posicion del primer elemento de la subsecuencia lis
    
    LIS_index = []
    while pos != -1:    # Voy restaurando el vector con las posiciones previas hata llegar al ultimo elemento (-1)
        LIS_index.append(pos)
        pos = prev[pos]
    
    return LIS_index

seq = []
for id, line in enumerate(sys.stdin):   # Leo el peso (w) e iq (d) de cada elefante y me quedo tmb con su id asi no lo pierdo despues
    w, s = map(int, line.split())
    seq.append([w, s, id+1])    # Como en el ejercicio los ids empiezan desde el 1 entonces les voy sumando 1 a todos

seq = sorted(seq, key=lambda x: (x[0], -x[1]))  # Ordeno el vector porque usando el algoritmo normal de LIS hay casos que me puedo perder en este ejercicio, lo hago por peso creciente y desempato por iq decreciente

LIS_index = lengthOfLIS(seq)

sys.stdout.write(f"{len(LIS_index)}\n")

for id in LIS_index:
    sys.stdout.write(f"{seq[id][2]}\n") # Uso el id para acceder a la secuencia ordenada y accedo al id original