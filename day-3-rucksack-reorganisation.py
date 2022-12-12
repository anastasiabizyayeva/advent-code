import string

alphabet_keys = list(string.ascii_letters)
alphabet_values = list(range(1, 53))

alphabet_points = {alphabet_keys[i]: alphabet_values[i] for i in range(len(alphabet_keys))}


def answer_part_one():
    with open('day-3-input.txt') as f:
        lines = f.read()
        rucksacks = lines.split('\n')

        total_duplicate_points = 0

        for rucksack in rucksacks:

            first_part, second_part = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]

            duplicate_letters = []
            for letter in first_part:
                if letter in second_part:
                    duplicate_letters.append(letter)

            unique_duplicates = set(duplicate_letters)

            for letter in unique_duplicates:
                total_duplicate_points += alphabet_points[letter]

        print(total_duplicate_points)

        # answer was 8039
        # time to solve was 11:30


def answer_part_two():
    with open('day-3-input.txt') as f:
        lines = f.read()
        rucksacks = lines.split('\n')

        grouped_lists = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

        total_badge_points = 0

        for rucksack_group in grouped_lists:
            first_ruck = rucksack_group[0]
            second_ruck = rucksack_group[1]
            third_ruck = rucksack_group[2]

            for letter in first_ruck:
                if letter in second_ruck and letter in third_ruck:
                    print(f"Letter {letter} is in {first_ruck}, {second_ruck}, and {third_ruck}")
                    print(f"Letter {letter} is worth {alphabet_points[letter]} points.")
                    total_badge_points += alphabet_points[letter]
                    break

        print(total_badge_points)

        # answer was 2510
        # time to solve was 6:08


answer_part_two()