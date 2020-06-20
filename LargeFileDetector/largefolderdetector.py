import os
import shutil
from pathlib import Path
import time

user_input = input('What drive would you like to check?\n')

while True:
    if not (drive_to_walk := Path(f'{user_input}:/')):
        user_input = input('Something went wrong, enter the drive you would like to check: \n')
    else:
        break

size_to_locate = int(input("What size folders would you like to locate?\n"))

while True:
    if size_to_locate < 1:
        size_to_locate = int(input("Please enter a suitable number:\n"))
    else:
        break


def get_size(root_directory):
    total_size = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
    return total_size


def locate_large_folders(drive):
    for folders in os.walk(drive):
        start = time.time()
        if get_size(Path(folders[0])) * (10 ** -6) > (size_to_locate * 1000):
            print(f"{folders[0]} is larger than {size_to_locate}GB.")
            end = time.time()
            print(f"Took {round(end - start)} seconds.")
            


locate_large_folders(drive_to_walk)

