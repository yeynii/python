def solution(progresses, speeds):
    answer = []
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s), 1])
        else :
            Q[-1][1] += 1
    answer = [p[1] for p in Q]
    return answer
