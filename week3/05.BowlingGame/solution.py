class Game(object):

    def __init__(self, shots):
        self.shots = []
        for shot in shots:
            self.shots.append(shot)
        self.result = self.total_score()

    def total_score(self):
        score = 0
        index = 0
        for frame in range(10):
            if self._is_strike(index):
                score += 10 + self.shots[index + 1] + self.shots[index + 2]
                index += 1
            elif self._is_spare(index):
                score += 10 + self.shots[index + 2]
                index += 2
            else:
                score += self.shots[index] + self.shots[index + 1]
                index += 2
        return score

    def _is_spare(self, index):
        return self.shots[index] + self.shots[index + 1] == 10

    def _is_strike(self, index):
        return self.shots[index] == 10

