def solution(answers):
    answer = []
    supos = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    max = 0
    for i in range(3):
        score = 0
        for j in range(len(answers)):
            if answers[j] == supos[i][j % len(supos[i])]:
                score += 1
        if max < score :
            answer.clear()
            answer.append(i + 1)
            max= score
        elif max == score :
            answer.append(i + 1)
    return answer
