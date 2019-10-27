# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:
#
# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
# As usual, your function/method should be pure, i.e. it should not mutate the original string.


def to_alternating_case(string):
    new_string = ''
    for i in range(0,len(string)):
        if string[i].isupper():
            new_string += string[i].lower()
        elif string[i].islower():
            new_string += string[i].upper()
        else:
            new_string += string[i]

    return new_string

# string.swapcase()
print(to_alternating_case("teXt k"))
