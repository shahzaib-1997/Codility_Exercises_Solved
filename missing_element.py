'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''



def solution(A):
    A.sort()
    if A and A[0] == 1:
        l = len(A) + 1
        if A[-1] == l:
            for i in range(1,l-1):
                if A[i] - A[i-1] != 1:
                    return A[i] - 1
        else:
            return l
    else:
        return 1
    
print(solution([2,8,5,4,3,1,6]))