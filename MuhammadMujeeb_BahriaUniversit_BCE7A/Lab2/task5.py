def count_ant_occurrences(input_string):
    count = sum(1 for i in range(len(input_string) - 2) if input_string[i:i+3].lower() == 'ant')
    print(f"count = {count}")

# Sample Run
count_ant_occurrences("Antandart")
