import sys

# IMPORTANTE, NO FUNCIONA Y NO ENTIENDO POR QUE (me da el mismo output que los casos de udebug). SERA CONSULTADO HOY MISMO SI ME DAN BOLA

def LCS(tile_a, tile_b):
    '''
        Devuelve la longitud de la subsecuencia mas comun
    '''
    # Inicializo la dimension fisica de la columna y la fila, + 1 por el caso de null
    n = len(tile_a) + 1
    m = len(tile_b) + 1
    
    # Creo la matriz toda en 0 porque la vamos a usar como matriz contador
    memo = [[0 for row in range(m)] for column in range(n)]
    
    # Ahora la recorro y voy contando en la matriz
    for I in range(1, n):
        for J in range(1, m):
            if tile_a[I-1] == tile_b[J-1]:  # Si coinciden sumo 1 a la posicion actual + el diagonal para atras arriba de donde estoy parado
                memo[I][J] = memo[I-1][J-1] + 1
            else:   # Si no son iguales me quedo con el maximo entre arriba o a la izq
                memo[I][J] = max(memo[I-1][J], memo[I][J-1])
                
    return memo[n-1][m-1]

sequence = 1
while True:
    number_of_tiles = list(map(int, sys.stdin.readline().split()))
    
    if 0 in number_of_tiles:
        break
    
    tile_a = list(map(int, sys.stdin.readline().split()))
    tile_b = list(map(int, sys.stdin.readline().split()))
    
    sys.stdout.write(f"Twin Towers #{sequence}\n")
    sys.stdout.write(f"Number of Tiles : {LCS(tile_a, tile_b)}\n")
    