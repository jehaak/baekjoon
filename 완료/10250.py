T = int(input())

for i in range(T):
    H, W, N = map(int, input().split(' '))
    floor = N % H
    num = N // H + 1
    if floor == 0:
        floor = H
        num -= 1
    
    print(f'{floor}{num:02}')

