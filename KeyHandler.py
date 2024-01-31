import pygame

class KeyHandler:
    def __init__(self, keybinds_table) -> None:
        self.keybinds_table = keybinds_table
        self.key_code_table = {}
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.key_code_table[getattr(pygame, f'K_{letter.lower()}')] = letter
        for number in '1234567890':
            self.key_code_table[getattr(pygame, f'K_{number}')] = number
    
    def get_key_operation(self, pygame_key_code, pygame_mod_keys):
        # get pressed key and held mod keys to build the shortcut string
        if pygame_key_code not in self.key_code_table.keys():
            return
        shortcut_string = ''
        if (pygame_mod_keys & pygame.KMOD_CTRL):
            shortcut_string += 'CTRL '
        if (pygame_mod_keys & pygame.KMOD_SHIFT):
            shortcut_string += 'SHIFT '
        if (pygame_mod_keys & pygame.KMOD_ALT):
            shortcut_string += 'ALT '
        shortcut_string += self.key_code_table[pygame_key_code]

        # look for the operation in the keybinds table that uses that key combination
        for operation in self.keybinds_table.keys():
            print(f'key associated with {operation} is {self.keybinds_table[operation]}')
            if shortcut_string in self.keybinds_table[operation]:
                return operation