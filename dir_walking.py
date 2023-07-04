import os

for root, dirs, files in os.walk("../or-3-07"):
    for file in files:
        if file == "apiget.py":
            file_path = os.path.join(root, file)
            print(file_path)  # ../or-3-07\apiget.py

for root, dirs, files in os.walk('..'):
    abs_root = os.path.abspath(root)
    print(abs_root)
    if dirs:
        print("Directories:")
        for dir_ in dirs:
            print(dir_)
        print()
    if files:
        print("Files:")
        for filename in files:
            print(filename)
        print()
