def f(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    elif (n==2):
        return f(1)+f(0)
    else:
        return f(n-1)+f(n-2)
print("Fabonacci Series - ",f(0),f(1),f(2),f(3),f(4),f(5),f(6),f(7),f(8),f(9),f(10))

