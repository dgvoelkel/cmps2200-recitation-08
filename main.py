from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    def ssp_helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            cost, node = heappop(frontier)
            current_weight, current_edges = cost
            
            if node in visited:
                return ssp_helper(visited, frontier)
            else:
                visited[node] = (current_weight, current_edges)
                for neighbor, weight in graph.get(node, set()):
                    new_weight = current_weight + weight
                    new_edges = current_edges + 1
                    heappush(frontier, ((new_weight, new_edges), neighbor))
                
                return ssp_helper(visited, frontier)
    frontier = []
    heappush(frontier, ((0, 0), source))
    visited = dict()
    return ssp_helper(visited, frontier)
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """

    frontier = deque([source])

    parents = {source: None}
    
    while frontier:
        current = frontier.popleft()

        for neighbor in graph.get(current, set()):
            if neighbor not in parents:
                parents[neighbor] = current
                frontier.append(neighbor)
                
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    curr = destination

    while curr is not None:
        path.append(curr)
        curr = parents.get(curr)
    path.reverse()

    return "".join(path[:-1])

