def fib(n):
    arr = [0,1]   #los primeros dos 0 y 1
    while(len(arr) < n+1):
        arr.append(0)
    
    if(n <= 1):
        return n
    else:
        if(arr[n-1] == 0):
            arr[n-1] = fib(n-1)
        if(arr[n-2] == 0):
            arr[n-2] = fib(n-2)
        
        arr[n] = arr[n-2] + arr[n-1]
    return arr[n]


print(fib(32))

    
