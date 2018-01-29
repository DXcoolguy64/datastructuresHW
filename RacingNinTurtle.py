from turtle import *

#Donny = Turtle()

#Donny.forward(100)
#Donny.left(30)
#Donny.forward(100)



#Create a simulation that predicts what turtle will win the race
#Donny runs 15% faster than an average turtle but has to wait half a second whenever he turns
#Mikey is on his skateboard so he moves at 40% incresed speed


class RacingTurtle:
    def __init__(self, speed, turnlag, name):
        self.name = name
        self.turt = turtle.Turtle()
        self.speed = 20 * (1 + speed/100)
        self.turnlag = 0 + turnlag

    def getX(self):
        return self.turt.xcor()
    def getY(self):
        return self.turt.ycor()

    def forward(self, distance):
        """moves turtle forward speed * distance"""

        self.turt.forward(distance * self.speed)

Mikey = RacingTurtle(0,0,"Mikey")
Donny = RacingTurtle(15,0.5,"Donny")
MasterSplinter = RacingTurtle(40,0,"Master Splinter")

    def turnRight(degrees)

        self.turt.right(degrees)
        sleep(self.turnlag)

    def turnLeft(degrees)

        self.turt.left(degrees)
        sleep(self.turnlag)


Mikey.turt.penup()
Mikey.turt.sety( 50)
Mikey.turt.pendown()


while (Mikey.getX() < 100):
    turtle.forward(1)
    




while True:
    Mikey.forward(5)
    Donny.forward(1)

    if Mikey.turt.x > 100: #fix
        print(Mikey.name, "Wins Cowabunga")

def runRace(rt):
    startTime = time.clock()


    rt.forward(100,rt)


def runForward(dist, rt):
    turnlag = 100 * (1 - rt.speed/100)

    for i in range (turnlag):
        rt.forward()
