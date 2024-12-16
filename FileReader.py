##
# The config folder has the following structure:
# ~/.config/notebook-py/
#    client.json
#    themes/
#       theme1.json
#       theme2.json
#       ...
#
# The client config file is a json file which contains configuration about the
# client application, such as the font and text size, as well as the contents of the
# debug screen or custom macros and the default page settings and themes.
#
# The themes/ folder contains a set of *.json file, one for each theme. Themes
# are used by note files and contain information such as the set of pen profiles (colour,
# width and transparency for each pen) and the page background color.
#
# FileReader is the class that handles all of the operations involving reading from
# and writing to files, both config files and note files.
##

import pathlib
import os
import shutil
import json

class FileReader:
    client_config = os.path.join(str(pathlib.Path.home()), '.config/notebook-py/config.json')
    default_notebook = os.path.join(str(pathlib.Path.home()), '.config/notebook-py/default.nbpy')

    builtin_client_config = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'default.json')
    builtin_notebook = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'default.nbpy')


    def read_notebook(filepath: str):
        # create the notebook file if not present
        if not os.path.isfile(filepath):

            # create the default notebook file if not present
            if not os.path.isfile(FileReader.default_notebook):
                shutil.copy(FileReader.builtin_notebook, FileReader.default_notebook)
            
            print(f'Trying to copy {FileReader.default_notebook} to {filepath}')
            shutil.copy(FileReader.default_notebook, filepath)
            print(f'Notebook file {filepath} created successfully!')
        
        return FileReader.decode_file(filepath)

    def read_client_config(filepath: str):
        # read given client config file
        if os.path.isfile(filepath):
            return FileReader.decode_file(filepath)
        
        # create client config file inside .config/notebook-py if not present
        print(f'Could not find specified config file {filepath}, defaulting to {FileReader.client_config}')
        if not os.path.isfile(FileReader.client_config):

        return FileReader.decode_file(filepath)
        
        # copy file inside

        

        # try opening the given config file
        try:
            return FileReader.decode_file(filepath)
        except:
            # if this file can't be loaded try the user config file
            if (os.path.exists(FileReader.client_config)):
                try:
                    print(f'trying to load user config file: {FileReader.client_config}')
                    return FileReader.decode_file(FileReader.client_config)
                # if the user config can't be lodaded, load the default config
                except:
                    print(f'loading default config file: {FileReader.client_config}')
                    return FileReader.decode_file(FileReader.default_client_config)
            # if the user config file doesn't exist create it and load it
            else:
                # this has to work, otherwise will throw an exception
                print(f'no user config file found, initialising from default config file and loading...')
                path = os.path.join(str(pathlib.Path.home()), '.config/notebook-py/')
                os.makedirs(path)
                shutil.copy(FileReader.default_client_config, FileReader.client_config)
                return FileReader.decode_file(FileReader.client_config)
    
    def decode_file(filepath: str):
        with open(filepath, 'r') as f:
            text = f.read()
            f.close()
            decoder = json.JSONDecoder()
            object = decoder.decode(text)
            return object

    def write_notebook(filepath: str, file_obj):
        file_content = json.dumps(file_obj, indent=4)
        with open(filepath, 'w') as f:
            f.write(file_content)
            f.close()

