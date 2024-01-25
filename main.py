import pygame
import array

from FileReader import FileReader
from Renderer import Renderer
from KeyHandler import KeyHandler

class Window:
    def __init__(self) -> None:
        pygame.init()
        # read note file
        # TODO: get filename from command line args (but default to user config)
        self.opened_file_path = '/home/stefano/code/python/pynotes/project/testfiles/note.pynotes'
        self.file_object = FileReader.read_note_file(self.opened_file_path)
        # read config file
        # TODO: get filename from command line args or from opening a pynotes file from os gui
        self.config = FileReader.read_config_file(FileReader.user_config)

        # some aliases for commonly used variables
        self.current_page = self.file_object['pages'][self.file_object['session']['page']]
        self.pen_profiles = self.file_object['profile']['pen_profiles']
        self.width, self.height = self.config['client']['display_width'], self.config['client']['display_height']

        self.surface = pygame.display.set_mode((self.width, self.height))
        self.surface_buffer = array.array('B', [0]*self.width*self.height*4)

        self.current_pen = 0
        # 60 fps should probably remain constant
        self.FPS = 60
        # every how many frames a point should get recorded should also be constant but we'll see
        self.record_interval = 3
        self.clock = pygame.time.Clock()
        self.frame = 0
        self.running = False
        self.renderer = Renderer(self.surface_buffer, self.width, self.height)

        # set keybinds table for keybinds
        self.key_handler = KeyHandler(self.config['client']['keybinds'])
    
    def run(self):
        running = True
        need_velo = False
        recording = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # TODO: handle file saving
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
                    operation = self.key_handler.get_key_operation(event.key, pygame.key.get_pressed())
                    print(f'operation is: {operation}')
                    for pen_number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        if operation == f'select_pen_{pen_number}':
                            self.current_pen = (pen_number-1) % 10
                    
            
            # RECORD VELOCITY POINT FIRST (EVEN IF NOT RECORDING TO GUARANTEE THAT EVERY POSITION POINT
            # GETS A RESPECTIVE VELOCITY POINT)
            if need_velo:
                mouse_pos = pygame.mouse.get_pos()
                prev_pos = self.current_page['strokes'][-1]['points'][-1]
                # not sure why you need the 0.05 factor but sure i'll have it
                velo = (
                    (mouse_pos[0] - prev_pos[0])*self.FPS*0.05,
                    (mouse_pos[1] - prev_pos[1])*self.FPS*0.05
                )
                print(f'recording velocity... {velo} from current {mouse_pos} and previous {prev_pos}')
                self.current_page['strokes'][-1]['points'].append(velo)
                need_velo = False

            if recording:
                if self.frame == 0:
                    print(f'recording position... {pygame.mouse.get_pos()}')
                    self.current_page['strokes'][-1]['points'].append(pygame.mouse.get_pos())
                    need_velo = True
                self.frame = (self.frame+1) % self.record_interval

            self.render()
            self.clock.tick(self.FPS)
        
        # saving file when closing
        print('saving...')
        if self.opened_file_path != '':
            FileReader.write_to_note_file(self.opened_file_path, self.file_object)
    
    def render(self):
        print('rendering page...')
        self.surface.fill('#FFFFFF')
        for stroke in self.current_page['strokes']:
            self.renderer.render_stroke(stroke['points'], self.pen_profiles[stroke['pen']])
        
        from_cairo = pygame.image.fromstring(self.surface_buffer.tobytes(), (self.width, self.height), 'BGRA')
        self.surface.blit(from_cairo, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    w = Window()
    w.run()