A = set(map(int, input().split()))
n = int(input())
result = []
for inst in range(0,n):
    new_set = set(map(int, input().split()))
    if A.issuperset(new_set):
        result.append(1)
    else:
        result.append(0)
 
if 0 in result:
    print(False)
else:
    print(True)