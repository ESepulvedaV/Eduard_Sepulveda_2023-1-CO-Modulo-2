import pygame

from dino_runner.utils.constants import FONT_STYLE

class Score:
    def __init__(self):
        self.score = 0
        self.highscore = 0 

    def update_score(self, game):
        self.score += 1

        if self.score % 100 == 0 and game.game_speed < 500:
              game.game_speed += 5

        if self.score > self.highscore:
            self.highscore = self.score      

    def draw_score(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Score: {self.score}    HighScore: {self.highscore}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (860, 50)
        screen.blit(text, text_rect)


    def reset_score(self):
        self.score = 0


        
  