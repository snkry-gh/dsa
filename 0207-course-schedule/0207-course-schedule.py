class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = defaultdict(list)

        for c, p in prerequisites:
            pre[c].append(p)
        
        taken = set()

        def dfs(c):

            if not pre[c]:
                return True

            if c in taken:
                return False
            
            taken.add(c)

            for p in pre[c]:
                if not dfs(p): return False
            
            pre[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        
        return True

            
