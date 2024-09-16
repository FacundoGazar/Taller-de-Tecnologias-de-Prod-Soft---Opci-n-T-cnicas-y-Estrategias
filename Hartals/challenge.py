import sys

def read_stdin():
    '''
        Lee la entrada estandar, lo convierte en int y arma una lista con los hartal parameter de cada espacio politico.
    '''
    
    N = int(sys.stdin.readline()) # Numero de dias que la simulacion debe durar.
    aux = int(sys.stdin.readline()) # Numero de espacios politicos.
    
    return N, [int(sys.stdin.readline()) for num_parties in range(aux)]

def is_holiday(day):
    '''
        Empezando como si domingo fuera el dia 0, cuenta si el dia pasado como parametro es viernes o sabado
    '''
    return (day % 7 == 6) or (day % 7 == 5)

def total_hartals(N, P):
    '''
        Retorna la cantidad total de hartals en la cantidad de dias (N) teniendo en cuenta la frecuencia (P[i])
    '''
    
    aux_calendar = [0 for _ in range(N)] # Vector contador, lo inicializo en 0.

    for hartal_freq in P:
        hartal_day = hartal_freq
        while(hartal_day <= N):
            aux_calendar[hartal_day-1] = 1
            hartal_day += hartal_freq
            
    for day in range(N):
        if(is_holiday(day)):
            aux_calendar[day] = 0
    
    return sum(aux_calendar)
    
T = int(sys.stdin.readline()) # Numero de casos prueba a seguir.

for test_cases in range(T):
    N, P = read_stdin()
    sys.stdout.write(str(total_hartals(N, P)) +  "\n" )