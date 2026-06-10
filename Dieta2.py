N, M = map(int, input().split())

P = [int(x) for x in input().split()][:N]
G = [int(x) for x in input().split()][:N]
C = [int(x) for x in input().split()][:N]

tta = (sum(P) * 4) + (sum(G) * 8) + (sum(C) * 4)

print(max(0, M - tta))
