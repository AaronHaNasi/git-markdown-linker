import os
from pathlib import Path

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def main():
    file_path = find('linker.py', '.')
    print(file_path)

main()
