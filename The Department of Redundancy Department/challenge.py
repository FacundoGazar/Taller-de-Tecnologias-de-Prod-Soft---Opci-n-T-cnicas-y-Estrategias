from collections import Counter
import sys

aux = sys.stdin.read().strip()
    
seq_list = list(map(int, aux.split()))

occurrences = Counter(seq_list)
    
rep = set()
    
for I in seq_list:
    if I not in rep:
        sys.stdout.write(f"{I} {occurrences[I]}\n")
        rep.add(I)