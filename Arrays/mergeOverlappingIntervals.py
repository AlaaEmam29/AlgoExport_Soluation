def mergeOverlappingIntervals(intervals):
    #O(nlog(n)) T | O(n) Space
    intervals =  sorted(intervals , key = lambda x : x[0])
    currIntervals = intervals[0]
    merge = []
    merge.append(currIntervals)
    for i in range(len(intervals)):
        f ,s = intervals[i]
        endinCurr= currIntervals[1]
        if endinCurr  >= f:
             currIntervals[1] = max(endinCurr , s) 
        else:
             currIntervals = intervals[i]
             merge.append(currIntervals)
    return     merge

             
            
        