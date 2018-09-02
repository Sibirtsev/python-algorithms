def flatten(array):
    res = []
    for i in array:
        if i.__class__.__name__ == 'list':
            res += flatten(i)
        else:
            res.append(i)
    return res


if __name__ == '__main__':
    array = [1, [2, 3], [4, [5, 6], 7], 8]
    print(array)
    print(flatten(array))

    array = ['a', ['b', 'c'], 'd', ['e', ['f', 'g'], 'h'], 'i']
    print(array)
    print(flatten(array))
