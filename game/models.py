from django.db import models

class Game(models.Model):
    board = models.CharField(max_length=9, default=' ' * 9)
    current_turn = models.CharField(max_length=1, default='X')
    winner = models.CharField(max_length=1, null=True, blank=True)
    game_over = models.BooleanField(default=False)

    def make_move(self, position, player):
        if self.board[position] == ' ' and not self.game_over:
            board_list = list(self.board)
            board_list[position] = player
            self.board = ''.join(board_list)
            self.check_winner()
            self.switch_turn()
            self.save()

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                self.winner = self.board[combo[0]]
                self.game_over = True
                break
        if ' ' not in self.board and not self.winner:
            self.game_over = True

    def switch_turn(self):
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'
