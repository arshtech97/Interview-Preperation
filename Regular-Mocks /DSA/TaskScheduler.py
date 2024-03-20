# PS : https://leetcode.com/problems/task-scheduler

from collections import deque, Counter
from heapq import heapify, heappush, heappop


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-freq for task, freq in counter.items()]  # max-heap
        heapify(heap)  # convert list into heap

        q = deque()  # [cnt, idleTime]
        time = 0
        while q or heap:
            time += 1
            if heap:
                cnt = 1 + heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heappush(heap, q.popleft()[0])
        return time
