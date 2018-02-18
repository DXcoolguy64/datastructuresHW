#Kerwin Rounds Jr.
# Program B


from timeit import default_timer as timer


#Recursive
def Fibonacci(n):
    if n==1 or n==2:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

for i in range(1,100):
    print(Fibonacci(i))

start = timer()
end = timer()
print (end - start)

#Non Recursive(Loop) #Tutor help
def LoopFib(n):
    x,y = 1,1
    for i in range(n-1):
        x,y = y, x+y
        return x

for i in range(1,100):
    print(LoopFib(i))   


start2 = timer()
end2 = timer()
print (end2 - start2)




    
