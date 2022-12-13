#  https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/python
#  Rules there^

# From what I remember this task was tricky because it wasn't just about creating a game, it was about accepting
# class input and starting from different positions.

# We create class to make objects with their turn and position on map

class Player:
    def __init__(self, turn, x):
        self.turn = turn
        self.x = x

player_1 = Player(True, 0)
player_2 = Player(False, 0)

# Then we create official class SnakeLadders which has method play but if we put turn and x in this class's init,
# site won't let us pass. So we have class Player to make object to use, and SnakeLadders class to zero their value
# and so site can use our play method

class SnakesLadders:

    def __init__(self):
        player_1.x = 0
        player_2.x = 0
        player_1.turn = True
        player_2.turn = False



    def play(self, die1, die2):
        self.die1 = die1
        self.die2 = die2

        if player_1.turn:

            # if player 2 won, don't continue

            if (player_2.x == 100):
                return "Game over!"

            # sum the dice and overwrite x as x+sum

            sum_of_dice = die1 + die2
            player_1.x += sum_of_dice

            # if x>100 then we have to bounce back as it is written in the rules

            if player_1.x > 100:
                over_100 = player_1.x - 100
                player_1.x -= 2 * over_100

            # Then there is main point of the game, snake and ladders so if we step on for example 51 ladder should take
            # us to x=67, we will use dictionaries to make it happen

            snake_and_ladder_dict = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98,
                                     87: 94,16: 6, 46: 25, 49: 11,62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}

            if player_1.x in snake_and_ladder_dict.keys():
                player_1.x = snake_and_ladder_dict[player_1.x]


            # If we have both dice with same number on them then same person should throw again

            if (die1 != die2):
                player_1.turn = False
                player_2.turn = True

            # Normally creating a game you would put there condition for program to throw again if dice are identical
            # as else statement but in this case game do this for us.

            if (player_1.x == 100):
                return "Player 1 Wins!"
            else:
                return "Player 1 is on square " + str(player_1.x)

        else:

            if (player_1.x == 100):
                return "Game over!"


            sum_of_dice = die1 + die2
            player_2.x += sum_of_dice

            if player_2.x > 100:
                over_100 = player_2.x - 100
                player_2.x -= 2 * over_100

            snake_and_ladder_dict = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98,
                                     87: 94, 16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75,
                                     99: 80}

            if player_2.x in snake_and_ladder_dict.keys():
                player_2.x = snake_and_ladder_dict[player_2.x]



            if (die1 != die2):
                player_1.turn = True
                player_2.turn = False

            if (player_2.x == 100):
                return "Player 2 Wins!"
            else:
                return "Player 2 is on square " + str(player_2.x)

            
            
            
