#Kerwin Rounds Jr.
#Read and Write file program


kFile = input("What is the name of the file? ")

rFile = open(kFile, "r")

wFile = open("Knuckles.txt","w")

Count = 0


for sentence in rFile:
    Count = Count + 1
    List = str(Count) + " " + sentence
    kFile.close()
    wFile.close()
 
