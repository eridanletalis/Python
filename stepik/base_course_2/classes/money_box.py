class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.v = 0

    def can_add(self, v):
        if self.v + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.v += v