import os
import shutil
from pathlib import Path
import zipfile

import requests

zip_to_install = 'https://github.com/Random-Creation-of-YassiGame/Coran-Converter/archive/refs/heads/main.zip'
update_cache_in_github = ''
path_update_cache = "../data/files/cache/cache_version.json"

def LaunchUpdate():





    update_zipfile = '../data/files/cache/update/update.zip'



    try:
        global r
        r = requests.get(zip_to_install, allow_redirects=True)

    except requests.exceptions.ConnectionError:
        print("Download Error: We think, you have no connection or you are banned ip from GitHub")

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

def CreateCacheVersionFile():
    try:  # try to create a file
        f = open(path_update_cache, "w")  # create file

    except:  # error when create the file
        print("Une Erreur est survenue, lors de la creation du fichier")  # paste eror
        input()  # wait the user input
        exit()  # and exit after the interaction

    else:  # if no erorr
        f.close()  # close the file
        print("Le fichier a été créé avec succès")  # create file

if __name__ == '__main__':
    try:
        my_file = Path(path_update_cache)
        my_abs_path = my_file.resolve(strict=True)

    except FileNotFoundError:
        print(" >  Je ne trouve pas le fichier 'cache_version.json', je vais créé un nouveau fichier:")
        CreateCacheVersionFile()
        LaunchUpdate()

    finally:
        LaunchUpdate()


