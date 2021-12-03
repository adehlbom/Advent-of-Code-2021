
    
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
            
    f.close()
    return c

def sumThreeIndices():
    with open('./1/input.txt') as f:
        list = []
        c = 0

        for line in f:
           list.append(line.rstrip())
        
        while(len(list)>=6):
            sum1 = int(list[0]) + int(list[1]) + int(list[2])
            sum2 = int(list[1]) + int(list[2]) + int(list[3])

            if(sum2>sum1):
                c+=1
            
           
            list.pop(0)


        f.close()
        return c  

print(sumThreeIndices())







