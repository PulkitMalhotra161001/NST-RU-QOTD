https://my.newtonschool.co/playground/code/2w5umym69zjn


def remove_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])
    prev_end = intervals[0][1]
    res = 0
    for i in range(1, len(intervals)):
        if prev_end > intervals[i][0]:
            res += 1
        else:
            prev_end = intervals[i][1]
    return res
