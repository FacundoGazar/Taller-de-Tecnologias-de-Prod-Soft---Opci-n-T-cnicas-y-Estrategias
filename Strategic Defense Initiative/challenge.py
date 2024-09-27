import sys

def LIS(seq):
    '''
        Devuelve una lista con los valores de la LIS
    '''
    DP = [1] * len(seq)
    prev = [-1] * len(seq)
    
    for i in range(len(seq) -1,-1,-1):
        for j in range(i + 1, len(seq)):
            if seq[i] < seq[j] and DP[i] < 1 + DP[j]:
                DP[i] = DP[j] + 1
                prev[i] = j # Para despues reconstruir el array mediante los indices
    
    pos = DP.index(max(DP))
    
    LIS_seq = []
    
    while pos != -1:
        LIS_seq.append(seq[pos])
        pos = prev[pos]

    return LIS_seq

test_cases = int(sys.stdin.readline().rstrip()) # Leo la cantidad de test cases a evaluar
blank_space = sys.stdin.readline()  # leo el primer espacio en blanco despues del test cases

output = []
for _ in range(test_cases):
    seq = []
    
    for line in sys.stdin:  # Leo cada numero de la secuencia de altitudes
        try:
            seq.append(int(line))
        except:
            break
        
    LIS_seq = LIS(seq)
    
    aux = f"Max hits: {len(LIS_seq)}"
    
    for num in LIS_seq:
        aux += f"\n{num}"
    
    output.append(aux)

sys.stdout.write("\n\n".join(output) + "\n")
