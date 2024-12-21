from collections import deque

def can_traverse(graph, si, ti, mid):
    visited = set()
    queue = deque([si])
    while queue:
        node = queue.popleft()
        if node == ti:
            return True
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited and weight >= mid:
                queue.append(neighbor)
    return False

def max_min_path(n, edges, si, ti):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    low, high = 1, max(w for _, _, w in edges)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_traverse(graph, si, ti, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

# Read input
n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

q = int(input())

changes = []
for _ in range(q):
    ki = int(input())
    change = []
    for __ in range(ki):
        a, b, c = map(int, input().split())
        change.append((a, b, c))
    changes.append(change)

queries = []
for _ in range(q + 1):
    si, ti = map(int, input().split())
    queries.append((si, ti))

# Process each query and changes
results = []
for i in range(q + 1):
    if i > 0:
        for a, b, c in changes[i - 1]:
            for j in range(len(edges)):
                if (edges[j][0] == a and edges[j][1] == b) or (edges[j][1] == a and edges[j][0] == b):
                    edges[j] = (a, b, c)
                    break
    
    si, ti = queries[i]
    results.append(max_min_path(n, edges, si, ti))

for result in results:
    print(result)
