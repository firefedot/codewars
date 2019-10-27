import math

# def strong_num(number):
#     strong = 0
#     for i in range(0, len(str(number))):
#         strong += math.factorial(int(str(number)[i]))
#     return "STRONG!!!!" if strong == number else 'Not Strong !!'

def strong_num(number):
    return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(number)) == number else "Not Strong !!"

print(strong_num(145))
