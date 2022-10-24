# arr = ['un', 'iq', 'ue']
# arr = ['cha', 'r', 'act', 'ers']
# arr = ["abcdefghijklmnopqrstuvwxyz"]
arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
if len(arr) >= 2:
    arr = sorted(arr, key=lambda x: len(x), reverse=True)
    answer = 0

    while arr and not answer:
        for i in range(1, len(arr)):
            if len(list(set(arr[0] + arr[i]))) == len(arr[0]) + len(arr[i]):
                answer = len(arr[0]) + len(arr[i])
                print(arr[0], arr[i])
                break
            else:
                continue

        arr.pop(0)

    print(answer)

else:
    print(len(arr[0]))