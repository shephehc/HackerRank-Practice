'''
Input Format

The first line contains an integer, n, the size of arr.
The second line contains n space-separated integers arr[i].

Constraints
1<=n<=10^5
1<=arr[i]<=n

Output Format

Return the minimum number of swaps to sort the given array.
'''

def minimumSwaps(arr):
    numSwaps = 0
    i = 0
    while (i < len(arr)-1):
        if arr[i] != i+1:
            temp = arr[i]
            arr[i], arr[temp-1] = arr[temp-1], arr[i]
            numSwaps +=1
        else:
            i+=1
    print(numSwaps)
    return numSwaps

arr = [1,3,5,2,4,6,7]
minimumSwaps(arr)
#3
