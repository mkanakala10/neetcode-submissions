class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for req in prerequisites:
            adj_list[req[0]].append(req[1])
            
        visiting = set()
        completed = set()
        
        for i in range(numCourses):
            if i in completed:
                continue
                
            stack = [i]
            
            while stack:
                curr = stack[-1]
                
                if curr in completed:
                    stack.pop()
                    continue
                    
                if curr in visiting:
                    visiting.remove(curr)
                    completed.add(curr)
                    stack.pop()
                    continue
                    
                visiting.add(curr)
                
                for neighbor in adj_list[curr]:
                    if neighbor in visiting:
                        return False
                    if neighbor not in completed:
                        stack.append(neighbor)
                        
        return True