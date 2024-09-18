import sys

def read_entry():
    '''
        Lee el input en entrada estandar y lo retorna, devuelve None en caso de que no se ingrese nada
    '''
    
    aux = sys.stdin.readline().strip()
    
    if aux == "0 0":
        return None
    
    return list(map(int, aux.split()))

def read_catalog(n):
    '''
        Lee el catalogo de CDs y lo retorna como un set
    '''
    
    myset = set()
    
    for _ in range(n):
        cd_id = int(sys.stdin.readline().strip())
        myset.add(cd_id)

    return myset

while True:
    cd_cant = read_entry()
    
    if cd_cant is None:
        break
    
    jack_set = read_catalog(cd_cant[0])
    jill_set = read_catalog(cd_cant[1])
    
    sys.stdout.write(str(len(jack_set.intersection(jill_set))) + "\n")
    