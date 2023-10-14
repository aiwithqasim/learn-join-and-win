#DANIA SAMI AI AND MACHINE LEARNING LAB 02 TASK NO 05
import re

def ant_count(input_string):
    match = re.findall(r'a[a-z]t', string)
    
    return len(match)

string = "apt, alt, ant, act, art"
result = ant_count(string)
print(f"String: {string}")
print(f"Count = {result}")