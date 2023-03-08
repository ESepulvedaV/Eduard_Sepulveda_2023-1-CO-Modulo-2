import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.score import Score
from dino_runner.components.volume import Volume
from dino_runner.components.clouds import Cloud

class Game:
    GAME_SPEED = 20
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu("Press any key to Start ...", self.screen)
        self.music = False
        self.running = False
        self.score_player = Score()
        self.volume = Volume()
        self.cloud = Cloud()

        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
              if not self.playing:
                   self.show_menu()
        pygame.display.quit()
        pygame.quit()
    
              
    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.sound_game()
            

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

        self.volume_config()


    def sound_game(self):
        if not self.music:
            pygame.mixer.music.load('sound1.mp3')
            pygame.mixer.music.play(-1)
            self.music = True

    def volume_config(self):
        keys = pygame.key.get_pressed()
        self.volume.config_vol(keys, self.screen)
                  

    def update(self):
        user_Input = pygame.key.get_pressed()
        self.player.update(user_Input)
        self.obstacle_manager.update(self)
        self.score_player.update_score(self)
        self.cloud.update(self)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score_player.draw_score(self.screen)
        self.cloud.draw(self.screen)

        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    

    def show_menu(self):
         self.menu.reset_screen_color(self.screen)
         half_screen_width = SCREEN_WIDTH // 2
         half_screen_heigth = SCREEN_HEIGHT // 2

         if self.death_count == 0:   
            self.menu.draw(self.screen)
         else:
              self.menu.update_message("Press any Key to Restart")
              self.menu.draw(self.screen)

         self.screen.blit(ICON, (half_screen_width - 50 , half_screen_heigth - 140))
         self.menu.update(self)

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score_player.reset_score()

