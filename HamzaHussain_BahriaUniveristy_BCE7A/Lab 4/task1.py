from collections import Counter

data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

print(sorted_data)
