#Kerwin Rounds Jr
#Program A


N = int(input("Enter a number: "))

def ColCon(N):
    Count = 0
    while N > 1:
        if N % 2 == 0:
            N = N / 2
            Count+=1
            print('{}. {}'.format(Count,N))

        else:
            N = N * 3 + 1
            Count+=1
            print('{}. {}'.format(Count,N))
         
ColCon(N)
        
        
        
