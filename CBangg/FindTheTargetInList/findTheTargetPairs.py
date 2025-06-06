def findTargetPairs(nums: list[int], target: int) -> list[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return sorted([i, num_dict[complement]])
        num_dict[num] = i
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(findTargetPairs(nums, target))