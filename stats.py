class Stats():
    'stat tracking'

    def __init__(self):
        'initializes statistics'
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        'stats that vary during play'
        self.guns_left = 2
        self.score = 0

