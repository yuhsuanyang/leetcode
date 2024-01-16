# no. 380
import random
class RandomizedSet:

    def __init__(self):
        self.num_set = []
        return

    def insert(self, val: int) -> bool:
        for i in self.num_set:
            if i == val:
                return False
        self.num_set.append(val)
        return True

    def remove(self, val: int) -> bool:
        for i in range(len(self.num_set)):
            if self.num_set[i] == val:
                del self.num_set[i]
                return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.num_set)

