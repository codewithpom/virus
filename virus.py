import os
from datetime import datetime
from shutil import move
file_paths = []
counter = 0
print("If you want all the excel file, for example write .xlsx")
inp = ".png"
thisdir = os.getcwd()
print(datetime.now().strftime(("%H:%M:%S")))
for r, d, f in os.walk("C:\\"):
    for file in f:
        filepath = os.path.join(r, file)
        if inp in file:
            counter += 1
            file_name = os.path.join(r, file)
            print(file_name)
            file_paths.append(file_name)
            """
            copy(src=file_name, dst="F:\\")
            """

print(f"trovati {counter} files.")

print(datetime.now().strftime(("%H:%M:%S")))

# importing required modules

from zipfile import ZipFile


def main():
    # path to folder which needs to be zipped

    print('Following files will be zipped:')

    with ZipFile('my_python_files.zip', 'w') as zipper:

        for files in file_paths:
            zipper.write(files)

    print('All files zipped successfully!')


if __name__ == "__main__":
    main()
    move(src="my_python_files.zip", dst="F:\\")






