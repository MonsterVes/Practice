def average(array):
    dist_height = set(array)
    return sum(dist_height)/len(dist_height)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)