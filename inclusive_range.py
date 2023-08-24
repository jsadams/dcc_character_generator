
import re

def range_string_to_inclusive_integer_range(input_string):
    """
       
        

        "1" --> range(1,2)
        
        "06-08" --> range(6,9)

    """
    
    pattern = re.compile(r"(\d+)-(\d+)")
    match = pattern.match(input_string)

    if match:
        start = int(match.group(1))
        end = int(match.group(2))
        print("Start:", start)
        print("End:", end)
    else:
        #print("No match found.")
        pattern = re.compile(r"(\d+)")
        match = pattern.match(input_string)

        if match:
            start = int(match.group(1))
            end = start
            print("Start:", start)
            print("End:", end)

        else:
            raise Exception(f"Can't parse input_string={input_string}")


    ## make range inclusive
    return range(start,end+1)


########################################
#
#
#   main
#
#
########################################


if __name__ == '__main__':


    s="10"
    r1=range_string_to_inclusive_integer_range(s)

    print(f"{s}--> {r1}")


    s="5-8"
    r1=range_string_to_inclusive_integer_range(s)

    print(f"{s}--> {r1}")
