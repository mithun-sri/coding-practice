from typing import List

# checks for the size of the smallest subarray whose sum is 
# greater than or equal to the given number
def dynamic_window_sliding(arr: List[int], x: int) -> int:
    min_length = float('inf')

    start = 0
    end = 0
    current_sum = 0

    while end < len(arr):
        current_sum = current_sum + arr[end]
        end += 1

        while start < end and current_sum >= x:
            current_sum = current_sum - arr[start]
            start += 1
            min_length = min(min_length, end - start + 1)
    
    return min_length