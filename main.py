import pygame

from FileReader import FileReader

class Window:
    def __init__(self) -> None:
        pygame.init()
        # read note file
        # TODO: actually read a file
        self.file_object = FileReader.read_note_file('')
        # read config file
        # TODO: actually read a file
        self.config = FileReader.read_config_file('')
        self.surface = pygame.display.set_mode((
            self.config['client']['display_width'],
            self.config['client']['display_height']
        ))
        self.current_pen = 0
        # 60 fps should probably remain constant
        self.FPS = 60
        # every how many frames a point should get recorded should also be constant but we'll see
        self.record_interval = 20
        self.clock = pygame.time.Clock()
        self.frame = 0
        self.running = False

        # some aliases for commonly used variables
        self.current_page = self.file_object['pages'][self.file_object['session']['page']]
    
    def run(self):
        running = True
        need_velo = False
        recording = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print('mouse down')
                    # START RECORDING STROKE
                    # create an empty stroke in the current
                    recording = True
                    self.current_page['strokes'].append({
                        'pen': self.current_pen,
                        'points': []
                    })

                elif event.type == pygame.MOUSEBUTTONUP:
                    print('mouse up')
                    # END RECORDING STROKE
                    self.frame = 0
                    recording = False
                    print(self.current_page['strokes'][-1])
                
                elif event.type == pygame.KEYDOWN:
                    print('key down')
            
            # RECORD VELOCITY POINT FIRST (EVEN IF NOT RECORDING TO GUARANTEE THAT EVERY POSITION POINT
            # GETS A RESPECTIVE VELOCITY POINT)
            if need_velo:
                self.current_page['strokes']['points'][-1].append((
                    pygame.mouse.get_pos()[0] - self.current_page['strokes'][-1]['points'][-1][0]*self.FPS,
                    pygame.mouse.get_pos()[1] - self.current_page['strokes'][-1]['points'][-1][1]*self.FPS
                ))
                need_velo = False

            if recording:
                if self.frame == 0:
                    self.current_page['strokes'][-1]['points'].append(pygame.mouse.get_pos())
                    need_velo = 0
                self.frame = (self.frame+1) % self.record_interval

            self.clock.tick(self.FPS)
    
    def render(self):
        print('rendering page...')


if __name__ == '__main__':
    w = Window()
    w.run()