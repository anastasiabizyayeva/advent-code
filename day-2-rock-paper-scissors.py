import pandas as pd

df = pd.read_csv('day-2-input.txt', sep=' ')


# part 1
def answer_part_one():

    point_mapping = {
        'A': 1,  # rock
        'B': 2,  # paper
        'C': 3,  # scissors
        'X': 1,  # rock
        'Y': 2,  # paper
        'Z': 3  # scissors
    }

    win_for_opponent = ['AZ', 'BX', 'CY']
    win_for_me = ['CX', 'AY', 'BZ']
    draw = ['AX', 'BY', 'CZ']

    final_score = 0

    for index, row in df.iterrows():

        opponent_move = row['opponent']
        my_move = row['me']
        item_chosen_points = point_mapping[my_move]

        combined_move = opponent_move + my_move

        if combined_move in win_for_me:
            print(f"Win for me with {combined_move}!")

            my_score = 6

        elif combined_move in draw:
            print(f"Draw for me with {combined_move}!")

            my_score = 3

        else:
            print(f"Loss for me with {combined_move}!")

            my_score = 0

        total_round_score = item_chosen_points + my_score
        print(total_round_score)

        final_score += total_round_score

    print(final_score)

    # answer was 13446
    # time to solve was 14:45


def answer_part_two():

    final_score = 0

    winning_points = {'A': 8, 'B': 9, 'C': 7}
    losing_points = {'A': 3, 'B': 1, 'C': 2}
    drawing_points = {'A': 4, 'B': 5, 'C': 6}

    for index, row in df.iterrows():

        opponent_move = row['opponent']
        round_ending = row['me']

        if round_ending == 'X':
            # this means I need to lose
            round_points = losing_points[opponent_move]
        elif round_ending == 'Y':
            # this means I have to draw
            round_points = drawing_points[opponent_move]
            print(f"Round ending is {round_ending}, opponent move is {opponent_move}, and my points are {drawing_points[opponent_move]}")

        else:
            # this means I have to win
            round_points = winning_points[opponent_move]

        final_score += round_points

    print(final_score)

    # answer is 13509


answer_part_two()
