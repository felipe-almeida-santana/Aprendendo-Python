N, M = map(int, input().split())
P = int(input());
G = int(input());
C = int(input());
tt=(P*4)+(G*9)+(C*4);
print (max(0,tt-M))
