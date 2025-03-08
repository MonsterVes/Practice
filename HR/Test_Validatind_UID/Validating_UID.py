def main():
    T = int(input())
    list_of_uids = []
    results_list = []
     
    while T > 0:
        uid = input()
        list_of_uids.append(uid)
        T -= 1

    for item in list_of_uids:
        if is_valid(item) and repeat_check(item,list_of_uids):
            results_list.append("Valid")
        else:
            results_list.append("Invalid")
    
    print(results_list)


def is_valid(s):
    if not (s.isalnum() and len(s) == 10 and len(s) == len(set(s))):
        return False
    list_UID = list(s[::1])
    alpha_check = 0
    digit_check = 0
    while alpha_check < 2 and digit_check < 3:
        for i in list_UID:
            if i.isalpha().isupper():
                alpha_check += 1
            elif i.isdigit():
                digit_check += 1
            else:
                continue
    return True

def repeat_check(uid, l):
    if uid not in l:
        return True

                
    
main()  