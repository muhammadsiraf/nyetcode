'''
two sum
nums=[5,5]
target=10
'''
def twoSum(nums: list[int], target: int) -> list[int]:
        current_sum = 0
        n = 1
        for i in range(len(nums)):
            for j in range(n, len(nums)):
                current_sum = nums[i] + nums[j]
                if current_sum == target:
                    return [i+1, j+1]

            n += 1
        
        return [0, 0]
    
nums = [1,2,3,4]
target = 3

result = twoSum(nums, target)
print(result)