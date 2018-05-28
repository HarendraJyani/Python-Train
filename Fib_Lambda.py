cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a= 0
    b = 1
    i = 2
    if(n==0):
        d = []
    elif(n==1):
        d = [a]
    else:
        d= [a,b]
        while(i < n):
            c = a+b
            d.append(c)
            a = b
            b = c
            i += 1
    return d
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
