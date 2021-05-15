def solution(clothes):
    answer = 1
    clothes_type = []
    clothes_num = []
    for c in clothes:
        if c[1] in clothes_type:
            clothes_num[clothes_type.index([c[1]][0])] += 1
        else:
            clothes_type.append(c[1])
            clothes_num.append(1)
    for n in clothes_num:
        answer *= (n + 1)
    answer -= 1
    return answer
