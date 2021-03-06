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


## Import some other modules:
import json, os, shutil, zipfile, requests
from tkinter import messagebox
from pathlib import Path

zip_to_install = 'https://github.com/Random-Creation-of-YassiGame/Coran-Converter/archive/refs/heads/main.zip'
update_cache_in_github = 'https://raw.githubusercontent.com/Random-Creation-of-YassiGame/Coran-Converter/main/data/files/cache/cache_version.json'
path_update_cache = "../data/files/cache/cache_version.json"
update_zipfile = '../data/files/cache/update/update.zip'


def launchapp():
    import scripts.app as app
    app.launchapp()


class MessageBox():
    def info(self, title, str, startapp=False):
        root = Tk()
        root.geometry("0x0")
        root.withdraw()
        messagebox.showinfo(title, str)
        root.destroy()
        if startapp: launchapp()
    def warn(self, title, str, startapp=False):
        root = Tk()
        root.geometry("0x0")
        root.withdraw()
        messagebox.showwarning(title, str)
        root.destroy()
        if startapp: launchapp()
    def error(self, title, str, startapp=False):
        root = Tk()
        root.geometry("0x0")
        root.withdraw()
        messagebox.showerror(title, str)
        root.destroy()
        if startapp: launchapp()

message = MessageBox()

def error(id):
    if id == 1:
        message.error("Download Error:","Unable to connect to server at 'github.com'.\nHere are three other things you can try to fix this problem :\n\n↪ Try again later.\n↪ Check your network connection.\n↪ If you are connected through a firewall, verify that the app has permission to access the web.\n\n↳ The app will be launched without the update !",True)


def LaunchUpdate():
    try:
        r = requests.get(zip_to_install, allow_redirects=True)

    except requests.exceptions.ConnectionError:
        error(1)

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

        message.info("The Update is done", "The latest version has been successfully installed.\n\n↪ Please restart the program again.")
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
        message.error("No Version Cache File", "The file responsible for storing the local version of the app does not exist. We will launch the update.")
        LaunchUpdate()

    else:
        try:
            r = requests.get(update_cache_in_github, stream=True)
        except requests.exceptions.ConnectionError:
            error(1)
        else:
            r = str(r.content).replace("'", "")
            version_in_github = r.replace("b", "")

            version_in_github = json.loads(version_in_github)

            try:
                with open(path_update_cache, 'r') as file:  # open file ('settings.json')
                    output = json.load(file)

                if str(output['version']) == str(version_in_github['version']):
                    print(f"You have the latest version\n ↪ The version: V{str(output['version'])}")
                    launchapp()
                else:
                    message.warn("You don't have the latest version !", f"You have the version 'V{str(output['version'])}', But the latest version according to the repo on GitHub is 'V{str(version_in_github['version'])}'.\n\n↪ We will launch the update.")
                    LaunchUpdate()

            except json.decoder.JSONDecodeError:
                message.error("No Data in the cache version file", "The file responsible for checking the version of the app has no data. We will launch the update.")
                LaunchUpdate()


