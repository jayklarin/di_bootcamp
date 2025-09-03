# Read the file line by line
# Read only the 5th line of the file
# Read only the 5 first characters of the file

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'star_wars.txt')

with open(file_path, 'r', encoding='utf-8') as f:
    print("-- Line by Line --")
    for line in f:
        print(f.readline())

with open(file_path, 'r', encoding='utf-8') as f:
    # Read only the 5th line of the file
    print('Fifth line only')
    # for i, element in enumerate(f):
    #     if i == 5:
    #         print(f.readlines())
    print(f.readline(4))
