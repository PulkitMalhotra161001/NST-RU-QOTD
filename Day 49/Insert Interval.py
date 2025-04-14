https://my.newtonschool.co/playground/code/8i8c1rbe5a1k


def insert(intervals, new_interval):
    res = []
    i = 0
    n = len(intervals)
    
    # Case 1: No overlapping case before the merge intervals
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1
    
    # Case 2: Overlapping case and merging of intervals
    while i < n and new_interval[1] >= intervals[i][0]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    res.append(new_interval)
    
    # Case 3: No overlapping of intervals after new interval being merged
    while i < n:
        res.append(intervals[i])
        i += 1
    
    return res
