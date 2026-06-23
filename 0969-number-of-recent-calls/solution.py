class RecentCounter:

    def __init__(self):
        self.rc=deque()
        

    def ping(self, t: int) -> int:
        self.rc.append(t)
        while t-self.rc[0]>3000:
            self.rc.popleft()
        return len(self.rc)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
