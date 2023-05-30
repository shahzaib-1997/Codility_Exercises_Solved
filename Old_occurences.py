def solution(A):
    if A:
        count_dict = {}
        for e in A:
            if e in count_dict.keys():
                count_dict[e] += 1
            else:
                count_dict[e] = 1
        
        for k,v in count_dict.items():
            if v % 2 != 0:
                return k
    return 0


print(solution([5,3,1,7,3,5,7,1,9]))