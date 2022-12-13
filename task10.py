#  Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it,
#  is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
#   Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
#  A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
#  (contributing to the 500 points) or as a single 50 points, but not both in the same roll.



def score(dice):
    points = 0

    # So first thing first we have to check what numbers are on top of our dice.

    how_many_1s = dice.count(1)
    how_many_6s = dice.count(6)
    how_many_5s = dice.count(5)
    how_many_4s = dice.count(4)
    how_many_3s = dice.count(3)
    how_many_2s = dice.count(2)

    # Then we create dictionary with matching points for every time we got "one" on top of a die.
    # (!remember to add 0 as option otherwise you will raise an error)

    points_for_1s = {0:0,1:100,2:200,3:1000,4:1100,5:1200}
    few_points = points_for_1s[how_many_1s]

    # We need to add these few_points to our sum of points

    points += few_points

    # Some numbers like 6 get you points only if you got 3 of them:

    if how_many_6s >= 3:
        points += 600


    points_for_5s = {0:0 ,1: 50, 2: 100, 3: 500, 4: 550, 5: 600}
    few_points = points_for_5s[how_many_5s]

    points += few_points


    if how_many_4s >= 3:
        points += 400


    if how_many_3s >= 3:
        points += 300


    if how_many_2s >= 3:
        points += 200


    return points
