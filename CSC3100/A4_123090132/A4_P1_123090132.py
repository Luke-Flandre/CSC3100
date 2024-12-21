from itertools import permutations, product


def floyd_warshall(n, edges):
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Distance from a node to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Fill in the initial distances based on the provided edges
    for u, v, w in edges:
        dist[u-1][v-1] = w
        dist[v-1][u-1] = w  # Since the graph is undirected
    
    # Apply Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        
    return dist

def generate_orders(numbers):
    # Validate the input length
        
    first, last = numbers[0], numbers[-1]
    middle = numbers[1:-1]
    
    # Form pairs from the middle numbers
    pairs = [(middle[i], middle[i + 1]) for i in range(0, len(middle), 2)]
    
    # Generate all pair permutations
    pair_permutations = permutations(pairs)
    
    # Generate all combinations of internal pair swaps
    all_orders = []
    for perm in pair_permutations:
        # Generate all internal swaps for the current permutation
        internal_swaps = product(*[(p, (p[1], p[0])) for p in perm])
        for swapped in internal_swaps:
            # Flatten the pairs and add the first and last elements
            order = [first] + [num for pair in swapped for num in pair] + [last]
            all_orders.append(order)
    
    return all_orders

def shortest_path_through_edges(dist, mandatory_edges, start, end):
    # Convert edges to a flat list of nodes
    flat_nodes = [start] + [node - 1 for edge in mandatory_edges for node in edge[:2]] + [end]
    
    # Generate all valid orders of nodes
    all_orders = generate_orders(flat_nodes)
    
    min_distance = float('inf')
    distance = []
    
    for order in all_orders:
        total_distance = 0
        for i in range(0,len(order) - 1,2):
            u = order[i]
            v = order[i + 1]
            total_distance += dist[u][v]
        
        

        min_distance = min(total_distance, min_distance)
    
        
    
    
    return min_distance
def main():
    # Read the first line containing n, m, q
    n, m, q = map(int, input().split())

    edges = []
    mustgo = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    dist_matrix = floyd_warshall(n, edges)

    results = []
    for _ in range(q):
        k = int(input())
        mandatory_edge_indices = list(map(int, input().split()))
        mandatory_edges = [edges[i-1] for i in mandatory_edge_indices]
        mustgo.append(mandatory_edges)
    for _ in range(q):
        s, t = map(int, input().split())
        min_distance = shortest_path_through_edges(dist_matrix, mustgo[_], s - 1, t - 1)
        min_distance += sum(i[2] for i in mustgo[_])
        results.append(min_distance)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
