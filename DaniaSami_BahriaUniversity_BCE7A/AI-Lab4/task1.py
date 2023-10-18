#DANIA SAMI AI AND MACHINE LEARNING LAB 04 TASK NO 01
from collections import Counter

values = Counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})

sorted_values = dict(sorted(values.items(), key=lambda item: item[1], reverse=True))

for key, value in sorted_values.items():
    print(f'{key}: {value}')