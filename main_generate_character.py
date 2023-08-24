import random
import pandas as pd
import inclusive_range

def roll_1d(n):
    roll = random.randint(1, n)
    return roll

def roll_nd(n,x):
    rolls=[]

    for i in range(0,n):
        roll_i=roll_1d(x)
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
def get_occupation():

    data={
        "1": ["Alchemist","Staff","Oil, 1 flask"],
        "2": ["Animal trainer", "Club", "Pony"],
        "03-04": ["Armorer","Hammer (as club)","Iron helmet"],
        "5": ["Astrologer","Dagger","Spyglass"],
        "06-08": ["Blacksmith","Hammer (as club)","Steel tongs"],
        "09-10": ["Caravan guard","Short sword","Linen, 1 yard"],
        "11": ["Cobbler","Awl (as dagger)","Shoehorn"],
        "12": ["Confidence artist","Dagger","Quality cloak"],
        "13": ["Cooper","Crowbar (as club)","Barrel"],
        "14-15": ["Cutpurse","Dagger","Small chest"],
        "16-17": ["Ditch digger","Shovel (as staff)","Fine dirt, 1 lb"],
        "18-21": ["Dwarven blacksmith","Hammer (as club)","Mithril, 1 oz."],
        "22-23": ["Dwarven herder","Staff","Sow**"],        
        "24-27": ["Dwarven miner","Pick (as club)","Lantern"],
        "28-31": ["Elven artisan","Staff","Clay, 1 lb."],
        "32-35": [" Elven forester"," Staff"," Herbs, 1 lb."],
        "36-37": [" Elven sage","Dagger","Parchment and quill pen"],
        "38-47": [" Farmer*"," Pitchfork (as spear)"," Hen**"],
        "48": [" Fortune-teller"," Dagger"," Tarot deck"],
        "49": [" Gambler"," Club"," Dice"],
        "50": [" Gongfarmer"," Trowel (as dagger)"," Sack of night soil"],
        "51-52": [" Grave digger"," Shovel (as staff)"," Trowel"],
        "53-54": [" Guild beggar"," Sling"," Crutches"],
        "55-58": [" Halfling gypsy"," Sling"," Hex doll"],
        "59-62": [" Halfling trader"," Short sword"," 20 sp"],
        "63-64": [" Halfling vagrant"," Club"," Begging bowl"],
        "65": [" Healer"," Club"," Holy water, 1 vial"],
        "66": [" Herbalist"," Club"," Herbs, 1 lb."],
        "67-69": [" Herder"," Staff"," Herding dog**"],
        "70-72": [" Hunter"," Shortbow"," Deer pelt"],
        "73": [" Indentured servant"," Staff"," Locket"],
        "74": [" Jester"," Dart"," Silk clothes"],
        "75": [" Jeweler"," Dagger"," Gem worth 20 gp"],
        "76": [" Locksmith"," Dagger"," Fine tools"],
        "77": [" Mercenary"," Longsword"," Hide armor"],
        "78": [" Miller/baker"," Club"," Flour, 1 lb."],
        "79": [" Minstrel"," Dagger"," Ukulele"],
        "80": [" Noble"," Longsword"," Gold ring worth 10 gp"],
        "81": [" Orphan"," Club"," Rag doll"],
        "82": [" Ostler"," Staff"," Bridle"],
        "83": [" Outlaw"," Short sword"," Leather armor"],
        "84": [" Scribe"," Dart"," Parchment, 10 sheets"],
        "85": [" Shaman"," Mace"," Herbs, 1 lb."],
        "86": [" Slave"," Club"," Strange-looking rock"],
        "87": [" Smuggler"," Sling"," Waterproof sack"],
        "88-89": [" Soldier"," Spear"," Shield"],
        "90-91": [" Squire"," Longsword"," Steel helmet"],
        "92-93": [" Trapper"," Sling"," Badger pelt"],
        "94": [" Urchin"," Stick (as club)"," Begging bowl"],
        "95": [" Wainwright"," Club"," Pushcart***"],
        "96": [" Weaver"," Dagger"," Fine suit of clothes"],
        "97": [" Wizard’s apprentice"," Dagger"," Black grimoire"],
        "98-100": [" Woodcutter"," Handaxe"," Bundle of wood"]}

    return data
    
