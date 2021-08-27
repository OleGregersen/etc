# complete the lambda function 
cube = lambda x: x ** 3 

def fibonacci(n):
    # return a list of fibonacci numbers
    l = [0, 1]
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])
        
    return(l[0:n])

