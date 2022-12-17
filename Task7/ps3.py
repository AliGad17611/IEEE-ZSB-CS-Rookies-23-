class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mn = 0
        list1 =[]
        for i in range(len(points)):
            r = (((points[i][0])**2)+((points[i][1])**2))**0.5
            if r<=mn:
                mn = r
                list1.append(points[i])
        return list1[-k::]