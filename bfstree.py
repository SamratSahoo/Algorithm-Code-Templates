from collections import deque

# Traverse Tree Level by Level
def bfs(root):
    # Queue required for BFS
    queue = deque()

    # Add root to the queue
    queue.append(root)

    # Keep track of whatever result you want
    results = []

    # Traverse tree while the queue is not empty
    while len(queue) > 0:

        # Size = number of nodes on curent level
        size = len(queue)
        level = []

        # Traverse through the current level you are on
        for i in range(size):

            # Get the current node
            current = queue.popleft()

            # If there is a left child, add it to the queue
            if current.left:
                queue.append(current.left)

            # If there is a right child, add it to the queue
            if current.right:
                queue.append(current.right)
            
            # Add current child to whatever result you need
            level.append(current)
        results.append(level)

    # Return result
    return results


