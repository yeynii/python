def solution(priorities, location):
    answer = 0
    while len(priorities) > 0 :
        flag = 0
        
        for i in range(1,len(priorities)): # 맨 앞문서와 뒤에있는 대기목록들 우선순위 비교
            if priorities[0] < priorities[i]:
                flag = 1
                break
                
        if flag == 0: # 뒤에 우선순위 높은게 없는 경우
            priorities.pop(0)
            answer += 1
            if location == 0:
                location -= 1
                return answer
            elif location > 0:
                location -= 1
            else:
                loaction = len(priorities) - 1 
                
        else : # 뒤에 우선순위 높은게 있는 경우
            priorities.append(priorities[0])
            priorities.pop(0)
            if location > 0:
                location -= 1
            else:
                location = len(priorities) - 1
    return answer
