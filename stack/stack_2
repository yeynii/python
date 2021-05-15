def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        if progresses[0] >= 100:
            while True:
                if len(progresses) <= 0:
                    break
                if progresses[0] >= 100:
                    cnt += 1
                    progresses.pop(0)
                    speeds.pop(0)
                else: 
                    break
            answer.append(cnt)                      
    return answer
