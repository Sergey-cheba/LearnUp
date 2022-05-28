
def cutString(arr):
    newArr = []
    for i in range(len(arr)):
        if len(arr[i]) > 10:
            newArr.append(arr[i][:7] + "...")
        else:
            newArr.append(arr[i])
    print(newArr)

