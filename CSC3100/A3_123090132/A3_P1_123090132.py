from collections import defaultdict

class Tree:
    def __init__(self, n):
        self.n = n  # number of nodes
        self.edges = defaultdict(list)  # adjacency list to store nodes and weights

    def add_edge(self, u, v, w):
        # Since it's an undirected tree, add edges both ways
        self.edges[u].append((v, w))
        self.edges[v].append((u, w))

    def find_deepest_branch(self, root):
        visited = set()
        max_distance = 0
        deepest_branch = []

        # Helper function to perform DFS and track the deepest path
        def dfs(node, distance, height, path):
            nonlocal max_distance, deepest_branch
            visited.add(node)
            path.append(node)

            # If this is a leaf node and the current distance is the maximum so far, update the deepest branch
            if distance > max_distance and len(self.edges[node]) == 1 and node != root:
                max_distance = distance
                deepest_branch = path[:]

            # Explore neighbors
            for neighbor, original_weight in self.edges[node]:
                if neighbor not in visited:
                    # Calculate the modified weight based on height
                    adjusted_weight = max(0, original_weight - height - 1)
                    dfs(neighbor, distance + adjusted_weight, height + 1, path)

            # Backtrack
            path.pop()
            visited.remove(node)

        # Start DFS from the root node
        dfs(root, 0, 0, [])
        
        return max_distance, deepest_branch

# Input the data
n, m, t = map(int, input().split())
tree = Tree(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    tree.add_edge(u, v, w)

# Find the deepest branch from the root (node `t` as per the input)
max_distance, deepest_branch = tree.find_deepest_branch(t)
print(max_distance)
