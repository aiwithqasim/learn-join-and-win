from collections import Counter

counter = Counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})

sorted_value = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))

for key, value in sorted_value.items():
    print(f'{key}: {value}')