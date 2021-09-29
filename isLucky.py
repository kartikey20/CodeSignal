def isLucky(n):
    num_arr = [int(x) for x in str(n)]
    mid = len(num_arr) // 2
    return sum(num_arr[:mid]) == sum(num_arr[mid:])
