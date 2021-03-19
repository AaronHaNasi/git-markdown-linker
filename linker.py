import os
from pathlib import Path

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def main():
    file_to_link = ''
    file_path = find(file_to_link, '.')
    print(file_path)

main()
