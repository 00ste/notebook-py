##
# The config folder has the following structure:
# ~/.config/pynotes/
#    config.json
#    profiles/
#       profile1.json
#       profile2.json
#       ...
#
# The main config file is a config.json file which contains configuration about the
# client application, such as the font and text size, as well as the contents of the
# debug screen or custom macros and the default profiles for light, dark and high
# contrast themes.
#
# The profiles/ folder contains a set of *.json file, one for each profile. Profiles
# are used by note files and contain information such as the set of pen profiles (colour,
# width and transparency for each pen) and the page style (size, background colour).
#
# FileReader is the class that handles all of the operations involving reading from
# and writing to files, both config files and note files.
##

import pathlib
import os
import shutil
import json

class FileReader:
    user_config = os.path.join(str(pathlib.Path.home()), '.config/pynotes/config.json')
    default_config = os.path.join(os.getcwd(), 'default.json')
    default_pynotes = os.path.join(os.getcwd(), 'default.pynotes')

    def read_note_file(filepath: str):
        # try opening the given note file
        try:
            return FileReader.decode_file(filepath)
        except:
            # if this file can't be loaded create an empty one
            print(f'no user config file found, initialising from default config file and loading...')
            return FileReader.decode_file(FileReader.default_pynotes)

    def read_config_file(filepath: str):
        # try opening the given config file
        try:
            return FileReader.decode_file(filepath)
        except:
            # if this file can't be loaded try the user config file
            if (os.path.exists(FileReader.user_config)):
                try:
                    print(f'trying to load user config file: {FileReader.user_config}')
                    return FileReader.decode_file(FileReader.user_config)
                # if the user config can't be lodaded, load the default config
                except:
                    print(f'loading default config file: {FileReader.user_config}')
                    return FileReader.decode_file(FileReader.default_config)
            # if the user config file doesn't exist create it and load it
            else:
                # this has to work, otherwise will throw an exception
                print(f'no user config file found, initialising from default config file and loading...')
                path = os.path.join(str(pathlib.Path.home()), '.config/pynotes/')
                os.makedirs(path)
                shutil.copy(FileReader.default_config, FileReader.user_config)
                return FileReader.decode_file(FileReader.user_config)
    
    def decode_file(filepath: str):
        with open(filepath, 'r') as f:
            text = f.read()
            f.close()
            decoder = json.JSONDecoder()
            object = decoder.decode(text)
            print(f'decoded object: {object} from file {filepath}')
            return object

    def write_to_note_file(filepath: str, file_obj):
        file_content = json.dumps(file_obj, indent=4)
        with open(filepath, 'w') as f:
            f.write(file_content)
            f.close()

