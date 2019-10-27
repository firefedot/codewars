def sum_of_intervals(intervals):
    # print('l: ',(intervals[1][1]))
    for i in range(len(intervals)):
        if i < (len(intervals)-1) and intervals[i + 1][0] >= intervals[i][1]:
            print(intervals[i],intervals[i + 1])
        print(f'{intervals[i]} min: {min(intervals[i][:])}, max: {max(intervals[i][:])} interval: ', intervals[i][1]-intervals[i][0])
    return



print(sum_of_intervals([(1, 5), (6, 10)]))
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))