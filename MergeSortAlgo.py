def Merge(A, aux, low, mid, high):
    
    # k is an index marker for the final list, while i and j are just for the list beings merged after comparison
    k = low
    i = low
    j = mid + 1
    
    # During comparison, as long as the marker hasn't reached the maximum index, all elements of both lists will be in place for comparison
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            k += 1
            i += 1
        else:
            aux[k] = A[j]
            k += 1
            j += 1
    
    # This will only run if the index of the latter half is exceeded
    # The reason we don't run it for the j is because if the first half runs out, then the latter half should already be sorted
    while i <= mid:
        aux[k] = A[i]
        k += 1
        i += 1
    
    # We proceed to append our merged and sorted list onto A, our initial/final list
    for i in range(low, high + 1):
        A[i] = aux[i]
    

def MergeSort(A, aux, low, high):
    
    # When the markers (the lowest index and the highest index) switch, we want to end this iteration of mergesort
    if high <= low:
        return
    
    # Since the above isn't true, that means the markers can be used further on to divide the given list
    # Find the mid point to divide the current list into two smaller components
    mid = low + ((high - low) >> 1)
    # mid = low + ((high - low) // 2) -> this line and the one above do the same thing
    
    # Run another interation of mergesort using the new parameters for the divided list
    # These first line will divide continually with the first half, until there's only one element per list
    # The second line will then divide the latter half until there's only one element per list
    MergeSort(A, aux, low, mid)
    print(A)

    MergeSort(A, aux, mid + 1, high)
    print(A)
    
    # Merge the the divided two consecutive divided lists into a singular list whilst sorting
    Merge(A, aux, low, mid, high)
    print(A)

# This will be the final check to see if mergesort went through properly
def IsSorted(A):
    # We'll set the first element of list A
    prev = A[0]
    
    # Then start a loop to check if the following element is greater than the previous
    # if not, we will sound an alarm
    for i in range(1, len(A)):
        if prev > A[i]:
            print("Merge sort fails!")
            return False
        
        prev = A[i]
    
    return True

if __name__ == "__main__":
    A = [12, 3, 18, 24, 0, 5, -2]
    aux = A.copy()
    
    MergeSort(A, aux, 0, len(A) - 1)

    if IsSorted(A):
        print(A)
