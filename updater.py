# -*- coding: UTF-8 -*-
#  ______________________________________________________________
# |  __________________________________________________________  |
# | | Debut du système ;)                                      | |
# | |  → "Créé par YassiGame | Ici c'est le main de l'app"     | |
# | |__________________________________________________________| |
# |______________________________________________________________|
import time

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
from tkinter import messagebox

from scripts.app import launchapp

zip_to_install = 'https://github.com/Random-Creation-of-YassiGame/Coran-Converter/archive/refs/heads/main.zip'
update_cache_in_github = 'https://raw.githubusercontent.com/Random-Creation-of-YassiGame/Coran-Converter/main/data/files/cache/cache_version.json'
path_update_cache = "../data/files/cache/cache_version.json"
update_zipfile = '../data/files/cache/update/update.zip'

root = Tk()
root.geometry("0x0")
root.withdraw()

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
        root_dst_dir = './'


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

        messagebox.showinfo("The Update are done", "So, please restart the program.")
        exit()


#  _________________________________________________
# |  _____________________________________________  |
# | | Main Launcher:                              | |
# | |  → "Une des fonctions clé de l'application" | |
# | |_____________________________________________| |
# |_________________________________________________|

if __name__ == '__main__':

    try:
        my_file = Path(path_update_cache)
        my_abs_path = my_file.resolve(strict=True)

    except FileNotFoundError:
        messagebox.showerror("No Version Cache File", "The file responsible for storing the local version of the app does not exist. We will launch the update.")
        LaunchUpdate()

    else:
        r = requests.get(update_cache_in_github, stream=True)
        r = str(r.content).replace("'", "")
        version_in_github = r.replace("b", "")

        version_in_github = json.loads(version_in_github)

        try:
            with open(path_update_cache, 'r') as file:  # open file ('settings.json')
                output = json.load(file)

            if str(output['version']) == str(version_in_github['version']):
                messagebox.showinfo("You have the latest version", "The app has latest version")
                root.destroy()
                launchapp()
            else:
                messagebox.showwarning("Don't Have recent version !", f"You have the version '{str(output['version'])}', but in github the new version is '{str(version_in_github['version'])}'. We will launch the update.")
                root.destroy()
                LaunchUpdate()

        except json.decoder.JSONDecodeError:
            messagebox.showerror("No Data in the cache version file", "The file responsible for checking the version of the app has no data. We will launch the update.")
            root.destroy()
            LaunchUpdate()


