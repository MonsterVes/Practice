T = int(input())
result = []
for inst in range(0,T):
    A_count = input()
    A = set(map(int, input().split()))
    B_count = input()
    B = set(map(int, input().split()))
    result.append(A.issubset(B))

for i in result:
    print(i)
