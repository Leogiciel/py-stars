class Chain:
    def __init__(self, string):
        lines = string.splitlines()
        # map to bool arrays
        self.state = [ele == "1" for ele in list(lines[0])]
        self.target = [ele == "1" for ele in list(lines[1])]
        self.length = len(self.state)
        self.counter = 0

    def need_to_change(self, rank):
        return self.state[rank] != self.target[rank]

    def change(self, rank):
        if not self.can_change_rank(rank):
            self.make_changeable(rank)
        self.state[rank] = not self.state[rank]
        self.counter += 1

    def can_change_rank(self, rank):
        # last one can always be switched
        if rank == self.length - 1:
            return True
        # cannot switch if n+1 is off
        if not self.state[rank+1]:
            return False
        result = True
        # inspect n+2...N
        while result:
            for i in range(self.length - rank - 1):
                result &= not self.state[rank+i]
            break
        return result

    def make_changeable(self, rank):
        # turn on n+1
        if not self.state[rank + 1]:
            self.change(rank + 1)
        # turn off n+2...N
        for i in range(self.length - rank - 2):
            if self.state[rank + 2 + i]:
                self.change(rank + 2 + i)

    def compute(self):
        for i in range(self.length):
            if self.need_to_change(i):
                self.change(i)
        return self.counter
