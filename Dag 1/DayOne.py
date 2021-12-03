f = open('input.txt')

c = 0
    
def countDepth():
    global c
    for line in f:
        currentNumber = int(line.rstrip()) 
        if(int(line.rstrip())<=currentNumber):
            c+=1
        else:    
            currentNumber = line.rstrip()



countDepth()

print(c)

        

        







