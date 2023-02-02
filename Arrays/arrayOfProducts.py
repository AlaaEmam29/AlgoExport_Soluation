def arrayOfProducts(array):
    #O(N)TS
    nums = [1 for _ in range(len(array))]
    leftproduct , rightProduct = 1 , 1
    for i in range(len(array)):
        nums[i] = leftproduct
        leftproduct *= array[i]
    for i in reversed(range(len(array))):
        nums[i] *= rightProduct
        rightProduct *= array[i]
    return nums
        