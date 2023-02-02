def zeroSumSubarray(nums):
    #O(N)TS
        res = 0
        sumMap = {0 : 1}
        currSum = 0
        for num in nums:
            currSum += num
            res += sumMap.get(currSum , 0)
            sumMap[currSum] = sumMap.get(currSum , 0) + 1
        return res > 0