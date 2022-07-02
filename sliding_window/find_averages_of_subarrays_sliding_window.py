def find_averages_of_subarrays(K, arr):
    results = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K-1:
            results.append(windowSum / K)
            windowSum -= arr[windowStart]
            windowStart += 1
    
    return results

def main():
    results = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print('Average of subarrays of size K is: ' + str(results))


main()
