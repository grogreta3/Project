# in: a = [1, 7, 3, 5, 4, 2] out: 3 ([1, 3, 5])
# lis = longest increasing subsequence

def lis(arr):
    n = len(arr)
    lis = [1]*n
    prev = [0]*n

    for i in range(0, n):
        prev[i] = i

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
                prev[i] = j

    maximum = 0
    idx = 0

    for i in range(n):
        if maximum < lis[i]:
            maximum = lis[i]
            idx = i

    seq = [arr[idx]]
    while idx != prev[idx]:
        idx = prev[idx]
        seq.append(arr[idx])

    return maximum, reversed(seq)


arr = [1, 7, 3, 5, 4, 2]
ans = lis(arr)
print(ans[0])
print("The longest sequence is", ", ".join(str(x) for x in ans[1]))
