class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        at_least_one_edge = set()

        for edge in edges:
            at_least_one_edge.add(edge[1])
        
        no_directed_edges = []
        
        for i in range(n):
            if i not in at_least_one_edge: 
                no_directed_edges.append(i)
        
        return no_directed_edges
        
