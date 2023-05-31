'''
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
'''

def solution_chatgpt(A, B, K):

    count_b = B // K
    count_a_minus_one = (A - 1) // K
    count = count_b - count_a_minus_one

    return count

def solution(A, B, K):
    div_int = 0

    if A <= B and K > 0:
    
        up_div = B // K
        low_div = A // K
        div_int = up_div - low_div
    
        if A % K == 0:
            div_int += 1
    
    return div_int

print(solution(1, 14, 2))
print(solution_chatgpt(11, 345, 17))