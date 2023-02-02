def fourNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    res , quad = [] , []
    def kSum(k , start , targetSum):
      if k != 2:
        for i in range(start , len(array) - k + 1):
          if i > start and array[i] == array[i-1]:
            continue
          quad.append(array[i])
          kSum(k-1 , i+1 , targetSum - array[i])
          quad.pop()
        return
      l , r = start , len(array) - 1
      while l < r:
        currerntSum = array[l] + array[r]
        if currerntSum < targetSum:
          l += 1
        elif currerntSum > targetSum:
          r -= 1
        else:
          res.append(quad + [array[l] , array[r]])
          l += 1
          while l < r and array[l] == array[l-1]:
            l += 1
    kSum(4 , 0 , targetSum)
    return res