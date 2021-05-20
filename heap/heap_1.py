import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    min1 = heapq.heappop(scoville)
    while min1 < K:
        try:
            min2 = heapq.heappop(scoville)
        except:
            return -1
        heapq.heappush(scoville, min1 + min2 * 2)
        count += 1
        min1 = heapq.heappop(scoville)
    return count
