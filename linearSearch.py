def search(arr, name):
 
    for i in range(len(arr)):
 
        if arr[i].name == name:
            return i
 
    return -1
