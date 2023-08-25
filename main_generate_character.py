import random
import pandas as pd
import inclusive_range
from roll import *

########################################
#
#
#   main
#
#
########################################
def get_occupation_table():

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

def get_occupation():

    score=roll_1d(100)

    data=get_occupation_table()

    for key,value in data.items():

        ### we need to convert the key to a python range
        range_i=inclusive_range.range_string_to_inclusive_integer_range(key)
        

        if score in range_i:
            #print(f"key={key} = ",end='')
            #print(f"value={value}")
            
            #print(f"score={score}")
            #print(f"range_i={range_i}")


            [occupation,trained_weapon,trade_goods]=value

            result={}
            result["Occupation"]=occupation
            result["Trained Weapon"]=trained_weapon
            result["Trade Goods"]=trade_goods
            
            return [result, score]


        
    return [{}, score]


def get_random_equipment():
    data= {
        1: "Backpack",
        2: "Candle",
        3: "Chain, 10’",
        4: "Chalk, 1 piece",
        5: "Chest, empty",
        6: "Crowbar",
        7: "Flask, empty",
        8: "Flint & steel",
        9: "Grappling hook",
        10: "Hammer, small",
        11: "Holy symbol",
        12: "Holy water, 1 vial**",
        13: "Iron spikes, each",
        14: "Lantern",
        15: "Mirror, hand-sized",
        16: "Oil, 1 flask***",
        17: "Pole, 10-foot",
        18: "Rations, per day",
        19: "Rope, 50’",
        20: "Sack, large",
        21: "Sack, small",
        22: "Thieves’ tools",
        23: "Torch, each",
        24: "Waterskin"}

    score=roll_1d(len(data))

    result={}
    result["Equipment"]=data[score]
    
    return [result, score]

def get_alignment():
    data= {
        1: "Chaotic",
        2: "Neutral",
        3: "Lawful",}

    score=roll_1d(len(data))

    result={}
    result["Alignment"]=data[score]
    
    return [result, score]

def get_sex():
    data={
        "1-47": "Male",
        "48-95": "Female",
        "96-100": "Non-Binary"}
    
    score=roll_1d(len(data))

    result={}    
    for key,value in data.items():
        ### we need to convert the key to a python range
        range_i=inclusive_range.range_string_to_inclusive_integer_range(key)   

        if score in range_i:
            result["Sex"]=value
            return [result, score]
    
    return [result, score]


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


    ### the table length should be 30
    n_sides=len(data)    
    assert(n_sides==30)


    
    score=roll_1d(n_sides)


    
    [birth_augur, lucky_roll]=data[score]

    result={}
    result["Birth Augur"]=birth_augur
    result["Lucky Roll"]=lucky_roll

    
    return [result, lucky_roll]


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

def ability_score_to_wizard_spells_known(score):
    data={ 3: "No Spellcasting Possible",
           4: "-2 Spells",
           5: "-2 Spells",
           6: "-1 Spells",
           7: "-1 Spells",
           8:  "No adjustment",
           9:  "No adjustment",
           10: "No adjustment",
           11: "No adjustment",
           12: "No adjustment",
           13: "No adjustment",
           14: "+1 Spell",
           15: "+1 Spell",
           16: "+2 Spells",
           17: "+2 Spells",
           18: "+2 Spells"}

    return data[score]

def ability_score_to_max_spell_level(score):
    data={ 3: "No Spellcasting Possible",
           4: 1,
           5: 1,
           6: 1,
           7: 1,
           8:  2,
           9:  2,
           10: 3,
           11: 3,
           12: 4,
           13: 4,
           14: 5,
           15: 5,
           16: 6,
           17: 6,
           18: 7}

    return data[score]

def get_max_cleric_spell_level(df_ability_scores):

    score=int(df_ability_scores["score"]["Personality"])

    value=ability_score_to_max_spell_level(score)
    result={"Max Cleric Spell Level": value}  
    return [result, score]


    
def get_max_wizard_spell_level(df_ability_scores):

    score=int(df_ability_scores["score"]["Intelligence"])

    value=ability_score_to_max_spell_level(score)
    result={"Max Wizard Spell Level": value}  
    return [result, score]

