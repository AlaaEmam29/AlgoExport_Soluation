def longestPeak(array):
    #O(n) Time | O(1) Space
    longestPeak = 0
    
    for i in range(1,len(array)-1):
        isPeak = array[i-1] < array[i] > array[i + 1]
        if not isPeak:
            continue
        leftLongestPeak = i - 2
        while leftLongestPeak >=0 and array[leftLongestPeak] < array[leftLongestPeak + 1]:
            leftLongestPeak -= 1
        rightLongestPeak = i + 2
        while rightLongestPeak < len(array) and array[rightLongestPeak] < array[rightLongestPeak - 1]:
            rightLongestPeak += 1
        currentPeak = rightLongestPeak - leftLongestPeak-1
        longestPeak = max(currentPeak , longestPeak)
    return longestPeak

        
        
        
            
            
        
  