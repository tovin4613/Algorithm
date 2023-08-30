import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N) :
    order = str(input().rstrip())
    order_split = order.split(' ')
    
    if order_split[0] == 'push' :
        arr.append(int(order_split[1]))
    elif order_split[0] == 'pop' :
        if len(arr) == 0 :
            print(-1)
        else :
            print(arr.pop())
    elif order_split[0] == 'size' :
        print(len(arr))
    elif order_split[0] == 'empty' :
        print(1 if len(arr) == 0 else 0)
    elif order_split[0] == 'top' :
        if len(arr) == 0 :
            print(-1)
        else :
            print(arr[-1])
            
