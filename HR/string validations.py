# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

s = input()
results = [False,False,False,False,False]

for i in s:
    if i.isalnum():
        results[0] = True
    if i.isalpha():
        results[1] = True
    if i.isdigit():
        results[2] = True
    if i.islower():
        results[3] = True  
    if i.isupper():
        results[4] = True   


for res in results:
    print(res)
