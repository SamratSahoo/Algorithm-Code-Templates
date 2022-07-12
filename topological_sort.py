from collections import defaultdict, deque

def topological_sort(numCourses, prerequisites):
    # build adjaceny list ("further along" --> "preliminary" elements)
    edges = defaultdict(list)
    for course, prereq in prerequisites:
        edges[course].append(prereq)
        
    # visited set to avoid repetitions in dfs
    visited = set()
    # path to detect cycles
    path = set()

    ordering = deque([]) # NOTE: Not part of Course Schedule Leetcode problem

    # dfs / topological sort method
    def dfs(course):
        # Detects cycle in graph (no valid topo sort)
        if course in path:
            return False
        
        # if the node is already visited then it has a valid topo sort or
        # if the current node has no other neighbors, then it as the "peak" of the graph
        if len(edges[course]) == 0 or course in visited:
            return True
        
        # add the course to the path
        path.add(course)
        # add the course to the visited set
        visited.add(course)
        
        # iterate over neighbors
        for neighbor in edges[course]:
            # return False for the topo sort if there is no valid topo sort for a neighbor
            if not dfs(neighbor):
                return False
        
        # remove the course from the path after iterating
        path.remove(course)
        # add element to the ordering
        ordering.appendleft(course)
        # return True for valid topo sort
        return True
    
    # iterate over all nodes and apply topo sort to verify for a valid topo sort
    for i in range(numCourses):
        if not dfs(i):
            return False

    # return true if all nodes have a valid topo sort
    return True