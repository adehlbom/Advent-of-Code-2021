#Use the binary numbers of input.txt to create 2 new binary numbers; epsilon_rate and gamma_rate

#Gamma rate is calculated from the most common bit on each index from all of the sample data.

#Epsilon rate is calculated from the least common bits on each index so the inverse of gamma rate.

#the output sought after is the gamma rate * epsilon rate in decimal which gives the power consumption





def part_one():

    with open('./3/input.txt') as f:
        list = [line.rstrip() for line in f]
       

    #can use 2 for loops to iterate first through the binary numbers and then through the bit values of the binary value
        gammaArray = [0]*len(list[0])
        gamma_output = ""
        epsilon_output = ""
        epsilonArray = [0]*len(list[0])
        #first add all the values on the corresponding index giving a total of 0->length of the binary value
        for binary in list:
            for index,bit in enumerate(binary):
                gammaArray[index]+=int(bit)

                #sumArray[index]+=int(bit)
        #then check if the total sum of the bits are higher or lower than the total number of binary values
        for index,value in enumerate(gammaArray):
            if(gammaArray[index] > len(list)/2):
                gammaArray[index] = 1
            else:
                gammaArray[index] = 0
        #now when we have the gamma value we can reverse this with a simple match 
        for index,value in enumerate(gammaArray):
            match(value):
                case 1:
                    epsilonArray[index] = 0
                    epsilon_output += str(epsilonArray[index])

                case 0:
                    epsilonArray[index] = 1
                    epsilon_output += str(epsilonArray[index])
            
            gamma_output += str(value)
            
    return int(gamma_output,2)*int(epsilon_output,2)

           
              


print(part_one())