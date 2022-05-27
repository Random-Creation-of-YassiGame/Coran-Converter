# -*- coding: UTF-8 -*-
#  ______________________________________________________________
# |  __________________________________________________________  |
# | | Debut du système ;)                                      | |
# | |  → "Créé par YassiGame | Ici c'est le main de l'app"     | |
# | |__________________________________________________________| |
# |______________________________________________________________|

print(f'''
       ______                         ______                           __           
      / ____/___  _________ _____    / ____/___  ____ _   _____  _____/ /____  _____
     / /   / __ \/ ___/ __ `/ __ \  / /   / __ \/ __ \ | / / _ \/ ___/ __/ _ \/ ___/
    / /___/ /_/ / /  / /_/ / / / / / /___/ /_/ / / / / |/ /  __/ /  / /_/  __/ /    
    \____/\____/_/   \__,_/_/ /_/  \____/\____/_/ /_/|___/\___/_/   \__/\___/_/     
                                                          --- Created by YassiGame ---
''')

print("Checking for the modules...")


#  ___________________________________________________________________
# |  _______________________________________________________________  |
# | | Importations (Import des modules Python):                     | |
# | |  → "Pour evité des bugs en essaye de importé chaque module    | |
# | |        s'il n'est pas présent, on l'installe automatiquement" | |
# | |_______________________________________________________________| |
# |___________________________________________________________________|

### function created for install module if not exist:
def install(package):
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


### --- Import with no errors: --- (Pov: J'essaye un petit programme, je promet rien...)

## Import with try statement the module (tkinter):
try:
    from tkinter import *
    import tkinter
except ModuleNotFoundError:
    install('tkinter')
else:
    print(" ↪ Tkinter is installed")

## Import with try statement the module (pillow):
try:
    from PIL import ImageTk, Image
except ModuleNotFoundError:
    install('pillow')
else:
    print(" ↪ Pillow is installed")



import json, os, shutil, zipfile, requests
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from scripts.app import launchapp

zip_to_install = 'https://github.com/Random-Creation-of-YassiGame/Coran-Converter/archive/refs/heads/main.zip'
update_cache_in_github = 'https://raw.githubusercontent.com/Random-Creation-of-YassiGame/Coran-Converter/main/data/files/cache/cache_version.json'
path_update_cache = "../data/files/cache/cache_version.json"
update_zipfile = '../data/files/cache/update/update.zip'


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x50')

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()

def LaunchUpdate():
    try:
        r = requests.get(zip_to_install, allow_redirects=True)

    except requests.exceptions.ConnectionError:
        print("Download Error: We think, you have no connection or you are banned ip from GitHub")

    else:

        open(update_zipfile, 'wb').write(r.content)

        with zipfile.ZipFile(update_zipfile, 'r') as zip_ref:
            zip_ref.extractall('../data/files/cache/update/unzip_update')

        root_src_dir = '../data/files/cache/update/unzip_update/Coran-Converter-main'
        root_dst_dir = '../'


        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    # in case of the src and dst are the same file
                    if os.path.samefile(src_file, dst_file):
                        continue
                    os.remove(dst_file)
                shutil.move(src_file, dst_dir)


#  _________________________________________________
# |  _____________________________________________  |
# | | Main Launcher:                              | |
# | |  → "Une des fonctions clé de l'application" | |
# | |_____________________________________________| |
# |_________________________________________________|

if __name__ == '__main__':

    update_app = App()
    update_app.mainloop()


