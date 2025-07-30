#merge sort for array
def merge(arr, l, m, r):
    # Create temp arrays
    left = arr[l:m+1]
    right = arr[m+1:r+1]

    i = j = 0
    k = l

    # Merge the temp arrays back into arr[l..r]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # Swapping using temp variable
            temp = left[i]
            arr[k] = temp
            i += 1
        else:
            temp = right[j]
            arr[k] = temp
            j += 1
        k += 1

    # Copy the remaining elements of left[], if any
    while i < len(left):
        temp = left[i]
        arr[k] = temp
        i += 1
        k += 1

    # Copy the remaining elements of right[], if any
    while j < len(right):
        temp = right[j]
        arr[k] = temp
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
