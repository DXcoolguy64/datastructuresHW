#File Program


counter = 0

infile = open ("HelloWorld.py",'r')

for lines in infile.readlines():
    print(counter, lines)
    counter = counter + 1
