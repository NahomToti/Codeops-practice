from collections import deque
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


def height(node):
    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


pq = []

heapq.heappush(pq, (3, "Finish Assignment"))
heapq.heappush(pq, (1, "Study"))
heapq.heappush(pq, (5, "Sleep"))
heapq.heappush(pq, (2, "Exercise"))
heapq.heappush(pq, (4, "Watch Movie"))


print("= 1. Binary Search Tree =")

balances = [5000, 2000, 7000, 1000, 3000, 6000, 8000]

root = None

for balance in balances:
    root = insert(root, balance)

print("In-order Traversal:")
inorder(root)

print("\n")

print("= 2. Tree Height =")
print("Tree Height:", height(root))


print("\n= 3. Graph BFS =")

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print("Reachable:", bfs(graph, "A"))


print("\n= 4. Graph DFS =")

print("Reachable:", dfs(graph, "A"))


print("\n= 5. Priority Queue =")

while pq:
    priority, task = heapq.heappop(pq)
    print(priority, "-", task)