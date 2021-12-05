#Use the binary numbers of input.txt to create 2 new binary numbers; epsilon_rate and gamma_rate

#Gamma rate is calculated from the most common bit on each index from all of the sample data.

#Epsilon rate is calculated from the least common bits on each index so the inverse of gamma rate.

#the output sought after is the gamma rate * epsilon rate in decimal which gives the power consumption





def part_one():

    with open('./3/input.txt') as f:
        list = [int(line,2) for line in f]
    
    #can use 2 for loops to iterate first through the binary numbers and then through the bit values of the binary value
        gammaArray = [0]*len(list[0])
        gamma_output = ""
        epsilon_output = ""
        epsilonArray = [0]*len(list[0])
        #first add all the values on the corresponding index giving a total of 0->length of the binary value
        for binary in list:
            for index,bit in enumerate(binary):
                gammaArray[index]+=int(bit)

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

           



#multiply oxygen generator rating with CO2 scrubber rating
#oxygen value = most common bit in that position, equal = 1
#CO2 value = least common bit, equal = 0

#so I can check for sum > len/2 to determine if I want to keep 0 or 1 for each bit in the number
#if less pop else do nothing and keep doing that until 1 number is left

def part_two():
    with open('./3/input.txt') as f:
        list = [line.rstrip() for line in f]
        oxygen_sheet = [0]*len(list[0])
        scrubber_sheet = [0]*len(list[0])
        oxygen_list = list.copy()
        scrubber_list = list.copy()

        for binary in list:
            for o,bit in enumerate(binary):
                oxygen_sheet[o]+=int(bit)
                #print(index)
        #determines the most common value and saves that to oxygen_sheet, the inverse is saved to scrubber_sheet
        
        for i,bit in enumerate(oxygen_sheet):
            if(int(oxygen_sheet[i])>=len(list)/2):
                oxygen_sheet[i]=1
                scrubber_sheet[i] = 0
            else: 
                oxygen_sheet[i] = 0
                scrubber_sheet[i] = 1
        print(len(oxygen_list))
        print(len(scrubber_list))
        carl = ""
        for x in oxygen_sheet:
            carl+=str(x)

            

        #nested for loop to match the most common bit value with the bit value from the list and remove if it does not match. 
        #111010001010
        #[1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
        #for binary in list:
            #for bit_index,bit in enumerate(binary):
                #if(oxygen_sheet[bit_index] != int(bit) and len(oxygen_list)>0):
                    #this should remove the binary value from the scrubber list that matches the oxygen sheet cheat
                    #oxygen_list.pop(oxygen_list.index(binary))
                    #print(binary)
                #if(scrubber_sheet[bit_index] != int(bit) and len(scrubber_list)>0):
                    #this should remove the binary value from the scrubber list that matches the oxygen sheet cheat
                    #scrubber_list.pop(scrubber_list.index(binary))
                   #print(binary)
        print(oxygen_list.index(carl))

                    
                    
       
        
   
             
       
        
                
                
        
        





print(part_two())