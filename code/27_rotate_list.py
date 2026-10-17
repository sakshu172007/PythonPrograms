def rotate_list(items, k):
    if len(items) == 0:
        return []

    n = len(items)
    k = k % n

    if k < 0:
        k = n + k

    return items[-k:] + items[:-k] if k != 0 else items.copy()