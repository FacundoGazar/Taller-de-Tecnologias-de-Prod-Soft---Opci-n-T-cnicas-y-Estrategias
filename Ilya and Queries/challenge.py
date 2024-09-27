import sys

def build_dp(seq):
    '''
        Construye el vector de una manera parecida a lo que vimos de RSQ en clase
    '''
    DP = [0] * len(seq)
    
    for I in range(1, len(seq)):
        if seq[I] == seq[I-1]:
            DP[I] = DP[I-1] + 1
        else:
            DP[I] = DP[I-1]

    return DP

seq = sys.stdin.readline() # Leo la secuencia de caracteres

queries = int(sys.stdin.readline()) # La cantidad de veces que voy a tener que leer dos rangos

DP = build_dp(seq) # Obtengo el vector ya construido

for _ in range(queries):
    line = sys.stdin.readline()
    l, r = map(int, line.split())
    
    sys.stdout.write((f"{DP[r-1] - DP[l-1]} \n"))
