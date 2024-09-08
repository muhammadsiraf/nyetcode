'''
Binary Search
'''

def binary_search(arr, value_searched):
    low = 0
    mid = (len(arr)-1)//2
    high = len(arr)-1
    run = True

    while run:
        if arr[mid] == value_searched:
            return mid
            
        if arr[mid] > value_searched:
            high = mid - 1
            
        elif arr[mid] < value_searched:
            low = mid + 1
                
        mid = low + ((high-low)//2)
        
        if mid == low and mid == high and arr[mid] != value_searched:
            run = False

        print(
            "Low: {} \n Mid: {} \n High: {} \n".format(low, mid, high)
        )
        
array_dummy = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
k = 77
result = binary_search(array_dummy, k)
print(result)