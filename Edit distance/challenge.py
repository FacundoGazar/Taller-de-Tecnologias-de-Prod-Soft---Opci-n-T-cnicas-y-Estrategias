import sys

def ED(to_convert, reference):
    '''
        Devuelve la cantidad de operaciones minimas para convertir el argumento a en el argumento b
    '''
    n = len(to_convert) + 1
    m = len(reference) + 1
    
    memo = [[0 for row in range(m)] for column in range(n)]
    
    for I in range(n):
        memo[I][0] = I
    for J in range(m):
        memo[0][J] = J
        
    for I in range(n):
        for J in range(m):
            if to_convert[I-1] == reference[J-1]:
                memo[I][J] = memo[I-1][J-1]
            else:
                memo[I][J] = min(
                    memo[I-1][J],
                    memo[I][J-1],
                    memo[I-1][J-1]
                ) + 1

    return memo[n-1][m-1]

test_cases = int(sys.stdin.readline())

for _ in range(test_cases):
    to_convert = sys.stdin.readline()
    reference = sys.stdin.readline()
    
    sys.stdout.write(f"{ED(to_convert, reference)}\n")
