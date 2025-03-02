n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))

# print(len(english.union(french)))

# print(len(english.intersection(french)))

# print(len(english.difference(french)))

print(len(english.symmetric_difference(french)))

