class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        conected=0
        visited=set()

        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        for r in range(n):
            if r not in visited:
                conected+=1
                dfs(r)
        return conected


        