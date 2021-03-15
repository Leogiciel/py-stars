"""Chain module

Returns:
    Chain: Representation of the star lights chain
"""
from typing import List


class Chain:
    """Representation of the star lights chain"""
    def __init__(self, start: str, target: str) -> None:
        # map to bool arrays
        self._state: List[bool] = [ele == "1" for ele in list(start)]
        self.__target: List[bool] = [ele == "1" for ele in list(target)]
        self.__length: int = len(self._state)
        self.__counter: int = 0

    def need_to_change(self, rank: int) -> bool:
        """Computes if light at rank n must be switched

        Args:
            rank (int): rank to check

        Returns:
            bool: difference between state and target at rank n
        """
        return self._state[rank] != self.__target[rank]

    def _change(self, rank: int) -> None:
        """Change light state at given rank

        Args:
            rank (int): rank to switch
        """
        if not self.can_change_rank(rank):
            self._make_changeable(rank)
        self._state[rank] = not self._state[rank]
        self.__counter += 1

    def can_change_rank(self, rank: int) -> bool:
        """Computes if light at given rank can be switched

        Args:
            rank (int): rank to check

        Returns:
            bool: True if light can be switched
        """
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

    def _make_changeable(self, rank: int) -> None:
        """Perform operations to make light at given rank switchable

        Args:
            rank (int): rank of the light to make switchable
        """
        # turn on n+1
        if not self._state[rank + 1]:
            self._change(rank + 1)
        # turn off n+2...N
        for i in range(self.__length - rank - 2):
            if self._state[rank + 2 + i]:
                self._change(rank + 2 + i)

    def compute(self) -> int:
        """Computes the minimum operations to switch all lights from the initial state to the final state

        Returns:
            int: number of steps to perform
        """
        for i in range(self.__length):
            if self.need_to_change(i):
                self._change(i)
        return self.__counter
