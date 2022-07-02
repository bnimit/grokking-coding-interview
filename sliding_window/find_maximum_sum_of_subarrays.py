def max_sub_array_of_size_k(K, arr):
    window_sum, max_sum = 0, 0
    for i in range(len(arr) -K + 1):
        window_sum = 0
        for j in range(i, i+K):
            window_sum += arr[j]
        max_sum = max(window_sum, max_sum)
    return max_sum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()