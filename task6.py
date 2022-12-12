#  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#  Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally,
#  if the number is negative, return 0 (for languages that do have them).
#  Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    if number < 0:
        return 0
    else:
        def solution1(number):
            multiples_of3 = 0
            multiples_of3_sum = 0

            while multiples_of3 + 3 < number:
                multiples_of3 += 3
                multiples_of3_sum += multiples_of3

                # multiples_of3_sum idea is to collect sum of all appearing multiples of 3, for example number=9 , 3+6+9=18

            return multiples_of3_sum

        def solution2(number):
            multiples_of5 = 0
            multiples_of5_sum = 0

            while multiples_of5+5 < number:
                multiples_of5 += 5
                multiples_of5_sum += multiples_of5

            return multiples_of5_sum


        def find_duplicates(number):
            multiples_of3 = 0
            multiples_of5 = 0
            multiples_of3_sum = 0
            multiples_of5_sum = 0
            multiples_of3_list = []
            multiples_of5_list = []

            # Right there we calculate how many times we can multiply 3 and 5, for it to be equal or 1 step from
            # being bigger than number, so we can use this number(range) as range in for loop later on.

            range_for3 = int(float(number / 3))
            range_for5 = int(float(number / 5))

            if range_for3 * 3 == number:
                range_for3 = range_for3 - 1
            if range_for5 * 5 == number:
                range_for5 = range_for5 - 1


            for i in range(range_for3):
                multiples_of3 += 3
                multiples_of3_sum = multiples_of3

                # It's basically the same as above, and it could be done in those 2 functions up there but this way
                # it looks more clear.

                multiples_of3_list.append(multiples_of3_sum)

                # We append our numbers to list, we will do the same with multiples of 5, then we are going to
                # connect both list into one,sort this new list and look for duplicates in it.

            for i in range(range_for5):
                multiples_of5 += 5
                multiples_of5_sum = multiples_of5
                multiples_of5_list.append(multiples_of5_sum)

            multiples_connected_list = multiples_of3_list + multiples_of5_list

            multiples_connected_list.sort()

            non_unique = []
            for i in range(0, len(multiples_connected_list) - 1):
                if multiples_connected_list[i] == multiples_connected_list[i + 1]:
                    non_unique.append(multiples_connected_list[i])

            # After we have found duplicates we append one of each to our non_unique list, and sum them

            Sum_of_non_unique = sum(non_unique)

            return Sum_of_non_unique

        multiples_of3_sum = solution1(number)
        multiples_of5_sum = solution2(number)
        Sum_of_non_unique = find_duplicates(number)

        Sum_of_multiples_3_and_5 = multiples_of3_sum + multiples_of5_sum - Sum_of_non_unique

    return Sum_of_multiples_3_and_5


