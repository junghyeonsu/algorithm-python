import heapq

def solution(strings, n):
    h = []
    answer = []
    for i in strings:
        heapq.heappush(h, [i[n], i])
        
    for j in range(len(h)):
        answer.append(heapq.heappop(h)[1])
    
    return answer