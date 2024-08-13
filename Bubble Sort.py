import time

"""
BUBBLE SORT
Difficulty: 5/10

Comments: Had to revise my concept on Bubble Sort
"""

def bubble_sort(arr, descending=False, visualize=False):
    """
    Function to perform Bubble Sort on a list with optional visualization and descending order.

    Parameters:
    arr (list): The list of elements to be sorted.
    descending (bool): Sort in descending order if True, ascending if False (default).
    visualize (bool): Show step-by-step visualization of the sorting process if True.

    Returns:
    list: The sorted list.
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if (arr[j] < arr[j + 1] and descending) or (arr[j] > arr[j + 1] and not descending):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

            if visualize:
                print(f"Step {i}.{j}: {arr}")  # Visualize each step

        if not swapped:
            break

    return arr

def main():
    sample_list = [21, 71, 53, 19, 7, -1, 0, 1, 1.1, 1.25]
    print("Original list:", sample_list)

    # Measure the time taken for sorting
    start_time = time.time()

    # Sort in ascending order with visualization
    sorted_list = bubble_sort(sample_list.copy(), visualize=True)

    end_time = time.time()

    print("Sorted list (Ascending):", sorted_list)
    print(f"Time taken to sort: {end_time - start_time:.6f} seconds")

    # Measure the time for sorting in descending order
    start_time = time.time()

    sorted_list_desc = bubble_sort(sample_list.copy(), descending=True, visualize=True)

    end_time = time.time()

    print("Sorted list (Descending):", sorted_list_desc)
    print(f"Time taken to sort (Descending): {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
