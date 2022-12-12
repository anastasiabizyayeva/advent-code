
# part 1

def answer_part_one():
    with open('day-1-input.txt') as f:
        lines = f.read()
        grouped_elves = lines.split('\n\n')

        top_elf_calories = 0

        for elf in grouped_elves:
            clean_elf_cals = list(map(int,elf.split('\n')))
            elf_total_cals = sum(clean_elf_cals)

            if elf_total_cals > top_elf_calories:
                top_elf_calories = elf_total_cals

        print(top_elf_calories)

        # answer was 71502


def answer_part_two():

    with open('day-1-input.txt') as f:
        lines = f.read()
        grouped_elves = lines.split('\n\n')

        all_cals = []

        for elf in grouped_elves:
            clean_elf_cals = list(map(int, elf.split('\n')))
            elf_total_cals = sum(clean_elf_cals)

            all_cals.append(elf_total_cals)

        sorted_cals = sorted(all_cals)

        print(sum(sorted_cals[-3:]))
        # answer is 208191