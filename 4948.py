while 1:
    n = int(input())
    if n == 0:
        break
    
    for num in range(n + 1, 2*n + 1):
        count = 0
        res = 0
        for i in range(2, num):
            if num % i == 0:
                count += 1
        print(count)
        if count == 0:
            res += 1
    print(res)