def get_wizard_spells_known(df_ability_scores):

    score=int(df_ability_scores["score"]["Intelligence"])

    value=ability_score_to_wizard_spells_known(score)
    result={"Wizard Spells Known": value}  
    return [result, score]


def roll_hp(df_ability_scores):

    stamina_modifier=int(df_ability_scores["modifier"]["Stamina"])

    [hp_roll,rolls]=roll("1d4")

    hp=hp_roll+stamina_modifier

    result={"hp": hp}
  
    return [result, hp_roll]

def roll_copper():

    [copper_roll,rolls]=roll("5d12")



    result={"Copper Pieces": copper_roll}
  
    return [result, copper_roll]

def generate_fixed_values():
    result={"XP": -100,
            "Attack Modifier": 0,
            "Save Modifier": 0,
            "Level": 0}
    
  
    return [result, 0]


if __name__ == '__main__':

 abilities=["Strength", "Agility", "Stamina","Personality","Intelligence","Luck"]

 list_of_dicts=[]
 
 for i, ability_i in enumerate(abilities):
     #print(f"i={i} = ",end='')
     #print(f"x={x_i}")


 
     [score,rolls]=roll("3d6")

     modifier=ability_score_to_modifier(score)

     # if ability_i == "Intelligence":
     #     wizard_spells_known=ability_score_to_wizard_spells_known(score)

     # if ability_i == "Personality":
     #     max_spell_level_cleric=ability_score_to_max_spell_level(score)

     # if ability_i == "Intelligence" or ability_i == "Personality":
     #     max_spell_level_wizard=ability_score_to_max_spell_level(score)
         
     #max_spell_level=ability_score_to_max_spell_level(score)

     
     record_i={"name": ability_i,
               "score": score,              
               "modifier": modifier,
               #"Wizard Spells Known":wizard_spells_known,
               #"Max Spell Level":max_spell_level,
                "rolls": rolls}
     
     
     list_of_dicts.append(record_i)


 df_ability_scores=pd.DataFrame(list_of_dicts)
 df_ability_scores.set_index("name",inplace=True)
 print(df_ability_scores)

 print("")

 misc_data={}
 
 # misc_data["wizard_spells_known"]=wizard_spells_known
 # misc_data["max_spell_level_wizard"]=max_spell_level_wizard
 # misc_data["max_spell_level_cleric"]=max_spell_level_cleric    
 
 
 #luck_score=roll_1d(30)

 [data,rolls]=get_wizard_spells_known(df_ability_scores)
 misc_data.update(data)

 [data,rolls]=get_max_wizard_spell_level(df_ability_scores)
 misc_data.update(data)
 
 [data,rolls]=get_max_cleric_spell_level(df_ability_scores)
 misc_data.update(data)
 
 [hp_data,hp_roll]=roll_hp(df_ability_scores)

 #print(f"hp_roll={hp_roll}")
 misc_data.update(hp_data)

 
 [birth_augur_data,lucky_roll]=get_birth_augur_and_lucky_roll()
 misc_data.update(birth_augur_data)
 # print(f"birth_augur_data={birth_augur_data}")
 #print(f"lucky_roll={lucky_roll}")

 

 [equipment_data,equipment_roll]=get_random_equipment()
 misc_data.update(equipment_data)
 
 #print(f"equipment_data={equipment_data}")
 #print(f"equipment_roll={equipment_roll}")

 [occupation_data, occupation_score]=get_occupation()
 #print(f"occupation_score={occupation_score}")
 misc_data.update(occupation_data)
 
 #print(f"occupation_data={occupation_data}")
 [copper_data, copper_roll]=roll_copper()
 misc_data.update(copper_data)

 [alignment_data, alignment_roll]=get_alignment()
 misc_data.update(alignment_data)

 [sex_data, sex_roll]=get_sex()
 misc_data.update(sex_data)

 [fixed_value_data, fixed_value_score]=generate_fixed_values()

 misc_data.update(fixed_value_data)


 ds_misc=pd.Series(misc_data)

 print(f"{ds_misc}")


 
