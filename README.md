# Bubble Sort

## Description

The **Bubble Sort** program is a Python implementation of the classic Bubble Sort algorithm. This program sorts a list of elements in either ascending or descending order, with additional functionalities such as step-by-step visualization and performance measurement.

## Features

- **Ascending/Descending Order:** Sort the list in either ascending (default) or descending order by specifying a parameter.
- **Step-by-Step Visualization:** Visualize the sorting process by printing the list after each swap, helping users understand how the algorithm works.
- **Performance Measurement:** The program tracks and displays the time taken to sort the list, providing insight into the efficiency of the algorithm.

## How It Works

The program performs the following steps:

1. **Input:** The program uses a predefined list of elements for sorting.
2. **Sorting:** The Bubble Sort algorithm compares adjacent elements and swaps them if they are in the wrong order, with options to sort in ascending or descending order.
3. **Visualization:** If enabled, the program prints the list at each step of the sorting process.
4. **Performance Measurement:** The program measures and displays the time taken to complete the sorting.
5. **Output:** The sorted list is printed, along with the time taken for the operation.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Clone the repository or download the script file `bubble_sort.py`.
2. Run the script using Python:

    ```bash
    python bubble_sort.py
    ```

3. The program will sort a sample list, visualizing the steps and measuring the time taken.
4. Modify the list or parameters directly in the script to customize the sorting behavior.

### Example

```bash
$ python bubble_sort.py

Original list: [21, 71, 53, 19, 7, -1, 0, 1, 1.1, 1.25]
Step 0.0: [21, 53, 71, 19, 7, -1, 0, 1, 1.1, 1.25]
Step 0.1: [21, 53, 19, 71, 7, -1, 0, 1, 1.1, 1.25]
...
Sorted list (Ascending): [-1, 0, 1, 1.1, 1.25, 7, 19, 21, 53, 71]
Time taken to sort: 0.000120 seconds

Sorted list (Descending): [71, 53, 21, 19, 7, 1.25, 1.1, 1, 0, -1]
Time taken to sort (Descending): 0.000115 seconds
```

## Program Structure

- **`bubble_sort(arr, descending=False, visualize=False)`**: bubble_sort(arr, descending=False, visualize=False)
- **`main()`**: Manages the execution of the sorting process, including performance measurement and visualization.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
