import unittest


class Chain:
    def __init__(self, string):
        lines = string.splitlines()
        self.state = [ele == "1" for ele in list(lines[0])]
        self.target = [ele == "1" for ele in list(lines[1])]
        self.length = len(self.state)
        self.counter = 0

    def need_to_change(self, rank):
        result = self.state[rank] != self.target[rank]
        return result

    def change(self, rank):
        if not self.can_change_rank(rank):
            self.make_changeable(rank)
        self.state[rank] = not self.state[rank]
        self.counter += 1

    def can_change_rank(self, rank):
        if rank == self.length - 1:
            return True
        if not self.state[rank+1]:
            return False
        result = True
        for i in range(self.length - rank - 1):
            result &= not self.state[rank+i]
        return result

    def make_changeable(self, rank):
        if not self.state[rank + 1]:
            if not self.can_change_rank(rank + 1):
                self.make_changeable(rank + 1)
            self.change(rank + 1)
        for i in range(self.length - rank - 2):
            if self.state[rank + 2 + i]:
                if not self.can_change_rank(rank + 2 + i):
                    self.make_changeable(rank + 2 + i)
                self.change(rank + 2 + i)

    def compute(self):
        for i in range(self.length):
            if self.need_to_change(i):
                self.change(i)
        return self.counter
