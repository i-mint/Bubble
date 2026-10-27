#!/usr/bin/python3
##########################################
#
# Bubble themes installer
# Create by auoi (auoi.fik@gmail.com)
#
##########################################

from pathlib import Path
import shutil
import fnmatch
import os

themes = [
        'Bubble',
        'Bubble-Dark',
        'Bubble-Darker',
        'Bubble-Lighter',
        'Bubble-Solid',
        'Bubble-Solid-Dark',
        'Bubble-Solid-Darker',
        'Bubble-Solid-Lighter'
        ]

class PathDestination:
    def __init__(self, path, retries, arg1):
        self.path = path
        self.retries = retries
        self.arg1 = arg1 

        print(f"=> {arg1}")
        print("Type 1 path = '/.themes'")
        print("Type 2 path = '/.local/share/themes'")
        print("Type 'root' path = '/usr/share/themes'")
        print('==========')

        while True:
            key = input('Type here: ')
            if key in {'1', '2', 'root'}:
                if key == '1':
                    self.path = Path.home() / '.themes'
                elif key == '2':
                    self.path = Path.home() / '.local/share/themes'
                elif key == 'root':
                    self.path = '/usr/share/themes'
                return True

            retries = retries - 1
            if retries < 0:
                raise ValueError('Invalid user response!')
            print("Type key 1, 2 or 'root'")

class InstallThemes(PathDestination):
    def __init__(self, path, retries, arg1):
        all_themes = []
        super().__init__(path, retries, arg1)
        for root, dirs, files in os.walk(Path.cwd(), topdown=False):
            for names in dirs:
                if fnmatch.fnmatch(names, themes[0]) \
                or fnmatch.fnmatch(names, themes[1]) \
                or fnmatch.fnmatch(names, themes[2]) \
                or fnmatch.fnmatch(names, themes[3]) \
                or fnmatch.fnmatch(names, themes[4]) \
                or fnmatch.fnmatch(names, themes[5]) \
                or fnmatch.fnmatch(names, themes[6]) \
                or fnmatch.fnmatch(names, themes[7]):
                    all_themes.append(names)

        # List of themes
        print('==========')

        for i, j in enumerate(sorted(all_themes), start=1):
            print(f'{i}: {j}')

        print('==========')

        # Installation of themes
        if len(all_themes) > 0:
            key = input("Install themes? type Yes (all) or Number(1..8): ")
            print('==========')
            if key == 'Yes' or key == 'yes':
                for i in sorted(all_themes):
                    shutil.copytree(i, Path(self.path).joinpath(i), dirs_exist_ok=True)
                    print(f'Installed..........{i}')

            elif key == '1':
                bubble = sorted(all_themes)[0]
                shutil.copytree(bubble, Path(self.path).joinpath(bubble), dirs_exist_ok=True)
                all_themes.clear()
                print(f'Installed..........{bubble}')

            elif key == '2':
                bubble = sorted(all_themes)[1]
                shutil.copytree(bubble, Path(self.path).joinpath(bubble), dirs_exist_ok=True)
                all_themes.clear()
                print(f'Installed..........{bubble}')

            elif key == '3':
                bubble = sorted(all_themes)[2]
                shutil.copytree(bubble, Path(self.path).joinpath(bubble), dirs_exist_ok=True)
                all_themes.clear()
                print(f'Installed..........{bubble}')

            elif key == '4':
                bubble = sorted(all_themes)[3]
                shutil.copytree(bubble, Path(self.path).joinpath(bubble), dirs_exist_ok=True)
                all_themes.clear()
                print(f'Installed..........{bubble}')

            elif key == '5':
                bubble = sorted(all_themes)[4]
                shutil.copytree(bubble, Path(self.path).joinpath(bubble), dirs_exist_ok=True)
                all_themes.clear()
                print(f'Installed..........{bubble}')

            elif key == '6':
                bubble = sorted(all_themes)[5]
                shutil.copytree(bubble, Path(self.path).joinpath(bubble), dirs_exist_ok=True)
                all_themes.clear()
                print(f'Installed..........{bubble}')

            elif key == '7':
                bubble = sorted(all_themes)[6]
                shutil.copytree(bubble, Path(self.path).joinpath(bubble), dirs_exist_ok=True)
                all_themes.clear()
                print(f'Installed..........{bubble}')

            elif key == '8':
                bubble = sorted(all_themes)[7]
                shutil.copytree(bubble, Path(self.path).joinpath(bubble), dirs_exist_ok=True)
                all_themes.clear()
                print(f'Installed..........{bubble}')

            else:
                print("Not installed......")

if __name__ == '__main__':
    InstallThemes('', 4, 'Select themes installation directory path: ')


            
