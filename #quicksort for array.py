#quicksort for array
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            # Swap arr[i] and arr[j] using a temp variable
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    # Swap arr[i+1] and pivot (arr[high])
    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)  # Before pi
        quick_sort(arr, pi + 1, high)  # After pi

# Example usage
arr = [29, 10, 14, 37, 13]
print("Original array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
