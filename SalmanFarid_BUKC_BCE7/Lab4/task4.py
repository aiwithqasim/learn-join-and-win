def reverse_words_in_string(input_string):

    words = input_string.split()

    reversed_words = words[::-1]

    reversed_string = ' '.join(reversed_words)

    return reversed_string

def main():

    input_string = input("Enter a long string with multiple words: ")

    reversed_string = reverse_words_in_string(input_string)

    print("Reversed string with words in backward order:")
    print(reversed_string)

if __name__ == "__main__":
    main()