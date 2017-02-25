def qsort(array_, ascending=True):
    if len(array_) < 2:
        return array_

    pivot = array_[0]
    tail = array_[1:]

    if ascending:
        left = [item for item in tail if item < pivot]
        right = [item for item in tail if item >= pivot]
    else:
        left = [item for item in tail if item > pivot]
        right = [item for item in tail if item <= pivot]

    return qsort(left, ascending) + [pivot] + qsort(right, ascending)

if __name__ == '__main__':
    array = [1, 5, 6, 2, 0, 3, 1, 8, -11]
    sorted_ = qsort(array, ascending=True)
    print(sorted_)
