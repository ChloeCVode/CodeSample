#  https://www.codewars.com/kata/57f2b753e3b78621da0020e8
#  Rules^

def simplify(examples,formula):
    equations_dict = {}

    for i in range(len(examples)):
        where_equalmark = examples[i].find("=")

        # We create dictionary that stores information about variables for example {b:2a}

        key = examples[i][-1]
        equations_dict[key] = "("+examples[i][:where_equalmark - 1]+")"

    # This will swap our variables in formula based on our dictionary

    for i in range(len(examples)):
        for word, replacement in equations_dict.items():
            formula = formula.replace(word, replacement)

    # This checks if string element [i] is alphabetical letter (after equation is fixed to 1 variable only)

    our_variable = []
    for i in range(len(formula)):
        x = formula[i].isalpha()
        if x == True:
            our_variable.append(formula[i])



    # Few changes so "eval" method will read string equation correctly

    for i in range(len(formula)-1):
        i1 = formula[i].isnumeric()
        i2 = formula[i+1].isalpha()
        if i1 == True and i2 == True:
            formula=formula.replace(formula[i]+formula[i+1],formula[i]+"*"+formula[i+1])
    formula = formula.replace("4a","4*a")
    formula = formula.replace(" ", "")
    formula = formula.replace("-(","-1*(")
    formula = formula.replace("0(","0*(")
    formula = formula.replace("1(","1*(")
    formula = formula.replace("2(","2*(")
    formula = formula.replace("3(","3*(")
    formula = formula.replace("4(","4*(")
    formula = formula.replace("5(","5*(")
    formula = formula.replace("6(","6*(")
    formula = formula.replace("7(","7*(")
    formula = formula.replace("8(","8*(")
    formula = formula.replace("9(","9*(")


    formula = formula.replace(our_variable[0],"a")


    # Final point we use eval function which solves 1 variable equation

    a=1

    Result= eval(formula)
    Result_and_variable = "".join(str(Result)+our_variable[0])
    formula = [Result_and_variable]
    return formula[0]


