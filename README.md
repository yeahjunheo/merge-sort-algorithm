# merge-sort-algorithm

## Context

Merge sort is another algorithm commonly used algorithm to sort an assortment of elements in a list. However, it uses the idea of divide-and-conquer, which by its name refers to cutting the list into smaller components, then combining these smaller components whilst checking their sequence.

## Looking at the code

### def Merge(A, tempA, low, mid, high)

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

### def IsSorted(A)


