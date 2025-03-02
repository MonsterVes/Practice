n = int(input())
s = set(map(int, input().split()))
moves = int(input())

while moves > 0:
    user_input = list(input().split(" "))
    if len(user_input) > 1:
        action, number = user_input  
        num = int(number)
    else:
        action = user_input[0]
        num = None


    if action == "discard":
        s.discard(num)
    elif action == "pop":
        s.pop()
    elif action == "remove":
        s.remove(num)
    
    moves-=1

print(sum(s))