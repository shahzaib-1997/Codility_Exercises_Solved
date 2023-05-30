'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution_by_bard(A):
    seen = set(A)

    for i in range(1, 100001):
        if i not in seen:
            return i
    
    return 100001



def solution(A):
    min_int = 1

    if A:
        pos_int = set()
        for i in A:
            if i > 0:
               pos_int.add(i)
            
        while min_int in pos_int:
            min_int += 1
    
    return min_int

print(solution_by_bard([1,-2,3,-1,4]))
print(solution([]))
