#  Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.


def move_zeros(lst):
    Count_zeros = 0

    # We create for loop to count zeros in array, then we will delete every zero and add it to the end.

    for i in range(len(lst)):
        if lst[i] == 0:
            Count_zeros += 1
    for i in range(Count_zeros):
        lst.remove(0)

    for i in range(Count_zeros):
        lst.append(0)
    return lst



