def max_value_continuous_sequence():
    
    n, k, bag_size = map(int, input().split())
    
    items = []
    for _ in range(n):
        item_id, value = input().split()
        items.append((int(item_id), float(value)))

    # Step 1: Categorize items into shelves based on shelf number (id % k)
    shelves = {i: [] for i in range(k)}
    for item_id, value in items:
        shelf_num = item_id % k
        shelves[shelf_num].append((shelf_num, item_id, value))
    
    # Step 2: Sort each shelf by descending order of item ID
    for shelf_num in shelves:
        shelves[shelf_num].sort(reverse=True, key=lambda x: x[1])

    # Step 3: Create a flattened list that respects the new continuity rules
    flattened_items = []
    last_non_empty = None

    for i in range(2 * k):  # Traverse twice to simulate circular behavior
        shelf_num = i % k
        if shelves[shelf_num]:  # If shelf has items
            if last_non_empty is not None:
                # If exactly one empty shelf between two non-empty shelves, treat as continuous
                flattened_items.extend(shelves[shelf_num])
            else:
                # If multiple empty shelves, treat as discontinuous and start a new segment
                flattened_items.append(None)  # None signifies a break in continuity
                flattened_items.extend(shelves[shelf_num])
            last_non_empty = shelf_num

    # Initialize max value
    max_value = 0

    # Helper function to check distinct item counts from shelves
    def is_valid(counts):
        count_set = set(counts.values())
        return len(count_set) == len(counts)  # Ensure all counts are unique

    # Backtracking function to explore all valid contiguous sequences
    def backtrack(start, end, current_value, counts):
        nonlocal max_value
        
        # Update max_value if the current sequence is valid and has distinct item counts
        if end - start <= bag_size and is_valid(counts):
            max_value = max(max_value, current_value)

        # Try extending the window by including the next item
        if end < len(flattened_items) and end - start < bag_size:
            next_item = flattened_items[end]
            if next_item is not None:  # Only consider non-None (continuous) items
                next_shelf, _, next_value = next_item
                
                # Update counts and value
                counts[next_shelf] = counts.get(next_shelf, 0) + 1
                backtrack(start, end + 1, current_value + next_value, counts)
                
                # Backtrack by removing the last item added
                counts[next_shelf] -= 1
                if counts[next_shelf] == 0:
                    del counts[next_shelf]

    # Explore all possible starting points within the first half of flattened_items
    original_length = len(flattened_items) // 2
    for i in range(original_length):
        if flattened_items[i] is not None:  # Start only from non-empty entries
            backtrack(i, i, 0, {})

    # Output the maximum total value
    print(f"{max_value:.1f}")

max_value_continuous_sequence()
