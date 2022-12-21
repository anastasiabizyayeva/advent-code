
def answer_part_one():
    with open('day-8-input.txt', 'r') as f:

        data = list(list(int(n) for n in line.rstrip()) for line in f)

        # determine the outer bounds - first row, last row. First in row, last in row
        first_row = 0
        last_row = len(data) - 1

        first_in_row = 0
        last_in_row = len(data[0]) - 1

        visible_trees = 0

        for index, tree_row in enumerate(data):
            for index_two, tree in enumerate(tree_row):
                # add every tree in the first row and last row to the visible trees count
                if index == first_row or index == last_row or index_two == first_in_row or index_two == last_in_row:
                    visible_trees += 1
                else:
                    shorter_in_row_left = [tree_bro for tree_bro in tree_row[:index_two] if tree_bro < tree]
                    shorter_in_row_right = [tree_bro for tree_bro in tree_row[index_two+1:] if tree_bro < tree]
                    shorter_in_column_above = []
                    shorter_in_column_below = []
                    for index_three, tree_row_again in enumerate(data):
                        if index_three < index:
                            if tree_row_again[index_two] < tree:
                                shorter_in_column_above.append(tree_row_again[index_two])
                        else:
                            if tree_row_again[index_two] < tree:
                                shorter_in_column_below.append(tree_row_again[index_two])

                    left_in_row = index_two-first_in_row
                    right_in_row = last_in_row - index_two

                    above_in_column = index-first_row
                    below_in_column = last_row-index

                    if left_in_row == len(shorter_in_row_left):
                        print(f"Tree {tree} in position {index}, {index_two} is exposed on the left with {shorter_in_row_left}!")
                        visible_trees += 1
                        continue
                    elif right_in_row == len(shorter_in_row_right):
                        print(f"Tree {tree} in position {index}, {index_two} is exposed on the right with {shorter_in_row_right}!")
                        visible_trees += 1
                        continue
                    elif above_in_column == len(shorter_in_column_above):
                        print(f"Tree {tree} in position {index}, {index_two} is exposed from above with {shorter_in_column_above}!")
                        visible_trees += 1
                        continue
                    elif below_in_column == len(shorter_in_column_below):
                        print(f"Tree {tree} in position {index}, {index_two} is exposed from below with {shorter_in_column_below}!")
                        visible_trees += 1
                        continue

                    print(f"\n\n")

        print(visible_trees)

        # answer was 1794
        # time to answer was 46:04


def answer_part_two():
    with open('day-8-input.txt', 'r') as f:

        data = list(list(int(n) for n in line.rstrip()) for line in f)

        # determine the outer bounds - first row, last row. First in row, last in row
        first_row = 0
        last_row = len(data) - 1

        first_in_row = 0
        last_in_row = len(data[0]) - 1

        highest_scenic_score = 0

        for index, tree_row in enumerate(data):
            for index_two, tree in enumerate(tree_row):
                # add every tree in the first row and last row to the visible trees count
                if index == first_row or index == last_row or index_two == first_in_row or index_two == last_in_row:
                    continue
                else:
                    endpoint_left = [ind for ind, x in enumerate(tree_row[:index_two]) if x >= tree]
                    endpoint_right = [ind for ind, x in enumerate(tree_row) if x >= tree and ind > index_two]

                    if len(endpoint_left) > 0:
                        left_calc = index_two - endpoint_left[-1]
                    else:
                        left_calc = index_two - first_in_row

                    if len(endpoint_right) > 0:
                        right_calc = endpoint_right[0] - index_two
                    else:
                        right_calc = last_in_row - index_two

                    above_calc = index - first_row
                    below_calc = last_row - index

                    index_diff_above = 10000
                    index_diff_below = 10000
                    for index_three, tree_row_again in enumerate(data):
                        if index_three < index:
                            difference = index - index_three
                            if tree_row_again[index_two] >= tree and index_diff_above > difference:
                                index_diff_above = difference
                                above_calc = difference
                        elif index_three > index:
                            difference = index_three - index
                            if tree_row_again[index_two] >= tree and index_diff_below > difference:
                                index_diff_below = difference
                                below_calc = difference
                        else:
                            continue

                    tree_visibility = left_calc * right_calc * above_calc * below_calc
                    print(f"Calc options  for tree {tree} in {index}, {index_two} are {left_calc} * {right_calc} * {above_calc} * {below_calc}, giving us {tree_visibility}")

                    if tree_visibility > highest_scenic_score:
                        highest_scenic_score = tree_visibility

        print(f"The best tree visibility score is {highest_scenic_score}")

        # answer was 199272