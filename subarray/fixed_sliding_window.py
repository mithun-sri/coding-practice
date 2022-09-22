from typing import List

def fixed_sliding_window(arr: List[int], k: int) -> List[int]:
    """Fixed sliding window algorithm.
    Args:
        arr: list of integers.
        k: size of the window.
    Returns:
        list of integers.
    """
    curr_subarray = sum(arr[:k])
    result = [curr_subarray]

    # Iterate over the array
    # and update the current subarray sum
    for i in range(1, len(arr)-k+1):
        curr_subarray = curr_subarray - arr[i-1] + arr[i+k-1]
        result.append(curr_subarray)
    
    return result