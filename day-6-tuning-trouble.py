
def answer_part_one():
    with open("day-6-input.txt") as f:
        instructions = f.read()

        letter_list = list(instructions)
        n = len(letter_list)

        for i in range(0,n):
            window = letter_list[i:i+4]
            if len(set(window)) == 4:
                print(window)
                print(i+4)
                break

        # answer is 1987
        # time to solve was 5:00


def answer_part_two():
    with open("day-6-input.txt") as f:
        instructions = f.read()

        letter_list = list(instructions)
        n = len(letter_list)

        for i in range(0, n):
            window = letter_list[i:i + 14]
            if len(set(window)) == 14:
                print(window)
                print(i + 14)
                break

        # answer is 3059
        # time to solve was 30 seconds