#  https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
#  Rules^


def solution(args):
    solution = args
    # We need this huge number for i to not run out of range for last numbers in order, it might be an issue for
    # numbers close to this big one but as long as we are far from this number program should work fine.
    solution.append(9999999999999999999999999999999)

    def interval(solution):
        temporary_interv_list = []
        Final_string = ''


        for i in range(len(solution)-1):

            if abs(solution[i]-solution[i+1]) == 1:

                temporary_interv_list.append(solution[i])    # We add this append here and below, and decide in conditions
                                                             # if we cut it into 1number long piece or for example 3number long piece

                # Condition that add single numbers to our final string (1number long piece)

                if abs(solution[i + 1] - solution[i + 2]) != 1 and len(temporary_interv_list) == 1:
                    Final_string += "," + str(temporary_interv_list[0])
                    temporary_interv_list = []


            else:
                if bool(temporary_interv_list) == True:

                    temporary_interv_list.append(solution[i])

                    # Condition to create interval, taking first and last numbers from temporary list 1,2,3,4 = "1-4"

                    Final_string+= ","+str(temporary_interv_list[0])+"-"+str(temporary_interv_list[-1])
                    temporary_interv_list = []


                # Similar condition above, is as if difference between numbers i and i+1 is 1 but next difference is not equal to 1
                # in this case it's just for single numbers which that differences between number to the right and left aren't equal to 1

                elif abs(solution[i]-solution[i+1]) != 1:
                    Final_string += str("," + str(solution[i]))

        Final_string = Final_string[1:]
        return Final_string





    Final_string = interval(solution)
    return Final_string

