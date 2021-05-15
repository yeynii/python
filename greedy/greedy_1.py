def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    i = 0
    while i < len(lost) :
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost.pop(i)
        else:
            i += 1
    i = 0
    while i < len(lost) :
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost.pop(i)
        elif (lost[i] - 1) in reserve:
            reserve.remove(lost[i] - 1)
            lost.pop(i)
        elif (lost[i] + 1) in reserve:
            reserve.remove(lost[i] + 1)
            lost.pop(i)
        else:
            i += 1
    answer = n - len(lost)
    return answer
