# merge-sort-algorithm

## Context

Merge sort is another algorithm commonly used algorithm to sort an assortment of elements in a list. However, it uses the idea of divide-and-conquer, which by its name refers to cutting the list into smaller components, then combining these smaller components whilst checking their sequence.

## Looking at the code

### def MergeSort(A, tempA, low, high)

The first step for a merge sort algorithm will be to divide before the conquer (how does that sound ;\)). With this in mind, we take four variables: the initial list `A`, a temporary list of A `tempA`, the lowest index `low`, and the highest index `high`. 

At the start of this function, you will notice the if-check:

```
if high <= low:
    return
```

This makes sure that the markers used for dividing the list `A` does not pass each other, aka makes sure that the right marker is is the higher number and not the other way around.

The variable `mid` is the middle value of `low` and `high`, which will be used to divide the list `A` until only one element exists in each unit. 

You would have noticed that to get `mid`, we use:

```
mid = low + ((high - low) >> 1)
```

instead of:

```
mid = (low + high) // 2
```

This is to prevent integer overflow, if the values were to become to big. But this worry doesn't apply to our case (but just in case its good practice).

Also, we use the `>>` operator, which is equaivalent of the `//` operator where the `y` in `x >> y` is equaivalent to `2**y` in `x // (2**y)`.

Next, we implement recursion in the form of:

```
MergeSort(A, tempA, low, mid)
MergeSort(A, tempA, mid + 1, high)
```

The prior line will continue division on the index from the `low` to `mid`, while the latter will continue divison on the index from `mid + 1` to `high`

Afterwards, this will call the function `Merge()` which will proceed to conquering the sorting task.

### def Merge(A, tempA, low, mid, high)

The merging step of this algorithm will take another variable `mid` from the iteration it was called. This is important in setting up markers to be used while merging.

We introduce three marker variables `k`, `i`, and `j`, which will represent the index of our `tempA`, the left-half, and right-half after `MergeSort()` respectively. `k` and `i` are set as `low` since that's where they start, while `j` is set to `mid + 1` to represent the starting index of the right-half.

Then we first run a while-loop:

```
while i <= mid and j <= high:
    if A[i] <= A[j]:
        tempA[k] = A[i]
        k += 1
        i += 1
    else:
        tempA[k] = A[j]
        k += 1
        j += 1
```

This while-loop will run as long as `i` and `j` are still values are within their upper bounds. While this stays `True`, the if-check is to order the merging list in a rising sequence. Then, it will add the lower number to our `tempA` and move the which ever marker by one.

When the constraints for the while-loop is not met, we proceed with:

```
while i <= mid:
    tempA[k] = A[i]
    k += 1
    i += 1
```

This while-loop only works when `j` runs out, meaning the elements in the left-half are still geater than the right-half. this requires us to move and store whatever values in the left-half to the ends of the last element of the right-half. 

Some would ask why we don't do this for the `j` when `i` runs out. The reason we don't do this is because we already know that the elements of `j` will be in their rightful place.

Lastly, the for-loop at the end:

```
for i in range(low, high + 1):
    A[i] = tempA[i]
```

will update our list `A` with the newly ordered and merged elements in our temporary list `tempA`. 

### def IsSorted(A)

This function will run last to check if list `A` was sorted properly by comparing `prev` to the next index element of `A`, followed by ticking `prev` to the next index. Quite self explanitory.

## Testing

### A = [8, 7, 6, 5, 4, 3, 2, 1]

If we were to set `A` as a decreaseing sequence to re-sort it to an increaseing sequence, the alogirthm will proceed and give:

```
[7, 8, 6, 5, 4, 3, 2, 1]
[7, 8, 5, 6, 4, 3, 2, 1]
[5, 6, 7, 8, 4, 3, 2, 1]
[5, 6, 7, 8, 3, 4, 2, 1]
[5, 6, 7, 8, 3, 4, 1, 2]
[5, 6, 7, 8, 1, 2, 3, 4]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
```

The first line shows `[8, 7]` re-ordered to `[7, 8]`, followed by `[6, 5]` to `[5, 6]`. Then these two merge to give `[5, 6, 7, 8]`. Next the latter half does its own merging, the same way as the prior half to give `[1, 2, 3, 4]`. Finally, we get `[1, 2, 3, 4, 5, 6, 7, 8]`.

### A = [8, 7, 6, 5, 4, 3, 2, 1, 0]

What will happen if we add `0` to `A`? To answer that, we get:

```
[7, 8, 6, 5, 4, 3, 2, 1, 0]
[6, 7, 8, 5, 4, 3, 2, 1, 0]
[6, 7, 8, 4, 5, 3, 2, 1, 0]
[4, 5, 6, 7, 8, 3, 2, 1, 0]
[4, 5, 6, 7, 8, 2, 3, 1, 0]
[4, 5, 6, 7, 8, 2, 3, 0, 1]
[4, 5, 6, 7, 8, 0, 1, 2, 3]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
```

In this case, the merging runs similarly as the previous list, but the initial two lines of sorting might come out as somewhat confusing. Especially with the introduction of `0`, leading to an odd number of elements. We can check the specifics if we add `print(A[low: mid + 1])` and `print(A[mid + 1: high + 1])` at the start of the `Merge()` function. Then we get:

```
[8]
[7]
[7, 8]
[6]
[5]
[4]
[6, 7, 8]
[4, 5]
```

Which shows that when `A` was divided, the most left list divides `[8, 7, 6]` into `[8, 7]` and `[6]`, which will further split into `[8]` and `[7]`.