class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distances(start):
            n = len(edges)
            dis = [-1] * n

            curr = start
            steps = 0

            while curr != -1 and dis[curr] == -1:
                dis[curr] = steps
                steps += 1
                curr = edges[curr]

            return dis

        dis1 = get_distances(node1)
        dis2 = get_distances(node2)

        min_dis = float("inf")
        res = -1
        for i in range(len(edges)):
            if dis1[i] != -1 and dis2[i] != -1:
                maxi = max(dis1[i], dis2[i])
                if min_dis > maxi:
                    min_dis = maxi
                    res = i

        return res
