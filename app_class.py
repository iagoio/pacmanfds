import pygame, sys
from settings import *


pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = WIDTH//28
        self.cell_height = HEIGHT//36

        self.load()


    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
############################# HELPER FUNCTIONS ######################
    def draw_text (self, words, screen, pos, size, colour, font_name, centered = False ):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def load(self):
        self.bg = pygame.image.load('maz11 (1).png')
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))

    def draw_grid(self):
        for x in range(WIDTH//cell_width):
            pygame.draw.line(self.screen, GREY, (x*cell_width//28, 0), (x*cell_width//28, HEIGHT))
        for x in range(HEIGHT//cell_height):
            pygame.draw.line(self.screen, GREY, (0, x*self.cell_height), (WIDTH, x*self.cell_height))


############################# INTRO FUNCTIONS ######################


    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'



    def start_update(self):
        pass





    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('APPUIER SUR LA CLE "ESPACE"', self.screen, [WIDTH//2, HEIGHT//2], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text('SEULEMENT UN JOUEUR', self.screen, [WIDTH//2, HEIGHT//2 + 50], START_TEXT_SIZE, (65, 105, 225), START_FONT, centered=True)
        self.draw_text('HIGH SCORE', self.screen, [WIDTH//2,0], START_TEXT_SIZE, (255, 255, 255), START_FONT)
        pygame.display.update()

############################# PlAYING FUNCTIONS###########################
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False




    def start_update(self):
        pass





    def start_draw(self):
        self.screen.blit(self.bg, (0,0))
        self.draw_grid()
        pygame.display.update()
