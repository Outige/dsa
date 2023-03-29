class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if graph[course] == []:
                return True
            
            visit.add(course)

            for pre in graph[course]:
                defs(pre)
            
            visit.remove(course)
            graph[course] = []
        