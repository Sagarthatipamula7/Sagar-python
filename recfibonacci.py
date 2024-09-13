def fibonacci_series(n):
    if n<=1:
        return n
    else:
         return(fibonacci_series(n-1)+fibonacci_series(n-2))
    
for i in range(10):
    print(fibonacci_series(i))