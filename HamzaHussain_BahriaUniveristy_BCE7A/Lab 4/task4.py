def reverse_words_order(input_string):
    words = input_string.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

user_input = input("Enter a long string containing multiple words: ")
result = reverse_words_order(user_input)
print("Output:", result)
