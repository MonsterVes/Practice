number_of_elements_in_A = int(input())
A = set(map(int,input().split()))

number_of_other_sets = int(input())

while number_of_other_sets > 0:
    action_and_set_len = input().split(" ")
    action, lenght = action_and_set_len
    len = int(lenght)
    setN = set(map(int,input().split()))

    if action == "intersection_update":
        A.intersection_update(setN)
    elif action == "update":
        A.update(setN)
    elif action == "symmetric_difference_update":
        A.symmetric_difference_update(setN)
    elif action == "difference_update":
        A.difference_update(setN)
    
    number_of_other_sets -= 1

print(sum(A))
    


