
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29


def row_sum_odd_numbers(n):
    index = n*(n-1)+1
    end = index + 2*(n-1)
    r = index+end
    for odds in range((index+2), end, 2):
        r += odds
    if n == index:
        r = n
    return r


print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(3))
print(row_sum_odd_numbers(4))
print(row_sum_odd_numbers(5))
print(row_sum_odd_numbers(13))
