class Chain:
    def __init__(self, start: str, target: str):
        # map to bool arrays
        self._state = [ele == "1" for ele in list(start)]
        self.__target = [ele == "1" for ele in list(target)]
        self.__length = len(self._state)
        self.__counter = 0

    def need_to_change(self, rank: int) -> bool:
        return self._state[rank] != self.__target[rank]

    def _change(self, rank: int):
        if not self.can_change_rank(rank):
            self._make_changeable(rank)
        self._state[rank] = not self._state[rank]
        self.__counter += 1

    def can_change_rank(self, rank: int) -> bool:
        # last one can always be switched
        if rank == self.__length - 1:
            return True
        # cannot switch if n+1 is off
        if not self._state[rank+1]:
            return False
        result = True
        # inspect n+2...N
        while result:
            for i in range(self.__length - rank - 1):
                result &= not self._state[rank+i]
            break
        return result

    def _make_changeable(self, rank: int):
        # turn on n+1
        if not self._state[rank + 1]:
            self._change(rank + 1)
        # turn off n+2...N
        for i in range(self.__length - rank - 2):
            if self._state[rank + 2 + i]:
                self._change(rank + 2 + i)

    def compute(self) -> bool:
        for i in range(self.__length):
            if self.need_to_change(i):
                self._change(i)
        return self.__counter
