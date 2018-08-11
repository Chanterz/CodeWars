from itertools import product


def roll_dice_sum_prob(sum_, dice_amount):
    return len(list(filter(lambda x: x == sum_,
                           map(sum,
                               product(*([[1, 2, 3, 4, 5, 6]] * dice_amount)))
                           )
                    )
               ) / 6 ** dice_amount
