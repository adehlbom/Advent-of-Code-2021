
    
def countDepth():
    with open('./1/input.txt') as f:
        c = 0
        #set the value of the first index to currentNumber.
        currentNumber = int(f.readline().rstrip()) 
        #for each line
        for line in f:
            l = int(line.rstrip())
            if(l>currentNumber):
                c+=1
            currentNumber = l
            

    return c


print(countDepth())
        

        







