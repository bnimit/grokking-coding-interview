def find_averages_of_subarrays(K, arr):
    results = []
    for i in range(len(arr)-K+1):
        _sum=0.0
        for j in range(i, i+K):
            _sum += arr[j]
        results.append(_sum/K)
    
    return results 

def main():
    results = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print('Average of subarrays of size K is: ' + str(results))

main()
