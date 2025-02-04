# Product of Array Except Self

## Problem Statement
Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`, **without using division**.

---

## Example
### **Input:**  
```python
nums = [1, 2, 3, 4]
```
### **Output:**  
```python
output = [24, 12, 8, 6]
```
### **Explanation:**  
- `output[0] = 2 × 3 × 4 = 24`
- `output[1] = 1 × 3 × 4 = 12`
- `output[2] = 1 × 2 × 4 = 8`
- `output[3] = 1 × 2 × 3 = 6`

---

## Optimal Solution (Without Division)
To solve this efficiently in **O(n) time and O(1) space (excluding output array)**, we use **prefix and suffix products**:

### **Key Idea:**
1. Create an `output` array where:
   - `output[i]` first stores the **product of all elements to the left** of `i`.
   - Then we multiply it by the **product of all elements to the right** of `i`.

2. **Compute left product array (`prefix product`)**
   - Traverse from left to right.
   - Store the **cumulative product** of all elements before `i`.

3. **Compute right product (`suffix product`) while updating output**
   - Traverse from right to left.
   - Multiply the output by the **cumulative product** of all elements after `i`.

---

## **Code Implementation**
```python
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    output = [1] * n
    
    # Step 1: Compute prefix products
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]  # Accumulate product

    # Step 2: Compute suffix products while updating output
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix  # Multiply with the suffix product
        suffix *= nums[i]  # Accumulate suffix product

    return output
```

---

## **How This Works**
### **Step 1: Compute Prefix Products**
| `i`  | `nums[i]` | `prefix` (before update) | `output[i]` (stores left product) | `prefix` (after update) |
|------|----------|------------------------|-------------------------------|------------------------|
| 0    | 1        | 1                      | 1                             | 1 × 1 = 1              |
| 1    | 2        | 1                      | 1                             | 1 × 2 = 2              |
| 2    | 3        | 2                      | 2                             | 2 × 3 = 6              |
| 3    | 4        | 6                      | 6                             | 6 × 4 = 24             |

After this step:  
`output = [1, 1, 2, 6]`

### **Step 2: Compute Suffix Products**
| `i`  | `nums[i]` | `suffix` (before update) | `output[i]` (multiplied by suffix) | `suffix` (after update) |
|------|----------|------------------------|--------------------------------|------------------------|
| 3    | 4        | 1                      | 6 × 1 = 6                     | 1 × 4 = 4              |
| 2    | 3        | 4                      | 2 × 4 = 8                     | 4 × 3 = 12             |
| 1    | 2        | 12                     | 1 × 12 = 12                   | 12 × 2 = 24            |
| 0    | 1        | 24                     | 1 × 24 = 24                   | 24 × 1 = 24            |

Final `output = [24, 12, 8, 6]`

---

## **Complexity Analysis**
- **Time Complexity:** **O(n)** (Two passes: one left-to-right, one right-to-left)
- **Space Complexity:** **O(1)** (Only using `output`, which is required for the answer)

---

## **Edge Cases**
✅ **Contains Zero:**  
If `nums = [1, 2, 0, 4]`, the algorithm correctly handles it.  

✅ **Contains Negative Numbers:**  
If `nums = [-1, 2, -3, 4]`, the product signs are handled correctly.  

✅ **Single Element Array (`n = 1`)**  
If `nums = [10]`, the output should be `[1]`.

---

## **Key Takeaways**
- **Using division is an easy but incorrect approach** (zero causes problems).
- **Prefix & suffix products** allow an efficient **O(n) solution**.
- **This approach only requires O(1) extra space** (excluding output array).

Would you like to see an alternative solution using logarithms or recursion? 🚀

