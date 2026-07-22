#Big-o complexity
first = accounts[0]              # O(1) — one operation 
  
for acc in accounts:            # O(n) — each account once 
    print(acc.owner) 
  
for a in accounts:              # O(n^2) — loop inside a loop 
    for b in accounts: 
        if a.owner == b.owner: 

 #Array
 accounts = [acc0, acc1, acc2] 
accounts[2]            # O(1) — jump straight to it 
accounts.append(acc)  # O(1)* —amortised(occasionally resizes) 
accounts.insert(0, x) # O(n) — every later item shifts 
x in accounts         # O(n) — may check every item

#hashmap
accounts = {"CBE-1": acc1, "CBE-2": acc2} 
accounts["CBE-1"]       # O(1) — look up by key 
accounts["CBE-3"] = x   # O(1) — insert 
"CBE-1" in accounts     # O(1) — membership on keys 
del accounts["CBE-1"]   # O(1) — delete

#linked list 
class Node: 
def __init__(self, data): 
self.data = data 
self.next = None     # points to the next node 
head = Node(acc1) 
head.next = Node(acc2)       # acc1 -> acc2 -> None 

#stack
stack = [] 
stack.append(x) # push — O(1)   
stack.pop()     # pop  — O(1), removes the most recent

#queue
from collections import deque 
q = deque() 
q.append(x)  # enqueue — O(1), joins the back        
q.popleft()  # dequeue — O(1), serves the front

