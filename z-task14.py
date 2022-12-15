#  https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
#  Rules ^

def snail(snail_map):
    row_length = len(snail_map[0])

    if row_length % 2 == 0 :
        x = (row_length - 2)/2
    else:
        x = (row_length - 1)/2


    # if [[2]]

    if len(snail_map)==1:
        return [item for sublist in snail_map for item in sublist]

    # if 2x2 array

    if len(snail_map)==2:
        column_1 = snail_map[0]
        column_2 = snail_map[1]
        column_2.reverse()
        return column_1+column_2

    def form_a_snail():

        # Same as above but empty, it's useful because we will use recursion

        if snail_map == [[]]:
            return []

        row_length = len(snail_map[0])



        # We have to create frame then we will work on what's in the middle, variables are named after sides +0 as it's frame

        up0=snail_map[0]

        r_edge0 = []

        down0 = snail_map[-1]
        down0.reverse()

        l_edge0 = []

        square_inside_list = []

        for i in range(row_length-2):
            r_edge_i=snail_map[i+1][row_length-1]
            r_edge0.append(r_edge_i)

        for i in range(row_length-2):
            l_edge_i=snail_map[i+1][0]
            l_edge0.append(l_edge_i)

        l_edge0.reverse()

        square = snail_map[1:-1]

        # Options to define what's inside our shell (frame)

        if len(square) == 1:
            middle = [square[0][1]]
            part_of_whole_snail = up0+r_edge0+down0+l_edge0+middle
            print(square_inside_list, part_of_whole_snail)

            return square_inside_list, part_of_whole_snail

        elif len(square) == 2:
            middle = square[1][1:-1]
            middle.reverse()
            part_of_whole_snail = up0+r_edge0+down0+l_edge0+square[0][1:-1]+middle
            print(square_inside_list, part_of_whole_snail)

            return square_inside_list, part_of_whole_snail

        else:
            for i in range(0,row_length-2):
                square_inside = square[i][1:-1]
                square_inside_list.append(square_inside)

            part_of_whole_snail = up0+r_edge0+down0+l_edge0
            print(square_inside_list,part_of_whole_snail)

        return square_inside_list, part_of_whole_snail

    whole_snail = []

    # There we will use recursion to call function as many times as we need to create whole snail array  part after
    # part creating one "frame" after another

    for j in range(int(x)):

        form_a_snail_call = form_a_snail()

        snail_map = form_a_snail_call[0]
        part_of_whole_snail = form_a_snail_call[1]

        # And we add another layers to our snake

        whole_snail += part_of_whole_snail






    return whole_snail



