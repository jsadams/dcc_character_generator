import random
import pandas as pd

def roll_d(n):
    roll = random.randint(1, n)
    return roll

def roll_ndx(n,x):
    rolls=[]

    for i in range(0,n):
        roll_i=roll_d(x)
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

def ability_score_to_modifier(score):
    data={ 3: -3,
           4: -2,
           5: -2,
           6: -1,
           7: -1,
           8: -1,
           9:  0,
           10: 0,
           11: 0,
           12: 0,
           13: 1,
           14: 1,
           15: 1,
           16: 2,
           17: 2,
           18: 3}

    return data[score]

def ability_score_to_spells_known(score):
    data={ 3: -999,
           4: -2,
           5: -2,
           6: -1,
           7: -1,
           8:  0,
           9:  0,
           10: 0,
           11: 0,
           12: 0,
           13: 0,
           14: 1,
           15: 1,
           16: 2,
           17: 2,
           18: 2}

    return data[score]



if __name__ == '__main__':

 abilities=["Strength", "Agility", "Stamina","Personality","Intelligence","Luck"]

 list_of_dicts=[]
 
 for i, ability_i in enumerate(abilities):
     #print(f"i={i} = ",end='')
     #print(f"x={x_i}")


 
     [score,rolls]=roll_ndx(3,6)

     modifier=ability_score_to_modifier(score)
     spells_known=ability_score_to_spells_known(score)

     record_i={"name": ability_i,
               "score": score,              
               "modifier": modifier,
               "spells_known":spells_known,
                "rolls": rolls}
     
     
     list_of_dicts.append(record_i)

     


 df=pd.DataFrame(list_of_dicts)

 print(df)
 
