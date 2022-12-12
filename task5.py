#  Johnny is a farmer and he annually holds a beet farmers convention "Drop the beet".
#  Every year he takes photos of farmers handshaking. Johnny knows that no two farmers handshake more than once.
#  He also knows that some of the possible handshake combinations may not happen.
#  However, Johnny would like to know the minimal amount of people that participated this year just by counting all the handshakes.
#  Help Johnny by writing a function, that takes the amount of handshakes and returns the minimal amount of people
#  needed to perform these handshakes (a pair of farmers handshake only once).


def get_participants(handshakes):

    counting_up_people = 0
    counting_up_handshakes = 0

    if handshakes == 0:
        return 0

    while True:
        counting_up_people += 1
        handshakes_now = counting_up_handshakes + counting_up_people - 1

        counting_up_handshakes = handshakes_now

        if handshakes <= handshakes_now:
            break
    return counting_up_people
