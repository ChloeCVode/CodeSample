#  Return the number (count) of vowels in the given string.
#  We will consider a, e, i, o, u as vowels for this Kata (but not y).
#  The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"

    count1 = sentence.count(a)
    count2 = sentence.count(e)
    count3 = sentence.count(i)
    count4 = sentence.count(o)
    count5 = sentence.count(u)

    def add(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
    return (add(count1,count2,count3,count4,count5))




