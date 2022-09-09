class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.traversal(graph, [0], 0)
        return self.res
    
    def traversal(self, graph: List[List[int]], path: List[int], node: int):
        if node == len(graph) - 1:
            self.res.append(path[:])  # path.copy()
            return
        for neighbor in graph[node]:
            path.append(neighbor)
            self.traversal(graph, path, neighbor)
            path.pop()
