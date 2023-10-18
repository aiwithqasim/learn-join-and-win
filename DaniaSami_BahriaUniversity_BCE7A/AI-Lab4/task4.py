#DANIA SAMI AI AND MACHINE LEARNING LAB 04 TASK NO 04
def reversed_string(input_string):
    # Split the input string into words
    splited_string = input_string.split()

    # Reverse the order of the words
    reversed_words = splited_string[::-1]

    # Join the reversed words to form a new string
    updated_string = ' '.join(reversed_words)

    return updated_string

def main():
    # Ask the user for input
    input_string = input("Enter a string with different words: ")

    # Call the function to reverse the words
    updated_string = reversed_string(input_string)

    # Print the reversed string
    print("Reversed string:")
    print(updated_string)

if __name__ == "__main__":
    main()