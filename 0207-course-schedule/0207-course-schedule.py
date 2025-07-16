class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indgree = [0] * numCourses
        for p in prerequisites:
            graph[p[0]].append(p[1])
            indgree[p[1]] += 1

        queue = deque()
        for i in range(numCourses):
            if indgree[i] == 0:
                queue.append(i)

        processed = 0
        while queue:
            node = queue.popleft()
            processed += 1
            for nighbour in graph[node]:
                indgree[nighbour] -= 1
                if indgree[nighbour] == 0:
                    queue.append(nighbour)

        return processed == numCourses
