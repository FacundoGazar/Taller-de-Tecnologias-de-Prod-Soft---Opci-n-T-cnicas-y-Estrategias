import sys
from heapq import *

def find_type(n):
    '''
        Retorna el string del tipo de estructura de datos que logró descifrar
    '''
    
    is_queue = is_stack = is_pqueue = True
    pqueue_list = []
    stack_list = []
    queue_list = []
    
    cant = 0
        
    for I in range(n):
        command_list = list(map(int, sys.stdin.readline().split()))
        if command_list[0] == 1:
            if is_queue:
                queue_list.append(command_list[1])
            if is_stack:
                stack_list.append(command_list[1])
            if is_pqueue:
                heappush(pqueue_list, -command_list[1])
            cant+= 1
        else:
            if cant == 0:
                is_queue = is_stack = is_pqueue = False
            else:
                if is_queue and command_list[1] != queue_list.pop(0):
                    is_queue = False
                if is_stack and command_list[1] != stack_list.pop():
                    is_stack = False
                if is_pqueue and heappop(pqueue_list) != -command_list[1]:
                    is_pqueue = False
                cant -= 1
    
    if not is_queue and not is_stack and not is_pqueue:
        return "impossible"
    elif is_queue and not is_stack and not is_pqueue:
        return "queue"
    elif is_stack and not is_queue and not is_pqueue:
        return "stack"
    elif is_pqueue and not is_queue and not is_stack:
        return "priority queue"
    else:
        return "not sure"

for line in sys.stdin:
    sys.stdout.write(find_type(int(line))