from collections import deque

dq = deque()

dq.append(10)      # right
dq.append(20)      # right
dq.appendleft(5)   # left

dq.pop()           # right
dq.popleft()       # left

print(dq)