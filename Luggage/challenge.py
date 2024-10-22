import sys


def knapsack(n, k):
    
    DP = [[0 for row in range(k+1)] for column in range(len(n)+1)]

    for i in range(1, len(n)+1):
        for j in range(1, k+1):
            if n[i - 1] > j:
                DP[i][j] = DP[i - 1][j]
            else:
                DP[i][j] = max(
                    DP[i - 1][j],
                    DP[i - 1][j - n[i - 1]] + n[i - 1],
                )

    return DP[len(n)+1 - 1][k]


test_cases = int(sys.stdin.readline().strip())

for _ in range(test_cases):
    n = list(map(int, sys.stdin.readline().split()))
    k = sum(n) / 2
    
    if not k.is_integer():
        output = "NO"
    else:
        output = "YES" if knapsack(n, int(k)) == k else "NO"
    
    sys.stdout.write(f"{output}\n")