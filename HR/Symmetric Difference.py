M = int(input())
a = set(map(int,input().split(" ")))

N = int(input())
b = set(map(int,input().split(" ")))

sorted = sorted(a.symmetric_difference(b))
for i in sorted:
    print(i)

