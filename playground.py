array_yeni = [3,4,6,7,8,9,10]
k = 4

def find_max_sum_k(arry, k):
    n = len(arry)
    max_sum = sum(array_yeni[:k])
    current_sum = max_sum
    array_combi = '{};{}'.format(0,n-k)
    
    if n<k:
        return None
    
    for i in range(k, n):
        current_sum += arry[i] - arry[i-k]
        max_sum = max(max_sum, current_sum)
        array_combi = '{};{}'.format(i-k, i)
                
    return [max_sum, array_combi]
    
result = find_max_sum_k(array_yeni, k)
print("Result: ", result)