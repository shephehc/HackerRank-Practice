'''
Input Format

The first line contains two space-separated integers n and d, the size of a
and the number of left rotations you must perform.
The second line contains n space-separated integers a[i].

Constraints

1<=n<=10^5
a<=d<=n
a<=a[i]<=10^6

Output Format

Print a single line of n space-separated integers denoting the final
state of the array after performing d left rotations.
'''

def rotate(l, n):
    return l[n:] + l[:n]

def rotLeft(a, d):
    new_arr = rotate(a, d)
    print(new_arr)
    return new_arr

#test

arr = [1,2,3,4,5]
rotations = 4
rotLeft(arr, rotations)
#[5, 1, 2, 3, 4]

