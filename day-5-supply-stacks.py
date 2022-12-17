import pandas as pd


def part_one():
    with open("day-5-input.txt") as f:
        stacks_str, procedures = f.read().split("\n\n")

        print(stacks_str)

        stack_list = stacks_str.splitlines()

        stack_list = [stack + "   " if len(stack) < 34 else stack for stack in stack_list]

        instructions = procedures.splitlines()

        initial_stacking = create_stacks(stack_list)

        final_top = get_transformations(initial_stacking, instructions)

        print(final_top)
        # answer is LJSVLTWQM
        # took 500 years


def part_two():
    with open("day-5-input.txt") as f:
        stacks_str, procedures = f.read().split("\n\n")

        print(stacks_str)

        stack_list = stacks_str.splitlines()

        stack_list = [stack + "   " if len(stack) < 34 else stack for stack in stack_list]

        instructions = procedures.splitlines()

        initial_stacking = create_stacks(stack_list)

        final_top = get_transformations_9001(initial_stacking, instructions)

        print(final_top)
        # answer is BRQWDBBJM
        # took 1 second


def get_transformations_9001(initial_stacking, instructions):

    for command in instructions:
        number_crates_moved = int(command.split()[1])
        from_position = int(command.split()[3]) - 1  # to transform to index position - from 1 to 0 for example
        to_position = int(command.split()[5]) - 1

        new_from = initial_stacking[from_position][:-number_crates_moved] # for the boxes from the 'from' instruction,
        from_position_movement = initial_stacking[from_position][-number_crates_moved:]
        new_to = initial_stacking[to_position] + from_position_movement

        initial_stacking[from_position] = new_from
        initial_stacking[to_position] = new_to

        print(f"For {command} the old positions were {initial_stacking[from_position]} and {initial_stacking[to_position]}")
        print(f"New positions are {new_from} and {new_to}")

    final_top = ''
    for stack in initial_stacking:
        final_top += stack[-1]

    return final_top


def get_transformations(initial_stacking, instructions):

    for command in instructions:
        number_crates_moved = int(command.split()[1])
        from_position = int(command.split()[3]) - 1  # to transform to index position - from 1 to 0 for example
        to_position = int(command.split()[5]) - 1

        new_from = initial_stacking[from_position][:-number_crates_moved] # for the boxes from the 'from' instruction,
        from_position_movement = initial_stacking[from_position][-number_crates_moved:][::-1]
        new_to = initial_stacking[to_position] + from_position_movement

        initial_stacking[from_position] = new_from
        initial_stacking[to_position] = new_to

        print(f"For {command} the old positions were {initial_stacking[from_position]} and {initial_stacking[to_position]}")
        print(f"New positions are {new_from} and {new_to}")

    final_top = ''
    for stack in initial_stacking:
        final_top += stack[-1]

    return final_top


def create_stacks(stack_list):

    initial_stacking = [""]*9  # 9 stacks we need to populate

    for box_row in range(len(stack_list)-2, -1, -1):  # start with the length of the list -2 (taking out the row with the box numbers, and decrease by 1 (reversing through list)
        # print(stack_list[box_row])
        for specific_box in range(1, len(stack_list[8]), 4):
            # print(specific_box)
            if stack_list[box_row][specific_box] != " ":
                initial_stacking[specific_box//4] += stack_list[box_row][specific_box]

    return initial_stacking


part_two()