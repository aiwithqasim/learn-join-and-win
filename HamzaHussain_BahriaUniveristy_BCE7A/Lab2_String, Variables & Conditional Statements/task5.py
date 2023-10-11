def count_ant_strings(input_string):
    count = 0

    for i in range(len(input_string) - 2):
        if input_string[i] == 'a' and input_string[i + 2] == 't':
            count += 1

    return count


input_string = "Antandart"
result = count_ant_strings(input_string)
print("String:", input_string)
print("Output: count =", result)
