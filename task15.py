#  https://www.codewars.com/kata/5263c6999e0f40dee200059d
#  Rules ^

def get_pins(observed):

    # Create dictionary for every possible mistake in code detective might've seen

    possibilities = []
    leng = len(observed)
    possible_mistakes = {"1":["1","2","4"],"2":["1","2","3","5"],"3":["2","3","6"],"4":["1","4","5","7"],"5":["2","4","5","6","8"],"6":["3","5","6","9"],"7":["4","7","8"],"8":["0","5","7","8","9"],"9":["6","8","9"],"0":["0","8"]}


    # Create list of all possible variations for our PIN

    if leng == 1:
        for i in possible_mistakes.get(observed[0]):
            possibility = (str(i))
            possibilities.append(possibility)
    if leng == 2:
        for i in possible_mistakes.get(observed[0]):
            for j in possible_mistakes.get(observed[1]):
                possibility = (str(i) + str(j))
                possibilities.append(possibility)
    if leng == 3:
        for j in possible_mistakes.get(observed[0]):
            for k in possible_mistakes.get(observed[1]):
                for l in possible_mistakes.get(observed[2]):
                    possibility = (str(j) + str(k) + str(l))
                    possibilities.append(possibility)
    if leng == 4:
        for j in possible_mistakes.get(observed[0]):
            for k in possible_mistakes.get(observed[1]):
                for l in possible_mistakes.get(observed[2]):
                    for m in possible_mistakes.get(observed[3]):
                            possibility = (str(j) + str(k) + str(l) + str(m))
                            possibilities.append(possibility)
    if leng == 5:
        for j in possible_mistakes.get(observed[0]):
            for k in possible_mistakes.get(observed[1]):
                for l in possible_mistakes.get(observed[2]):
                    for m in possible_mistakes.get(observed[3]):
                        for n in possible_mistakes.get(observed[4]):
                            possibility = (str(j) + str(k) + str(l) + str(m) + str(n))
                            possibilities.append(possibility)
    if leng == 6:
        for j in possible_mistakes.get(observed[0]):
            for k in possible_mistakes.get(observed[1]):
                for l in possible_mistakes.get(observed[2]):
                    for m in possible_mistakes.get(observed[3]):
                        for n in possible_mistakes.get(observed[4]):
                            for b in possible_mistakes.get(observed[5]):
                                possibility = (str(j) + str(k) + str(l) + str(m) + str(n) + str(b))
                                possibilities.append(possibility)
    if leng == 7:
        for j in possible_mistakes.get(observed[0]):
            for k in possible_mistakes.get(observed[1]):
                for l in possible_mistakes.get(observed[2]):
                    for m in possible_mistakes.get(observed[3]):
                        for n in possible_mistakes.get(observed[4]):
                            for b in possible_mistakes.get(observed[5]):
                                for v in possible_mistakes.get(observed[6]):
                                    possibility = (str(j) + str(k) + str(l) + str(m) + str(n) + str(b) + str(v))
                                    possibilities.append(possibility)
    if leng == 8:
        for j in possible_mistakes.get(observed[0]):
            for k in possible_mistakes.get(observed[1]):
                for l in possible_mistakes.get(observed[2]):
                    for m in possible_mistakes.get(observed[3]):
                        for n in possible_mistakes.get(observed[4]):
                            for b in possible_mistakes.get(observed[5]):
                                for v in possible_mistakes.get(observed[6]):
                                    for c in possible_mistakes.get(observed[7]):
                                        possibility = (str(j) + str(k) + str(l) + str(m) + str(n) + str(b) + str(v) + str(
                                            c))
                                        possibilities.append(possibility)

    # Check for duplicates

    for i in range(len(possibilities)-1):
        if possibilities[i] == possibilities[i+1]:
            possibilities.pop(i)

    return possibilities