def Merge(A, aux, low, mid, high):
    
    # k is an index marker for the final list, while i and j are just for the list beings merged after comparison
    k = low
    i = low
    j = mid + 1
    
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            k += 1
            i += 1
            print(A)
        else:
            aux[k] = A[j]
            k += 1
            j += 1
            print(A)
            
    while i <= mid:
        aux[k] = A[i]
        k += 1
        i += 1
        print(A)
        
    for i in range(low, high + 1):
        A[i] = aux[i]
        print(A)
    

def MergeSort(A, aux, low, high):
    
    # base case
    if high <= low:
        print(A)
        return
    
    # find the mid point
    mid = low + ((high - low) >> 1)
    print(A)
    # mid = low + ((high - low) // 2)
    
    MergeSort(A, aux, low, mid)
    MergeSort(A, aux, mid + 1, high)
    
    Merge(A, aux, low, mid, high)
    
def IsSorted(A):
    prev = A[0]
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
