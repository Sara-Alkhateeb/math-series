
def fibonacci(n):
    ''' n = index of the elemnt in series
     If n =0,1 it will return it self otherwise call the function again with new n '''
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
def lucas(n):
    ''' n = index of the elemnt in series
     If n=0 return 2 and if n= 1 return 1 otherwise call the function again with new n  '''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    
    
def sum_series(n, x=0 , y=1):
    ''' (n = index of the elemnt in series, x, y = integers) ''' 

    if (x==0 and y==1):
        return fibonacci(n)

    elif (x==2 and y==1) :
        return lucas(n)

    else :
        return sum_series(n-1 , x , y)+ sum_series(n-2 , x , y)
    