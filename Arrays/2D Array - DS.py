'''
Input Format

Each of the 6 lines of inputs arr[i][j] contains 6 space-separated integers arr[i][j].

Constraints -9<=arr[i][j]<=9, 0<=i, j<=5


Output Format

Print the largest (maximum) hourglass sum found in arr.
'''

# Complete the hourglassSum function below.
def hourglassSum(arr):
    values = []
    for row in range(0,4):
        for col in range(0,4):
            topleft = arr[row][col]
            topmid = arr[row][col+1]
            topright = arr[row][col+2]
            mid = arr[row+1][col+1]
            botleft = arr[row+2][col]
            botmid = arr[row+2][col+1]
            botright = arr[row+2][col+2]
            values.append(topleft+topmid+topright+mid+botleft+botmid+botright)
    maxVal = -63
    for i in range(len(values)):
        if values[i]>maxVal:
            maxVal = values[i]
    print(maxVal)
    return maxVal

#Test Case
arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]
hourglassSum(arr) #19
