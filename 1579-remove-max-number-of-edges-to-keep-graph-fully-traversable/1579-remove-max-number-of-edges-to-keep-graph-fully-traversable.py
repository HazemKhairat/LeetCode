class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: -x[0])
        bob = [i for i in range(n + 1)]
        alice = [i for i in range(n + 1)]
        bob_components = alice_components = n

        def find(node, parent):
            if parent[node] == node:
                return node

            parent[node] = find(parent[node], parent)
            return parent[node]

        def union(n1, n2, parent):
            p1 = find(n1, parent)
            p2 = find(n2, parent)

            if p1 < p2:
                parent[p2] = p1
                return
            parent[p1] = p2

        m = 0
        for t, u, v in edges:
            if (
                t == 3
                and find(u, bob) != find(v, bob)
                and find(u, alice) != find(v, alice)
            ):
                union(u, v, bob)
                union(u, v, alice)
                bob_components -= 1
                alice_components -= 1
            elif t == 2 and find(u, bob) != find(v, bob):
                union(u, v, bob)
                bob_components -= 1
            elif t == 1 and find(u, alice) != find(v, alice):
                union(u, v, alice)
                alice_components -= 1
            else:
                continue
            m += 1

        # print(bob)
        # print(alice)
        # print(alice_components)
        # print(bob_components)
        if alice_components == bob_components == 1:
            return len(edges) - m

        return -1
