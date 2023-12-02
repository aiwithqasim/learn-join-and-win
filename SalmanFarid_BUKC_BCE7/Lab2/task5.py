import re

def count_ant(input_string):
    match = re.findall(r'a[a-z]t', input_string)
    
    return len(match)

input_string = "ant, art, act, agt, dant, dart"
count = count_ant(input_string)
print(count)