def rearrange_negative_first(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Increment left pointer until a nonnegative element is found
        while arr[left] < 0:
            left += 1

        # Decrement right pointer until a negative element is found
        while arr[right] >= 0:
            right -= 1

        if left < right:
            # Swap the elements at left and right
            arr[left], arr[right] = arr[right], arr[left]
    return arr

A=[-1,5,-2,4,-2]
print(rearrange_negative_first(A))
