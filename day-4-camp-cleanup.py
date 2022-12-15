

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

    # It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.
    #
    # In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:
    #
    # 5-7,7-9 overlaps in a single section, 7.
    # 2-8,3-7 overlaps all of the sections 3 through 7.
    # 6-6,4-6 overlaps in a single section, 6.
    # 2-6,4-8 overlaps in sections 4, 5, and 6.
    # So, in this example, the number of overlapping assignment pairs is 4.
    #
    # In how many assignment pairs do the ranges overlap?

answer_part_two()

