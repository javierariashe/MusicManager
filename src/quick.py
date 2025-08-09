def partitionArtist(array, low, high):
    pivot = array[high].artist
    i = low - 1
    
    for j in range(low, high): 
        if array[j].artist <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSortArtist(array, low, high):
    if low < high:
        pi = partitionArtist(array, low, high)
        quickSortArtist(array, low, pi - 1)
        quickSortArtist(array, pi + 1, high)


def partitionName(array, low, high):
    pivot = array[high].name
    i = low - 1

    for j in range(low, high): 
        if array[j].name <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSortName(array, low, high):
    if low < high:
        pi = partitionName(array, low, high)
        quickSortName(array, low, pi - 1)
        quickSortName(array, pi + 1, high)


def partitionYear(array, low, high):
    pivot = array[high].year
    i = low - 1
    
    for j in range(low, high): 
        if array[j].year <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSortYear(array, low, high):
    if low < high:
        pi = partitionYear(array, low, high)
        quickSortYear(array, low, pi - 1)
        quickSortYear(array, pi + 1, high)