def get_random_equipment():
    data= {
        1: "Backpack",
        2: "Candle",
        3: "Chain, 10’",
        4: "Chalk, 1 piece",
        5: "Chest, empty",
        6: "Crowbar",
        7:"Flask, empty",
        8:"Flint & steel",
        9:"Grappling hook",
        10:"Hammer, small",
        11:"Holy symbol",
        12:"Holy water, 1 vial**",
        13:"Iron spikes, each",
        14:"Lantern",
        15:"Mirror, hand-sized",
        16:"Oil, 1 flask***",
        17:"Pole, 10-foot",
        18:"Rations, per day",
        19:"Rope, 50’",
        20:"Sack, large",
        21:"Sack, small",
        22:"Thieves’ tools",
        23:"Torch, each",
        24:"Waterskin"}

    score=roll_1d(len(data))
    return data[score]

def get_birth_augur_and_lucky_roll():

    data={
        1: ["Harsh winter"," All attack rolls"],
        2: ["Taurus"," Melee attack rolls"],
        3: ["Fortunate date"," Missile fire attack rolls"],
        4: ["Raised by wolves"," Unarmed attack rolls"],
        5: ["Conceived on horseback"," Mounted attack rolls"],
        6: ["Born on the battlefield"," Damage rolls"],        
        7: ["Path of the bear"," Melee damage rolls"],
        8: ["Hawkeye"," Missile fire damage rolls"],
        9: ["Pack hunter"," Attack and damage rolls for 0-level trained weapon"],
        10: ["Born under the loom"," Skill checks (including thief skills)"],
        11: ["Foxs cunning"," Find/disable traps"],
        12: ["Four-leafed clover"," Find secret doors"],
        13: ["Seventh son"," Spell checks"],
        14: ["The raging storm"," Spell damage"],
        15: ["Righteous heart"," Turn unholy checks"],
        16: ["Survived the plague"," Magical healing"],
        17: ["Lucky sign"," Saving throws"],
        18: ["Guardian angel"," Savings throws to escape traps"],
        19: ["Survived a spider bite"," Saving throws against poison"],
        20: ["Struck by lightning"," Reflex saving throws"],
        21: ["Lived through famine"," Fortitude saving throws"],
        22: ["Resisted temptation"," Willpower saving throws"],
        23: ["Charmed house"," Armor Class"],
        24: ["Speed of the cobra"," Initiative"],
        25: ["Bountiful harvest"," Hit points (applies at each level)"],
        26: ["Warrior’s arm"," Critical hit tables**"],
        27: ["Unholy house"," Corruption rolls"],
        28: ["The Broken Star"," Fumbles**"],
        29: ["Birdsong"," Number of languages"],
        30: ["Wild child"," Speed (each +1 = +5’ speed)"]}

    score=roll_1d(len(data))
    [birth_augur, lucky_roll]=data[score]

    return [birth_augur, lucky_roll]


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


 
     [score,rolls]=roll_nd(3,6)

     modifier=ability_score_to_modifier(score)
     spells_known=ability_score_to_spells_known(score)

     record_i={"name": ability_i,
               "score": score,              
               "modifier": modifier,
               "spells_known":spells_known,
                "rolls": rolls}
     
     
     list_of_dicts.append(record_i)

 df_ability_scores=pd.DataFrame(list_of_dicts)

 print(df_ability_scores)

 print("")
 
 #luck_score=roll_1d(30)

 
 [birth_augur,lucky_roll]=get_birth_augur_and_lucky_roll()

 #print(f"luck_score={luck_score}", end="\t")
 print(f"birth_augur={birth_augur}")
 print(f"lucky_roll={lucky_roll}")


 equipment=get_random_equipment()
 print(f"equipment={equipment}")
