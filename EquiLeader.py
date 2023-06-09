'''
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
'''

def lead(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            leader = A[k]
        elif (leader != A[k]):
            size -= 1
        else:
            size += 1
    
    return leader if size > 0 else -1

def solution(A):
    count = 0
    leader = lead(A)
    leader_count = A.count(leader)

    if leader_count > len(A) // 2:
        left_count = 0
        right_count = leader_count
    
        for i in range(len(A) - 1):
            if A[i] == leader:
                left_count += 1
                right_count -= 1
            
            if left_count > (i + 1) // 2 and right_count > (len(A) - i - 1) // 2:
                count += 1

    return count

print(solution([4, 3, 4, 4, 4, 2]))