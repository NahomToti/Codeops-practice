#binary trees
class Node: 

def __init__(self, value): 

self.value = value 

self.left = None      # smaller values 

self.right = None     # larger values

#Traversals

def in_order(node): 

if node is None:        # base case 

return 

in_order(node.left)   # left    

print(node.value)      # node 

in_order(node.right)    # right 

#Graphs

graph = { 
"Almaz":  ["Dawit", "Tigist", "Samuel"], 
"Dawit":  ["Almaz", "Hanna"], 
"Tigist": ["Almaz", "Samuel"], 
"Samuel": ["Almaz", "Tigist", "Hanna"], 
"Hanna":  ["Dawit", "Samuel"], 
} 

#BFS


from collections import deque 

def bfs(graph, start): 

seen = {start} 

q = deque([start]) 

while q: 

node = q.popleft() 

for n in graph[node]: 

if n not in seen: 

seen.add(n) 

q.append(n) 

return seen

#Heaps


import heapq 

queue = [] 

heapq.heappush(queue, (1, "Rent"))     # priority 1 

heapq.heappush(queue, (5, "Snacks"))   # priority 5 

heapq.heappush(queue, (2, "Salary"))   # priority 2 

heapq.heappop(queue)    # (1, "Rent") — smallest first
