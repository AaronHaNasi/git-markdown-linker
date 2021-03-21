import os
import sys
from pathlib import Path
import glob 

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def get_file_list(): 
    file_list = []
    for filename in glob.glob('*.md'):
        file_list.append(filename)
    return file_list

def main():
    term_to_link = sys.argv[1]
    file_to_link = sys.argv[2]
    file_path = find(file_to_link, '.')
    print(file_path)
    files = get_file_list()
    print(files)

main()
