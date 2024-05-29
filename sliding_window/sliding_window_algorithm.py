def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1  # Not enough elements

    # Calculate the sum of the first window of size k
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window from start to end
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum
