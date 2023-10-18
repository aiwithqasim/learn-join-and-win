def reverse_words_order(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    output_string = ' '.join(reversed_words)
    return output_string


user_input = input("Enter a long string containing multiple words: ")
result = reverse_words_order(user_input)
print("Output:", result)
