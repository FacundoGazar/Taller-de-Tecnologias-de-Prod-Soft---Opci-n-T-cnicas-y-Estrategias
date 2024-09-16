import sys

# Leer inputs
inp_str = sys.stdin.readline()
inp_list = list(map(int, inp_str.split()))

X = inp_list[0]
Y = inp_list[1]

# Tabla de los precios pasado a lista
table = [4, 4.5, 5, 2, 1.5]

# Calculo el total segun la lista
total = table[X - 1] * Y
# Output formateado a dos decimales
sys.stdout.write(f"Total: R$ {total:.2f}" + "\n")