#!/usr/bin/python3
##########################################
#
# Bubble themes uninstaller
# Create by auoi (auoi.fik@gmail.com)
#
##########################################

from pathlib import Path
import shutil
import fnmatch
import os

from install import themes, PathDestination

class UninstallThemes(PathDestination):
    def __init__(self, path, retries, arg1):
        all_themes = []
        super().__init__(path, retries, arg1)
        for root, dirs, files in os.walk(self.path, topdown=False):
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
        
        #List themes
        print('==========')

        for i, j in enumerate(sorted(all_themes), start=1):
            print(f'{i}: {j}')

        print('==========')

        #Remove themes
        if len(all_themes) > 0:
            key = input("Remove themes? type Yes (all) or Number(1..8): ")
            print('==========')
            if key == 'Yes' or key == 'yes':
                for i in all_themes:
                    shutil.rmtree(self.path.joinpath(i))
                    print(f'Removed..........{i}')


            elif key == '1':
                bubble = sorted(all_themes)[0]
                shutil.rmtree(self.path.joinpath(bubble))
                all_themes.clear()
                print(f'Removed..........{bubble}')

            elif key == '2':
                bubble = sorted(all_themes)[1]
                shutil.rmtree(self.path.joinpath(bubble))
                all_themes.clear()
                print(f'Removed..........{bubble}')

            elif key == '3':
                bubble = sorted(all_themes)[2]
                shutil.rmtree(self.path.joinpath(bubble))
                all_themes.clear()
                print(f'Removed..........{bubble}')

            elif key == '4':
                bubble = sorted(all_themes)[3]
                shutil.rmtree(self.path.joinpath(bubble))
                all_themes.clear()
                print(f'Removed..........{bubble}')

            elif key == '5':
                bubble = sorted(all_themes)[4]
                shutil.rmtree(self.path.joinpath(bubble))
                all_themes.clear()
                print(f'Removed..........{bubble}')

            elif key == '6':
                bubble = sorted(all_themes)[5]
                shutil.rmtree(self.path.joinpath(bubble))
                all_themes.clear()
                print(f'Removed..........{bubble}')

            elif key == '7':
                bubble = sorted(all_themes)[6]
                shutil.rmtree(self.path.joinpath(bubble))
                all_themes.clear()
                print(f'Removed..........{bubble}')

            elif key == '8':
                bubble = sorted(all_themes)[7]
                shutil.rmtree(self.path.joinpath(bubble))
                all_themes.clear()
                print(f'Removed..........{bubble}')

            else:
                print("Not removed......")

if __name__ == '__main__':
    UninstallThemes('', 4, 'Select installed themes directory path: ')

