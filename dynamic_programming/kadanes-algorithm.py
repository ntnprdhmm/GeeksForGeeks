def max_sum_subarray(arr, n):
    max_so_far = max_ending_here = 0

    for i in range(n):
        max_ending_here += arr[i]
        if max_ending_here < 0 :
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far if max_so_far != 0 else max(arr)

# for each test case
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_sum_subarray(arr, n))
