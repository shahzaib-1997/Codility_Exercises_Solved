'''
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''

import math

def solution_chatgpt(N):

    if N > 1:
        factor = 2
        sqrt_N = int(math.sqrt(N))
        for n in range(2,sqrt_N + 1):
            if N % n == 0:
                factor += 2
        
        if sqrt_N * sqrt_N == N:
            factor -= 1

    else: 
        factor = 1
        
    return factor

def solution(N):

    if N > 1:
        factor = 2
        for n in range(2,(N // 2) + 1):
            if N % n == 0:
                factor += 1
    else: 
        factor = 1
        
    return factor

print(solution(24))
print(solution_chatgpt(24))
