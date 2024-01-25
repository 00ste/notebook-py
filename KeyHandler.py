import pygame

class KeyHandler:
    '''
    # TODO:
                                    *****
    pygame.K_x -------------------> *   *                                         ******
                                    * I * -------> '[CTRL ][SHIFT ][ALT ]X' ----> * II * ------> 'operation_code'
    pygame.keys.get_pressed() ----> *   *                                         ******
                                    *****

    a dictionary is not the best way to do this
    '''
    def __init__(self, keybinds_table) -> None:
        self.keybinds_table = keybinds_table
        self.key_code_table = {}
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.key_code_table[getattr(pygame, f'K_{letter.lower()}')] = letter
        for number in '1234567890':
            self.key_code_table[getattr(pygame, f'K_{number}')] = number
    
    def get_key_operation(self, pygame_key_code, pygame_keys_held):
        key_combination = ''
        for special_key in ['SHIFT', 'ALT', 'CTRL']:
            pass
        if pygame_key_code not in self.key_code_table.keys():
            return
        decoded_key = self.key_code_table[pygame_key_code]
        for operation in self.keybinds_table.keys():
            print(f'key associated with {operation} is {self.keybinds_table[operation]}')
            if decoded_key in self.keybinds_table[operation]:
                return operation