import sys

def read_entry():
    '''
        Lee el input en entrada estandar y devuelve None en caso de que no se ingrese nada
    '''
    
    aux = sys.stdin.readline().strip()
    
    if aux == "" or aux == "\n":
        aux = None
    
    return aux

def read_dict_entry():
    '''
        Lee las entradas del diccionario y retorna el mismo como foreign_word:english_word
    '''
    
    dict_inp = {}
    
    while True:
        inp = read_entry()
        
        if inp is None:
            break
        
        spliteado = inp.split()
        
        dict_inp[spliteado[1]] = spliteado[0]
    
    return dict_inp

dict_inp = read_dict_entry()

while True:
    msg = read_entry()
    if msg is None:
        break
    
    if msg in dict_inp.keys():
        sys.stdout.write(str(dict_inp[msg] + "\n"))
    else:
        sys.stdout.write("eh\n")