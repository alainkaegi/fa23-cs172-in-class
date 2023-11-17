def search(key, a):
    """Linear search for key in a.  Return -1 if key is not found."""
    n = len(a)
    for i in range(n):
        if a[i] == key:
            return i
    return -1

def _bsearch(key, a, lo, hi):
    """Binary search for key in a[lo:hi)."""
    if hi <= lo:
        return -1
    mid = (lo + hi)//2
    if key < a[mid]:
        return _bsearch(key, a, lo, mid)
    elif key > a[mid]:
        return _bsearch(key, a, mid + 1, hi)
    else:
        return mid

def bsearch(key, a):
    """Binary search for key in a.  a must be sorted.  Return -1 if key is not found."""
    n = len(a)
    return _bsearch(key, a, 0, n)
