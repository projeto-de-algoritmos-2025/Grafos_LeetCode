class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path[:])
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
        dfs(0, [0])
        return res
