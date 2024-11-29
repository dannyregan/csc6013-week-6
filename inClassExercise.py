# Takes an array, A, the first index, left, and final index, right, and sorts the array so that all elements less than right are to its left and all elements greater than right are to its right.
def lomuto(A, left, right):
    lesserThan = []
    greaterThan = []
    leftToCompare = A[:]
    p = A[right]
    print("Pivot =", p)
    i = left
    for j in range(left, right):
        print("Left to compare", leftToCompare)
        print("i =", A[i])
        print("j = ", A[j])
        # print(f"Checking if {A[j]} < {p}...")
        if A[j] < p:
            print(f"Swapping i ({A[i]}) and j ({A[j]})")
            lesserThan.append(A[j])
            leftToCompare.remove(A[j])
            A[i], A[j] = A[j], A[i]
            i += 1
            print("i = ", A[i])
        else:
            # print("It's not")
            greaterThan.append(A[j])
            leftToCompare.remove(A[j])
        print("Less than the pivot:", lesserThan)
        print("Greater than the pivot:", greaterThan)
    print(f"Swapping i ({A[i]}) and j ({A[right]})")
    A[i], A[right] = A[right], A[i]
    return i

A = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]

pivot_index = lomuto(A, 0, len(A) - 1)
print("Final array:", A)
print("Pivot index:", pivot_index)