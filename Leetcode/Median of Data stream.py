import heapq
class MedianFinder:

    def __init__(self):
        self.maxhp=[]
        self.minhp=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxhp,-num)
        heapq.heappush(self.minhp,-heapq.heappop(self.maxhp))
        if len(self.maxhp) < len(self.minhp):
            heapq.heappush(self.maxhp,-heapq.heappop(self.minhp))

    def findMedian(self) -> float:
        if len(self.maxhp) == len(self.minhp):
            return (float(-(self.maxhp[0]))+float(self.minhp[0]))/2 
        return -(self.maxhp[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()