#Kerwin Rounds Jr
#Apples Program


def Program():
    Prices = [14,6,9,7,8,10,3,9]
    Limit = 100
    a = 0
    b = 0

    for i in range(len(Prices)):
        Apples = 100/Prices[i]
        if(i < 7):
            Profit = Apples * Prices[i + 1]
            a = Profit
            if a > b:
                a = b
                c = Prices[i]
                d = Prices[i + 1]

            print(Profit)

    print("The best profit is " , b , " , by buying at " , c , " and selling at " , d)
Program()        

