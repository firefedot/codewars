# def count_squares(cuts):
#     # your code here
#     return x       # an integer number


cuts = 4
one_side = (cuts+1)**2
gran = 4*cuts
noconflict_side = 6*(one_side - gran)
all_gran = 4*gran-(cuts+1)*4+noconflict_side

print(f'tiles one side: {one_side}')
print(f'Gran only: {gran}')
print(all_gran)
print(noconflict_side)