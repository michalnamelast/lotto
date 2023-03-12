import random

class Lotto:
    def __init__(self):
        self.chosen_numbers = [5,7,14,23,34,39]

    def bet(self):
        self.drawn_numbers = self._generate_number()
        self.hits = self._check_matches()
        return self.hits

    def _generate_number(self):
        return [random.randint(1, 49) for element in range(6)]

    def _check_matches(self):
        return [element for element in self.chosen_numbers if element in self.drawn_numbers]


class Counter:
    def __init__(self):
        self.budget = 0
        self.summary_win = 0
        self.hit_price = {0:0, 1:0, 2:0, 3:24, 4:204.9, 5:5997.5, 6:4059640}

    def count(self, points):
        self._update_budget()
        self._update_winnings(points)
        return f' Summary win: {self.summary_win}zł Budget: {self.budget}zł'

    def _update_budget(self):
        self.budget -= 3

    def _update_winnings(self, points):
        self.summary_win += self.hit_price[points]
        self.summary_win = self._round_winnings(self.summary_win)

    def _round_winnings(self, number):
        return round(number, 2)



class LetsRoll:
    def __init__(self):
        self.trials_number = 0
        self.game = Lotto()
        self.counter = Counter()

    def start(self):
        hits = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        while hits[6] == 0:
            game_result = self.game.bet()
            self.trials_number += 1
            hits[len(game_result)] += 1
            Test(self.trials_number, len(game_result))
            self._display_result(hits)
        print('We got the 6!')

    def _display_result(self, hits):
        print(f'attempt n0: {self.trials_number}, {hits}, {self.counter.count(len(self.game.bet()))}')
        # print(self.counter.count(len(self.game.bet())))


class Test:
    def __init__(self, attempt, hits):
        self.attempt_number = attempt
        self.hits = hits
        self.show_win_details()

    def show_win_details(self):
        if self.hits == 5 or self.hits == 6:
            with open('trafienia.txt', 'a') as file:
                text = f'{self.attempt_number}, {self.hits} \n'
                file.write(text)



LetsRoll().start()
