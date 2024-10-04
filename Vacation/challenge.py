import sys

# IMPORTANTE, NO FUNCIONA Y NO ENTIENDO POR QUE. SERA CONSULTADO HOY MISMO SI ME DAN BOLA

def LCS(mom_suggestion, dad_suggestion):
    '''
        Devuelve la longitud de la subsecuencia mas comun
    '''
    # Inicializo la cantidad de columnas y filas (el orden como tenga ganas) segun la cantidad de caracteres del string, + 1 porque puede ser null
    n = len(mom_suggestion) + 1
    m = len(dad_suggestion) + 1
    
    # Inicializo toda la matriz en 0 pq es contadora
    memo = [[0 for row in range(m)] for column in
            range(n)]
    
    for I in range(1, n):
        for J in range(1, m):
            if mom_suggestion[I-1] == dad_suggestion[J-1]:
                memo[I][J] = memo[I-1][J-1] + 1 # Si hay coincidencia sumo en diagonal
            else:
                memo[I][J] = max(memo[I-1][J], memo[I][J-1]) # Me copio del maximo entre el costado y arriba
    return memo[n-1][m-1]

def read_suggestion():
    mom_suggestion = sys.stdin.readline().rstrip()
    
    if mom_suggestion == "#":
        return None, None

    dad_suggestion = sys.stdin.readline().rstrip()
    
    return mom_suggestion, dad_suggestion

sequence_case = 1
while True:
    mom_suggestion, dad_suggestion = read_suggestion()
    
    if mom_suggestion is None:
        break
    
    sys.stdout.write(f"Case #{sequence_case}: you can visit at most {LCS(mom_suggestion, dad_suggestion)} cities.\n")
    sequence_case += 1