#  Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.
#  If the digits can't be rearranged to form a bigger number, return -1




# Whole idea of this program is that if n=549652 we have to find the the spot where number to right is larger than
# number to left which is there =   5<49>652,   then we have to find minimally larger number to the right from 4.
#                    5 4 <96 <5> 2>  and put swap their order  55<9642> now we sort our digits in
#                   triangular bracket, and that's how you find next bigger number


def next_bigger(n):

    #  n is our input: number

    n = str(n)
    numbers_separated = []


    for number in n:
        numbers_separated.append(number)

    # This function is there to check if such number might even exist

    def if_exist():
        smallest_number = int(numbers_separated[-1])

        for i in range(len(numbers_separated)):
            if int(numbers_separated[-i-1]) >= smallest_number:
                smallest_number = int(numbers_separated[-i-1])
            else:
                return True
        return False


    if_exist = if_exist()

    if if_exist == False:
        return -1

    def Find_index():

        for i in range(len(n)):

            #  Checking from the end if last number is bigger than second to last etc etc, if so we return the
            #  index of the one to the left

            if int(numbers_separated[-i - 1]) - int(numbers_separated[-i - 2]) > 0:

                index = -i - 2

                return index

    index = Find_index()

    if len(numbers_separated) >2:

        diffs = []
        for i in numbers_separated[index:]:
            if int(i) > int(numbers_separated[index]):
                difference = -(int(numbers_separated[index])-int(i))
                diffs.append(difference)

        our_number_index = numbers_separated.index(str(int(numbers_separated[index])+min(diffs)),index)
        our_number = numbers_separated.pop(our_number_index)
        numbers_separated.insert(index+1,our_number)
        beginning = numbers_separated[0:index+1]
        end = numbers_separated[index+1:]
        end.sort()

        #  Part above was described before, part below is just converting strings into int


        next_bigger = "".join(beginning)+"".join(end)
        next_bigger = int(next_bigger)
        return next_bigger
    else:
        next_bigger = "".join(numbers_separated[1])+"".join(numbers_separated[0])
        next_bigger = int(next_bigger)
        return next_bigger
    
    
    
