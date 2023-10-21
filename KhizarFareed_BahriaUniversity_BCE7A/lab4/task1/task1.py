data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

sort = sorted(data.items(), key=lambda x: x[1], reverse=True)

print(sort)
