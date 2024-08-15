'''
two sum
nums=[5,5]
target=10
'''
def twoSum(nums: List[int], target: int) -> List[int]:
        current_sum = 0
        n = 1
        for i in range(len(nums)):
            for j in range(n, len(nums)):
                current_sum = nums[i] + nums[j]
                if current_sum == target:
                    return [i, j]

            n += 1
        
        return [0, 0]
    
nums = [5, 5]
target = 10

result = twoSum(nums, target)