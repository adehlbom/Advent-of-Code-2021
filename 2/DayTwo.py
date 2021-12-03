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
    f.close()
    return sum(forward)*(sum(down)-sum(up))
print("part 1 depth: " + str(part_one()))
    
def part_two():
    with open('./2/input.txt') as f:
            list = []
            horizontal_pos = 0
            depth = 0
            aim = 0
            for line in f:
                list.append(line.rstrip().split(" "))
                
            for value in list:
                
                for item in value:
                    match item:
                        case "forward":
                            horizontal_pos+=int(value[1])
                            depth+=int(value[1])*aim
                        case "up":
                            aim-=int(value[1])
                        case "down":
                            aim+=int(value[1])
    f.close()
    return horizontal_pos*depth


print("part 2 depth: " + str(part_two()))        

                    

        

   

