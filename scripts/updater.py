import json, os, shutil, zipfile, requests
from pathlib import Path

zip_to_install = 'https://github.com/Random-Creation-of-YassiGame/Coran-Converter/archive/refs/heads/main.zip'
update_cache_in_github = 'https://raw.githubusercontent.com/Random-Creation-of-YassiGame/Coran-Converter/main/data/files/cache/cache_version.json'
path_update_cache = "../data/files/cache/cache_version.json"
update_zipfile = '../data/files/cache/update/update.zip'


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


if __name__ == '__main__':
    
    try:
        my_file = Path(path_update_cache)
        my_abs_path = my_file.resolve(strict=True)

    except FileNotFoundError:
        print(" >  Je ne trouve pas le fichier 'cache_version.json', je vais créé un nouveau fichier:")
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
                print('You have the latest version')
            else:
                print("you don't have the latest version")
                LaunchUpdate()

        except json.decoder.JSONDecodeError:
            LaunchUpdate()


