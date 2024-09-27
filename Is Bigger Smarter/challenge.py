import sys

def lengthOfLIS(seq):
    '''
        Devuelve una lista de los índices que forman la subsecuencia creciente más larga.
    '''
    n = len(seq)
    LIS = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if seq[j][0] < seq[i][0] and seq[j][1] > seq[i][1]:
                if LIS[i] < 1 + LIS[j]:
                    LIS[i] = 1 + LIS[j]
                    prev[i] = j

    max_len = max(LIS)
    pos = LIS.index(max_len)

    lis_indices = []
    while pos != -1:
        lis_indices.append(pos)
        pos = prev[pos]

    lis_indices.reverse()
    return lis_indices

elephants = []
index_map = []

for idx, line in enumerate(sys.stdin):
    w, iq = map(int, line.split())
    elephants.append((w, iq, idx + 1))

elephants.sort(key=lambda x: (x[0], -x[1]))

lis_indices = lengthOfLIS(elephants)

sys.stdout.write(f"{len(lis_indices)}\n")

for id in lis_indices:
    sys.stdout.write(f"{elephants[id][2]}\n")
