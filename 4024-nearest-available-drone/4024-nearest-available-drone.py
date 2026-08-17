class Solution(object):
    def nearestDrone(self, drones, target):
        """
        :type drones: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        rang = 0
        ans = []
        for i in range(len(drones)):
            rang = drones[i][2]
            if abs(drones[i][0]-target[0])+abs(drones[i][1]-target[1])<=rang:
                ans.append(abs(drones[i][0]-target[0])+abs(drones[i][1]-target[1]))
            else:
                ans.append(float("inf"))

        
        if min(ans)==float('inf'):
            return -1
        else:
            return ans.index(min(ans))
