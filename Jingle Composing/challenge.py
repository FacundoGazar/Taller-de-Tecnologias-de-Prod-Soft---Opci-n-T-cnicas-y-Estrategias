import sys

def read_comp():
    '''
        Lee las composicion ingresada, sacandole el salto de linea al final (rstrip) y pasando los measures a lista con el split
    '''
    aux_str = sys.stdin.readline().rstrip().split("/")
    
    if aux_str[0] == "*":
        return None
    else:
        return aux_str

dic_notes = {
    "W" : 1,
    "H" : 0.5,
    "Q" : 0.25,
    "E" : 0.125,
    "S" : 0.0625,
    "T" : 0.03125,
    "X" : 0.015625
}

while True:
    composition = read_comp()
    
    if composition is None:
        break
    
    cant = sum(1 for measure in composition[1:-1] if sum(dic_notes[note] for note in measure) == 1)
        
    sys.stdout.write(str(cant) + "\n")