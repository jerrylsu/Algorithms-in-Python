class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """1.traversing the graph.
           2.coloring while traversing the graph.
           3.return True if the entire graph is corlored, 
             return False if the neighbor nodes have the same color and terminate immediately.
        """
        n = len(graph)
        self.visited = [False] * n
        self.color = [False] * n
        self.is_bipartite = True
        # traversing all subgraphs because subgraphs are not necessarily all connected.
        for cur_node in range(0, n):
            if self.visited[cur_node] == False:
                self.traversal(graph, cur_node)
        return self.is_bipartite
    
    def traversal(self, graph: List[List[int]], cur_node: int):
        if not self.is_bipartite:
            return
        self.visited[cur_node] = True
        for neighbor in graph[cur_node]:
            if self.visited[neighbor] == False:
                self.color[neighbor] = not self.color[cur_node]
                self.traversal(graph, neighbor)
            else:
                if self.color[neighbor] == self.color[cur_node]:
                    self.is_bipartite = False
                    return
        