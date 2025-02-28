n = int(input())

def print_formatted(number1):
    w = len(bin(n)[2:])
    for number in range(1,n+1):

        print(f"{number:>{w}} {oct(number)[2:]:>{w}} {str(hex(number)).upper()[2:]:>{w}} {bin(number)[2:]:>{w}}")

print_formatted(n)