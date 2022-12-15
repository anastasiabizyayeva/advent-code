

def answer_part_one():
    with open('day-4-input.txt') as f:
        lines = f.read()
        cleanup_groups = lines.split('\n')

        overlapping_group_count = 0

        for cleanup_group in cleanup_groups:
            first_elf = cleanup_group.split(',')[0]
            second_elf = cleanup_group.split(',')[1]

            first_range_start = int(first_elf.split('-')[0])
            first_range_finish = int(first_elf.split('-')[1]) + 1
            first_range = list(range(first_range_start, first_range_finish))

            second_range_start = int(second_elf.split('-')[0])
            second_range_finish = int(second_elf.split('-')[1]) + 1
            second_range = list(range(second_range_start, second_range_finish))

            check_one = all(item in first_range for item in second_range)
            check_two = all(item in second_range for item in first_range)

            if check_one is True or check_two is True:
                overlapping_group_count += 1

        print(overlapping_group_count)

    # answer is 490
    # time to solve was 9:30


def answer_part_two():

    with open('day-4-input.txt') as f:
        lines = f.read()
        cleanup_groups = lines.split('\n')

        overlapping_group_count = 0

        for cleanup_group in cleanup_groups:
            first_elf = cleanup_group.split(',')[0]
            second_elf = cleanup_group.split(',')[1]

            first_range_start = int(first_elf.split('-')[0])
            first_range_finish = int(first_elf.split('-')[1]) + 1
            first_range = list(range(first_range_start, first_range_finish))

            second_range_start = int(second_elf.split('-')[0])
            second_range_finish = int(second_elf.split('-')[1]) + 1
            second_range = list(range(second_range_start, second_range_finish))

            check_one = any(item in first_range for item in second_range)
            check_two = any(item in second_range for item in first_range)

            if check_one is True or check_two is True:
                overlapping_group_count += 1

        print(overlapping_group_count)

        # answer is 921
        # time to solve was 1:00

answer_part_two()

