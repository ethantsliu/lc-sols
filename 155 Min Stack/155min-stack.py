class MinStack(object):

    def __init__(self):
        self.stk = []
        self.mini = [] #min values 

    def push(self, val):
        self.stk.append(val)
        if not self.mini or val <= self.mini[-1]:
            self.mini.append(val)

    def pop(self):
        if self.stk:
            x = self.stk.pop()
            if x == self.mini[-1]:
                self.mini.pop()

    def top(self):
        return self.stk[-1] if self.stk else None


    def getMin(self):
        return self.mini[-1] if self.stk else None