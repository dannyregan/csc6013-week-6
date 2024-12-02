import random

def main():
    """
    This program generates an array of 1000 random integers between 1 and 10,000
    and allows the user to search for the k-th smallest element in the array.
    """
    def quickSelect(A, startIndex, endIndex, k):
        """
        Finds the k-th smallest element in the array A within the range [startIndex, endIndex].

        Parameters:
        A (list): The array to search.
        startIndex (int): The starting index of the array/subarray.
        endIndex (int): The ending index of the array/subarray.
        k (int): The rank of the target element.

        Returns:
        int: The k-th smallest element in the array.
        """
        partitionIndex, pivotElement = startIndex, A[endIndex]

        # Parition the array around the pivot
        for i in range(startIndex, endIndex):
            if A[i] <= pivotElement:
                A[i], A[partitionIndex] = A[partitionIndex], A[i]
                partitionIndex += 1

        # Place the pivot in the correct position
        A[endIndex], A[partitionIndex] = A[partitionIndex], A[endIndex]

        # Recur the appropriate partition
        if A[k-1] < pivotElement:  return quickSelect(A, startIndex, partitionIndex - 1, k)
        if A[k-1] > pivotElement:  return quickSelect(A, partitionIndex + 1, endIndex, k)
        if A[k-1] == pivotElement: return pivotElement


    true = True
    A = [round(random.random()*10000) for i in range(1000)]
    print("I've generated an array with 1000 elements from 1-10,000.")
    while true:
        try:
            k = int(input("Search for the kth smallest number. k = "))
            if not (1 <= k <= 1000):
                raise ValueError("k must be between 1 and 1000.")
        except:
            print("Input a value between 1 and 1000.")
        else:
            true = False
            print(quickSelect(A, 0, len(A)-1, k))

# =================================================================================

main()