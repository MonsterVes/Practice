N = int(input())
countries = set()
while N > 0:
    countries.add(input())
    N-=1
print(len(countries))