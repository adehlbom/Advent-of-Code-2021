from re import U, match
from typing import Match

def part_one():
    with open('./2/input.txt') as f:
        list = []
        forward = []
        up = []
        down = []
        for line in f:
            list.append(line.rstrip().split(" "))
            
        for value in list:
            
            for item in value:
                match item:
                    case "forward":

                        forward.append(int(value[1]))
                    case "up":
                        up.append(int(value[1]))
                    case "down":
                        down.append(int(value[1]))
    return sum(forward)*(sum(down)-sum(up))
print(part_one())
    

                    

        

   

