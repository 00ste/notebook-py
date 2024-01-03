import pygame

class Window:
    def __init__(self) -> None:
        pygame.init()
        # TODO: replace with values from config file
        self.WIDTH, self.HEIGHT = 1000, 700
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # 60 fps should probably remain constant
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.frame = 0
        self.running = False
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print('mouse down')
                elif event.type == pygame.MOUSEBUTTONUP:
                    print('mouse up')
                elif event.type == pygame.KEYDOWN:
                    print('key down')
    
            print(self.frame)
            self.frame += 1
            self.clock.tick(self.FPS)
    
    def render():
        print('rendering page...')


if __name__ == '__main__':
    w = Window()
    w.run()