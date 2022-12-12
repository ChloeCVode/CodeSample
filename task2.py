#   Your task is to implement an algorithm that is able to execute the Twenty-One Card Trick. To simplify things,
#   the cards will be changed to the set of integers between 1 and 21(inclusive).
#   The function will be passed as argument a member of the audience that has selected a certain card and has a method
#   get_input that receives a list of 3 lists as arguments and returns the index of the column containing the selected card.

import random

DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
random.shuffle(DECK)


def guess_the_card(audience):
    DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    # audience = Audience(13)
    for i in range(3):
        a = DECK[0:21:3]
        b = DECK[1:21:3]
        c = DECK[2:21:3]
        print(a, b, c)

        x = audience.get_input([a, b, c])

        if x == 0:
            b.extend(a)
            b.extend(c)
            DECK = b
        elif x == 1:
            a.extend(b)
            a.extend(c)
            DECK = a
        else:
            a.extend(c)
            a.extend(b)
            DECK = a
    return DECK[10]


