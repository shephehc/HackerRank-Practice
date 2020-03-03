'''
Input Format

The first line contains an integer t, the number of test cases.

Each of the next t pairs of lines are as follows:
- The first line contains an integer t, the number of people in the queue
- The second line has n space-separated integers describing the final state
of the queue.

Constraints

1<=t<=10
1<=n<=10^5

Subtasks


Output Format

Print an integer denoting the minimum number of bribes needed to get the
queue into its final state. Print Too chaotic if the state is invalid, i.e.
it requires a person to have bribed more than 2 people.
'''

def minimumBribes(q):
    q = [X-1 for X in q]
    moves = 0
    for i,X in enumerate(q):
        if X - i > 2:
            print("Too chaotic")
            return
        for j in range(max(0, X-1), i):
            if q[j]>X:
                moves +=1

    print(moves)

#Test

arr = [2, 1, 5, 3, 4]
minimumBribes(arr)
#3
