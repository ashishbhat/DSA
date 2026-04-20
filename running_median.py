import heapq

def solution(arr):
    lo = [] #max heap
    hi = [] #min heap

    for n in arr:
        if len(lo) == 0:
            heapq.heappush_max(lo, n)
            yield lo[0]
            continue
        if n >= lo[0]:
            heapq.heappush(hi, n)
        else:
            heapq.heappush_max(lo, n)

        if len(hi) - len(lo) == 2:
            heapq.heappush_max(lo, heapq.heappop(hi))
        elif len(lo) - len(hi) == 2:
            heapq.heappush(hi, heapq.heappop_max(lo))

        if len(lo) == len(hi):
            yield (lo[0] + hi[0]) / 2
        elif len(lo) > len(hi):
            yield lo[0]
        else:
            yield hi[0]

            

arr = [6,5,4,3,2,1]
median = solution(arr)
for i in median:
     print(i)

