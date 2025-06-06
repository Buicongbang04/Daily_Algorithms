def findTheThirdBiggest(nums: list[int]) -> int:
    st = nd = rd = None
    for num in nums:
        if st is None or num > st:
            rd, nd, st = nd, st, num
        elif nd is None or num > nd:
            rd, nd = nd, num
        elif rd is None or num > rd:
            rd = num
    return rd
  
# Example usage:
nums = [3, 1, 4, 5, 7, 5, 9]
print(sorted(nums))
print(findTheThirdBiggest(nums))