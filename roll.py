import random
import pandas as pd
import inclusive_range
import re

def roll(roll_string):
    [n_dice,n_sides]=roll_string_to_n_dice_and_n_sides(roll_string)

    return roll_ndx(n_dice=n_dice,n_sides=n_sides)

def roll_string_to_n_dice_and_n_sides(roll_string):
    
    pattern = re.compile(r"(\d+)d(\d+)")
    match = pattern.match(roll_string)

    if match:
        n_dice = int(match.group(1))
        n_sides = int(match.group(2))
    else:

        pattern = re.compile(r"d(\d+)")
        match = pattern.match(roll_string)

        if match:
            n_dice = 1
            n_sides = int(match.group(1))
        else:

            pattern = re.compile(r"(\d+)")
            match = pattern.match(roll_string)

            if match:
                n_dice = 1
                n_sides = int(match.group(1))

            else:

                raise("Can't parse string {roll_string}")
                
    #print("Number of dice:", n_dice)
    #print("Number of sides:", n_sides)
        
    return [n_dice,n_sides]
        
def roll_1d(n_sides):
    roll = random.randint(1, n_sides)
    return roll

def roll_ndx(n_dice,n_sides):
    rolls=[]

    for i in range(0,n_dice):
        roll_i=roll_1d(n_sides)
        rolls.append(roll_i)

    s=sum(rolls)
    return [s,rolls]

########################################
#
#
#   main
#
#
########################################

if __name__ == '__main__':



    roll_string="3d6"

    [n_dice,n_sides]=roll_string_to_n_dice_and_n_sides(roll_string)

    print(f"n_dice={n_dice}")
    print(f"n_sides={n_sides}")

    [score,rolls]=roll_ndx(3,6)
    

    print(f"score={score}")
    print(f"rolls={rolls}")

    
    s="3d6"

    
